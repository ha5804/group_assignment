from openai import OpenAI
import matplotlib.pyplot as plt

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="",
)


count_question = 0
user_count = 10

while True:
    user_q = input("환율에 관한 궁금한 점들을 물어보세요!\n""종료를 희망하시면 exit이라고 적어주세요: ")
    if(user_q.lower() == "exit"):
        break
  


completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},  
  model="meta-llama/llama-3.3-8b-instruct:free",
  messages=[
    {
      "role": "system",
      "content": 
    }
  ]
)
print(completion.choices[0].message.content)



completion.choices[0].message.content