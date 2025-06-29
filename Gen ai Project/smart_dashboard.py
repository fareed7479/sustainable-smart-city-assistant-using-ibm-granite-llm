import streamlit as st
from streamlit_option_menu import option_menu
from frontend.components import chat_assistant

st.set_page_config(page_title="Sustainable Smart City Assistant", layout="wide")

def main():
    st.markdown(
        """
        <style>
        .main-header {
            background: linear-gradient(90deg, #00b09b, #96c93d);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="main-header">Sustainable Smart City Assistant</div>', unsafe_allow_html=True)

    with st.sidebar:
        selected = option_menu(
            "Modules",
            ["Chat Assistant", "Eco Tips", "Policy Search", "KPI Forecasting", "Anomaly Detection", "Citizen Feedback", "Report Generator", "Dashboard"],
            icons=["chat-dots", "leaf", "file-earmark-text", "bar-chart-line", "exclamation-triangle", "person-lines-fill", "file-text", "speedometer2"],
            menu_icon="cast",
            default_index=0,
        )

    if selected == "Chat Assistant":
        chat_assistant.chat_assistant()
    else:
        st.info(f"{selected} module is under construction.")

if __name__ == "__main__":
    main()
