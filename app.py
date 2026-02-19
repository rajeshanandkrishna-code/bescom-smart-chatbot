import streamlit as st
import google.generativeai as genai

# ---------------- CONFIG ---------------- #

st.set_page_config(page_title="BESCOM Smart Chatbot", page_icon="⚡")

# ---------------- LOGIN SYSTEM (FAKE) ---------------- #



# ---------------- MAIN PAGE ---------------- #

st.title("⚡ BESCOM Smart Energy Chatbot")
st.subheader("Electricity Bill Assistant & AI Support")

# ---------------- GEMINI API ---------------- #

API_KEY = "AIzaSyASMX7HMF5ewHscAUgLnDrnp5x18NF0vMw"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# ---------------- BILL CALCULATION ---------------- #

def calculate_bill(units):
    if units <= 100:
        return units * 4
    elif units <= 200:
        return (100 * 4) + ((units - 100) * 6)
    else:
        return (100 * 4) + (100 * 6) + ((units - 200) * 8)

# ---------------- SIDEBAR ---------------- #

option = st.sidebar.selectbox(
    "Choose Option",
    ["Bill Calculator",
     "Appliance Calculator",
     "Reduce My Bill Plan",
     "Peak Hour Advice",
     "Ask Questions (AI Chatbot)"]
)

# ---------------- EXISTING FEATURES ---------------- #

if option == "Bill Calculator":
    units = st.number_input("Enter Units Consumed:", min_value=0)
    if st.button("Calculate Bill"):
        bill = calculate_bill(units)
        st.success(f"Estimated Bill: ₹ {bill}")

elif option == "Appliance Calculator":
    ac = st.number_input("AC usage (hours/day):", min_value=0)
    geyser = st.number_input("Geyser usage (hours/day):", min_value=0)
    wm = st.number_input("Washing Machine usage (hours/day):", min_value=0)

    if st.button("Estimate Cost"):
        total_units = (1.5*ac*30) + (2*geyser*30) + (0.5*wm*30)
        cost = calculate_bill(total_units)
        st.success(f"Estimated Units: {round(total_units)}")
        st.success(f"Estimated Cost: ₹ {round(cost)}")

elif option == "Reduce My Bill Plan":
    st.info("""
    ✔ Set AC to 26°C  
    ✔ Use AC only 5 hours/day  
    ✔ Avoid peak hours (6PM–10PM)  
    ✔ Use LED bulbs  
    ✔ Reduce geyser to 30 mins  
    """)
    st.success("Estimated Savings: ₹500–₹900 per month")

elif option == "Peak Hour Advice":
    st.warning("⚠ Peak Hours: 6PM–10PM")
    st.success("✅ Best Time: 10AM–4PM for heavy appliances")

# ---------------- AI CHATBOT SECTION ---------------- #

elif option == "Ask Questions (AI Chatbot)":

    st.header("🤖 BESCOM AI Assistant")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_question = st.text_input("Ask your electricity-related question:")

    if st.button("Ask"):
        if user_question:

            # Restrict to BESCOM electricity topics
            prompt = f"""
            You are a BESCOM Electricity Support Assistant.
            Only answer questions related to:
            - Electricity bills
            - BESCOM services
            - Energy saving tips
            - Appliance usage
            - Peak hour advice
            - Electricity tariff

            If question is unrelated, reply:
            "This question is not part of BESCOM Smart Chatbot services."

            Question: {user_question}
            """

            response = model.generate_content(prompt)

            st.session_state.chat_history.append(("You", user_question))
            st.session_state.chat_history.append(("Bot", response.text))


        

    # Display Chat
    for speaker, message in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(f"**🧑 You:** {message}")
        else:
            st.markdown(f"**⚡ Bot:** {message}")
