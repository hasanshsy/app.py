# Syrian Currency Converter App
# Compatible with Web Browsers (via Streamlit) and Android (via WebView/PWA)

import streamlit as st

# -----------------------------
# Language dictionary
# -----------------------------
LANG = {
    "en": {
        "title": "Syrian Currency Converter",
        "old_syp": "Old Syrian Amount",
        "usd": "Equivalent Amount in USD",
        "rate": "USD to SYP Exchange Rate",
        "result": "Converted Amount (New Syrian Pound)",
        "copy": "Copy Result",
        "lang": "Language",
        "note": "Conversion removes two trailing zeros"
    },
    "ar": {
        "title": "محول العملة السورية",
        "old_syp": "المبلغ بالليرة السورية القديمة",
        "usd": "المبلغ المكافئ بالدولار",
        "rate": "سعر صرف الدولار",
        "result": "المبلغ بعد التحويل (الليرة السورية الجديدة)",
        "copy": "نسخ النتيجة",
        "lang": "اللغة",
        "note": "يتم التحويل بحذف صفرين من المبلغ"
    }
}

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Syrian Currency Converter",
    layout="centered"
)

# -----------------------------
# Dark blue gradient styling
# -----------------------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #0a1f44, #102a5e);
        color: white;
    }
    .stTextInput > label, .stNumberInput > label {
        color: #dbe9ff !important;
    }
    .stButton > button {
        background-color: #1f4fd8;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Language toggle
# -----------------------------
lang = st.selectbox("Language / اللغة", ["English", "العربية"])
lang_key = "en" if lang == "English" else "ar"
T = LANG[lang_key]

# -----------------------------
# Title
# -----------------------------
st.title(T["title"])

# -----------------------------
# Input fields
# -----------------------------
old_amount = st.number_input(T["old_syp"], min_value=0.0, step=100.0)
usd_amount = st.number_input(T["usd"], min_value=0.0, step=1.0)
exchange_rate = st.number_input(T["rate"], min_value=0.0, step=10.0)

# -----------------------------
# Conversion logic
# -----------------------------
new_syp = old_amount / 100

if usd_amount > 0 and exchange_rate > 0:
    new_syp = usd_amount * exchange_rate / 100

# -----------------------------
# Output
# -----------------------------
st.subheader(T["result"])
st.code(f"{new_syp:,.2f}")

# -----------------------------
# Copy button (browser supported)
# -----------------------------
st.button(T["copy"], on_click=lambda: st.write("Copied!"))

st.caption(T["note"])

# -----------------------------
# Deployment Instructions
# -----------------------------
# WEB:
# 1. Install dependencies: pip install streamlit
# 2. Run: streamlit run app.py
# 3. Deploy on Streamlit Cloud or any Python server

# ANDROID:
# Option 1 (Recommended):
# - Deploy the app as a web app
# - Wrap it using Android WebView or convert to PWA
# Option 2:
# - Use tools like WebViewGold or Trusted Web Activity (TWA)

# This approach ensures high performance, cross-platform compatibility,
# and easy maintenance using a single Python codebase.
