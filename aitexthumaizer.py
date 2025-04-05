import streamlit as st
import re
import random
import io
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime
import json

# (Previous EnhancedTextHumanizer class remains the same)
# ... (copy the entire class from the previous artifact)

def main():
    # Page configuration with enterprise blue design
    st.set_page_config(
        page_title="Enterprise Text Intelligence", 
        page_icon="🏢",
        layout="wide"
    )

    # Enterprise Blue Color Palette
    ENTERPRISE_BLUE = {
        'primary': '#0D47A1',     # Deep blue (primary)
        'secondary': '#1565C0',   # Slightly lighter blue
        'accent': '#2196F3',      # Bright blue for highlights
        'background': '#F1F8E9',  # Light background
        'text': '#212121',        # Nearly black for text
        'white': '#FFFFFF'        # Pure white
    }

    # Custom CSS for enterprise-style design
    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {ENTERPRISE_BLUE['background']};
        color: {ENTERPRISE_BLUE['text']};
    }}
    .big-font {{
        font-size: 22px !important;
        font-weight: bold;
        color: {ENTERPRISE_BLUE['primary']};
    }}
    .stTextArea textarea {{
        background-color: {ENTERPRISE_BLUE['white']};
        border: 2px solid {ENTERPRISE_BLUE['primary']};
        border-radius: 8px;
        color: {ENTERPRISE_BLUE['text']};
    }}
    .stButton>button {{
        background-color: {ENTERPRISE_BLUE['primary']} !important;
        color: {ENTERPRISE_BLUE['white']} !important;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: {ENTERPRISE_BLUE['secondary']} !important;
        transform: scale(1.05);
    }}
    .result-box {{
        background-color: {ENTERPRISE_BLUE['white']};
        border: 1px solid {ENTERPRISE_BLUE['accent']};
        border-radius: 8px;
        padding: 20px;
        margin-top: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    .stColumnContainer {{
        background-color: {ENTERPRISE_BLUE['background']};
        padding: 20px;
        border-radius: 12px;
    }}
    </style>
    """, unsafe_allow_html=True)

    # Initialize the humanizer
    if 'humanizer' not in st.session_state:
        st.session_state.humanizer = EnhancedTextHumanizer()

    # Main content
    st.title("🏢 Enterprise Text Intelligence Platform")
    st.markdown("<p class='big-font'>Transform Your Communication with AI-Powered Insights</p>", unsafe_allow_html=True)

    # Create a container for input and controls with proper padding
    input_container = st.container()
    with input_container:
        # Input columns with enhanced spacing
        col1, col2 = st.columns([3, 1])

        with col1:
            input_text = st.text_area("Enter Your Text", 
                                      height=250, 
                                      placeholder="Paste the text you want to transform...",
                                      help="Input the text you'd like to elevate to enterprise-level communication")

        with col2:
            style = st.selectbox("Communication Style", 
                                 ["Professional", "Casual", "Technical"],
                                 help="Select the tone of your transformed text")
            
            intensity = st.slider("Transformation Intensity", 1, 10, 5,
                                  help="Adjust the depth of linguistic refinement")

    # Humanize button with centered alignment
    col_button = st.columns(3)[1]
    with col_button:
        humanize_button = st.button("Humanize Text", type="primary")

    # Result display
    if humanize_button and input_text:
        # Perform text humanization
        humanized_text = st.session_state.humanizer.humanize(
            input_text, 
            style=style, 
            intensity=intensity
        )
        
        # Create two columns for original and humanized text with padding
        col_orig, col_human = st.columns(2)
        
        with col_orig:
            st.markdown("### 📝 Original Text")
            st.markdown(f"<div class='result-box'>{input_text}</div>", unsafe_allow_html=True)
        
        with col_human:
            st.markdown("### 🚀 Humanized Text")
            st.markdown(f"<div class='result-box'>{humanized_text}</div>", unsafe_allow_html=True)
        
        # Transformation details
        with st.expander("Transformation Insights"):
            last_transformation = st.session_state.humanizer.transformation_history[-1]
            st.json(last_transformation)

    elif humanize_button and not input_text:
        st.warning("Please enter some text to transform!")

    # Footer
    st.markdown("---")
    st.markdown(f"<p style='color:{ENTERPRISE_BLUE['primary']}'>Powered by Enterprise AI Communication Solutions</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
