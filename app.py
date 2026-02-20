import streamlit as st
import google.generativeai as genai

# ==============================
# CONFIGURATION
# ==============================

st.set_page_config(page_title="BESCOM Smart Chatbot", layout="wide")

# ------------------------------
# Add your Gemini API key here
# ------------------------------
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# ==============================
# FAKE LOGIN DETAILS
# ==============================

FAKE_METER = "1234567890"
FAKE_PERMISSION = "BESCOM2026"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ==============================
# LOGIN PAGE
# ==============================

def login_page():
    st.title("🔐 BESCOM Smart Chatbot Login")
    st.write("Enter your Meter Number and Permission Code")

    meter = st.text_input("Meter Number (Username)")
    permission = st.text_input("Permission Code (Password)", type="password")

    if st.button("Login"):
        if meter == FAKE_METER and permission == FAKE_PERMISSION:
            st.session_state.logged_in = True
            st.success("Login Successful ✅")
            st.rerun()
        else:
            st.error("Invalid Meter Number or Permission Code ❌")

# If not logged in, show login page only
if not st.session_state.logged_in:
    login_page()
    st.stop()

# ==============================
# SIDEBAR MENU
# ==============================

st.sidebar.title("BESCOM Smart System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Bill Calculator", "Appliance Calculator", "Ask Questions (AI Chatbot)"]
)

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

# ==============================
# BILL CALCULATOR
# ==============================

if menu == "Bill Calculator":

    st.title("💰 BESCOM Bill Calculator")

    units = st.number_input("Enter Units Consumed (kWh)", min_value=0)

    if st.button("Calculate Bill"):

        if units <= 100:
            bill = units * 4
        elif units <= 200:
            bill = (100 * 4) + (units - 100) * 6
        else:
            bill = (100 * 4) + (100 * 6) + (units - 200) * 8

        st.success(f"Estimated Electricity Bill: ₹ {bill}")

# ==============================
# APPLIANCE CALCULATOR
# ==============================

elif menu == "Appliance Calculator":

    st.title("⚡ Appliance Usage Calculator")

    appliance = st.text_input("Enter Appliance Name")
    power = st.number_input("Power Rating (Watts)", min_value=0)
    hours = st.number_input("Usage Hours per Day", min_value=0)
    days = st.number_input("Number of Days Used", min_value=0)

    if st.button("Calculate Consumption"):

        units = (power * hours * days) / 1000
        cost = units * 6

        st.success(f"Total Units Consumed: {units} kWh")
        st.success(f"Estimated Cost: ₹ {cost}")

# ==============================
# AI CHATBOT
# ==============================

elif menu == "Ask Questions (AI Chatbot)":

    st.title("🤖 BESCOM Smart AI Chatbot")

    user_question = st.text_area("Ask your question about BESCOM electricity services")

    if st.button("Get Answer"):

        if user_question.strip() == "":
            st.warning("Please enter a question.")
        else:

            try:
                prompt = f"""
                You are a BESCOM Electricity Support Assistant.

                If the question is related to electricity, appliances,
                energy usage, current, voltage, bill calculation,
                or BESCOM services — answer properly.

                If the question is unrelated (like sports, movies, politics),
                reply exactly:
                "This question is not part of BESCOM Smart Chatbot services."

                Question: {user_question}
                """

                response = model.generate_content(prompt)
                st.success(response.text)

            except:
                st.error("Error generating response. Check API key.")


