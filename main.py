import streamlit as st

# Fungsi untuk halaman utama
def halaman_utama():
    st.title("Selamat Datang")
    if st.button("Masuk ke Halaman Perbandingan Jumlah Penduduk"):
        st.session_state['halaman'] = 'penduduk'
    if st.button("Masuk ke Halaman Perbandingan Jumlah Penduduk Berdasarkan Jenis Kelamin"):
        st.session_state['halaman'] = 'jk'
    if st.button("Masuk ke Halaman Perkembangan Jumlah Penduduk"):
        st.session_state['halaman'] = 'perkembangan'

# Menentukan halaman yang akan ditampilkan berdasarkan status aplikasi
if 'halaman' not in st.session_state:
    st.session_state['halaman'] = 'utama'

if st.session_state['halaman'] == 'utama':
    halaman_utama()
elif st.session_state['halaman'] == 'penduduk':
    import penduduk
    penduduk.tampilkan_halaman()
elif st.session_state['halaman'] == 'jk':
    import jk
    jk.tampilkan_halaman()
elif st.session_state['halaman'] == 'perkembangan':
    import perkembangan
    perkembangan.tampilkan_halaman()
