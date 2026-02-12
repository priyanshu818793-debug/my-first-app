import streamlit as st

# पेज की सुंदर सेटिंग
st.set_page_config(page_title="Priyanshu's Royal Kitchen", page_icon="🍲", layout="wide")

# मुख्य टाइटल
st.title("🌟 Priyanshu's Royal Restaurant & Cafe")
st.markdown("---")

# कॉलम बनाकर मेनू दिखाना (Unique लुक के लिए)
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📋 आज का विशेष मेनू")
    
    tab1, tab2, tab3 = st.tabs(["🍟 स्टार्टर्स", "🍛 मेन कोर्स", "🥤 ड्रिंक्स"])
    
    with tab1:
        st.subheader("Crispy Snacks")
        st.info("🔹 पनीर टिक्का - ₹220 | 🔹 मसाला फ्राइज़ - ₹90")
        st.image("pk.jpg", caption="Tandoori Special", width=400)
        st.image("mf.jpg", caption="Tandoori Special", width=400)

    with tab2:
        st.subheader("Delicious Meals")
        st.success("🔹 बटर पनीर - ₹280 | 🔹 शाही बिरयानी - ₹180")
        st.image("pp.jpg", caption="Main Course", width=400)
        st.image("sp.jpg", caption="Main Course", width=400)

    with tab3:
        st.subheader("Refreshing Beverages")
        st.warning("🔹 कोल्ड कॉफ़ी - ₹120 | 🔹 ताज़ा नींबू पानी - ₹60")
        st.image("cc.jpg", caption="cold coffee", width=400)
        st.image("np.jpg", caption="cold coffee", width=400)

# पेमेंट सेक्शन (QR कोड के साथ)
with col2:
    st.header("💳 पेमेंट करें")
    st.write("अपना ऑर्डर कंफर्म करने के लिए नीचे दिए गए QR कोड को स्कैन करें:")
    
    # यहाँ आप अपने असली QR कोड की इमेज का लिंक डाल सकते हैं
    st.image("unnamed.png", caption="Scan to Pay via UPI")
    
    st.markdown("---")
    if st.button("ऑर्डर बुक करें 🚀"):
        st.balloons()
        st.success("बधाई हो! आपका ऑर्डर सफलतापूर्वक बुक हो गया है।")

# नीचे फुटर
st.markdown("---")
st.write("📍 पता: आपका पसंदीदा चौराहा, दिल्ली | 📞 संपर्क: +91 1234567890")
