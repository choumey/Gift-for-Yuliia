import streamlit as st
import time


st.set_page_config(
    page_title="Для Юли 🩷", 
    page_icon="💌", 
    layout="centered"
)
#css
st.markdown("""
    <style>
    /* Главный фон всей страницы */
    .stApp {
        background-color: #3E2723;
    }

    /* Стиль заголовков */
    h1, h3 {
        color: #F5F5DC !important;
        font-family: 'Georgia', serif;
        text-align: center;
    }

    /* Текст подписи */
    .footer-text {
        text-align: center;
        color: #D7CCC8;
        font-size: 14px;
        margin-top: 50px;
    }

    /* Контейнер для письма (эффект бумаги на темном фоне) */
    .letter-box {
        background-color: rgba(245, 245, 220, 0.05);
        border: 1px solid rgba(215, 204, 200, 0.2);
        border-radius: 15px;
        padding: 20px;
        transition: all 0.5s ease-in-out;
    }

    /* Кнопка "Открыть" */
    .stButton>button {
        background-color: #8D6E63;
        color: #F5F5DC;
        border-radius: 25px;
        border: 1px solid #D7CCC8;
        padding: 10px 30px;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #5D4037;
        border: 1px solid #F5F5DC;
        color: #FFFFFF;
    }

    /* Центровка контента */
    .center-content {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Логика приложения
if 'opened' not in st.session_state:
    st.session_state.opened = False

# Заголовок
st.markdown("<h1>не в бумажном виде..., но письмо на месте! 💌</h1>", unsafe_allow_html=True)
st.write("---")

# 4. Контент (Конверт или Письмо)
if not st.session_state.opened:
    # Состояние ЗАКРЫТО
    st.markdown("<div class='center-content'><br><br></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h3 style='font-style: italic;'>давай глянем что внутри хохох</h3>", unsafe_allow_html=True)
        if st.button("Открыть ✉️"):
            st.session_state.opened = True
            st.balloons()
            st.rerun()
else:

    with st.spinner('Разворачиваю...'):
        time.sleep(1)
    
    st.markdown("<div class='letter-box'>", unsafe_allow_html=True)
    
    try:
        st.image("letter.png", use_container_width=True)
    except:
        st.error("Ошибка: Файл 'letter.png' не найден в репозитории. Проверь название!")

    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Закрыть"):
            st.session_state.opened = False
            st.rerun()

# 5. Футер
st.markdown("<div class='footer-text'>для Юли  •  от Васи</div>", unsafe_allow_html=True)




