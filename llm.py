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
      "content": "",
      "role": "system",
      "content": "미국을 포함한 다른 나라들의 10년치 환율(달러 대비) 값들이야. 현재 각 나라들의 환율이 높은지 낮은지를를"
    }
  ]
)
print(completion.choices[0].message.content)