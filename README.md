# GeoInvest-MVP

# 🌍 GeoInvest MVP - Al Sheikh Zayed City

**GeoInvest** is an advanced AI-driven geospatial analytics platform designed to help real estate investors identify investment gaps and opportunities in Al Sheikh Zayed City, Egypt, using real-time data and LLM insights.

## 🚀 Key Features
* **Interactive Spatial Mapping:** Visualizes real-world commercial hubs, business parks, and retail outlets using Folium.
* **AI Investment Strategist:** Leverages GPT-4 to analyze geographical density and provide automated investment recommendations.
* **Data Integrity Audit:** An automated auditing system that validates data accuracy and completeness before visualization.
* **Cloud-Native Architecture:** Fully integrated with a PostgreSQL Cloud Database (Neon DB) and deployed via Streamlit Cloud.

---

## 🛠 Tech Stack
* **Core Logic:** Python 3.13
* **Web Framework:** Streamlit
* **Cloud Database:** PostgreSQL (Neon DB)
* **AI Engine:** OpenAI API (GPT-4o)
* **Geospatial Tools:** Folium & Geopy
* **Deployment:** GitHub & Streamlit Cloud

---

## ⚙️ Local Setup & Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/marwan-yasser644/GeoInvest-MVP.git](https://github.com/marwan-yasser644/GeoInvest-MVP.git)
    cd GeoInvest-MVP
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables:**
    Create a `.env` file in the root directory and add your credentials:
    ```env
    DB_HOST=your_neon_host
    DB_NAME=neondb
    DB_USER=your_user
    DB_PASS=your_password
    OPENAI_API_KEY=your_api_key
    ```

4.  **Run the Application:**
    ```bash
    streamlit run premium_app.py
    ```

---

## 📊 Business Impact
This MVP demonstrates how data-driven decisions can minimize risk in real estate. By identifying "underserved" zones in Sheikh Zayed, investors can optimize their capital placement for higher ROI.

---

**Developed with precision by Marwan Yasser** 🚀
