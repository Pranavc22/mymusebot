import os
from together import Together

api_key = os.environ.get("TOGETHER_API_KEY")
if not api_key:
  raise RuntimeError("API Key missing.")

try:
  client = Together()

  stream = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    messages=[{"role": "user", "content": "What is the capital of India?"}],
    stream=True,
    max_tokens=20,
    temperature=0.2
  )

  for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
except Exception as e:
  print(e)