import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def tampilkan_halaman():
    # Menampilkan komponen file uploader
    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

    # Jika file diunggah
    if uploaded_file is not None:
        # Membaca data dari file CSV yang diunggah
        data = pd.read_csv(uploaded_file)
        st.success("File berhasil diunggah dan dibaca")

        # Ekstraksi data dari dataframe
        tahun = data.columns[1:].tolist()
        jumlah_penduduk = data.iloc[0, 1:].values

        # Fungsi untuk format angka pada sumbu y
        def format_angka(x, pos):
            return '{:,.0f}'.format(x)

        # Membuat diagram garis
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(tahun, jumlah_penduduk, marker='o')

        # Menambahkan judul dan label
        ax.set_title('Perkembangan Jumlah Penduduk di Tulungagung 2019-2023')
        ax.set_xlabel('Tahun')
        ax.set_ylabel('Jumlah Penduduk')

        # Menambahkan grid dan format angka pada sumbu y
        ax.yaxis.set_major_formatter(FuncFormatter(format_angka))
        ax.grid(True)

        # Menampilkan diagram menggunakan Streamlit
        st.pyplot(fig)
    else:
        st.info("Silakan unggah file CSV.")
