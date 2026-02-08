import streamlit as st
from PIL import Image
from detector_backend import detect_objects, detect_video

# Sätter sidans titel och layout
st.set_page_config(page_title="Byggarbetsplats-detektor", layout="wide")

# Titel högst upp
st.title("Byggarbetsplats‑detektor")

# Delar sidan i två kolumner (vänster och höger)
tab1, tab2 = st.tabs(["Bilddetektering", "Videodetektering"])

# ---------------- TAB 1: BILD ----------------
with tab1:

    # Bild 
    st.subheader("Ladda upp bild")
    uploaded_file = st.file_uploader("Välj en bild", type=["jpg", "jpeg", "png"], key="image_uploader")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uppladdad bild", use_container_width=True)

        if st.button("Kör bild-detektering"):
            result_image, stats = detect_objects(image)
            st.session_state["result_image"] = result_image
            st.session_state["stats"] = stats

    # Bildresultat 
    if "result_image" in st.session_state:
        st.subheader("Detekterad bild")
        st.image(
            st.session_state["result_image"],
            caption="Detekterat resultat",
            use_container_width=True
        )

        st.subheader("Statistik")
        for key, value in st.session_state["stats"].items():
            st.write(f"{key}: {value}")

# ---------------- TAB 2: VIDEO ----------------
with tab2:

    # Video 
    st.subheader("Ladda upp video")
    video_file = st.file_uploader("Välj en video", type=["mp4", "mov", "avi"], key="video_uploader")

    if video_file is not None:
        st.video(video_file)

        if st.button("Kör video-detektering"):
            st.session_state["video_file"] = video_file

    # Videoresultat (real‑time streaming)
    if "video_file" in st.session_state:
        st.subheader("Videodetektering (real‑time)")
        stframe = st.empty()

        for frame in detect_video(st.session_state["video_file"]):
            stframe.image(frame, channels="BGR", use_container_width=True)
