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
        years = data.columns[1:]
        male_counts = data[data['JENIS KELAMIN'] == 'LAKI-LAKI'].iloc[0, 1:].values
        female_counts = data[data['JENIS KELAMIN'] == 'PEREMPUAN'].iloc[0, 1:].values

        # Membuat diagram batang
        fig, ax = plt.subplots(figsize=(12, 6))

        bar_width = 0.35
        gap = 0.05
        index = range(len(years))

        bars1 = ax.bar(index, male_counts, bar_width, label='LAKI-LAKI')
        bars2 = ax.bar([i + bar_width + gap for i in index], female_counts, bar_width, label='PEREMPUAN')

        ax.set_xlabel('Tahun')
        ax.set_ylabel('Jumlah')
        ax.set_title('Jumlah Penduduk Berdasarkan Jenis Kelamin (2017-2023)', pad=60)
        ax.set_xticks([i + (bar_width + gap) / 2 for i in index])
        ax.set_xticklabels(years)

        # Menempatkan legenda di atas judul
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)

        # Menambahkan angka di atas batang
        for bar in bars1:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}',
                    ha='center', va='bottom')

        for bar in bars2:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}',
                    ha='center', va='bottom')

        plt.xticks(rotation=45)
        plt.tight_layout()

        # Menampilkan diagram menggunakan Streamlit
        st.pyplot(fig)
    else:
        st.info("Silakan unggah file CSV.")
