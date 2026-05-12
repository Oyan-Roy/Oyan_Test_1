import streamlit as st
from openai import OpenAI
from openai._exceptions import RateLimitError

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

st.title("Welcome to AIpedia! Ask Anything")
user_input = st.text_area("Enter your question:")

if st.button("Submit") and user_input.strip():
    with st.spinner("Thinking..."):
        completion = client.chat.completions.create(
            model= "openai/gpt-oss-120b:free",
            messages= [
                {"role": "user", "content": user_input}
            ]
        )
        response = completion.choices[0].message.content
        st.markdown("### Response:")
        st.write(response)
