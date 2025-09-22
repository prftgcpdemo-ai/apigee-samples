from google import genai
from google.genai import types


PROJECT_ID = "corp-apigee"
LOCATION = "us-central1"
API_ENDPOINT = "https://api.prftgcpdemo.ai/v1/samples/llm-token-limits"
API_KEY = "i9UzcHfetMSMDvaJQk638QlhxR1VYaBTEJSuGrq2Ph388wju"
MODEL = "gemini-2.0-flash"

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
    http_options=types.HttpOptions(api_version='v1', base_url=API_ENDPOINT, headers = {"x-apikey": API_KEY})
)

prompts = [
    "Why is the sky blue? Provide a very long and detailed explanation.",
    "Furnish and exhaustive and long explanation (as long as a scence magazine article) for the phenomenon of the blue sky.",
    "Can you give me a really in-depth and as long as a book chapter of why the sky is blue?",
    "Give me a super detailed and very extensive explanation (as long as the yellow pages) of why the sky is blue.",
    "Can you tell me all about why the sky is blue, and make sure it's longer than a novel?"
]

for prompt in prompts:
  response = client.models.generate_content(model=MODEL, contents=prompt)
  print(response.text)