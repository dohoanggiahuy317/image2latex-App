# Image-to-LaTeX Projects
Recognizing the challenges faced by my friends when learning LaTeX and typing LaTeX equations for homework, I developed a web app that employs a Transformers machine learning model to simplify the conversion of images into LaTeX equations for school assignments.

## Usage
As a hosting server for the application is not available, you will need to clone this project to run the application.

```
git clone https://github.com/dohoanggiahuy317/App-image2latex-web.git
```

Next, open the command prompt or terminal and navigate to the project folder.

You can create a new Python virtual environment if desired. Then, download the required packages for the application using:

```
pip3 install -r requirements.txt
```

Finally, from the root directory of the application, execute the following command to run the application:

```
python3 app.py
```

The application will start on the localhost at port 8080.

## User Interface

Upload your image and click the Upload button. Wait for the system to process, which may take 1 to 2 minutes, to display the result.

![Alt text](<static/images/image demo.png>)

## Further Information

If the model is not functioning correctly, refer to https://github.com/NormXU/nougat-latex-ocr and https://huggingface.co/Norm/nougat-latex-base to download the model. Note that Git LFS is required for downloading as the model size is 1.4GB.

After downloading, go to `process/run_latex_ocr.py` and update the default parameters from `"Norm/nougat-latex-base"` of HuggingFace to the `path\to\the model\you\downloaded`.

References
The Transformers model used in this project is from https://github.com/NormXU/nougat-latex-ocr and https://huggingface.co/Norm/nougat-latex-base.