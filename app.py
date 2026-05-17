import streamlit as st
import google.generativeai as genai

# ใส่ API Key ของ Gemini
genai.configure(api_key="AIzaSyBGhFI3cToqMLJFVde-Dkdmg_IWdSUZWvM")
st.set_page_config(page_title="OKJ AI Agent", layout="wide")
st.markdown("<h4 style='text-align: center;'>✨ Ask AI about financial savings...</h4>", unsafe_allow_html=True)

# Pre-prompt gemini เพื่อให้เข้าใจบริบทของเรา
system_instruction = """
คุณคือ AI ผู้ช่วยผู้บริหาร (CFO Assistant) ของแบรนด์ร้านอาหาร 'โอ้กะจู่ (OKJ)'
คุณมีข้อมูลสรุป POC ขยะอาหาร (Food Waste) ของเดือนพฤษภาคม 2026 ดังนี้:
- Total Waste Value (มูลค่าความสูญเสียรวม): 26,277 บาท
- Estimated Cost Savings (ประหยัดได้หากลดขยะ 26%): 6,832 บาท
- สาเหตุหลักอันดับ 1: Spoilage (ของเสีย) 46.7%
- วัตถุดิบที่ต้องระวัง: เนื้อไก่ (ใกล้หมดอายุ) และ แซลมอน (Demand ต่ำ)
จงตอบคำถามผู้บริหารด้วยความกระชับ เป็นมืออาชีพ และเน้นตัวเลขทางการเงิน
"""

model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_instruction)

# ระบบรับข้อความแชท
user_input = st.chat_input("พิมพ์คำถามของคุณที่นี่ เช่น 'สรุปปัญหาขยะอาหารเดือนนี้ให้หน่อย'")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        response = model.generate_content(user_input)
        st.write(response.text)