
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Fasilitas Umum",
    page_icon="📊",
    layout="wide"
)

# Membaca data
@st.cache_data
def load_data():
    return pd.read_csv("data_fasilitas.csv")

df = load_data()

# Judul dashboard
st.title("Dashboard Fasilitas Umum Kota Bengkulu")
st.write(
    "Visualisasi data simulasi untuk membantu pengguna "
    "memahami kategori, lokasi, dan jumlah pengguna fasilitas."
)

st.info(
    "Catatan: Data pada dashboard ini merupakan data simulasi, "
    "bukan data resmi Kota Bengkulu."
)

# Filter kategori
st.sidebar.header("Filter Data")
kategori_pilihan = st.sidebar.multiselect(
    "Pilih kategori fasilitas:",
    options=sorted(df["kategori"].unique()),
    default=sorted(df["kategori"].unique())
)

data_filter = df[df["kategori"].isin(kategori_pilihan)]

# Ringkasan data
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Jumlah Fasilitas", len(data_filter))

with col2:
    st.metric("Jumlah Pengguna", int(data_filter["jumlah_pengguna"].sum()))

with col3:
    st.metric("Jumlah Kecamatan", data_filter["kecamatan"].nunique())

st.divider()

# Grafik kategori
kiri, kanan = st.columns(2)

with kiri:
    st.subheader("Jumlah Fasilitas per Kategori")
    jumlah_kategori = data_filter["kategori"].value_counts()

    fig, ax = plt.subplots()
    jumlah_kategori.plot(kind="bar", ax=ax)
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Jumlah Fasilitas")
    ax.tick_params(axis="x", rotation=20)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with kanan:
    st.subheader("Jumlah Pengguna per Kecamatan")
    pengguna_kecamatan = (
        data_filter.groupby("kecamatan")["jumlah_pengguna"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots()
    pengguna_kecamatan.plot(kind="bar", ax=ax)
    ax.set_xlabel("Kecamatan")
    ax.set_ylabel("Jumlah Pengguna")
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# Pencarian fasilitas
st.divider()
st.subheader("Daftar Fasilitas")

kata_kunci = st.text_input("Cari nama fasilitas:")

if kata_kunci:
    hasil = data_filter[
        data_filter["nama_fasilitas"].str.contains(
            kata_kunci, case=False, na=False
        )
    ]
else:
    hasil = data_filter

st.dataframe(hasil, use_container_width=True, hide_index=True)

st.caption(
    "Proyek pembelajaran Human-Computer Interaction "
    "and Data Visualization."
)
