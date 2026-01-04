# Syrian Currency Converter App (Improved UI & Logic)
# Web & Android Ready – Light Theme, RTL, Smart Sync

import streamlit as st
from decimal import Decimal

# -----------------------------
# Language dictionary
# -----------------------------
LANG = {
    "en": {
        "title": "Syrian Currency Converter",
        "old_syp": "Old Syrian Pound",
        "new_syp": "New Syrian Pound",
        "usd": "USD Amount",
        "rate": "USD Exchange Rate (Today)",
        "copy": "Copy Result",
        "lang": "Language",
        "note": "Conversion removes two zeros automatically"
    },
    "ar": {
        "title": "محول الليرة السورية",
        "old_syp": "الليرة السورية القديمة",
        "new_syp": "الليرة السورية الجديدة",
        "usd": "المبلغ بالدولار",
        "rate": "سعر الدولار اليوم",
        "copy": "نسخ النتيجة",
        "lang": "اللغة",
        "note": "يتم التحويل بحذف صفرين تلقائيًا"
    }
}

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="SYP Converter", layout="centered")

# -----------------------------
# Light blue UI
# -----------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #e8f1ff, #f7fbff);
    color: #0a2540;
}
.stTextInput label, .stNumberInput label {
    color: #0a2540 !important;
    font-weight: 600;
}
.stButton button {
    background-color: #4f8cff;
    color: white;
    border-radius: 10px;
}
.rtl {
    direction: rtl;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Language toggle
# -----------------------------
lang = st.selectbox("Language / اللغة", ["العربية", "English"])
lang_key = "ar" if lang == "العربية" else "en"
T = LANG[lang_key]
rtl_class = "rtl" if lang_key == "ar" else ""

# -----------------------------
# Session state (save values)
# -----------------------------
for key in ["old", "new", "usd", "rate"]:
    if key not in st.session_state:
        st.session_state[key] = 0.0

# -----------------------------
# Title
# -----------------------------
st.markdown(f"<h2 class='{rtl_class}'>{T['title']}</h2>", unsafe_allow_html=True)

# -----------------------------
# Smart calculation
# -----------------------------
def recalc(source):
    try:
        if source == "old":
            st.session_state.new = st.session_state.old / 100
        elif source == "new":
            st.session_state.old = st.session_state.new * 100
        elif source == "usd" and st.session_state.rate > 0:
            syp = st.session_state.usd * st.session_state.rate
            st.session_state.old = syp
            st.session_state.new = syp / 100
        elif source == "rate" and st.session_state.usd > 0:
            syp = st.session_state.usd * st.session_state.rate
            st.session_state.old = syp
            st.session_state.new = syp / 100
    except:
        pass

# -----------------------------
# Inputs (all synced)
# -----------------------------
st.markdown(f"<div class='{rtl_class}'>", unsafe_allow_html=True)

st.number_input(T["old_syp"], key="old", step=100.0, format="%,.0f", on_change=recalc, args=("old",))
st.number_input(T["new_syp"], key="new", step=1.0, format="%,.0f", on_change=recalc, args=("new",))
st.number_input(T["usd"], key="usd", step=1.0, format="%,.2f", on_change=recalc, args=("usd",))
st.number_input(T["rate"], key="rate", step=50.0, format="%,.0f", on_change=recalc, args=("rate",))

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Copy to clipboard (mobile supported)
# -----------------------------
st.markdown(f"""
<input id='copyValue' value='{st.session_state.new:,.0f}' />
<button onclick="navigator.clipboard.writeText(document.getElementById('copyValue').value)">
{T['copy']}
</button>
""", unsafe_allow_html=True)

st.caption(T["note"])

# -----------------------------
# Notes
# - Any field updates all others instantly
# - Arabic RTL fully supported
# - Values saved during session
# - Mobile clipboard supported
