import openai

API_KEY = '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' # Dec1 key

openai.api_key = API_KEY

chat_history = []

while True:
    user_message = input('User: '); print()
    if user_message.lower() == "exit": break

    chat_history.append(
        {"role": "user", "content": user_message}
    )

    response = openai.ChatCompletion.create(
        # model = 'gpt-3.5-turbo',
        model = "ft:gpt-3.5-turbo-0613:personal::8RDCqgNm",
        messages = chat_history
    )

    assistant_response = response['choices'][0]['message']['content']
    print(f"ChatGPT: {assistant_response}\n\n")
    chat_history.append(response['choices'][0]['message'])




