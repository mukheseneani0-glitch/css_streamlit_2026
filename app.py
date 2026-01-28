# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 15:03:20 2026

@author: 22001691
"""

import streamlit as st
import base64

# Page config
st.set_page_config(page_title="Physics Educator Profile", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .profile-header {background: linear-gradient(90deg, #007bff, #0056b3); color: white; padding: 2rem; border-radius: 10px; text-align: center;}
    .profile-card {background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="profile-header"><h1>🔬 Physics Education Specialist</h1><p>University of Venda | Senior Phase & FET Physical Sciences</p></div>', unsafe_allow_html=True)

# Profile image (placeholder - replace with your photo path)
st.image("https://via.placeholder.com/200?text=Your+Photo", width=200)

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="profile-card">', unsafe_allow_html=True)
    st.subheader("📚 About Me")
    st.write("""
    - Education professional from Thohoyandou, Limpopo
    - Qualified BEd student specializing in physics education
    - Passionate about innovative science teaching methods
    - Developing Python skills for educational applications
    """)
    
    st.subheader("💼 Expertise")
    expertise = [
        "Physics & Physical Sciences teaching",
        "FET lesson planning & assessments", 
        "Student tutoring & exam preparation",
        "Python for educational tools"
    ]
    for skill in expertise:
        st.write(f"• {skill}")

with col2:
    st.markdown('<div class="profile-card">', unsafe_allow_html=True)
    st.subheader("🎯 Interests")
    interests = [
        "⚽ Football (Chelsea FC)",
        "💻 Coding & Programming", 
        "🎮 Gaming & Music",
        "📖 Reading & Learning",
        "🏊 Swimming"
    ]
    for interest in interests:
        st.write(interest)
    
    st.subheader("📍 Location")
    st.write("**Thohoyandou, Limpopo, South Africa**")
    st.write("Connect for physics education collaborations!")

# Footer
st.markdown("---")
st.markdown("*Profile created with Python & Streamlit for physics educators*")