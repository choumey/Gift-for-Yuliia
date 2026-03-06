import streamlit as st
import time

st.set_page_config(page_title="Для Юли 🩷", page_icon="💌", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #4B3621; 
        
    }
    
    
    h1, h3, p, span, div {
        color: #F5F5DC !important; 
    }

    .stButton>button {
        background-color: #8B4513;
        color: white;
        border-radius: 20px;
        border: 2px solid #F5F5DC;
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

