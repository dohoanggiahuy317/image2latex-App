import os
from flask import Flask, request, render_template
from PIL import Image
import base64
import io
from process.run_latex_ocr import run_nougat_latex

app = Flask(__name__, static_folder="static")

# Ensure the 'uploads' directory exists
uploads_dir = os.path.join(os.getcwd(), 'static')
os.makedirs(uploads_dir, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        # Check if the file has a valid extension
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        if file:
            # Save the uploaded file
            file_path = os.path.join(uploads_dir, file.filename)
            file.save(file_path)

            # Get the model prediction
            prediction = run_nougat_latex(file_path)
            # prediction = "hahkadsjbfwekjfielhgfkwercnjlwemkchtnielmctlwhtcwiomcahhahkadsjbfwekjfielhgfkwercnjlwemkchtnielmctlwhtcwiomcahhahkadsjbfwekjfielhgfkwercnjlwemkchtnielmctlwhtcwiomcahhahkadsjbfwekjfielhgfkwercnjlwemkchtnielmctlwhtcwiomcah"

            # Display the prediction as text
            result_text = f'{prediction}'  # Customize this based on your model output

            # Remove the uploaded image after processing
            os.remove(file_path)

            im = Image.open(file.stream)
            im = im.convert('RGB')
            data = io.BytesIO()
            im.save(data, "JPEG")
            encoded_img_data = base64.b64encode(data.getvalue())

            return render_template("index.html", result=result_text, img_data=encoded_img_data.decode('utf-8'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

