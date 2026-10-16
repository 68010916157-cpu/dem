import streamlit as st

# ตั้งค่าหน้าจอและหัวข้อโปรแกรม
st.set_page_config(
    page_title="Special Anniversary ❤️", page_icon="❤️", layout="centered"
)

# จัดการขั้นตอนการทำงาน (State)
if "step" not in st.session_state:
    st.session_state.step = 1
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# ==========================================
# 1. ใส่ชื่อ
# ==========================================
if st.session_state.step == 1:
    st.subheader("1. กรอกชื่อของคุณ")
    name_input = st.text_input("กรุณากรอกชื่อของคุณ:")
    if st.button("ตกลง / ไปขั้นตอนถัดไป"):
        if name_input.strip() != "":
            st.session_state.user_name = name_input.strip()
            st.session_state.step = 2
            st.rerun()
        else:
            st.warning("กรุณากรอกชื่อก่อนนะครับ")

# ==========================================
# 2. ใส่รหัสผ่าน (151125)
# ==========================================
elif st.session_state.step == 2:
    st.subheader("2. ยืนยันรหัสผ่าน")
    pwd_input = st.text_input("กรุณาใส่รหัสผ่าน:", type="password")
    if st.button("ยืนยัน"):
        if pwd_input == "151125":
            st.session_state.step = 3
            st.rerun()
        else:
            st.error("ไม่ถูก จำก็ไม่ได้ใส่ใหม่เลย")

# ==========================================
# 3 & 4. ตอบคำถาม "รักแฟนมั๊ย"
# ==========================================
elif st.session_state.step == 3:
    st.subheader("3. คำถาม: รักแฟนมั๊ย")

    col1, col2 = st.columns(2)

    # เลือกตอบข้อ 1. ไม่รัก
    with col1:
        if st.button("1. ไม่รัก", use_container_width=True):
            st.session_state.choice = "1"

    # เลือกตอบข้อ 2. รัก
    with col2:
        if st.button("2. รัก", use_container_width=True):
            st.session_state.choice = "2"

    # แสดงผลลัพธ์ตามข้อที่เลือก
    if "choice" in st.session_state:
        if st.session_state.choice == "1":
            st.error("โอเคเลิกกันเลยไม่รักแล้ว")
        elif st.session_state.choice == "2":
            st.success("รักแฟนนนน")
            st.write("---")
            if st.button("กดไปขั้นตอนต่อไป ➡️"):
                st.session_state.step = 4
                del st.session_state.choice
                st.rerun()

# ==========================================
# 5. ตอบคำถามวันเกิดแฟน (190649)
# ==========================================
elif st.session_state.step == 4:
    st.subheader("5. คำถาม: วันเกิดแฟนเกิดวันที่เท่าไหร่")
    bday_input = st.text_input("กรอกวันเกิดแฟน:")
    if st.button("ส่งคำตอบ"):
        if bday_input == "190649":
            st.session_state.step = 5
            st.rerun()
        else:
            st.error("ไม่ถูก จำก็ไม่ได้ใส่ใหม่เลย")

# ==========================================
# 6, 7 & 8. แสดงข้อความความรัก + ชื่อ LOVE First + จบ
# ==========================================
elif st.session_state.step == 5:
    st.balloons()

    # ข้อ 6. ข้อความความรัก
    st.info(
        "รักแฟนมากเลย ขอบคุณนะที่แฟนรักเค้าตามใจเค้าตลอด "
        "ปีนี้ครบรอบปีที่ 2 ที่เราอยู่ด้วยกันหลังจากนี้เราก็จะอยู่ด้วยกันไปตลอดเลยยยย "
        "อิอิ รักนะจุ้บๆ"
    )

    # ข้อ 7. แสดง [ชื่อที่รับเข้ามาตอนแรก] LOVE First
    st.markdown(f"### ❤️ **{st.session_state.user_name} LOVE First** ❤️")

    # ข้อ 8. จบโปรแกรม (ปุ่มเริ่มใหม่)
    st.write("---")
    if st.button("เริ่มใหม่อีกครั้ง 🔄"):
        st.session_state.step = 1
        st.session_state.user_name = ""
        st.rerun()