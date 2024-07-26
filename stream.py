import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
file_path = "jumlah penduduk 2023.csv"
data = pd.read_csv(file_path)

# Ekstraksi data dari dataframe
kecamatan = data['KECAMATAN']
jumlah_penduduk_2023 = data['2023']

# Fungsi untuk format angka pada sumbu y
def format_angka(x, pos):
    return '{:,.0f}'.format(x)

# Membuat diagram lingkaran
fig, ax = plt.subplots(figsize=(10, 11))
ax.pie(jumlah_penduduk_2023, labels=kecamatan, autopct='%1.1f%%', startangle=140)

# Menambahkan jumlah total penduduk di pojok kanan atas
total_penduduk = sum(jumlah_penduduk_2023)
ax.text(1.5, 1.5, f'Total Penduduk: {total_penduduk}', horizontalalignment='right', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

ax.set_title('Jumlah Penduduk 2023')
ax.axis('equal')

# Menampilkan diagram menggunakan Streamlit
st.pyplot(fig)