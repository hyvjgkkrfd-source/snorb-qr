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

# Kodun hata vermemesi için dönüştüreceğimiz yeni şeffaf logonun adı
LOGO_DOSYA_ADI = "snorb_logo_seffaf.png" 

MENU_URL = "https://drive.google.com/file/d/1K4G8IqbEMC9MLgpQaunTz0BEZhGSXf6k/view?usp=sharing"
YORUM_URL = "https://share.google/0hW6Q4o13PHapIV3M"
INSTAGRAM_URL = "https://www.instagram.com/snorbcoffee/"
# -------------------------------------------------------------------------

# Arka plan rengini giydiren CSS (Hatalı mix-blend kodu tamamen kaldırıldı)
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {ARKA_PLAN_RENGI} !important;
    }}
    hr {{
        border-top: 1px solid #dcd7c9 !important;
    }}
    </style>
""", unsafe_allow_html=True)


# =========================================================================
# 📱 MÜŞTERI EKRANI
# =========================================================================

# Üst Logo Alanı
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Otomatik dönüştürülen şeffaf logo varsa onu bas
    if os.path.exists(LOGO_DOSYA_ADI):
        st.image(LOGO_DOSYA_ADI, use_container_width=True)
    # Eğer henüz dönüştürülmediyse orijinal PDF'i kurtarmaya çalış
    elif os.path.exists("Snorb_Coffee_Dikey_Logo_Yesil.pdf"):
        # Arka planda PDF'i şeffaf PNG'ye dönüştüren sihirli kod bloğu
        try:
            import pypdfium2 as pdfium
            from PIL import Image
            import io
            
            pdf = pdfium.PdfDocument("Snorb_Coffee_Dikey_Logo_Yesil.pdf")
            page = pdf[0]
            bitmap = page.render(scale=3)
            pil_img = bitmap.to_pil()
            
            # Beyaz arka planı pürüzsüzce şeffaf (transparent) yapma işlemi
            pil_img = pil_img.convert("RGBA")
            datas = pil_img.getdata()
            newData = []
            for item in datas:
                # Saf beyaz veya beyaza çok yakın olan pikselleri tamamen görünmez yap
                if item[0] > 240 and item[1] > 240 and item[2] > 240:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            pil_img.putdata(newData)
            pil_img.save(LOGO_DOSYA_ADI, "PNG")
            st.rerun()
        except:
            st.markdown("<div style='text-align:center; font-size:40px;'>☕</div>", unsafe_allow_html=True)
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

# Butonlar
st.markdown(f'<a href="{MENU_URL}" target="_blank" style="text-decoration: none;"><div style="background: linear-gradient(135deg, #3d2314, #52301c); color: white; padding: 20px; text-align: center; border-radius: 16px; font-size: 18px; font-weight: bold; margin-bottom: 18px; box-shadow: 0px 4px 12px rgba(61, 35, 20, 0.15);">📖 Dijital Menüyü Görüntüle</div></a>', unsafe_allow_html=True)
st.markdown(f'<a href="{YORUM_URL}" target="_blank" style="text-decoration: none;"><div style="background: linear-gradient(135deg, #ea4335, #fbbc05); color: white; padding: 20px; text-align: center; border-radius: 16px; font-size: 18px; font-weight: bold; margin-bottom: 18px; box-shadow: 0px 4px 12px rgba(234, 67, 53, 0.15);">⭐ Google\'da Bizi Değerlendir</div></a>', unsafe_allow_html=True)
st.markdown(f'<a href="{INSTAGRAM_URL}" target="_blank" style="text-decoration: none;"><div style="background: linear-gradient(135deg, #f94d5a, #833ab4); color: white; padding: 20px; text-align: center; border-radius: 16px; font-size: 18px; font-weight: bold; margin-bottom: 18px; box-shadow: 0px 4px 12px rgba(249, 77, 90, 0.15);">📸 Instagram\'da Takip Et</div></a>', unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; margin-top: 60px; color: #8a7f77; font-size: 12px; font-weight: 500;'>
        Hoş Geldiniz • Keyifli Vakit Geçirmeniz Dileğiyle
    </div>
""", unsafe_allow_html=True)
