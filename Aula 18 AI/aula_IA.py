import google.generativeai as genai

genai.configure(api_key="AIzaSyDD13AiX_8jJaAe_g5s_NJqsFjw2OxDV3E")

model = genai.GenerativeModel("gemini-1.5-flash")
pergunta = input("Digite sua pergunta: ")
response = model.generate_content(pergunta)
print(response.text)
