import streamlit as st
import os

# Sayfa Ayarları (Mobil Öncelikli Şık Tasarım)
st.set_page_config(
    page_title="Snorb Coffee - Dijital Menü", 
    page_icon="☕", 
    layout="centered"
)

# -------------------------------------------------------------------------
# 🎨 1. ARKA PLAN RENGİ VE LİNKLER
# -------------------------------------------------------------------------
ARKA_PLAN_RENGI = "#ffe4c3"  # Sıcak şeftali/krem tonu

# Logonun arka planını bu renge boyayıp ya da şeffaf yapıp yüklediğinde 
# adı neyse buraya onu yaz (Örn: logo.png veya logo.jpg)
LOGO_DOSYA_ADI = "Snorb_Coffee_Dikey_Logo_Yesil.png" 

MENU_URL = "https://drive.google.com/file/d/1K4G8IqbEMC9MLgpQaunTz0BEZhGSXf6k/view?usp=sharing"
YORUM_URL = "https://share.google/0hW6Q4o13PHapIV3M"
INSTAGRAM_URL = "https://www.instagram.com/snorbcoffee/"
# -------------------------------------------------------------------------

# Arka plan rengini tüm siteye giydiren saf CSS kodu
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {ARKA_PLAN_RENGI} !important;
    }}
    hr {{
        border-top: 1px solid #e6cbab !important;
    }}
    </style>
""", unsafe_allow_html=True)


# =========================================================================
# 📱 MÜŞTERİ EKRANI (SAFI KAFE SİTESİ)
# =========================================================================

# --- LOGO ALANI (BOYUTU ARTTIRILDI) ---
# Sütun kısıtlamasını kaldırıp logoyu doğrudan ekrana bastık, böylece alanı daha büyük kaplayacak
if os.path.exists(LOGO_DOSYA_ADI):
    st.image(LOGO_DOSYA_ADI, use_container_width=True)
else:
    st.markdown("<div style='text-align:center; font-size:50px;'>☕</div>", unsafe_allow_html=True)

# --- BAŞLIK ALANI (EKSTRA YAZI KALDIRILDI) ---
# Alttaki büyük "Snorb Coffee" yazısı silindi, sadece şık bir alt başlık ve çizgi bırakıldı
st.markdown("""
    <div style='text-align: center; margin-top: 10px; margin-bottom: 15px;'>
        <p style='color: #614a3e; font-size: 16px; font-weight: 600; letter-spacing: 0.5px;'>DİJİTAL MENÜ</p>
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
