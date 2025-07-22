# AI-SEE: AI-Spatial Equity Engine for Kibera

**AI-SEE** is an planning system that uses IBM watsonx and Agentic AI to identify, prioritize, and visualize essential infrastructure gaps like **toilets**, **water points**, and **clinics**—in **Kibera slums, Nairobi**.

🚀 Built for the **IBM TechXchange 2025 Pre-conference watsonx Hackathon**  
🎯 Targeting **SDG 11: Sustainable Cities and Communities**

---

## 🌍 Problem

Kibera is home to over 1 Million people, yet many residents walk hundreds of meters to access basic services—or go without. While initiatives like **Map Kibera** and the **Kibera Public Space Project** have mapped community infrastructure, critical gaps remain:

- 🚫 No real-time system to detect spatial service inequality
- 🚫 No data-driven way to decide where to place new toilets, clinics, or water points
- 🚫 No AI system to learn from citizen feedback and recommend high-impact solutions

Urban planners and NGOs still rely on manual decisions and incomplete data. The result? Underserved areas stay invisible, and resources are misallocated.

---

## 💡 Solution

AI-SEE empowers smarter planning in Kibera by combining geospatial data, population distribution, and community input. It uses IBM watsonx to:

- 🗺️ Generate a real-time **Equity Heatmap** of underserved areas
- 🧠 Classify community-submitted messages using **watsonx.ai NLP**
- ⚖️ Rank locations using a prioritization algorithm (urgency × population × walkability)
- 🤖 Recommend **Top 5 intervention zones weekly** using agentic AI workflows
- 👥 Let citizens vote on infrastructure needs and visualize outcomes in a **community dashboard**
- 🔮 Forecast impact of new services through a **“what-if” simulation tool**

---

## 🔧 Tech Stack

| Component        | Technology                          |
|------------------|-------------------------------------|
| Backend API      | Python + FastAPI                    |
| Dashboard        | Streamlit                           |
| AI Platform      | IBM watsonx.ai, Orchestrate         |
| Data Sources     | OpenStreetMap, WorldPop, UN-Habitat |
| NLP Interface    | Twilio + WhatsApp (optional)        |
| Hosting          | IBM Cloud / Contabo                 |

---

## 🧠 IBM watsonx Integration

- **watsonx.ai**: Parses and classifies community-submitted needs (e.g. “Hapa hakuna maji” → `lack_water`)
- **watsonx Orchestrate**: Coordinates prioritization logic and agent workflows for weekly recommendations
- **watsonx Assistant** *(optional)*: Can serve as a WhatsApp or chatbot interface for future citizen reporting

---

## 🗺️ Folder Structure

```bash
.
├── backend/
│   ├── main.py                # FastAPI app
│   └── models/                # Prioritization and NLP models
├── dashboard/
│   └── app.py                 # Streamlit UI for heatmap + simulator
├── data/
│   ├── osm_services.csv       # Locations of toilets, water points, clinics
│   ├── worldpop_grids.csv     # Population estimates by 100m grid
│   └── sample_inputs.csv      # Citizen-submitted infrastructure requests
├── notebooks/
│   └── equity_analysis.ipynb  # Jupyter analysis and prioritization logic
├── .env.example               # Template for API keys/configs
└── README.md
````

---

## 🧪 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/DuniAfrika/ai-see.git
cd ai-see
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

* 📽️ A demo video will be added here before hackathon submission
* ✅ Use `notebooks/equity_analysis.ipynb` to explore data-driven prioritization logic and simulation outputs

---

## 🌱 SDG 11 Impact

* **Target 11.1**: Improve access to toilets, clinics, and clean water
* **Target 11.6**: Reduce health risks via better sanitation
* **Target 11.B**: Enable inclusive, participatory urban planning

---

## 🤝 Contributing

Pull requests are welcome. For major updates, please open an issue first to discuss your idea. Let’s build spatial equity together.

---

## 📄 License

MIT License. See `LICENSE` for full terms.

---

## 🏁 Team & Credits

Built by: **Team Ubunifu**
Inspired by: **Kibera residents**, **Map Kibera**, and **KPSP (Kibera Public Space Project)**
Supported by: **IBM watsonx** through the **TechXchange Hackathon 2025**
