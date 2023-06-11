# genai-pybcndata2023
Generative AI workshop delivered at PyDataBCN 2023

## Role play

Help ResponsibleLending company to automate money loans to the right people, which are those aligning with ESG goals.   
In order to do that we'll create a Gen-AI classification system to generate loan/no loan decisions according to two features:
1. email sentiment
2. ESG motivation of the sender    

The system will also generate an automated email response for the sender extracting information such as:
1. sender
2. requested loan quantity
3. loan motivation

Seven loan request from different candidates are provided:
1. Lex Luthor
2. Thanos
3. The Joker
4. Agatha Christie
5. Aquaman
6. Coco Chanel
7. Salvador Dali

## Content

This repo contains a notebook with code to:
1. Interact with models from [HugginFace Inference API](https://huggingface.co/inference-api)
2. Interact with a custom, fine-tuned ESG model from HuggingFace, [ESG-BERT](https://huggingface.co/nbroad/ESG-BERT)
3. Use prompts for [Falcon-7b-instruct](https://huggingface.co/tiiuae/falcon-7b-instruct) and [flan-t5-xxl models](https://huggingface.co/google/flan-t5-xxl) models
4. Custom prompts to generate emails and their automated responses.
