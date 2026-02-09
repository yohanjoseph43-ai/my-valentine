import streamlit as st

# 1. Setup the page
st.set_page_config(page_title="For My Favorite Person", page_icon="❤️")

# 2. Custom CSS for "Alive" animations and Romantic Fonts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300&display=swap');

    /* Soft pink gradient background */
    .stApp {
        background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    }

    /* Pulsing heart animation */
    .heart-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }
    .pulsing-heart {
        font-size: 100px;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }

    /* Elegant Font Styles */
    .main-title {
        font-family: 'Great Vibes', cursive;
        font-size: 80px !important;
        color: #d00000;
        text-align: center;
        margin-top: -20px;
    }
    .love-letter {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
        color: #4a4a4a;
        text-align: center;
        background: rgba(255, 255, 255, 0.4);
        padding: 30px;
        border-radius: 20px;
        margin: 20px auto;
        max-width: 600px;
    }
    </style>

    <div class="heart-container">
        <div class="pulsing-heart">💖</div>
    </div>
    <h1 class="main-title">Happy Valentine's Day</h1>
    
    <div class="love-letter">
        Every line of this code was written thinking of you.<br><br>
        You are my favorite person, my greatest adventure,<br>
        and the heart of my world.
    </div>
    """, unsafe_allow_html=True)

# 3. Interactive Surprise Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✨ Tap for a Surprise ✨"):
        st.balloons()
        st.snow()
        st.markdown("<h1 style='text-align:center; color:#d00000; font-family:Great Vibes;'>I Love You!</h1>", unsafe_allow_html=True)
