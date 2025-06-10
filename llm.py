from openai import OpenAI


while True:
  user_order = input("이 국가들의 환율에 대해 무엇이 궁금하시나요?: ")
  order_list = []
  if user_order.lower() == "exit":
    break
  
  else:
    order_list.append(user_order)
  



client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="",
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
      "content": order_list
    },  
    {
      "role": "system",
      "content": "너는 환율에 대한 답변을 해주는 어시스턴트야. user_order을 바탕으로 답변을 해줘."
    }  
  ]
)
print(completion.choices[0].message.content)