import streamlit as st
import os

# Sayfa Ayarları
st.set_page_config(
    page_title="Snorb Coffee - Dijital Menü", 
    page_icon="☕", 
    layout="centered"
)

# -------------------------------------------------------------------------
# 🎨 1. ARKA PLAN RENGİ VE LİNKLER
# -------------------------------------------------------------------------
ARKA_PLAN_RENGI = "#f2ede0"  

# GitHub'a yüklediğin PDF logonun tam adı
LOGO_DOSYA_ADI = "logo.png" 

MENU_URL = "https://drive.google.com/file/d/1K4G8IqbEMC9MLgpQaunTz0BEZhGSXf6k/view?usp=sharing"
YORUM_URL = "https://share.google/0hW6Q4o13PHapIV3M"
INSTAGRAM_URL = "https://www.instagram.com/snorbcoffee/"
# -------------------------------------------------------------------------

# CRITICAL CSS FIX: Hem arka plan rengini giydiriyoruz hem de logonun beyazlığını yok ediyoruz
st.markdown(f"""
    <style>
    /* Tüm sitenin arka planı */
    .stApp {{
        background-color: {ARKA_PLAN_RENGI} !important;
    }}
    /* Çizgilerin rengi */
    hr {{
        border-top: 1px solid #dcd7c9 !important;
    }}
    /* Logonun etrafındaki beyaz kareyi yok eden sihirli dokunuş */
    .snorb-logo-konteyner img {{
        mix-blend-mode: multiply !important;
        background-color: transparent !important;
    }}
    </style>
""", unsafe_allow_html=True)


# =========================================================================
# 📱 MÜŞTERİ EKRANI
# =========================================================================

# Üst Logo Alanı (Beyazlığı yok eden özel HTML sınıfı içine alındı)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(LOGO_DOSYA_ADI):
        st.markdown(f'<div class="snorb-logo-konteyner">', unsafe_allow_html=True)
        st.image(LOGO_DOSYA_ADI, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("<div style='text-align:center; font-size:40px;'>☕</div>", unsafe_allow_html=True)

# Başlık Alanı
st.markdown("""
    <div style='text-align: center; margin-top: 5px; margin-bottom: 20px;'>
        <h1 style='color: #2c1a12; font-family: "Helvetica Neue", sans-serif; font-size: 30px; font-weight: 800; letter-spacing: -0.5px;'>
            Snorb Coffee
        </h1>
        <p style='color: #614a3e; font-size: 15px; font-weight: 500;'>Dijital Menü</p>
    </div>
    <hr style='margin-bottom: 30px;'>
""", unsafe_allow_html=True)

# 1. Buton: Menü PDF'i
st.markdown(f"""
    <a href="{MENU_URL}" target="_blank" style="text-decoration: none;">
        <div style="background: linear-gradient(135deg, #3d2314, #52301c); color: white; padding: 20px; text-align: center; border-radius: 16px; font-size: 18px; font-weight: bold; margin-bottom: 18px; box-shadow: 0px 4px 12px rgba(61, 35, 20, 0.15); transition: 0.3s;">
            📖 Dijital Menüyü Görüntüle
        </div>
    </a>
""", unsafe_allow_html=True)

# 2. Buton: Google Yorumları
st.markdown(f"""
    <a href="{YORUM_URL}" target="_blank" style="text-decoration: none;">
        <div style="background: linear-gradient(135deg, #ea4335, #fbbc05); color: white; padding: 20px; text-align: center; border-radius: 16px; font-size: 18px; font-weight: bold; margin-bottom: 18px; box-shadow: 0px 4px 12px rgba(234, 67, 53, 0.15); transition: 0.3s;">
            ⭐ Google'da Bizi Değerlendir
        </div>
    </a>
""", unsafe_allow_html=True)

# 3. Buton: Instagram Profil Linki
st.markdown(f"""
    <a href="{INSTAGRAM_URL}" target="_blank" style="text-decoration: none;">
        <div style="background: linear-gradient(135deg, #f94d5a, #833ab4); color: white; padding: 20px; text-align: center; border-radius: 16px; font-size: 18px; font-weight: bold; margin-bottom: 18px; box-shadow: 0px 4px 12px rgba(249, 77, 90, 0.15); transition: 0.3s;">
            📸 Instagram'da Takip Et
        </div>
    </a>
""", unsafe_allow_html=True)

# Alt Sabit Yazı
st.markdown("""
    <div style='text-align: center; margin-top: 60px; color: #8a7f77; font-size: 12px; font-weight: 500;'>
        Hoş Geldiniz • Keyifli Vakit Geçirmeniz Dileğiyle
    </div>
""", unsafe_allow_html=True)
