import openai

openai.api_key = "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"

models = openai.Model.list()
# print(models)

def handle_input(user_input):
    copletion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}]
    )
    return copletion