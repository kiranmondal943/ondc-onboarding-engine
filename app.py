import streamlit as st

st.set_page_config(page_title="Google Business Technologist", page_icon="📍")

st.title("🚀 Google Maps Business Growth Tool")

# Sidebar for Navigation
menu = st.sidebar.selectbox("Select Service", ["Google Business Audit", "ONDC Catalog Generator"])

if menu == "Google Business Audit":
    st.header("🔍 Google Maps Profit Audit")
    st.write("Use this to show a shop owner how much money they are losing.")

    shop_name = st.text_input("Enter Shop Name (as seen on Google)")
    
    col1, col2 = st.columns(2)
    with col1:
        has_phone = st.checkbox("Has Verified Phone Number?")
        has_website = st.checkbox("Has Website/WhatsApp Link?")
    with col2:
        has_photos = st.checkbox("Has Photos from last 30 days?")
        replies_reviews = st.checkbox("Replies to all Reviews?")

    current_rating = st.slider("Current Star Rating", 1.0, 5.0, 3.5)

    if st.button("Generate Audit Report"):
        st.divider()
        st.subheader(f"Analysis for {shop_name}")
        
        score = 0
        checks = [has_phone, has_website, has_photos, replies_reviews]
        score = sum(checks) + (current_rating / 1.25)
        
        st.metric("Business Health Score", f"{int(score*10)}/100")

        # The "Pain Points" - This is what sells the service
        if not has_phone:
            st.error("❌ **Critical:** No phone number means ~25% of searching customers go to competitors.")
        if not has_photos:
            st.warning("⚠️ **Growth Gap:** Profiles with recent photos get 35% more clicks.")
        if current_rating < 4.0:
            st.info("📉 **Reputation Risk:** Ratings below 4.0 drive away premium customers.")

        st.success("✅ **Opportunity:** Optimizing this profile could increase footfall by 20-40% in 30 days.")
        
        st.write("---")
        st.write("### 💰 Suggested Service Fee: ₹1,500")
        st.write("Includes: Profile Verification, 10 High-Res Photos, and Review Management setup.")

elif menu == "ONDC Catalog Generator":
    # (Your previous ONDC code goes here)
    st.header("📦 ONDC Catalog Generator")
    store_name = st.text_input("Shop Name")
    inventory_text = st.text_area("Inventory (Item: Price)")
    if st.button("Generate JSON"):
        st.json({"store": store_name, "status": "Ready for ONDC"})
