import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def tampilkan_halaman():
    # Menampilkan komponen file uploader
    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

    # Jika file diunggah
    if uploaded_file is not None:
        # Membaca data dari file CSV yang diunggah
        data = pd.read_csv(uploaded_file)
        st.success("File berhasil diunggah dan dibaca")

        # Ekstraksi data dari dataframe
        kecamatan = data['KECAMATAN']
        
        # Menampilkan daftar tahun yang tersedia
        years = data.columns[1:]  # Mengambil semua kolom kecuali kolom pertama ('KECAMATAN')
        selected_year = st.selectbox("Pilih tahun:", years)

        # Ekstraksi jumlah penduduk untuk tahun yang dipilih
        jumlah_penduduk = data[selected_year]

        # Fungsi untuk format angka pada sumbu y
        def format_angka(x, pos):
            return '{:,.0f}'.format(x)

        # Membuat diagram lingkaran
        fig, ax = plt.subplots(figsize=(10, 11))
        ax.pie(jumlah_penduduk, labels=kecamatan, autopct='%1.1f%%', startangle=140)

        # Menambahkan jumlah total penduduk di pojok kanan atas
        total_penduduk = sum(jumlah_penduduk)
        ax.text(1.5, 1.5, f'Total Penduduk: {total_penduduk}', horizontalalignment='right', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

        ax.set_title(f'Jumlah Penduduk {selected_year}')
        ax.axis('equal')

        # Menampilkan diagram menggunakan Streamlit
        st.pyplot(fig)
    else:
        st.info("Silakan unggah file CSV.")
