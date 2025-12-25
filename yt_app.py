import streamlit as st
import yt_dlp
import os
import tempfile

st.title("YouTube Audio Downloader")

url = st.text_input("Paste YouTube link")

if st.button("Download Audio"):
    if not url:
        st.warning("Please paste a YouTube link")
    else:
        with st.spinner("Downloading audio..."):
            # Create temp directory
            with tempfile.TemporaryDirectory() as tmpdir:
                ydl_opts = {
                    "format": "bestaudio/best",
                    "outtmpl": os.path.join(tmpdir, "%(title)s.%(ext)s"),
                    "quiet": True,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    file_path = ydl.prepare_filename(info)

                # Read file into memory
                with open(file_path, "rb") as f:
                    audio_bytes = f.read()

                st.success("Download ready!")

                st.download_button(
                    label="Download Audio",
                    data=audio_bytes,
                    file_name=os.path.basename(file_path),
                    mime="audio/mpeg"
                )

        # File is auto-deleted because TemporaryDirectory is used
