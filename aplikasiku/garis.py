import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def tampilkan_halaman():

    # Tombol di sidebar untuk kembali ke halaman utama
    with st.sidebar:
        if st.button("Halaman Utama"):
            st.session_state.halaman = 'utama'
            st.experimental_rerun()

    # Menampilkan komponen file uploader
    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

    # Menambahkan tombol Syarat dan Ketentuan
    if st.button("Syarat dan Ketentuan"):
        if st.button("Tutup"):
            st.session_state.show_terms = False
        st.info("Berikut adalah syarat dan ketentuan penggunaan aplikasi:")
        st.text("1. File harus berformat CSV \n2. Untuk contoh isi file CSV seperti gambar ini :")
        st.image("E:/magang/streamlit/foto/image2.png")

    # Jika file diunggah
    if uploaded_file is not None:
        # Membaca data dari file CSV yang diunggah
        data = pd.read_csv(uploaded_file)
        st.success("File berhasil diunggah dan dibaca")

        # Ekstraksi data dari dataframe
        horizontal = data.columns[1:].tolist()
        vertikal = data.iloc[0, 1:].values
        kolom_pertama = data.columns[0]

        # Fungsi untuk format angka pada sumbu y
        def format_angka(x, pos):
            return '{:,.0f}'.format(x)

        # Membuat diagram garis
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(horizontal, vertikal, marker='o')

        # Menambahkan angka detail di atas titik data
        for i, value in enumerate(vertikal):
            ax.annotate(f'{value:,.0f}', xy=(horizontal[i], value), xytext=(0, 5), textcoords='offset points', ha='center')

        # Menambahkan judul
        ax.set_title(f'Diagram Garis {kolom_pertama}')

        # Menambahkan grid dan format angka pada sumbu y
        ax.yaxis.set_major_formatter(FuncFormatter(format_angka))
        ax.grid(True)

        # Menampilkan diagram menggunakan Streamlit
        st.pyplot(fig)
    else:
        st.info("Silakan unggah file CSV.")