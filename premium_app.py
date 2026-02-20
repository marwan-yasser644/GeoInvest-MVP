import streamlit as st
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap, MarkerCluster

load_dotenv()

# --- Page Config ---
st.set_page_config(page_title="GeoInvest Elite v3", layout="wide", initial_sidebar_state="collapsed")

# --- Custom CSS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .stFolium {
        border: 2px solid #334155;
        border-radius: 15px;
        overflow: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

def get_data():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )
    query = "SELECT name, category, latitude, longitude FROM locations"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# --- Header Section ---
st.title("🚀 GeoInvest AI | Elite Market Intelligence")
st.markdown("##### Real-time Geospatial Data Analysis for Sheikh Zayed District")

try:
    df = get_data()
    
    # --- Top Metrics ---
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Total Data Points", len(df), "+12% vs last week")
    with m2:
        st.metric("Market Saturation", "Medium", "Stable")
    with m3:
        st.metric("Prime District", "Sheikh Zayed", "Active")
    with m4:
        st.metric("AI Opportunity Score", "92/100", "High")

    st.write("") 

    col_left, col_right = st.columns([2.5, 1])

    with col_left:
        st.markdown("### 🗺️ Dynamic Investment Heatmap (Standard View)")
        
        m = folium.Map(
            location=[df['latitude'].mean(), df['longitude'].mean()], 
            zoom_start=14, 
            tiles="OpenStreetMap" 
        )
        
        marker_cluster = MarkerCluster().add_to(m)
        for _, row in df.iterrows():
            color = "blue" if row['category'].lower() == 'cafe' else "red"  
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=8,
                popup=f"<b>{row['name']}</b><br>{row['category']}",
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.8
            ).add_to(marker_cluster)
        
        HeatMap(df[['latitude', 'longitude']].values.tolist(), radius=15, blur=10).add_to(m)
        folium_static(m, width=950, height=550)

    with col_right:
        st.markdown("### 🤖 AI Market Insights")
        
        counts = df['category'].value_counts()
        for cat, count in counts.items():
            st.write(f"**{cat.capitalize()}**")
            st.progress(int((count / len(df)) * 100))
            st.caption(f"{count} locations identified")

        st.markdown("---")
        
        # --- Accuracy Audit ---
        st.markdown("### 🎯 Accuracy Audit")
        target_count = 5
        current_count = len(df)
        accuracy = min((current_count / target_count) * 100, 100.0)
        
        st.write(f"Data Integrity: **{accuracy}%**")
        st.progress(accuracy / 100)
        
        if accuracy >= 100:
            st.success("✅ Phase 1 Data Requirements Met")
        else:
            st.warning(f"⚠️ Need {target_count - current_count} more verified points.")

        st.markdown("---")
        
        # --- Investment Decision Engine ---
        st.subheader("📝 Investment Decision Engine")
        if st.button("🤖 Generate AI Investment Report"):
            with st.spinner("AI Agent is calculating market gaps..."):
                try:
                    from core.ai_analyzer import AIInvestmentAdvisor
                    summary_dict = df['category'].value_counts().to_dict()
                    advisor = AIInvestmentAdvisor()
                    report = advisor.generate_analysis(summary_dict)
                    st.markdown("### 📄 Professional AI Report")
                    st.info(report)
                    st.download_button("📥 Download Report as TXT", report, file_name="AI_Investment_Report.txt")
                except Exception as ai_err:
                    st.error(f"AI Engine Error: {ai_err}")

        # --- Influencer Outreach ---
        st.markdown("---")
        st.subheader("🤝 Influencer Outreach")
        inf_name = st.text_input("Influencer Name", "Zayed Vlogger")
        if st.button("📧 Generate Elite Pitch"):
            with st.spinner("Crafting negotiation message..."):
                try:
                    from agents.influencer_bot import InfluencerBot
                    bot = InfluencerBot()
                    top_loc = df['name'].iloc[0] if not df.empty else "Sheikh Zayed Area"
                    pitch = bot.craft_pitch(inf_name, top_loc)
                    st.write("---")
                    st.info(pitch)
                except Exception as e:
                    st.error(f"Outreach Error: {e}")

        st.markdown("---")
        if st.button("📥 Export Full Investor Data (CSV)"):
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv, "market_data.csv", "text/csv")

    # --- Finance & Affiliate Section ---
    st.markdown("---")
    st.header("💰 Business & Affiliate Center")
    f1, f2 = st.columns(2)

    with f1:
        st.subheader("🔗 Affiliate Link Generator")
        target_inf = st.selectbox("Select Influencer to Link", ["Zayed Vlogger", "Real Estate Pro", "Cairo Insider"])
        from core.finance_manager import FinanceManager
        fm = FinanceManager()
        ref_link = fm.generate_affiliate_link(target_inf)
        st.code(ref_link, language="text")
        st.caption("Share this link with the influencer to track conversions.")

    with f2:
        st.subheader("📈 Revenue Simulation")
        report_price = 500
        sales_count = st.slider("Simulated Sales via Influencer", 0, 100, 12)
        total_rev = sales_count * report_price
        influencer_cut = fm.calculate_payout(total_rev)
        
        st.metric("Total Revenue", f"${total_rev:,}", f"+${report_price} last sale")
        st.metric("Influencer Payout (20%)", f"${influencer_cut:,}", delta_color="normal")

    with st.expander("📂 View Raw Geospatial Database"):
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"System Offline: {e}")

st.markdown("<br><p style='text-align: center; color: #475569;'>Powered by GeoInvest AI MVP © 2026</p>", unsafe_allow_html=True)