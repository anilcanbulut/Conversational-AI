from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-6.7b-instruct", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-6.7b-instruct", trust_remote_code=True, torch_dtype=torch.bf>
code = 'def filter_even_keys(data_dict): \
    for key, value in data_dict.items(): \
        if value % 2 == 0: \
            del data_dict[key]  # Attempting to modify dictionary size during iteration \
    return data_dict \
    # Example dictionary with integer keys and values \
    example_dict = {1: 2, 3: 4, 5: 6, 7: 8} \
    # This will raise an error \
    filtered_dict = filter_even_keys(example_dict) \
    print(filtered_dict)'

messages=[
    { 'role': 'user', 'content': f"I have an LLM running locally. I want to interactively work on it so I might need to use web inter>]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
# tokenizer.eos_token_id is the id of <|EOT|> token
outputs = model.generate(inputs, max_new_tokens=512, do_sample=True, top_k=50, top_p=0.95, temperature=0.5, num_return_sequences=1, e>print(tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True))