import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AI-SEE Dashboard", layout="wide")
st.title("AI-SEE: Nairobi Slums Equity Engine")

BACKEND_URL = "http://localhost:8000"

# --- Heatmap Section ---
st.header("Equity Heatmap")
try:
    # Placeholder: In real app, fetch processed heatmap data from backend
    worldpop = pd.read_csv("../data/worldpop_grids.csv")
    st.map(worldpop.rename(columns={"lat": "latitude", "lon": "longitude"}))
except Exception as e:
    st.warning(f"Could not load heatmap data: {e}")

# --- Recommendations Section ---
st.header("Top 5 Recommendations")
try:
    resp = requests.get(f"{BACKEND_URL}/recommendations")
    if resp.ok:
        recs = resp.json()["recommendations"]
        for r in recs:
            st.write(f"- {r['type'].title()} at {r['location']} (score: {r['score']:.2f})")
    else:
        st.warning("Could not fetch recommendations from backend.")
except Exception as e:
    st.warning(f"Error: {e}")

# --- Submit a Need (Classify) ---
st.header("Submit a Need")
user_msg = st.text_input("Describe a need in your area:")
if st.button("Classify Need") and user_msg:
    try:
        resp = requests.post(f"{BACKEND_URL}/classify", json={"message": user_msg})
        if resp.ok:
            result = resp.json()
            st.success(f"Classified as: {result['category']} (confidence: {result['confidence']:.2f})")
        else:
            st.warning("Classification failed.")
    except Exception as e:
        st.warning(f"Error: {e}")

# --- Voting/Simulation Section ---
st.header("Vote or Simulate Interventions")
st.write("(Simulation and voting features coming soon!)") 