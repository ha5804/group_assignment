from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<OPENROUTER_API_KEY>",
)

completion = client.chat.completions.create(
  model="meta-llama/llama-3.3-8b-instruct:free",
  messages=[
    {
      "role": "user",
      "content": rate_dic,
      "role": "system",
      "content": "너는 환율에 대한 답변을 해주는 어시스턴트야. "
    }
  ]
)
print(completion.choices[0].message.content)