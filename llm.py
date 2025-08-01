from google import genai

client = genai.Client(api_key="AIzaSyCs_HydhUScy2pMK25JVHQ1pepNtGkygGo")

response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="Why is the sky blue?"
)

print(response.text)