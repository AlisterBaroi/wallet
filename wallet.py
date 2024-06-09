import streamlit as st

st.set_page_config(
    page_title="Alister's Online Wallet App", page_icon=":money_bag:", layout="wide"
)


def main():

    st.title("Alister's Online Wallet App")
    uploaded_file = st.file_uploader(
        "Upload a card", type=["jpg", "png"], accept_multiple_files=False
    )

    if uploaded_file is not None:
        st.image(uploaded_file)


if __name__ == "__main__":
    main()
