# app.py
# -*- coding: utf-8 -*-
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="الشباب يقدر | حملة الأستاذ محمد نبيل",
    page_icon="assets/favicon.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ====== تحميل الثيم والأنماط ======
def load_css():
    theme_css = Path("assets/theme.css").read_text(encoding="utf-8")
    styles_css = Path("assets/styles.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{theme_css}\n{styles_css}</style>", unsafe_allow_html=True)

load_css()

# خط عربي من Google (يمكن استبداله بـ Tajawal من theme.css)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;800;900&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ====== متغير التحكم في الـHero ======
HERO_VARIANT = "A"  # "A" أو "B"

# ====== بيانات قابلة للتخصيص ======
CAMPAIGN_SLOGAN = "الشباب يقدر"
CANDIDATE_NAME  = "الأستاذ محمد نبيل"
DISTRICT_NAME   = "الدائرة العمرانية"
PROGRAM_INTRO = (
    "أتعهدُ بخدمة أبناء الدائرة العمرانية بإدارة شفافة ومشاركة مجتمعية فاعلة، "
    "وتسريع المشاريع الخدمية مع تمكين الشباب والمرأة، وتطوير البنية التحتية الرقمية، "
    "وتحسين جودة الحياة عبر مبادرات واقعية قابلة للقياس."
)
PILLARS = [
    ("icon-services.svg", "الخدمات الأساسية", "رفع كفاءة الخدمات البلدية والصحية والتعليمية عبر خطط تنفيذ واضحة."),
    ("icon-infra.svg", "البنية التحتية", "تحسين الطرق والإنارة والصرف، وتوسيع الشبكات الذكية."),
    ("icon-youth.svg", "تمكين الشباب", "مسارات تدريب وتوظيف وريادة أعمال ودعم المبادرات الطلابية."),
    ("icon-women.svg", "دعم المرأة", "تمكين المشاركة الاقتصادية والاجتماعية مع برامج حضانة ومساندة."),
    ("icon-transparency.svg", "الشفافية", "منصّات متابعة المشاريع، نشر التقارير، وتفعيل المساءلة."),
    ("icon-local.svg", "التنمية المحلية", "تشجيع الاستثمار المجتمعي والسياحة الصغيرة والحرف المحلية."),
]
SOCIALS = {
    "X/Twitter": "#",
    "Facebook": "#",
    "Instagram": "#",
    "YouTube": "#",
    "TikTok": "#",
}

# ====== الشريط الجانبي ======
with st.sidebar:
    st.markdown("### التنقّل السريع")
    st.page_link("app.py", label="الصفحة الرئيسية")
    st.page_link("pages/1-عن-المرشح.py", label="عن المرشّح")
    st.page_link("pages/2-البرنامج.py", label="البرنامج")
    st.page_link("pages/3-تواصل.py", label="تواصل")
    st.markdown("---")
    st.markdown("### إجراءات سريعة")
    st.page_link("pages/3-تواصل.py", label="انضم/تطوّع")
    st.page_link("pages/3-تواصل.py", label="تواصل")
    st.markdown("---")
    chosen = st.radio("نمط الـHero", options=["A", "B"], index=0, horizontal=True)
    st.caption("لتثبيت النمط على الخادم غيّر HERO_VARIANT أعلى app.py")

