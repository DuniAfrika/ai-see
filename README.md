
### 📘 **README.md Template**

# AI-SEE: AI-Spatial Equity Engine for Nairobi Slums

**AI-SEE** is an agentic, AI-powered planning platform built using IBM watsonx to identify, prioritize, and visualize critical infrastructure needs in Nairobi’s informal settlements. The project focuses on underserved areas like Soweto East in Kibera to enable smarter, more inclusive urban service delivery.

🚀 Built for the **IBM TechXchange 2025 Pre-conference watsonx Hackathon**  
🎯 Targeting **SDG 11: Sustainable Cities and Communities**

---

## 🌍 Problem

Over 60% of Nairobi’s population lives in informal settlements on less than 6% of the land, with limited access to toilets, water points, schools, or clinics. There is no real-time, data-driven system for identifying where services are most needed. Urban planning tools are top-down, static, and often ignore local voices.

---

## 💡 Solution

AI-SEE uses **agentic AI** to process geospatial data, community inputs, and service locations to:

- Generate an **Equity Heatmap** of underserved zones
- Classify needs from citizen messages using **IBM watsonx.ai**
- Prioritize locations using an impact-based algorithm
- Recommend top 5 interventions weekly using **watsonx Orchestrate**
- Let citizens and local authorities **vote or simulate what-if scenarios**

---

## 🔧 Tech Stack

| Component        | Technology                          |
|------------------|-------------------------------------|
| Backend API      | Python + FastAPI                    |
| Dashboard        | Streamlit                           |
| AI Platform      | IBM watsonx.ai, Orchestrate         |
| Data Sources     | OpenStreetMap, WorldPop, UN-Habitat |
| NLP Interface    | Twilio + WhatsApp                   |
| Hosting          | IBM Cloud / Contabo                 |

---

## 🧠 IBM watsonx Integration

- **watsonx.ai**: Classifies community-submitted needs (e.g. “need water here”)
- **watsonx Orchestrate**: Coordinates agents to prioritize locations and recommend actions
- **watsonx Assistant**: Optional for chatbot interface (e.g. via WhatsApp)

---

## 🗺️ Folder Structure

```bash
.
├── backend/
│   ├── main.py            # FastAPI app
│   └── models/            # Prioritization and ML/NLP models
├── dashboard/
│   └── app.py             # Streamlit heatmap and simulation UI
├── data/
│   ├── osm_services.csv   # Toilets, water points, clinics
│   ├── worldpop_grids.csv # Population per 100m cell
│   └── sample_inputs.csv  # Community-submitted needs
├── notebooks/
│   └── equity_analysis.ipynb # Jupyter analysis
├── .env.example           # API keys template
└── README.md
```

---

## 🧪 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR-ORG/ai-see-nairobi.git
cd ai-see-nairobi
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Backend

```bash
uvicorn backend.main:app --reload
```

### 4. Run the Dashboard

```bash
cd dashboard
streamlit run app.py
```

---

## 🌐 Demo & Walkthrough

- 📽️ A demo video will be uploaded here before submission.
- ✅ Follow the instructions in `notebooks/equity_analysis.ipynb` to reproduce our prioritization engine.

---

## 🌱 SDG 11 Impact

- **Target 11.1:** Better access to toilets, water, schools
- **Target 11.6:** Improved sanitation and environmental health
- **Target 11.B:** Participatory and data-driven urban planning

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.

---

## 📄 License

MIT License. See `LICENSE` for details.

---

## 🏁 Team & Credits

Built by: **Team Ubunifu**  
Inspired by communities in Kibera and Mathare

