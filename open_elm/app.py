import pathlib

import streamlit as st
import open_elm

from inference import generate


def main():
    st.title("NonsEnse")

    model_dir = pathlib.Path(
        "/Users/paul/Models/mlx/model_1_1B_4bit")

    model, tokenizer = open_elm.load_model(model_dir)

    with st.form(key="MyForm"):

        prompt = st.text_input(
            label="Say what? Type yo prompt here:", value="In a hole in the ground there lived")

        temperature = st.slider("How warm?", 0.0, 2.0, value=0.80)

        max_tokens = st.slider("How much word?",
                               2, 512, value=96, step=2)

        submit = st.form_submit_button(label="Let's do this")

    if submit:
        st.markdown("**You said:**")
        st.write(prompt)
        st.markdown("**AI continues with:**")
        st.write_stream(
            generate(
                model,
                tokenizer,
                prompt=prompt,
                max_tokens=max_tokens,
                sampling_temperature=temperature,
            )
        )


main()
