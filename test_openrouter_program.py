import streamlit as st
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

st.title("Welcome to AIpedia! Ask Anything")
user_input = st.text_area("Enter your question:")

if st.button("Submit") and user_input.strip():
    with st.spinner("Thinking..."):
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        response = completion.choices[0].message.content
        st.markdown("### Response:")
        st.write(response)