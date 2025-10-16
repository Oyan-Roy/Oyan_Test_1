from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b:free",
    messages=[{"role": "user", "content": "Hello"}]
)

print(response.choices[0].message.content)