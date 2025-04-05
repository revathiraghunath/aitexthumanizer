import streamlit as st
import re
import random
import io
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime
import json

class EnhancedTextHumanizer:
    def __init__(self):
        """
        Enterprise-grade Text Humanizer with advanced transformation capabilities
        """
        self.modifications = [
            self._add_professional_transitions,
            self._vary_sentence_structure,
            self._introduce_professional_hesitation,
            self._add_enterprise_nuance,
            self._refine_enterprise_punctuation
        ]
        self.transformation_history = []
        self.enterprise_qualifiers = [
            'Strategic insights reveal that',
            'Our comprehensive analysis indicates',
            'From a holistic perspective,',
            'Leveraging our deep expertise,'
        ]

    def _add_professional_transitions(self, text):
        """Enhanced professional transition words with enterprise vocabulary"""
        transition_mappings = {
            r'\b(Furthermore|Moreover|Additionally)\b': [
                'In alignment with our strategic framework,', 
                'Complementing our comprehensive approach,', 
                'Extending our core insights,'
            ],
            r'\b(However|Nevertheless)\b': [
                'Balancing our strategic considerations,', 
                'Navigating potential complexities,', 
                'With nuanced strategic perspective,'
            ]
        }
        
        for pattern, replacements in transition_mappings.items():
            text = re.sub(pattern, lambda m: random.choice(replacements), text)
        
        return text

    def _vary_sentence_structure(self, text):
        """Advanced sentence structure variation for professional communication"""
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        
        varied_sentences = []
        
        for sentence in sentences:
            # More sophisticated structure modification
            if random.random() < 0.5:
                enterprise_interjections = [
                    'Strategically speaking,', 
                    'Core insights suggest,', 
                    'From an operational standpoint,'
                ]
                if not any(sentence.startswith(interj) for interj in enterprise_interjections):
                    sentence = f"{random.choice(enterprise_interjections)} {sentence}"
            
            varied_sentences.append(sentence)
        
        return ' '.join(varied_sentences)

    def _introduce_professional_hesitation(self, text):
        """Enterprise-level hesitation markers"""
        hesitation_markers = [
            ' — considering the broader context, ', 
            ' ... strategically speaking, ', 
            ' with careful consideration, ', 
            ' pivoting our perspective, '
        ]
        
        words = text.split()
        for i in range(len(words)-1, 0, -1):
            if random.random() < 0.15:
                words.insert(i, random.choice(hesitation_markers).strip())
        
        return ' '.join(words)

    def _add_enterprise_nuance(self, text):
        """Advanced contextual nuancing for enterprise communication"""
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        
        nuanced_sentences = []
        
        for sentence in sentences:
            # More sophisticated qualifier application
            if random.random() < 0.4:
                sentence = f"{random.choice(self.enterprise_qualifiers)} {sentence}"
            
            nuanced_sentences.append(sentence)
        
        return ' '.join(nuanced_sentences)

    def _refine_enterprise_punctuation(self, text):
        """Advanced punctuation refinement for professional communication"""
        # More sophisticated punctuation handling
        text = re.sub(r'(!{2,})', '!', text)
        text = re.sub(r'(\?{2,})', '?', text)
        
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        refined_sentences = []
        
        for sentence in sentences:
            if random.random() < 0.3:
                parts = sentence.split(',')
                if len(parts) > 1:
                    # More professional em dash usage
                    sentence = f"{parts[0]} — {','.join(parts[1:])}"
            
            refined_sentences.append(sentence)
        
        return ' '.join(refined_sentences)

    def humanize(self, text, style='Professional', intensity=5):
        """
        Enterprise-grade text transformation method
        
        Args:
            text (str): Input text to humanize
            style (str): Communication style 
            intensity (int): Transformation depth
        
        Returns:
            str: Professionally humanized text
        """
        if not text:
            return text

        # Enhanced style and intensity mapping
        style_modifiers = {
            'Professional': {'factor': 1.2, 'mods': 4},
            'Casual': {'factor': 0.9, 'mods': 3},
            'Technical': {'factor': 1.5, 'mods': 5}
        }
        
        style_config = style_modifiers.get(style, {'factor': 1.0, 'mods': 3})
        
        # More sophisticated modification selection
        num_mods = max(2, min(len(self.modifications), 
                               round(style_config['mods'] * (intensity/5) * style_config['factor'])))
        
        selected_mods = random.sample(self.modifications, num_mods)
        
        humanized_text = text
        for modification in selected_mods:
            humanized_text = modification(humanized_text)
        
        # Enhanced transformation tracking
        transformation_record = {
            'timestamp': datetime.now().isoformat(),
            'original_length': len(text),
            'humanized_length': len(humanized_text),
            'style': style,
            'intensity': intensity,
            'modifications_applied': [mod.__name__ for mod in selected_mods]
        }
        self.transformation_history.append(transformation_record)
        
        return humanized_text

def main():
    # Page configuration with enterprise branding
    st.set_page_config(
        page_title="Enterprise Text Intelligence Platform", 
        page_icon="🏢",
        layout="wide"
    )

    # Initialize the humanizer
    if 'humanizer' not in st.session_state:
        st.session_state.humanizer = EnhancedTextHumanizer()

    # Custom enterprise-style CSS
    st.markdown("""
    <style>
    .enterprise-title {
        color: #004080;
        font-weight: bold;
        text-align: center;
    }
    .stApp {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #004080;
        color: white;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Enterprise-style title
    st.markdown('<h1 class="enterprise-title">🏢 Enterprise Text Intelligence Platform</h1>', unsafe_allow_html=True)
    
    # Input text area
    input_text = st.text_area("Enter Text to Humanize", height=200)
    
    # Style and intensity selection
    col1, col2 = st.columns(2)
    
    with col1:
        style = st.selectbox("Select Communication Style", 
                              ["Professional", "Casual", "Technical"])
    
    with col2:
        intensity = st.slider("Transformation Intensity", 1, 10, 5)
    
    # Humanize button
    if st.button("Humanize Text"):
        if input_text:
            # Perform text humanization
            humanized_text = st.session_state.humanizer.humanize(
                input_text, 
                style=style, 
                intensity=intensity
            )
            
            # Display original and humanized text
            st.subheader("Original Text")
            st.text(input_text)
            
            st.subheader("Humanized Text")
            st.text(humanized_text)
            
            # Display transformation history
            st.subheader("Transformation Details")
            last_transformation = st.session_state.humanizer.transformation_history[-1]
            st.json(last_transformation)
        else:
            st.warning("Please enter some text to humanize.")

if __name__ == "__main__":
    main()
