import os
from time import sleep

import streamlit as st
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def main():
    client = get_client()
    model = "mistral-small-2312"

    with st.form(key="MyForm"):
        t = "What is the best French cheese for a scientist?"
        prompt = st.text_input(label="Say what?", value=t)
        submit = st.form_submit_button(label="Let's do this")

    if submit:
        chat_response = client.chat(
            model=model,
            messages=[ChatMessage(
                role="user", content=prompt)],
        )
        t = chat_response.choices[0].message.content
        st.write_stream(str_to_stream(t))


def get_client():
    api_key = os.environ["MISTRAL_API_KEY"]
    return MistralClient(api_key=api_key)


def str_to_stream(text: str):
    for word in text.split(" "):
        yield word + " "
        sleep(0.02)


if __name__ == "__main__":
    main()
