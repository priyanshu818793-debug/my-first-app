import streamlit as st

# पेज का टाइटल
st.set_page_config(page_title="Priyanshu's Calculator", page_icon="🔢")

st.title("🔢 स्मार्ट कैलकुलेटर")
st.write("अपना डेटा नीचे भरें और तुरंत नतीजे देखें।")

# इमेज डिस्प्ले करना (सावधानी: सुनिश्चित करें कि 'logo.png' आपके GitHub फोल्डर में है)
# अगर इमेज नहीं है, तो इस लाइन को हटा दें या कमेंट कर दें
try:
    st.image("logo.jpg",caption="आपका स्वागत है!",width=300)
except:
    st.info("नोट:'logo.jpg' फाइल नहीं मिली, इसलिए इमेज नहीं दिखाई गई।")

# यूजर इनपुट
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("पहला नंबर डालें", value=0)
with col2:
    num2 = st.number_input("दूसरा नंबर डालें", value=0)

operation = st.selectbox("ऑपरेशन चुनें", ["जोड़ (+)", "घटाव (-)", "गुणा (*)", "भाग (/)"])

# कैलकुलेशन और आउटपुट
if st.button("कैलकुलेट करें"):
    if operation == "जोड़ (+)":
        res = num1 + num2
    elif operation == "घटाव (-)":
        res = num1 - num2
    elif operation == "गुणा (*)":
        res = num1 * num2
    elif operation == "भाग (/)":
        res = num1 / num2 if num2 != 0 else "Error (0 से भाग संभव नहीं)"
    
    st.success(f"नतीजा: {res}")




