from google import genai
from google.genai import types


PROJECT_ID = "corp-apigee"
LOCATION = "us-central1"
API_ENDPOINT = "https://api.prftgcpdemo.ai/v1/samples/llm-token-limits"
API_KEY = "wfowu8PagE7OWe2eUOu7SGyJiCG03GsOwRem7GAGqKbCClcO"
MODEL = "gemini-2.0-flash"

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
    http_options=types.HttpOptions(api_version='v1', base_url=API_ENDPOINT, headers = {"x-apikey": API_KEY})
)

prompts = [
    "Why is the sky blue?",
    "What makes the sky blue?",
    "Why does the sky is blue colored?",
    "Can you explain why the sky is blue?",
    "The sky is blue, why is that?"
]

for prompt in prompts:
  response = client.models.generate_content(model=MODEL, contents=prompt)
  print(response.text)