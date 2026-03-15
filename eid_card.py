import streamlit as st
import random

st.set_page_config(page_title="Eid Mubarak Card", layout="centered")

# Custom CSS for animation
st.markdown("""
<style>
body {
background: linear-gradient(135deg,#1e3c72,#2a5298);
color:white;
text-align:center;
font-family:sans-serif;
}

.card {
background:white;
color:black;
padding:30px;
border-radius:20px;
margin-top:20px;
font-size:22px;
box-shadow:0 0 20px rgba(255,255,255,0.5);
}

.star {
position:fixed;
font-size:24px;
animation: float 8s linear infinite;
}

@keyframes float {
0% {transform: translateY(100vh);}
100% {transform: translateY(-10vh);}
}

.moon {
font-size:60px;
animation: glow 2s infinite alternate;
}

@keyframes glow {
from {opacity:0.6;}
to {opacity:1;}
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='moon'>🌙</div>", unsafe_allow_html=True)

st.title("Eid Mubarak Card Generator")

your_name = st.text_input("Your Name")
friend_name = st.text_input("Friend's Name")

duas = [
"May Allah accept your prayers and fill your life with happiness.",
"May this Eid bring peace, joy and success to your life.",
"May Allah shower countless blessings upon you.",
"May your home be filled with happiness and barakah."
]

if st.button("Send Eid Card 🎁"):

    dua = random.choice(duas)

    st.markdown(f"""
    <div class="card">
    🌙 Eid Mubarak {friend_name}! 🌙 <br><br>
    {dua} 🤲 <br><br>
    💖 From: {your_name}
    </div>
    """, unsafe_allow_html=True)

    stars = ["⭐","✨","🌟","🎉"]

    for i in range(25):
        st.markdown(
            f"<div class='star' style='left:{random.randint(0,100)}%'>{random.choice(stars)}</div>",
            unsafe_allow_html=True
        )