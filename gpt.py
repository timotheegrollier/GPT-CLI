#!/usr/bin/python3
from gpt4free import you

# simple request with links and details
response = you.Completion.create(
    prompt="hello world",
    detailed=True,
    include_links=True, )

print(response.dict())

# {
#     "response": "...",
#     "links": [...],
#     "extra": {...},
#         "slots": {...}
#     }
# }

# chatbot

chat = []
print("\n")

while True:
    prompt = input("You: ")
    if prompt == 'q':
        break
    elif prompt == 'exit':
        break
    print("\n")
    response = you.Completion.create(
        prompt=prompt,
        chat=chat)

    res = response.text.encode().decode('unicode-escape')
    print("Bot:", res)
    print("\n")


    chat.append({"question": prompt, "answer": response.text})