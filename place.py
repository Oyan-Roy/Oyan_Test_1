import streamlit as st
import openai

# Set your OpenAI API key here
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Streamlit application
st.title('Know a Place')

# Create a text box for user to input the place name
place_name = st.text_input("Enter the name of the place:")

if st.button('Submit'):
    if place_name:
        # Send the place name to the OpenAI API
        try:        
            response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                    {"role": "user", "content": f"Tell me about {place_name}.",
                    },
            ],
        )      
            # Extract and display the response
            about_text = response.choices[0].message.content
            st.subheader('About:')
            st.write(about_text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a place name.")