# -*- coding:utf-8 -*-
# create: @time: 10/8/23 11:47
import argparse

import torch
from PIL import Image
from transformers import VisionEncoderDecoderModel
from transformers.models.nougat import NougatTokenizerFast
from nougat_latex.util import process_raw_latex_code
from nougat_latex import NougatLaTexProcessor


def run_nougat_latex(img_path, model_path="Norm/nougat-latex-base", device="cpu"):

    # init model
    model = VisionEncoderDecoderModel.from_pretrained(model_path).to(device)

    # init processor
    tokenizer = NougatTokenizerFast.from_pretrained(model_path)
    latex_processor = NougatLaTexProcessor.from_pretrained(model_path)

    # run test
    image = Image.open(img_path)
    if not image.mode == "RGB":
        image = image.convert('RGB')

    pixel_values = latex_processor(image, return_tensors="pt").pixel_values
    task_prompt = tokenizer.bos_token
    decoder_input_ids = tokenizer(task_prompt, add_special_tokens=False,
                                  return_tensors="pt").input_ids
    with torch.no_grad():
        outputs = model.generate(
            pixel_values.to(device),
            decoder_input_ids=decoder_input_ids.to(device),
            max_length=model.decoder.config.max_length,
            early_stopping=True,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
            use_cache=True,
            num_beams=1,
            bad_words_ids=[[tokenizer.unk_token_id]],
            return_dict_in_generate=True,
        )
    sequence = tokenizer.batch_decode(outputs.sequences)[0]
    sequence = sequence.replace(tokenizer.eos_token, "").replace(tokenizer.pad_token, "").replace(tokenizer.bos_token,
                                                                                                  "")
    sequence = process_raw_latex_code(sequence)
    print(sequence)
    return sequence


if __name__ == '__main__':
    run_nougat_latex()
