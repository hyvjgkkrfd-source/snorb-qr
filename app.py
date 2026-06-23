import streamlit as st
import qrcode
from io import BytesIO

# Sayfa Genişliği ve Tarayıcı Başlığı
st.set_page_config(
    page_title="Dijital Menü & QR Sistem", 
    page_icon="☕", 
    layout="centered"
)

# -------------------------------------------------------------------------
# 🛠️ KAFE BİLGİLERİNİZİ VE LİNKLERİNİZİ BURADAN AYARLAYIN
# Google Drive'a yüklediğin menü PDF'inin paylaşım linkini MENU_URL kısmına yapıştır.
# -------------------------------------------------------------------------
KAFE_ADI = "Snorb Coffee" 
MENU_URL = "https://drive.google.com/file/d/1K4G8IqbEMC9MLgpQaunTz0BEZhGSXf6k/view?usp=sharing" # Buraya Drive linkini koy
YORUM_URL = "https://share.google/0hW6Q4o13PHapIV3M"         # Google Haritalar Yorum Linki
INSTAGRAM_URL = "https://www.instagram.com/snorbcoffee/"                               # Instagram Profil Linki
# -------------------------------------------------------------------------

# URL parametresi kontrolü (Müşteri ekranı mı, yönetim ekranı mı?)
query_params = st.query_params

if "page" in query_params and query_params["page"] == "menu":
    # =========================================================================
    # 📱 1. EKRAN: MÜŞTERİNİN TELEFONUNDA AÇILACAK OLAN LİNK TREE ARAYÜZÜ
    # =========================================================================
    
    st.markdown(f"""
        <div style='text-align: center; margin-top: 25px; margin-bottom: 20px;'>
            <div style='font-size: 50px;'>☕</div>
            <h1 style='color: #1a202c; font-family: "Helvetica Neue", sans-serif; font-size: 28px; font-weight: 800;'>
                {KAFE_ADI}
            </h1>
            <p style='color: #718096; font-size: 15px;'>Dijital Menü ve Sosyal Medya Paneli</p>
        </div>
        <hr style='border-top: 1px solid #e2e8f0; margin-bottom: 25px;'>
    """, unsafe_allow_html=True)

    # Buton 1: PDF Menü Linki
    st.markdown(f"""
        <a href="{MENU_URL}" target="_blank" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #2c3e50, #3498db); color: white; padding: 18px; text-align: center; border-radius: 14px; font-size: 17px; font-weight: bold; margin-bottom: 15px; box-shadow: 0px 4px 10px rgba(52, 152, 219, 0.2);">
                📖 PDF Menüyü Görüntüle
            </div>
        </a>
    """, unsafe_allow_html=True)

    # Buton 2: Google Yorumları
    st.markdown(f"""
        <a href="{YORUM_URL}" target="_blank" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #ea4335, #fbbc05); color: white; padding: 18px; text-align: center; border-radius: 14px; font-size: 17px; font-weight: bold; margin-bottom: 15px; box-shadow: 0px 4px 10px rgba(234, 67, 53, 0.2);">
                ⭐ Google'da Bizi Değerlendir
            </div>
        </a>
    """, unsafe_allow_html=True)

    # Buton 3: Instagram Takip
    st.markdown(f"""
        <a href="{INSTAGRAM_URL}" target="_blank" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #833ab4, #fd1d1d); color: white; padding: 18px; text-align: center; border-radius: 14px; font-size: 17px; font-weight: bold; margin-bottom: 15px; box-shadow: 0px 4px 10px rgba(253, 29, 29, 0.2);">
                📸 Instagram'da Takip Et
            </div>
        </a>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: center; margin-top: 60px; color: #a0aec0; font-size: 11px;'>
            Sürekli Aktif Bulut QR Sistemi v2.0
        </div>
    """, unsafe_allow_html=True)

else:
    # =========================================================================
    # 🛠️ 2. EKRAN: SENİN GİRECEĞİN QR KOD GENERATOR PANELİ
    # =========================================================================
    st.markdown("""
        <div style='text-align: center; padding-top: 10px;'>
            <h2 style='color: #2d3748;'>⚙️ Masa QR Kod Yönetim Paneli</h2>
            <p style='color: #4a5568;'>Masalara basılacak tek bir QR kodu buradan indirebilirsiniz.</p>
        </div>
        <hr>
    """, unsafe_allow_html=True)

    # NOT: Streamlit uygulamanı kurduktan sonra sana vereceği linki aşağıya yazacaksın!
    mevcut_site_adresi = "https://qr-kod-tav.streamlit.app"
    musteri_yonlendirme_linki = f"{mevcut_site_adresi}?page=menu"

    st.warning(f"🔗 Müşterilerin telefonla gideceği adres:\n{musteri_yonlendirme_linki}")

    if st.button("🚀 Masalar İçin Kalıcı QR Kodu Oluştur", use_container_width=True):
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(musteri_yonlendirme_linki)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#1a202c", back_color="white")

        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.markdown("<br><center>", unsafe_allow_html=True)
        st.image(byte_im, width=250, caption="Masalara Basılacak QR Kod")
        st.markdown("</center>", unsafe_allow_html=True)

        st.download_button(
            label="📥 QR Kodu İndir (PNG)",
            data=byte_im,
            file_name="kafe_masa_qr.png",
            mime="image/png",
            use_container_width=True
        )
