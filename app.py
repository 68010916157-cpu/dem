import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="Special Anniversary ❤️", page_icon="❤️", layout="centered"
)

st.title("❤️ โปรแกรมฉลองครบรอบ 2 ปี ❤️")

# สร้าง Session State สำหรับเก็บสถานะการผ่านแต่ละขั้นตอน
if "step" not in st.session_state:
    st.session_state.step = 1
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Step 1: กรอกชื่อ
if st.session_state.step == 1:
    user_name = st.text_input("กรุณากรอกชื่อของคุณ:")
    if st.button("ถัดไป"):
        if user_name.strip() != "":
            st.session_state.user_name = user_name
            st.session_state.step = 2
            st.rerun()
        else:
            st.warning("กรุณากรอกชื่อก่อนนะครับ")

# Step 2: กรอกรหัสผ่าน (151125)
elif st.session_state.step == 2:
    st.write(f"สวัสดีครับคุณ **{st.session_state.user_name}**")
    password = st.text_input("กรุณาใส่รหัสผ่าน:", type="password")
    if st.button("ยืนยันรหัสผ่าน"):
        if password == "151125":
            st.session_state.step = 3
            st.rerun()
        else:
            st.error("ไม่ถูก จำก็ไม่ได้ใส่ใหม่เลย!")

# Step 3: คำถาม "รักแฟนมั๊ย?"
elif st.session_state.step == 3:
    st.subheader("คำถาม: รักแฟนมั๊ย?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("1. ไม่รัก", use_container_width=True):
            st.error("โอเคเลิกกันเลยไม่รักแล้ว 😭")

    with col2:
        if st.button("2. รัก", use_container_width=True):
            st.success("รักแฟนนนน 🥰")
            if st.button("ไปขั้นตอนถัดไป ➡️"):
                st.session_state.step = 4
                st.rerun()

# Step 4: ตอบคำถามวันเกิดแฟน (190649)
elif st.session_state.step == 4:
    birthday = st.text_input("วันเกิดแฟนเกิดวันที่เท่าไหร่ (เช่น 190649):")
    if st.button("ส่งคำตอบ"):
        if birthday == "190649":
            st.session_state.step = 5
            st.rerun()
        else:
            st.error("ไม่ถูก จำก็ไม่ได้ใส่ใหม่เลย!")

# Step 5: แสดงข้อความความรัก
elif st.session_state.step == 5:
    st.balloons()
    st.success("🎉 ถูกต้องแล้วครับ! 🎉")
    st.markdown(
        """
    ### ❤️ ความในใจ ❤️
    รักแฟนมากเลย ขอบคุณนะที่แฟนรักเค้าตามใจเค้าตลอด 
    ปีนี้ครบรอบปีที่ 2 ที่เราอยู่ด้วยกันหลังจากนี้เราก็จะอยู่ด้วยกันไปตลอดเลยยยย อิอิ รักนะจุ้บๆ
    """
    )
    st.header(f"✨ {st.session_state.user_name} LOVE First ✨")

    if st.button("เริ่มใหม่อีกครั้ง 🔄"):
        st.session_state.step = 1
        st.session_state.user_name = ""
        st.rerun()