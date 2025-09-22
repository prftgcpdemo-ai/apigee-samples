from langchain_google_vertexai import VertexAI
import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# Define project information
PROJECT_ID = "corp-apigee"
LOCATION = "us-central1"
API_ENDPOINT = "https://api.prftgcpdemo.ai/v2/samples/llm-semantic-cache"
MODEL = "gemini-2.0-flash"

# Initialize LangChain
model = VertexAI(
      project=PROJECT_ID,
      location=LOCATION,
      api_endpoint=API_ENDPOINT,
      api_transport="rest",
      streaming=False,
      model_name=MODEL)

exec = 2
execs = []
prompts = ["Why is the sky blue?",
           "What makes the sky blue?",
           "Why does the sky is blue colored?",
           "Can you explain why the sky is blue?",
           "The sky is blue, why is that?"]

for i in range(exec):
  for prompt in prompts:
    start_time = time.time()
    model.invoke(prompt)
    response_time = time.time() - start_time
    execs.append(response_time)

mpl.rcParams['figure.figsize'] = [15, 5]
df = pd.DataFrame(execs, columns=['Response time'])
df['Exec'] = range(1, len(df) + 1)
df.plot(kind='line', x='Exec', y='Response time', legend=False)
plt.title('Semantic Cache Performance')
plt.xlabel('Executions')
plt.ylabel('Response Time')
plt.xticks(df['Exec'], rotation=0)

average = df['Response time'].mean()
plt.axhline(y=average, color='r', linestyle='--', label=f'Average: {average:.2f}')
plt.legend()

plt.show()