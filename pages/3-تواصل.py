# pages/3-تواصل.py
# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="تواصل | الشباب يقدر", page_icon="../assets/favicon.png", layout="wide")

st.markdown("## تواصل معنا")
st.write("يسعدنا استقبال ملاحظاتكم ومقترحاتكم، ونثمّن المبادرات التطوعية.")

with st.form("contact_form"):
    name = st.text_input("الاسم")
    phone = st.text_input("رقم الهاتف")
    subject = st.text_input("الموضوع")
    message = st.text_area("الرسالة")
    submitted = st.form_submit_button("إرسال")
    if submitted:
        st.success("تم إرسال رسالتك (Placeholder). سيتم التواصل معك قريبًا.")

st.markdown("### وسائل التواصل الاجتماعي")
cols = st.columns(5)
labels = ["X/Twitter", "Facebook", "Instagram", "YouTube", "TikTok"]
for i, label in enumerate(labels):
    with cols[i]:
        st.link_button(label, "#")
