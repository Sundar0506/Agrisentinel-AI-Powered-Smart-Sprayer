# dashboard_final_smart_pdf_full.py
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
from plant_infection_model import predict_leaf

# -----------------------------
# Streamlit setup
# -----------------------------
st.set_page_config(page_title="🌿 Agri Sentinel", layout="wide")
st.title("🌿 Smart Pesticide Sprayer Dashboard")
st.markdown("Upload leaf images, monitor soil moisture, and check for infections.")

# -----------------------------
# Plant input
# -----------------------------
num_plants = st.number_input("Number of Plants:", min_value=1, max_value=10, value=3, step=1)
plants_data = {}

for i in range(1, num_plants + 1):
    st.markdown(f"### Plant {i}")
    uploaded_file = st.file_uploader(f"Plant {i} Leaf Image", type=["jpg", "jpeg", "png"], key=f"plant_{i}")
    moisture = st.slider(f"Plant {i} Soil Moisture (%)", 0, 100, 30, key=f"moisture_{i}")

    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")
        prediction, confidence = predict_leaf(img)
        sprayer_on = prediction == "Infected" or moisture < 25
    else:
        img = Image.new('RGB', (224, 224), color=(200, 200, 200))
        prediction, confidence, sprayer_on = "Unknown", 0, False

    plants_data[f"Plant {i}"] = {
        "image": img,
        "prediction": prediction,
        "confidence": confidence,
        "sprayer": sprayer_on,
        "moisture": moisture
    }

# -----------------------------
# Display plant cards
# -----------------------------
st.subheader("🪴 Plant Status")
cols = st.columns(num_plants)

for i, (plant_id, info) in enumerate(plants_data.items()):
    with cols[i]:
        st.markdown(f"**{plant_id}**")
        st.image(info['image'], width=150)

        # Confidence color gradient
        conf_color = f"rgba(0,200,0,{info['confidence']/100})" if info['prediction'] == "Healthy" else f"rgba(200,0,0,{info['confidence']/100})"
        st.markdown(f"**Prediction:** <span style='color:{conf_color}'>{info['prediction']}</span>", unsafe_allow_html=True)
        st.write(f"Confidence: {info['confidence']:.2f}%")
        st.write(f"Moisture: {info['moisture']}%")

        # Sprayer toggle
        sprayer_state = st.checkbox("Sprayer ON", value=info['sprayer'], key=f"sprayer_{i}")
        plants_data[plant_id]['sprayer'] = sprayer_state

        # Visual sprayer indicator
        if sprayer_state:
            intensity = int(min(255, info['confidence']*2.55))
            st.markdown(f"<div style='font-size:30px; color: rgb({intensity},0,0)'>🔴 Sprayer Active!</div>", unsafe_allow_html=True)
        else:
            st.markdown("🟢 Sprayer OFF")

# -----------------------------
# Moisture Bar Chart
# -----------------------------
st.subheader("🌡️ Moisture Levels")
df_moisture = pd.DataFrame({
    'Plant': list(plants_data.keys()),
    'Moisture': [info['moisture'] for info in plants_data.values()]
})
bar_fig, bar_ax = plt.subplots(figsize=(6, 3))  # smaller figure
df_moisture.set_index('Plant').plot(kind='bar', ax=bar_ax, color='skyblue')
bar_ax.set_ylim(0, 100)
bar_ax.set_ylabel("Moisture (%)")
bar_ax.set_xlabel("Plant")
bar_ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(bar_fig)

# -----------------------------
# Healthy vs Unhealthy vs Unknown Pie
# -----------------------------
healthy = sum(1 for info in plants_data.values() if info['prediction'] == "Healthy")
unhealthy = sum(1 for info in plants_data.values() if info['prediction'] == "Infected")
unknown = sum(1 for info in plants_data.values() if info['prediction'] == "Unknown")
if healthy + unhealthy + unknown == 0:
    healthy, unhealthy, unknown = 1, 0, 0

st.subheader("🟢 Healthy vs 🔴 Unhealthy vs ⚪ Unknown")
pie_fig, pie_ax = plt.subplots(figsize=(4,4))
pie_ax.pie([healthy, unhealthy, unknown], labels=['Healthy', 'Unhealthy', 'Unknown'],
           autopct='%1.1f%%', colors=['green', 'red', 'gray'], startangle=90)
pie_ax.axis('equal')
plt.tight_layout()
st.pyplot(pie_fig)

# -----------------------------
# Summary
# -----------------------------
st.subheader("📊 Summary")
st.metric("Total Plants", num_plants)
st.metric("Healthy Plants", healthy)
st.metric("Unhealthy Plants", unhealthy)
st.metric("Unknown Plants", unknown)
st.metric("Sprayers ON", sum(1 for info in plants_data.values() if info['sprayer']))

# -----------------------------
# Prepare CSV
# -----------------------------
report_df = pd.DataFrame([
    {
        "Plant": plant_id,
        "Prediction": info['prediction'],
        "Confidence (%)": info['confidence'],
        "Moisture (%)": info['moisture'],
        "Sprayer ON": info['sprayer']
    }
    for plant_id, info in plants_data.items()
])
st.subheader("💾 Plant Status Report")
st.dataframe(report_df)

csv = report_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name='plant_status_report.csv',
    mime='text/csv'
)
