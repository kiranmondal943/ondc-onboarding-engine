import streamlit as st

# Title of the App
st.title("🇮🇳 ONDC Kirana Onboarding Engine")
st.write("Enter the store details below to generate a digital catalog.")

# Step 1: Google Maps Data Simulation
st.subheader("1. Store Location (Powered by Google Maps)")
store_name = st.text_input("Shop Name", placeholder="e.g. Gupta General Store")
location = st.text_input("Address", placeholder="Type address or paste Google Maps link")

# Step 2: Inventory Upload
st.subheader("2. Inventory")
inventory_text = st.text_area("List items and prices (one per line)", 
                              placeholder="Example:\nAashirvaad Atta 5kg: 250\nAmul Milk 1L: 60")

# Step 3: Deployment Logic
if st.button("Generate ONDC Digital Entry"):
    if store_name and inventory_text:
        st.success(f"✅ Success! {store_name} is ready for ONDC.")
        
        # Displaying what the digital data looks like
        st.json({
            "store": store_name,
            "address": location,
            "status": "Verified via Google Maps",
            "items_count": len(inventory_text.split('\n'))
        })
        st.balloons()
    else:
        st.error("Please fill in the Shop Name and Inventory.")
