import streamlit as st
import time

# 1. إعدادات واجهة الموقع
st.set_page_config(page_title="Tech Term Translator", page_icon="🌍", layout="centered")

# --- كود التنسيق (الديزاين الجديد: عناصر موسطنة + بيبي بلو + زرار أسود) ---
st.markdown("""
    <style>
    /* تنسيق المحتوى ليكون في المنتصف تماماً */
    .stApp {
        align-items: center;
    }
    
    /* العنوان الرئيسي الضخم */
    .tech-title {
        color: #89CFF0 !important;
        text-align: center;
        font-size: 60px !important;
        font-weight: 900 !important;
        margin-bottom: 10px !important;
    }
    
    /* العنوان الفرعي */
    .tech-sub {
        color: #5DADE2 !important;
        text-align: center;
        font-size: 28px !important;
        font-weight: 500 !important;
        margin-bottom: 40px !important;
    }

    /* تنسيق صندوق الاختيار (Selectbox) ليكون موسطن */
    div[data-baseweb="select"] {
        width: 100% !important;
        margin: 0 auto;
    }

    /* تنسيق الزرار: ضخم + نص أسود + موسطن */
    div.stButton > button:first-child {
        background-color: #89CFF0 !important;
        color: #000000 !important; /* نص أسود */
        border: none;
        width: 80% !important;
        display: block;
        margin: 30px auto !important; /* مسافة فوق وتحت */
        border-radius: 20px;
        height: 4.2em !important;
        font-size: 22px !important;
        font-weight: 900 !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    
    div.stButton > button:hover {
        background-color: #5DADE2 !important;
        color: white !important;
    }

    /* تنسيق كارت النتيجة */
    .result-card {
        background-color: #F0F8FF;
        padding: 25px;
        border-radius: 15px;
        border-right: 10px solid #89CFF0;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. عرض العناوين الموسطنة
st.markdown('<p class="tech-title">🌍 مترجم التقنيات الذكي 🌟</p>', unsafe_allow_html=True)
st.markdown('<p class="tech-sub">بوابتك لفهم مصطلحات تكنولوجيا التعليم والبرمجة</p>', unsafe_allow_html=True)
st.markdown("---")

# 3. واجهة الإدخال (تحت بعضها في النص)
st.markdown("<h3 style='text-align: center; color: #5DADE2;'>🔎 اختر المصطلح التقني:</h3>", unsafe_allow_html=True)

# قائمة مصطلحات احترافية في تكنولوجيا التعليم
term = st.selectbox("", [
    "LMS (Learning Management System)",
    "Gamification",
    "Blended Learning",
    "Augmented Reality (AR)",
    "Flipped Classroom",
    "Multimedia",
    "Cloud Computing"
])

# الزرار الضخم
if st.button("ترجمة المصطلح وشرحه"):
    with st.spinner("جاري استدعاء القاموس التقني..."):
        time.sleep(1.5)
    
    st.markdown("---")
    
    # 4. عرض النتيجة في "كارت" موسطن
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    
    if term == "LMS (Learning Management System)":
        st.markdown("<h2 style='color: #89CFF0;'>نظام إدارة التعلم</h2>", unsafe_allow_html=True)
        st.write("**الشرح:** هو منصة برمجية (مثل مودل أو كلاسيرا) تُستخدم لتنظيم الدروس، ورفع التكليفات، ومتابعة درجات الطلاب أونلاين.")
        
    elif term == "Gamification":
        st.markdown("<h2 style='color: #89CFF0;'>اللعبنة / التلعيب</h2>", unsafe_allow_html=True)
        st.write("**الشرح:** استخدام عناصر الألعاب (مثل النقاط والمستويات والأوسمة) في بيئة التعليم لزيادة حماس الطلاب وتفاعلهم.")
        
    elif term == "Blended Learning":
        st.markdown("<h2 style='color: #89CFF0;'>التعلم المدمج</h2>", unsafe_allow_html=True)
        st.write("**الشرح:** نظام يجمع بين التعليم التقليدي (داخل الفصل) والتعليم الإلكتروني (عن بُعد) في وقت واحد.")
        
    elif term == "Augmented Reality (AR)":
        st.markdown("<h2 style='color: #89CFF0;'>الواقع المعزز</h2>", unsafe_allow_html=True)
        st.write("**الشرح:** تكنولوجيا تسمح بإسقاط أجسام افتراضية (ثلاثية الأبعاد) داخل البيئة الحقيقية باستخدام كاميرا الموبايل.")
        
    elif term == "Flipped Classroom":
        st.markdown("<h2 style='color: #89CFF0;'>الفصل المقلوب</h2>", unsafe_allow_html=True)
        st.write("**الشرح:** استراتيجية تعليمية يشاهد فيها الطلاب الفيديو التعليمي في المنزل، ويخصص وقت الفصل للنقاش والأنشطة.")
        
    elif term == "Multimedia":
        st.markdown("<h2 style='color: #89CFF0;'>الوسائط المتعددة</h2>", unsafe_allow_html=True)
        st.write("**الشرح:** دمج النص والصوت والصورة والفيديو في وسيلة تعليمية واحدة لتوصيل المعلومة بشكل أفضل.")

    elif term == "Cloud Computing":
        st.markdown("<h2 style='color: #89CFF0;'>الحوسبة السحابية</h2>", unsafe_allow_html=True)
        st.write("**الشرح:** تخزين ومعالجة البيانات على خوادم الإنترنت (مثل Google Drive) بدل الهارد ديسك الشخصي.")

    st.markdown("</div>", unsafe_allow_html=True)

# 5. التذييل
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.caption("مشروع مترجم المصطلحات - قسم تكنولوجيا التعليم 2026")
