import openai


openai.api_key = "[OPENAI_API_KEY]"
messages = [
    {
        "role": "system",
        "content": "[CAHTBOT ROLE DESCRIPTION]"
    }
]

print("how do you feel?")

while True:
    msg = input()
    messages.append(
        {
            "role": "user",
            "content": msg,
        }
    )

    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    ans = resp.choices[0].message.content
    messages.append(
        {
            "role": "assistant",
            "content": ans,
        }
    )

    print(ans)
