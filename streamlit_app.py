import streamlit as st

# Kelasking Laptop
class Laptop:
    def __init__(self, merek, model, harga, gambar_url):
        self.merek = merek
        self.model = model
        self.harga = harga
        self.gambar_url = gambar_url

    def __str__(self):
        return f"{self.merek.upper()} - {self.model} - Rp{self.harga:,}"

# buat instal data awal
if "data_laptop" not in st.session_state:
    st.session_state.data_laptop = [
        Laptop("Asus", "Zenbook", 15000000, "https://cdn0-production-images-kly.akamaized.net/ho0zRvP6EUas2_iG0_l4_Jyzp2I=/640x360/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/3352378/original/067201500_1610971557-ZenBook_Pro_15_Full.jpg"),
        Laptop("Lenovo", "Thinkpad", 20000000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvJBBt81Pc1vHhlGenZYiD3tNqnGWD1PZeXw&s"),
        Laptop("HP", "Pavilion", 18000000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYKZzVVagVj3B21gajgQtdCItJNnKNn1QWMQ&s"),
        Laptop("Acer", "Aspire", 16000000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6Q6yJYJgFdYkgAXRbdzJoqEks4aAiJFJJew&s"),
        Laptop("Dell", "Inspiron", 17000000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_Zhqjb5N4u_Re0yA1XStyrBI5iIhb4ZIBjw&s"),
    ]

# dih sukirmin ini tuh buat tambah laptop baru
def tambah_laptop():
    st.subheader("➕ Tambah Laptop")
    with st.form("form_tambah"):
        merek = st.text_input("Merek Laptop")
        model = st.text_input("Model Laptop")
        harga = st.number_input("Harga Laptop", min_value=0, step=500000)
        gambar = st.text_input("URL Gambar Laptop (wajib diisi)")
        submitted = st.form_submit_button("Tambah Laptop")
        if submitted:
            if merek and model and gambar:
                laptop_baru = Laptop(merek, model, harga, gambar)
                st.session_state.data_laptop.append(laptop_baru)
                st.success("✅ Laptop berhasil ditambahkan!")

                # Tampilkan data yang baru ditambahkan
                st.markdown("### ✅ Data Laptop Baru:")
                st.markdown(f"**{laptop_baru.merek.upper()} - {laptop_baru.model}**")
                st.image(laptop_baru.gambar_url, width=250)
                st.write(f"💰 Harga: Rp{laptop_baru.harga:,}")
            else:
                st.error("❌ Merek, Model, dan URL Gambar wajib diisi.")

#  untuk menampilkan fungsi laptop YANTO wo kamu i pahamm gaa
def tampilkan_semua():
    st.subheader("📋 Daftar Laptop")
    if not st.session_state.data_laptop:
        st.warning("Belum ada data laptop.")
    else:
        for i, laptop in enumerate(st.session_state.data_laptop, 1):
            with st.container():
                st.markdown(f"### {i}. {laptop.merek.upper()} - {laptop.model}")
                st.image(laptop.gambar_url, width=250)
                st.write(f"💰 Harga: Rp{laptop.harga:,}")

# ini tuu buat mencari laptop aku HEHE
def cari_laptop():
    st.subheader("🔍 Cari Laptop")
    keyword = st.text_input("Masukkan kata kunci (merek/model):")
    if keyword:
        hasil = [
            l for l in st.session_state.data_laptop
            if keyword.lower() in l.merek.lower() or keyword.lower() in l.model.lower()
        ]
        if hasil:
            st.success(f"Ditemukan {len(hasil)} laptop:")
            for i, l in enumerate(hasil, 1):
                st.markdown(f"### {i}. {l.merek.upper()} - {l.model}")
                st.image(l.gambar_url, width=250)
                st.write(f"💰 Harga: Rp{l.harga:,}")
        else:
            st.warning("Tidak ditemukan laptop dengan kata kunci tersebut.")

# untuk ngehapus tau ga sieee 
def hapus_semua():
    if st.button("🗑️ Hapus Semua Data"):
        st.session_state.data_laptop.clear()
        st.success("✅ Semua data laptop berhasil dihapus.")

# Bukan Keluar Tapi selesai awkwkkw
def keluar():
    st.session_state.data_laptop.clear()
    st.markdown(
        """
        <style>
        .rainbow-text {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            background-image: linear-gradient(
                -45deg,
                red,
                orange,
                yellow,
                green,
                cyan,
                blue,
                violet
            );
            background-size: 400%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: rainbow 4s linear infinite;
        }

        @keyframes rainbow {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        </style>

        <div class="rainbow-text">🙏 TERIMAKASIH DATA YANG KAMU BERIKAN SANGAT MEMBANTU 🙏</div>
        """,
        unsafe_allow_html=True
    )
    st.stop()

# ===============================
# STREAMLIT LAYOUT
# ===============================
st.markdown(
    """
    <h1 style='text-align: center; font-size: 36px; white-space: nowrap;'>
        💻 Aplikasi Manajemen Data Laptop💻
    </h1>
    """,
    unsafe_allow_html=True
)

# Tampilan Menu
st.markdown(
    """
    <style>
    /* ANIMASI BINTANG LATAR BELAKANG */
    body::before {
        content: "";
        position: fixed;
        width: 100%;
        height: 100%;
        background: black;
        z-index: -0;
        top: 0;
        left: 0;
        background: radial-gradient(white 1px, transparent 1px),
                    radial-gradient(white 1px, transparent 1px);
        background-position: 0 0, 25px 25px;
        background-size: 50px 50px;
        animation: stars 20s linear infinite;
        opacity: 0.05;
    }

    @keyframes stars {
        from {
            background-position: 0 0, 25px 25px;
        }
        to {
            background-position: -1000px 1000px, -975px 1025px;
        }
    }

    /* MENU */
    .menu-container {
        font-size: 24px;
        font-weight: bold;
        color: var(--text-color);
        margin-bottom: 15px;
    }

    .menu-list {
        font-size: 18px;
        line-height: 5;
        color: var(--text-color);
        list-style-type: none;
        padding-left: 1;
    }
    </style>

    <div class='menu-container'>📋 Pilihan Menu:</div>
    <ul class='menu-list'>
      <li>1️⃣ <b>Tampilkan semua laptop</b> 💻</li>
      <li>2️⃣ <b>Tambah Laptop</b> ➕</li>
      <li>3️⃣ <b>Cari Laptop</b> 🔍</li>
      <li>4️⃣ <b>Hapus Semua Data</b> 🗑️</li>
      <li>5️⃣ <b>Keluar</b> 👋</li>
    </ul>
    """,
    unsafe_allow_html=True
)




#animasi 
st.markdown("""
<style>
.marquee {
  width: 90%;
  overflow: hidden;
  white-space: nowrap;
  box-sizing: border-box;
  animation: marquee 25s linear infinite;
  font-size: 25px;
  color: #00ffff;
  margin-top: 30px;
}

@keyframes marquee {
  0%   { text-indent: 100% }
  70% { text-indent: 0% }
}
</style>

<div class="marquee">
🎉 Selamat datangAplikasi Manajemen Data Laptop | Tambah, Cari, dan Kelola Laptop Anda dengan Mudah! di kerjakan oleh 24.02.1153 24.02.1119 24.02.1124 💻
</div>
""", unsafe_allow_html=True)


#animasi harus nya sie karakter




menu = st.text_input("Masukkan angka menu (1-5):")

if menu == "1":
    tampilkan_semua()
elif menu == "2":
    tambah_laptop()
elif menu == "3":
    cari_laptop()
elif menu == "4":
    hapus_semua()
elif menu == "5":
    keluar()
elif menu != "":
    st.error("⚠️⚠️ Masukkan hanya angka 1 - 5.")
