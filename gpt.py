from openai import OpenAI
from decouple import config

client = OpenAI(
    api_key=config("OPENAI_API_KEY")
)

user_prompt = input("Enter your prompt here: ")

response = client.chat.completions.create(
  model="gpt-4o-mini",
  stream= True,
  messages=[
    {"role": "system", "content": "you are a helpful assistant. Give detailed and academic explanation in which ever response you create"},
    {"role": "user", "content": user_prompt},
  ]
)


for chunk in response:
    print(chunk.choices[0].delta.content, end="")