import os
import export
import google.generativeai as genai
from keys import API_KEY

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Generate a puppy image")
print(response)