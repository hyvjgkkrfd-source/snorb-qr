import streamlit as st

# Sayfa Ayarları (Mobil Öncelikli Şık Tasarım)
st.set_page_config(
    page_title="Vadi Cafe - Dijital Menü", 
    page_icon="☕", 
    layout="centered"
)

# -------------------------------------------------------------------------
# 🛠️ KAFE BİLGİLERİNİZİ VE LİNKLERİNİZİ BURADAN DEĞİŞTİREBİLİRSİNİZ
# -------------------------------------------------------------------------
KAFE_ADI = "Snorb Coffee" 
MENU_URL = "https://drive.google.com/file/d/1K4G8IqbEMC9MLgpQaunTz0BEZhGSXf6k/view?usp=sharing" # Google Drive Menü PDF Linki
YORUM_URL = "https://share.google/0hW6Q4o13PHapIV3M"         # Google Haritalar Yorum Linki
INSTAGRAM_URL = "https://www.instagram.com/snorbcoffee/"                               # Instagram Profil Linki
# -------------------------------------------------------------------------

# =========================================================================
# 📱 MÜŞTERİNİN TELEFONUNDA AÇILACAK OLAN ANA İNTERNET SİTESİ
# =========================================================================

# Üst Başlık ve Karşılama Alanı
st.markdown(f"""
    <div style='text-align: center; margin-top: 35px; margin-bottom: 25px;'>
        <div style='font-size: 55px; margin-bottom: 10px;'>☕</div>
        <h1 style='color: #1a202c; font-family: "Helvetica Neue", sans-serif; font-size: 32px; font-weight: 800; letter-spacing: -0.5px;'>
            {KAFE_ADI}
        </h1>
        <p style='color: #4a5568; font-size: 16px; font-weight: 500;'>Dijital Menü ve Sosyal Medya Platformu</p>
    </div>
    <hr style='border-top: 1px solid #e2e8f0; margin-bottom: 30px;'>
""", unsafe_allow_html=True)

# 1. Buton: Menü PDF'i
st.markdown(f"""
    <a href="{MENU_URL}" target="_blank" style="text-decoration: none;">
        <div style="background: linear-gradient(135deg, #1e3c72, #2a5298); color: white; padding: 20px; text-align: center; border-radius: 16px; font-size: 18px; font-weight: bold; margin-bottom: 18px; box-shadow: 0px 4px 12px rgba(30, 60, 114, 0.2); transition: 0.3s;">
            📖 Dijital Menüyü Görüntüle
        </div>
    </a>
""", unsafe_allow_html=True)

# 2. Buton: Google Yorumları
st.markdown(f"""
    <a href="{YORUM_URL}" target="_blank" style="text-decoration: none;">
        <div style="background: linear-gradient(135deg, #ea4335, #fbbc05); color: white; padding: 20px; text-align: center; border-radius: 16px; font-size: 18px; font-weight: bold; margin-bottom: 18px; box-shadow: 0px 4px 12px rgba(234, 67, 53, 0.2); transition: 0.3s;">
            ⭐ Google'da Bizi Değerlendir
        </div>
    </a>
""", unsafe_allow_html=True)

# 3. Buton: Instagram Profil Linki
st.markdown(f"""
    <a href="{INSTAGRAM_URL}" target="_blank" style="text-decoration: none;">
        <div style="background: linear-gradient(135deg, #f94d5a, #833ab4); color: white; padding: 20px; text-align: center; border-radius: 16px; font-size: 18px; font-weight: bold; margin-bottom: 18px; box-shadow: 0px 4px 12px rgba(249, 77, 90, 0.2); transition: 0.3s;">
            📸 Instagram'da Takip Et
        </div>
    </a>
""", unsafe_allow_html=True)

# Alt Sabit Yazı
st.markdown("""
    <div style='text-align: center; margin-top: 70px; color: #a0aec0; font-size: 12px; font-weight: 500;'>
        Hoş Geldiniz • Keyifli Vakit Geçirmeniz Dileğiyle
    </div>
""", unsafe_allow_html=True)
