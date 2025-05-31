from openai import OpenAI


user_order = input("이 국가들의 환율에 대해해 무엇이 궁금하시나요?: ")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<OPENROUTER_API_KEY>",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},  
  model="meta-llama/llama-3.3-8b-instruct:free",
  messages=[
    {
      "role": "user",
      "content": user_order,
      "content": rate_dic  
      "role": "system",
      "content": "너는 환율에 대한 답변을 해주는 어시스턴트야."
    }  
  ]
)
print(completion.choices[0].message.content)