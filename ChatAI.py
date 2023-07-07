import openai

openai.api_key = "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"

models = openai.Model.list()
# print(models)

def handle_input(user_input):
    copletion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}]
    )
    return copletion


handle_input(input()).choices[0].message.content
