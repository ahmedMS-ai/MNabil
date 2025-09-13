# صفحة هبوط انتخابية عربية (RTL) — Streamlit

قالب جاهز لإطلاق صفحة هبوط انتخابية باللغة العربية، مع اتجاه RTL وهوية شبابية قابلة للتبديل من `assets/theme.css`.
يوفر قالبَي Hero: **A** (عمودان) و **B** (خلفية كاملة مع Overlay).

## التشغيل محليًا
```bash
pip install -r requirements.txt
streamlit run app.py
```

## النشر على Streamlit Cloud (خطوات سريعة)
1) اربط المستودع الذي يحوي هذا المشروع.
2) أنشئ تطبيقًا جديدًا واختر `app.py` كنقطة الدخول.
3) تأكد من رفع مجلدات `assets/`, `images/`, `static/`, `.streamlit/` كما هي.
4) غيّر `HERO_VARIANT` في `app.py` لاختيار النمط.
5) انشر واستعمل الرابط العام.

## تخصيص
- الألوان والخط: من `assets/theme.css` (المتغيرات تحت `:root`).
- الأنماط والشبكيّة: من `assets/styles.css`.
- استبدل الصور في مجلد `images/` وملفي `assets/favicon.png` و `static/og-image.png` بموادك.
