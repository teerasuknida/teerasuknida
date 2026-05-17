import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="OKJ AI Agent", layout="wide")
st.markdown("<h4 style='text-align: center;'>✨ Ask AI about financial savings...</h4>", unsafe_allow_html=True)

model = genai.GenerativeModel('gemini-pro')
user_input = st.chat_input("พิมพ์คำถามของคุณที่นี่ เช่น 'สรุปปัญหาขยะอาหารเดือนนี้ให้หน่อย'")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    
    with st.chat_message("assistant"):
        try:
            safe_prompt = f"""
            คุณคือ AI ผู้ช่วยผู้บริหาร (CFO Assistant) ของแบรนด์ร้านอาหาร 'โอ้กะจู่ (OKJ)'
            อ้างอิงข้อมูล Food Waste POC เดือนพฤษภาคม 2026:
            - Total Waste Value: 26,277 บาท
            - Estimated Cost Savings (26%): 6,832 บาท
            - สาเหตุหลัก: Spoilage (ของเสีย) 46.7%
            - สินค้าเฝ้าระวัง: เนื้อไก่ (ใกล้หมดอายุ), แซลมอน (Demand ต่ำ)
            
            จงตอบคำถามนี้แบบผู้เชี่ยวชาญ สั้น กระชับ: {user_input}
            """
            
            response = model.generate_content(safe_prompt)
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Error detail: {e}")
