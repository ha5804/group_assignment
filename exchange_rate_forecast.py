from openai import OpenAI
import matplotlib.pyplot as plt

while True:
   input_country = input("국가: ")
   if input_country in x:
     break
   else: 
      print("유효한 국가를 입력해주세요.")

c_rate = data[data["국가별"] == input_country]
b = c_rate.iloc[0][1:]
  
    


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
      "content": b
    },  
    {
      "role": "system",
      "content": "다음 데이터를 기반으로 향후 6개월 간의 환율 전망을 제공해주세요. 전망은 월별로 명확하게 제시하고, JSON 형식으로 제공해 주세요."
    }  
  ]
)
print(completion.choices[0].message.content)



completion.choices[0].message.content