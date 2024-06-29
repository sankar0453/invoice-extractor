from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel("gemini-pro-vision")


for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
    
# models/gemini-1.0-pro -- only for text
# models/gemini-1.0-pro-001
# models/gemini-1.0-pro-latest
# models/gemini-1.0-pro-vision-latest
# models/gemini-1.5-flash
# models/gemini-1.5-flash-001
# models/gemini-1.5-flash-latest
# models/gemini-1.5-pro
# models/gemini-1.5-pro-001
# models/gemini-1.5-pro-latest
# models/gemini-pro
# models/gemini-pro-vision