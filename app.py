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
ARKA_PLAN_RENGI = "#ffe4c3"  

LOGO_DOSYA_ADI = "Snorb_Coffee_Dikey_Logo_Yesil.png" 

MENU_URL = "https://drive.google.com/file/d/1K4G8IqbEMC9MLgpQaunTz0BEZhGSXf6k/view?usp=sharing"
YORUM_URL = "https://share.google/0hW6Q4o13PHapIV3M"
INSTAGRAM_URL = "https://www.instagram.com/snorbcoffee/"
# -------------------------------------------------------------------------

# CRITICAL FIX: GitHub logosunu, sağ alttaki yazıları ve üst barı tamamen gizleyen CSS
st.markdown(f"""
    <style>
    /* Tüm sitenin arka planı */
    .stApp {{
        background-color: {ARKA_PLAN_RENGI} !important;
    }}
    /* Çizgi rengi */
    hr {{
        border-top: 1px solid #e6cbab !important;
    }}
    /* Sağ üstteki GitHub ve Streamlit Menüsünü Gizle */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    stDecoration {{display:none;}}
    
    /* Mobil cihazlarda üstteki boşluğu sıfırlamak için ek temizlik */
    .stAppHeader {{
        display: none !important;
    }}
    .stMainBlockContainer {{
        padding-top: 2rem !important;
    }}
    </style>
""", unsafe_allow_html=True)


# =========================================================================
# 📱 MÜŞTERİ EKRANI (TAMAMEN SADELEŞTİRİLMİŞ)
# =========================================================================

# --- LOGO ALANI ---
if os.path.exists(LOGO_DOSYA_ADI):
    st.image(LOGO_DOSYA_ADI, use_container_width=True)
else:
    st.markdown("<div style='text-align:center; font-size:50px;'>☕</div>", unsafe_allow_html=True)

# --- ARA ÇİZGİ ---
st.markdown("""
    <div style='margin-top: 15px;'></div>
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
