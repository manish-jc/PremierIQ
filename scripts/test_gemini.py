from app.utils.gemini_client import GeminiClient

client = GeminiClient()

response = client.generate("Who is Erling Haaland?")

print(response)