import streamlit as st

from streamlit_gallery import apps, components
from streamlit_gallery.utils.page import page_group

def main():
    page = page_group("p")

    with st.sidebar:
        st.title("🌱 Simantab")

        with st.expander("🏕️ LAPANGAN"):
            page.item("Dokumen Dikembalikan", components.disqus)
            page.item("Rating PML", components.ace_editor)

        with st.expander("✨ EDITING CODING", True):
            page.item("Progres Petugas Editing Coding", apps.gallery, default=True)
            page.item("Progres Menurut Wilayah", components.quill_editor)
            #page.item("Elements⭐", components.elements)

        with st.expander("🧩 ENTRI"):
            page.item("Progres Operator Entri", components.ace_editor)
            #page.item("Quill editor", components.quill_editor)
            #page.item("React player", components.react_player)

    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="Simantab", page_icon="🌱", layout="wide")
    main()
