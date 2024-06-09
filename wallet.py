import streamlit as st
import copy

st.set_page_config(
    page_title="Alister's Online Wallet App", page_icon="💰", layout="wide"
)


if "upload_img" not in st.session_state:
    st.session_state.upload_img = None


def main():
    st.title("Alister's Online Wallet App")
    st.markdown(
        """This is the cards section. You can **:blue[upload]** and **:blue[capture]** card images. If you face any issue, feel free to **:orange[refresh]** the page, or **:red[clear]** all data.  
        <br>""",
        unsafe_allow_html=True,
    )

    row_1 = st.columns([1, 1, 2])
    with row_1[0]:
        # st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📁 Upload Image", use_container_width=True):
            input_card("file")

    with row_1[1]:
        # st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📸Take Picture", use_container_width=True):
            input_card("cam")
    with row_1[2]:
        row_2 = st.columns([2, 1, 1])
        with row_2[1]:
            # st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Refresh", use_container_width=True):
                st.rerun()
        with row_2[2]:
            # st.markdown("<br>", unsafe_allow_html=True)
            with st.popover("Clear", use_container_width=True):
                st.markdown("Clear all data?")
                if st.button("Yes", use_container_width=True):
                    st.cache_data.clear()
                    st.session_state.clear()
                    st.cache_resource.clear()
                    st.rerun()

    st.divider()

    st.table()

    if st.session_state.upload_img is not None:
        st.image(st.session_state.upload_img)
        st.session_state.upload_img = None


# @st.cache_resource
@st.experimental_dialog("Take a pic", width="large")
def input_card(item):
    uploaded_file, camera = None, None
    row_9 = st.columns([1, 1])
    with row_9[0]:
        if item == "cam":
            camera = st.camera_input("Take a pic", label_visibility="hidden")
        if item == "file":
            uploaded_file = st.file_uploader(
                "Upload a card",
                type=["jpg", "png"],
                label_visibility="hidden",
            )
            if uploaded_file is not None:
                st.image(uploaded_file)
    with row_9[1]:
        if (uploaded_file is not None) or (camera is not None):
            with st.form("input-card-data"):
                name = st.text_input(
                    "name", placeholder="Full Name", label_visibility="hidden"
                )
                company = st.text_input(
                    "company", placeholder="Company Name", label_visibility="hidden"
                )
                position = st.text_input(
                    "position",
                    placeholder="Position Name",
                    label_visibility="hidden",
                )
                email = st.text_input(
                    "email", placeholder="Contact Email", label_visibility="hidden"
                )
                phone = st.text_input(
                    "phone", placeholder="Contact Number", label_visibility="hidden"
                )
                if st.form_submit_button("Submit"):
                    if item == "file":
                        st.session_state.upload_img = uploaded_file
                        st.rerun()
                    if item == "cam":
                        st.session_state.upload_img = camera.getvalue()
                        st.rerun()


if __name__ == "__main__":
    main()
