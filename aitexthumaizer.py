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
        Initialize the Enhanced Text Humanizer with comprehensive transformations
        """
        self.modifications = [
            self._add_professional_transitions,
            self._vary_sentence_structure,
            self._introduce_natural_hesitation,
            self._add_contextual_nuance,
            self._refine_punctuation
        ]
        self.transformation_history = []

    def _simple_sentence_split(self, text):
        """Split text into sentences using regex"""
        return re.split(r'(?<=[.!?])\s+', text.strip())

    def _add_professional_transitions(self, text):
        """Add nuanced, professional-sounding transition words"""
        transition_mappings = {
            r'\b(Furthermore|Moreover|Additionally)\b': ['In light of this,', 'Considering this context,', 'From another perspective,'],
            r'\b(However|Nevertheless)\b': ['On the other hand,', 'With that said,', 'It\'s worth noting that']
        }
        
        for pattern, replacements in transition_mappings.items():
            text = re.sub(pattern, lambda m: random.choice(replacements), text)
        
        return text

    def _vary_sentence_structure(self, text):
        """Introduce variations in sentence structure"""
        sentences = self._simple_sentence_split(text)
        
        varied_sentences = []
        
        for sentence in sentences:
            # Randomly decide to modify sentence structure
            if random.random() < 0.4:
                # Add professional interjections
                interjections = ['Notably,', 'Interestingly,', 'Indeed,']
                if not any(sentence.startswith(interj) for interj in interjections):
                    sentence = f"{random.choice(interjections)} {sentence}"
            
            varied_sentences.append(sentence)
        
        return ' '.join(varied_sentences)

    def _introduce_natural_hesitation(self, text):
        """Add subtle, natural hesitation markers"""
        hesitation_markers = [' — ', ' ... ', ' well, ', ' actually, ']
        
        # Split into words and occasionally insert hesitation
        words = text.split()
        for i in range(len(words)-1, 0, -1):
            if random.random() < 0.1:
                words.insert(i, random.choice(hesitation_markers).strip())
        
        return ' '.join(words)

    def _add_contextual_nuance(self, text):
        """Add contextual nuance and professional qualifiers"""
        sentences = self._simple_sentence_split(text)
        
        qualifiers = [
            'It appears that',
            'From our analysis,',
            'Based on current insights,',
            'Our research suggests that'
        ]
        
        nuanced_sentences = []
        
        for sentence in sentences:
            # Occasionally prefix with a qualifier
            if random.random() < 0.3:
                sentence = f"{random.choice(qualifiers)} {sentence}"
            
            nuanced_sentences.append(sentence)
        
        return ' '.join(nuanced_sentences)

    def _refine_punctuation(self, text):
        """Refine punctuation for more natural flow"""
        # Replace overused punctuation
        text = re.sub(r'(!{2,})', '!', text)
        text = re.sub(r'(\?{2,})', '?', text)
        
        sentences = self._simple_sentence_split(text)
        refined_sentences = []
        
        for sentence in sentences:
            if random.random() < 0.2:
                parts = sentence.split(',')
                if len(parts) > 1:
                    sentence = f"{parts[0]} — {','.join(parts[1:])}"
            
            refined_sentences.append(sentence)
        
        return ' '.join(refined_sentences)

    def humanize(self, text, style='Professional', intensity=5):
        """
        Apply a random subset of humanization techniques
        
        Args:
            text (str): Input text to humanize
            style (str): Communication style (Professional, Casual, Technical)
            intensity (int): Transformation intensity (1-10)
        
        Returns:
            str: Humanized text
        """
        if not text:
            return text

        # Adjust modifications based on style and intensity
        style_modifiers = {
            'Professional': 1.0,
            'Casual': 0.8,
            'Technical': 1.2
        }
        style_factor = style_modifiers.get(style, 1.0)
        
        # Calculate number of modifications based on intensity and style
        num_mods = max(2, min(len(self.modifications), 
                               round(random.randint(2, len(self.modifications)) * (intensity/5) * style_factor)))
        
        selected_mods = random.sample(self.modifications, num_mods)
        
        humanized_text = text
        for modification in selected_mods:
            humanized_text = modification(humanized_text)
        
        # Record transformation history
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

def create_transformation_analytics(humanizer):
    """
    Create analytics visualization for transformations
    """
    if not humanizer.transformation_history:
        st.warning("No transformation history available.")
        return

    # Convert history to DataFrame
    df = pd.DataFrame(humanizer.transformation_history)
    
    # Transformation Intensity Distribution
    fig_intensity = go.Figure(data=[
        go.Histogram(x=df['intensity'], nbinsx=10, name='Transformation Intensity')
    ])
    fig_intensity.update_layout(title='Transformation Intensity Distribution')
    
    # Modifications Applied
    mod_counts = {}
    for record in humanizer.transformation_history:
        for mod in record['modifications_applied']:
            mod_counts[mod] = mod_counts.get(mod, 0) + 1
    
    fig_mods = go.Figure(data=[
        go.Pie(labels=list(mod_counts.keys()), values=list(mod_counts.values()), hole=.3)
    ])
    fig_mods.update_layout(title='Modifications Applied')
    
    return fig_intensity, fig_mods

def main():
    """
    Enterprise-grade Streamlit application for text humanization
    """
    # Page configuration
    st.set_page_config(
        page_title="Enterprise Text Humanizer", 
        page_icon="🧠",
        layout="wide"
    )

    # Initialize the humanizer
    if 'humanizer' not in st.session_state:
        st.session_state.humanizer = EnhancedTextHumanizer()

    # Custom CSS for enterprise look
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .stApp {
        background-color: #f4f4f4;
    }
    .stButton>button {
        background-color: #004080;
        color: white;
    }
    .stTextArea>div>div>textarea {
        border: 2px solid #004080;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title and Introduction
    st.title("🧠 Enterprise Text Humanization Platform")
    st.markdown("### Advanced AI-Powered Language Transformation")

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        # Input section
        st.subheader("Text Input")
        input_text = st.text_area(
            "Input AI-Generated Text", 
            height=300,
            placeholder="Paste your text here for humanization...",
            key="input_text"
        )

        # Transformation settings
        col_style, col_intensity = st.columns(2)
        
        with col_style:
            style = st.selectbox(
                "Communication Style",
                ["Professional", "Casual", "Technical"],
                help="Select the desired communication approach"
            )
        
        with col_intensity:
            intensity = st.slider(
                "Transformation Intensity", 
                min_value=1, 
                max_value=10, 
                value=5,
                help="Adjust the depth of linguistic transformations"
            )

        # Humanize button
        if st.button("Humanize Text", type="primary"):
            if input_text:
                # Humanize the text
                humanized_text = st.session_state.humanizer.humanize(
                    input_text, 
                    style=style, 
                    intensity=intensity
                )
                
                # Display results
                st.success("Text Successfully Transformed")
                
                # Display humanized text
                st.text_area(
                    "Humanized Text", 
                    value=humanized_text, 
                    height=300, 
                    key="humanized_output"
                )
                
                # Download and Copy options
                col_download, col_copy = st.columns(2)
                
                with col_download:
                    st.download_button(
                        label="Download Transformed Text",
                        data=humanized_text,
                        file_name="humanized_text.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col_copy:
                    st.button(
                        "Copy to Clipboard", 
                        on_click=lambda: st.toast("Text Copied!"),
                        use_container_width=True
                    )
            else:
                st.warning("Please enter text to transform")

    with col2:
        # Analytics and History
        st.subheader("Transformation Analytics")
        
        # Show transformation analytics if history exists
        if st.session_state.humanizer.transformation_history:
            try:
                fig_intensity, fig_mods = create_transformation_analytics(st.session_state.humanizer)
                
                # Intensity Distribution
                st.plotly_chart(fig_intensity, use_container_width=True)
                
                # Modifications Pie Chart
                st.plotly_chart(fig_mods, use_container_width=True)
                
                # Transformation History
                st.subheader("Recent Transformations")
                history_df = pd.DataFrame(st.session_state.humanizer.transformation_history)
                st.dataframe(history_df, use_container_width=True)
                
                # Export History Option
                if st.button("Export Transformation History"):
                    history_json = json.dumps(st.session_state.humanizer.transformation_history, indent=2)
                    st.download_button(
                        label="Download History",
                        data=history_json,
                        file_name="transformation_history.json",
                        mime="application/json"
                    )
            except Exception as e:
                st.error(f"Error generating analytics: {e}")
        else:
            st.info("Transform some text to see analytics")

    # Methodology and Features
    st.markdown("---")
    st.markdown("""
    ### 🚀 Enterprise-Grade Features
    - **Advanced Linguistic AI**: Sophisticated text transformation techniques
    - **Customizable Styles**: Professional, Casual, and Technical modes
    - **Intensity Control**: Fine-tune transformation depth
    - **Comprehensive Analytics**: Track and analyze text transformations
    - **Secure and Private**: Process text locally, no external data sharing
    """)

if __name__ == "__main__":
    main()