# ====== HERO A ======
def hero_A():
    with st.container():
        st.markdown('<section class="hero hero--A" dir="rtl">', unsafe_allow_html=True)
        col_text, col_img = st.columns([7, 5], gap="large")
        with col_text:
            st.markdown(f"""
            <div class="hero__text">
                <div class="badge">{CAMPAIGN_SLOGAN}</div>
                <h1 class="hero__title">{CANDIDATE_NAME}</h1>
                <p class="hero__subtitle">{DISTRICT_NAME}</p>
                <p class="hero__lead">{PROGRAM_INTRO}</p>
                <div class="hero__cta">
                    <a class="btn btn--primary" href="" onclick="return false;">انضم/تطوّع</a>
                    <a class="btn btn--ghost" href="" onclick="return false;">تواصل</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            # أزرار تعمل فعليًا (Streamlit APIs)
            c1, c2 = st.columns([1,1])
            with c1:
                if st.button("انضم/تطوّع ↗", key="joinA"):
                    st.switch_page("pages/3-تواصل.py")
            with c2:
                if st.button("تواصل ↗", key="contactA"):
                    st.switch_page("pages/3-تواصل.py")
        with col_img:
            st.image("images/candidate-hero.jpg", use_container_width=True, caption="صورة المرشّح", output_format="auto")
        st.markdown('</section>', unsafe_allow_html=True)

# ====== HERO B ======
def hero_B():
    st.markdown(f"""
    <section class="hero hero--B" role="banner" aria-label="قسم المقدمة">
        <div class="hero__bg" style="background-image:url('images/candidate-hero.jpg');" aria-hidden="true"></div>
        <div class="hero__overlay"></div>
        <div class="hero__center">
            <div class="badge">{CAMPAIGN_SLOGAN}</div>
            <h1 class="hero__title">{CANDIDATE_NAME}</h1>
            <p class="hero__subtitle">{DISTRICT_NAME}</p>
            <p class="hero__lead">{PROGRAM_INTRO}</p>
        </div>
    </section>
    """, unsafe_allow_html=True)
    # أزرار تعمل فعليًا أسفل الـHero
    c1, c2 = st.columns([1,1])
    with c1:
        if st.button("انضم/تطوّع ↗", key="joinB"):
            st.switch_page("pages/3-تواصل.py")
    with c2:
        if st.button("تواصل ↗", key="contactB"):
            st.switch_page("pages/3-تواصل.py")

# ====== الأقسام ======
def section_overview():
    with st.container():
        st.markdown("### نظرة عامة على البرنامج")
        st.write(
            "تركّز حملتنا على حلول عملية وسريعة الأثر، مع متابعة أسبوعية علنية لمؤشرات الأداء، "
            "وشراكات فاعلة مع المجتمع المدني والقطاع الخاص."
        )

def section_pillars():
    st.markdown("### محاور البرنامج الستة")
    cols = st.columns(3, gap="large")
    for i, (icon, title, desc) in enumerate(PILLARS):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card" role="article" aria-label="{title}">
                <img class="card__icon" src="images/{icon}" alt="{title}">
                <div class="card__body">
                    <h4 class="card__title">{title}</h4>
                    <p class="card__text">{desc}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

def section_fast_contact():
    with st.container():
        st.markdown("### تواصل سريع")
        with st.expander("نموذج تواصل مبسّط (Placeholder)"):
            name = st.text_input("الاسم")
            phone = st.text_input("رقم الهاتف")
            msg = st.text_area("رسالتك")
            sent = st.button("إرسال")
            if sent:
                st.success("شكرًا لتواصلك! (Placeholder — اربطه بنظامك لاحقًا)")

        st.markdown("#### حسابات الحملة (روابط مبدئية):")
        scols = st.columns(len(SOCIALS))
        for idx, (label, url) in enumerate(SOCIALS.items()):
            with scols[idx]:
                st.link_button(label, url)

def section_join_cta():
    with st.container():
        st.markdown("### انضم/تطوّع")
        st.write("سجّل رغبتك في الانضمام إلى فرق المتطوعين أو مجموعات الدعم الميداني والإعلامي.")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("الاسم الكامل")
            st.text_input("العمر")
            st.text_input("المنطقة")
        with col2:
            st.selectbox("مجال الاهتمام", ["الميدان", "الإعلام الرقمي", "رصد الاحتياجات", "الدعم اللوجستي"])
            st.text_area("ملاحظات إضافية")
        if st.button("تسجيل"):
            st.success("تم استلام بياناتك بنجاح (Placeholder).")

def footer():
    st.markdown("""
    <footer class="footer" role="contentinfo">
        <div class="footer__brand">
            <img src="images/logo.png" alt="شعار الحملة" />
            <span>#الشباب_يقدر</span>
        </div>
        <div class="footer__copy">
            © جميع الحقوق محفوظة — حملة الأستاذ محمد نبيل.
        </div>
    </footer>
    """, unsafe_allow_html=True)

# ====== عرض الـHero ======
variant_to_use = (chosen if chosen in ("A", "B") else HERO_VARIANT)
if variant_to_use == "A":
    hero_A()
else:
    hero_B()

# ====== بقية الصفحة ======
section_overview()
section_pillars()
section_fast_contact()
section_join_cta()
footer()
