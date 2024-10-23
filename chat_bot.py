def chat_bot(text,save_path):
  max_seq_length = 2048
  dtype = None
  load_in_4bit = True
  fine_tuned_model = AutoModelForCausalLM.from_pretrained(save_path, load_in_4bit=load_in_4bit)
  tokenizer = AutoTokenizer.from_pretrained(save_path)
  fine_tuned_model.eval()
  question= f"This is the question: {text}"
  prompt = f"<|start_header_id|>system<|end_header_id|> You are a Medical AI chatbot assistant. <|eot_id|><|start_header_id|>User: <|end_header_id|>{question}<|eot_id|>"

  inputs = tokenizer([prompt], return_tensors="pt").to("cuda")
  outputs = fine_tuned_model.generate(**inputs, max_new_tokens=256,use_cache=True)
  answer = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

  try:
    # Split the answer at the first line break, assuming system intro and question are on separate lines
    answer_parts = answer.split("\n", 1)
    # If there are multiple parts, consider the second part as the answer
    if len(answer_parts) > 1:
      answers = answer_parts[1].strip()  # Remove leading/trailing whitespaces
    else:
      answers = "There is no answer for your question"  # If no split possible, set answer to empty string
    print("****************** The Answer Is Generated ******************")
    return answers
  except:
    print("****************** The Answer Is Generated ******************")
    return answers
