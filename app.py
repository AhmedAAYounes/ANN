import streamlit as st
import time

# 1. إعدادات واجهة الموقع
st.set_page_config(page_title="Tech Term Translator", page_icon="🌍", layout="centered")

# --- كود التنسيق المحدث (عناوين هادية + زرار أسود مقاس الجملة) ---
st.markdown("""
    <style>
    .tech-title {
        color: #89CFF0 !important;
        text-align: center;
        font-size: 45px !important;
        font-weight: 900 !important;
        margin-bottom: 10px !important;
    }
    .tech-sub {
        color: #5DADE2 !important;
        text-align: center;
        font-size: 20px !important;
        font-weight: 500 !important;
        margin-bottom: 30px !important;
    }
    div.stButton {
        text-align: center;
    }
    div.stButton > button:first-child {
        background-color: #89CFF0 !important;
        color: #000000 !important; /* نص أسود */
        border: none;
        padding: 0px 30px !important;
        width: auto !important;
        min-width: 180px;
        border-radius: 20px;
        height: 3.2em !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        margin: 20px auto !important;
    }
    div.stButton > button:hover {
        background-color: #5DADE2 !important;
        color: white !important;
    }
    .result-card {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 15px;
        border-right: 8px solid #89CFF0;
        text-align: center;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. العناوين
st.markdown('<p class="tech-title">🌍 قاموس المصطلحات الذكي</p>', unsafe_allow_html=True)
st.markdown('<p class="tech-sub">دليلك المبسط لفهم أشهر المسميات في عالم التكنولوجيا</p>', unsafe_allow_html=True)
st.markdown("---")

# 3. الاختيارات
st.markdown("<p style='text-align: center; color: #5DADE2; font-weight: bold;'>(المصطلحات)</p>", unsafe_allow_html=True)

term = st.selectbox("", [
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "Graphic Designer",
    "Cybersecurity Specialist",
    "AI Engineer (Prompt Engineer)",
    "UI/UX Designer"
], label_visibility="collapsed")

# 4. زر شرح المصطلح
if st.button("شرح المصطلح"):
    with st.spinner("جاري جلب المعلومات..."):
        time.sleep(1)
    
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    
    if term == "Frontend Developer":
        st.markdown("<h2 style='color: #89CFF0;'>مطور واجهة المستخدم</h2>", unsafe_allow_html=True)
        st.write("""**الشرح:** هو المبرمج المسؤول عن كل شيء تراه بعينك في الموقع (الأزرار، الألوان، الخطوط، والتنسيق) باستخدام HTML و CSS و JavaScript.""")
        
    elif term == "Backend Developer":
        st.markdown("<h2 style='color: #89CFF0;'>مطور خلفية الموقع</h2>", unsafe_allow_html=True)
        st.write("""**الشرح:** هو الجندي المجهول المسؤول عن "عقل" الموقع (قواعد البيانات، السيرفرات، والعمليات المنطقية) التي لا يراها المستخدم.""")
        
    elif term == "Full Stack Developer":
        st.markdown("<h2 style='color: #89CFF0;'>المطور الشامل</h2>", unsafe_allow_html=True)
        st.write("""**الشرح:** هو مبرمج "جوكر" يستطيع العمل على الواجهة الأمامية (Frontend) والخلفية (Backend) في نفس الوقت.""")
        
    elif term == "Graphic Designer":
        st.markdown("<h2 style='color: #89CFF0;'>مصمم الجرافيك</h2>", unsafe_allow_html=True)
        st.write("""**الشرح:** الفنان المسؤول عن تصميم الصور، الشعارات (Logos)، والهوية البصرية التي تجذب العين باستخدام برامج مثل Photoshop.""")
        
    elif term == "Cybersecurity Specialist":
        st.markdown("<h2 style='color: #89CFF0;'>أخصائي الأمن السيبراني</h2>", unsafe_allow_html=True)
        st.write("""**الشرح:** هو "حارس الأمن" الرقمي الذي يحمي المواقع والبيانات من الاختراق والهجمات الإلكترونية.""")
        
    elif term == "AI Engineer (Prompt Engineer)":
        st.markdown("<h2 style='color: #89CFF0;'>مهندس الذكاء الاصطناعي</h2>", unsafe_allow_html=True)
        st.write("""**الشرح:** هو المبرمج الذي يبني أنظمة الذكاء الاصطناعي، أو الشخص الذي يعرف كيف يوجه "الأوامر" للذكاء الاصطناعي ليخرج أفضل النتائج.""")

    elif term == "UI/UX Designer":
        st.markdown("<h2 style='color: #89CFF0;'>مصمم تجربة وواجهة المستخدم</h2>", unsafe_allow_html=True)
        st.write("""**الشرح:** الشخص المسؤول عن دراسة سلوك المستخدم وتصميم واجهة سهلة ومريحة تجعل العميل سعيداً أثناء استخدامه للتطبيق.""")

    st.markdown("</div>", unsafe_allow_html=True)

# 5. التذييل
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
st.caption("مشروع مترجم المصطلحات التقنية - 2026")
