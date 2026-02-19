import streamlit as st

st.set_page_config(page_title="BESCOM Smart Chatbot", page_icon="⚡")

st.title("⚡ BESCOM Smart Energy Chatbot")
st.subheader("Your Personal Electricity Bill Assistant")

st.write("Ask about your bill, savings, appliances or peak hours.")

# ---------------- BILL CALCULATION ---------------- #

def calculate_bill(units):
    if units <= 100:
        return units * 4
    elif units <= 200:
        return (100 * 4) + ((units - 100) * 6)
    else:
        return (100 * 4) + (100 * 6) + ((units - 200) * 8)

# ---------------- SIDEBAR MENU ---------------- #

option = st.sidebar.selectbox(
    "Select Option",
    ["Bill Calculator", "Appliance Calculator", "Reduce My Bill Plan", "Peak Hour Advice"]
)

# ---------------- BILL CALCULATOR ---------------- #

if option == "Bill Calculator":
    st.header("📊 Electricity Bill Calculator")
    units = st.number_input("Enter Units Consumed This Month:", min_value=0)

    if st.button("Calculate Bill"):
        bill = calculate_bill(units)
        st.success(f"Estimated Bill: ₹ {bill}")

# ---------------- APPLIANCE CALCULATOR ---------------- #

elif option == "Appliance Calculator":
    st.header("🔌 Appliance Cost Calculator")

    ac_hours = st.number_input("AC Usage (hours per day):", min_value=0)
    geyser_hours = st.number_input("Geyser Usage (hours per day):", min_value=0)
    wm_hours = st.number_input("Washing Machine Usage (hours per day):", min_value=0)

    if st.button("Calculate Appliance Cost"):

        ac_units = (1.5 * ac_hours * 30)
        geyser_units = (2 * geyser_hours * 30)
        wm_units = (0.5 * wm_hours * 30)

        total_units = ac_units + geyser_units + wm_units
        bill = calculate_bill(total_units)

        st.success(f"Estimated Units: {round(total_units)} units")
        st.success(f"Estimated Cost: ₹ {round(bill)}")

# ---------------- REDUCE BILL PLAN ---------------- #

elif option == "Reduce My Bill Plan":
    st.header("💡 Personalized Bill Reduction Plan")

    st.info("""
    🔹 Set AC temperature to 26°C  
    🔹 Limit AC usage to 5 hours/day  
    🔹 Use washing machine only 3 times/week  
    🔹 Reduce geyser usage to 30–45 minutes  
    🔹 Replace all bulbs with LED  
    🔹 Switch off standby devices  
    """)

    st.success("Estimated Monthly Savings: ₹500 – ₹900")

# ---------------- PEAK HOUR ADVICE ---------------- #

elif option == "Peak Hour Advice":
    st.header("⏰ Peak & Off-Peak Hour Guidance")

    st.warning("""
    ⚠ Peak Hours: 6PM – 10PM  
    Avoid using:
    - AC
    - Iron Box
    - Water Heater
    - Washing Machine
    """)

    st.success("""
    ✅ Off-Peak Hours: 10AM – 4PM  
    Best time to use:
    - Washing Machine
    - Dishwasher
    - Water Pump
    - Heavy Appliances
    """)

st.markdown("---")
st.caption("Developed as Smart Energy Management System for BESCOM")
