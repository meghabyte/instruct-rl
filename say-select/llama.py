from transformers import LlamaForCausalLM, LlamaTokenizer
import torch
import json


def load_model(model_name="meta-llama/Llama-2-13b-chat-hf"):
    print("Loading Model...")
    model = LlamaForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
    model.to("cuda:0")
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    return model, tokenizer

MODEL, TOKENIZER = load_model(model_name="meta-llama/Llama-2-7b-chat-hf")

def prompt_model(model, tokenizer, description):
    
    prompt = '''[INST]'''+description+'''[/INST]'''
    inputs = tokenizer([prompt], return_tensors="pt").to("cuda:0")
    outputs = model.generate(**inputs, max_new_tokens=1024,  repetition_penalty=1.2, top_k=50, eos_token_id=tokenizer.eos_token_id,do_sample=True, top_p=0.9, temperature=0.6, num_return_sequences=1)
    output_text = tokenizer.batch_decode(outputs[:,inputs["input_ids"].shape[1]:])
    processed_text = output_text[0].strip() 
    print(processed_text)
    return processed_text