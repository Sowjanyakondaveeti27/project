import streamlit as st
from PIL import Image

st.set_page_config(page_title="Dermatology Assistant", layout="centered")

st.title("🌸 Dermatology Assistant")
st.subheader("Hey there! Let's understand your skin and help it glow! ✨")
st.write("Answer a few questions and I’ll suggest the best skincare products for you. No worries, we’ve got your back! 💖")

# Step 1: Questionnaire
st.markdown("### 🧴 Tell us a bit about your skin")

q1 = st.selectbox("1️⃣ How does your skin feel after washing it?",
                  ["Tight and dry", "Oily or greasy", "Smooth and comfortable", "Oily in T-zone but dry elsewhere", "Red or itchy"])

q2 = st.selectbox("2️⃣ How often do you get breakouts or irritation?",
                  ["Rarely", "Frequently", "Sometimes", "Almost never", "Often red or itchy"])

q3 = st.selectbox("3️⃣ What happens when you try a new product?",
                  ["Nothing much", "Breakouts", "Flaky or dry skin", "Redness or burning", "Gets oily quickly"])

uploaded_file = st.file_uploader("📷 Want to share a photo of your skin? (Optional)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Thanks for sharing!", use_column_width=True)

# Step 2: Determine skin condition
def determine_condition(q1, q2, q3):
    if "dry" in q1 or "Flaky" in q3:
        return "Dry Skin"
    elif "Oily" in q1 or "oily" in q3:
        return "Oily Skin"
    elif "T-zone" in q1:
        return "Combination Skin"
    elif "Red" in q1 or "burning" in q3:
        return "Sensitive Skin"
    else:
        return "Normal Skin"

# Step 3: Product suggestions
def get_product_recommendations(condition):
    if condition == "Dry Skin":
        return {
            "Cleanser": "Aqualogica Hydrate+ Cleanser with Coconut Water & Hyaluronic Acid",
            "Toner": "Minimalist PHA 3% Alcohol-Free Toner",
            "Moisturizer": "The Derma Co Hyaluronic Acid Oil-Free Moisturizer",
            "Sunscreen": "Minimalist SPF 50 Multi-Vitamin Sunscreen",
            "Tan Removal": "Dot & Key Cica & Niacinamide Brightening Mask"
        }
    elif condition == "Oily Skin":
        return {
            "Cleanser": "Minimalist Salicylic Acid Cleanser (2%)",
            "Toner": "Plum Green Tea Alcohol-Free Toner",
            "Moisturizer": "Aqualogica Radiance+ Oil-Free Moisturizer",
            "Sunscreen": "The Derma Co Ultra Matte Sunscreen Gel SPF 60 PA+++",
            "Tan Removal": "MCaffeine Coffee Tan Removal Face Pack"
        }
    elif condition == "Combination Skin":
        return {
            "Cleanser": "Cetaphil Gentle Skin Cleanser",
            "Toner": "The Derma Co 5% Niacinamide Toner",
            "Moisturizer": "Aqualogica Glow+ Oil-Free Gel Moisturizer",
            "Sunscreen": "Minimalist SPF 60 Sunscreen",
            "Tan Removal": "WOW Skin Science Ubtan Face Pack"
        }
    elif condition == "Sensitive Skin":
        return {
            "Cleanser": "Bioderma Sensibio H2O Micellar Water",
            "Toner": "Minimalist Polyhydroxy Acid (PHA) Toner",
            "Moisturizer": "Cetaphil Moisturizing Cream",
            "Sunscreen": "Aqualogica Hydrate+ Dewy Sunscreen SPF 50",
            "Tan Removal": "Mamaearth Ubtan Face Pack with Turmeric & Saffron"
        }
    else:
        return {
            "Cleanser": "Simple Kind to Skin Refreshing Facial Wash",
            "Toner": "Dot & Key CICA Calming Toner",
            "Moisturizer": "Neutrogena Hydro Boost Water Gel",
            "Sunscreen": "Aqualogica Glow+ Dewy Sunscreen SPF 50 PA+++",
            "Tan Removal": "Dot & Key Vitamin C + E Face Mask"
        }

# Step 4: Output
if st.button("💡 Get My Skin Analysis & Products"):
    skin_condition = determine_condition(q1, q2, q3)
    st.success(f"😊 No worries! Based on your answers, you likely have **{skin_condition}**.")

    st.markdown("### 🛍️ Here's what your skin will love:")
    products = get_product_recommendations(skin_condition)
    for category, product in products.items():
        st.markdown(f"**{category}:** {product}")

    st.markdown("💖 Take care of your skin, stay consistent, and always use sunscreen! If anything feels off, consult a dermatologist. You're doing great!")
