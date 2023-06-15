import openai
from django.http import HttpResponse

def  chatGpt(request):
  openai.api_key = ""
  prompt = "「あ」と返してください。"
  response = openai.Completion.create(
    # model="gpt-3.5-turbo",
    engine="curie",
    prompt=prompt,
    max_tokens=5,
    # messages=[
    #   {"role": "user", "content": "「あ」と返してください。"},
    # ]
  )
  print(response)
  print(response.choices[0].text.strip())
  print(response["choices"][0])

  return HttpResponse(response.choices[0].text.strip())
