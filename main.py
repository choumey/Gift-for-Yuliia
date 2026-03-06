import streamlit as st
import time

st.set_page_config(page_title="Для Юли 🩷", page_icon="💌", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #4B3621;
    }
    .stButton>button {
        background-color: #ffb7c5;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
        font-size: 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff8fa3;
        border: none;
        color: white;
    }
    .envelope-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin-top: 50px;
    }
    .heart {
        font-size: 50px;
        color: #ff4d6d;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

st.write("<div style='text-align: center;'><h1>Тебе пришло письмо! 💌</h1></div>", unsafe_allow_html=True)

if 'opened' not in st.session_state:
    st.session_state.opened = False

if not st.session_state.opened:
    st.markdown("<div class='envelope-container'><div class='heart'>❤️</div></div>", unsafe_allow_html=True)
    st.write("<div style='text-align: center; margin-bottom: 20px;'>Нажми на кнопку, чтобы открыть конвертик</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Открыть ✉️"):
            st.session_state.opened = True
            st.balloons() 
            st.rerun()

else:
    # Анимация "загрузки"
    with st.spinner('Сюрприз вот вот покажется...'):
        time.sleep(1.5)
    
    st.markdown("<div style='text-align: center;'><h3>С 8 Марта! ✨</h3></div>", unsafe_allow_html=True)
    
    try:
        st.image("letter.png", use_container_width=True)
    except:
        st.error("Файл 'letter.png' не найден. Положи картинку в папку с кодом!")

    if st.button("Закрыть письмо"):
        st.session_state.opened = False
        st.rerun()

# Футер

st.markdown("<br><br><div style='text-align: center; color: #888;'>от Васи с любовью</div>", unsafe_allow_html=True)
