from transformers import AutoModelForQuestionAnswering, AutoTokenizer

model = AutoModelForQuestionAnswering.from_pretrained("facebook/bart-base")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-base")


def answer_question(question):
    inputs = tokenizer(question, return_tensors="pt")
    outputs = model(**inputs)
    answer = tokenizer.decode(outputs.start_logits.argmax(-1), skip_special_tokens=True)

    return answer


question = "What is the weather today?"
answer = answer_question(question)
print(answer)
