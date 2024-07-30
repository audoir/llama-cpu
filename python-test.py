from openai import OpenAI

client = OpenAI(
        base_url='http://localhost:8080/v1',
        api_key='no-key'
        )

completion = client.chat.completions.create(
  model="not-used",
  messages=[
    {"role": "system", "content": "You are a coding assistant, skilled in programming.."},
    {"role": "user", "content": "Write a hello world program in C++."}
  ],
  stream=True,
)

for chunk in completion:
  print(chunk.choices[0].delta.content or "", end="")
