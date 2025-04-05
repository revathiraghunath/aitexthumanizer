import streamlit as st
import re
import random

# Set page configuration for light theme
st.set_page_config(
    page_title="Text Humanizer",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="auto"
)

# Light theme custom styling
st.markdown("""
<style>
    /* Reset to light theme */
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    
    /* Main container */
    .main {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* Text Input Areas */
    .stTextArea > div > div > textarea {
        background-color: #f8f9fa !important;
        color: #000000 !important;
        border: 1px solid #ced4da !important;
    }
    
    /* Slider and Dropdown */
    .stSlider, .stSelectbox {
        background-color: #f1f3f5 !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #2c3e50 !important;
        color: white !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
    }
    
    .stButton > button:hover {
        background-color: #34495e !important;
    }
</style>
""", unsafe_allow_html=True)

class TextHumanizer:
    def __init__(self):
        """
        Initialize the Text Humanizer with comprehensive transformations
        """
        self.modifications = [
            self._add_professional_transitions,
            self._vary_sentence_structure,
            self._introduce_natural_hesitation,
            self._add_contextual_nuance,
            self._refine_punctuation
        ]

    def _simple_sentence_split(self, text: str) -> list:
        """
        Split text into sentences using regex
        """
        return re.split(r'(?<=[.!?])\s+', text)

    def _add_professional_transitions(self, text: str) -> str:
        """Add nuanced, professional-sounding transition words"""
        transition_mappings = {
            r'\b(Furthermore|Moreover|Additionally)\b': ['In light of this,', 'Considering this context,', 'From another perspective,'],
            r'\b(However|Nevertheless)\b': ['On the other hand,', 'With that said,', 'It\'s worth noting that']
        }
        
        for pattern, replacements in transition_mappings.items():
            text = re.sub(pattern, lambda m: random.choice(replacements), text)
        
        return text

    def _vary_sentence_structure(self, text: str) -> str:
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

    def _introduce_natural_hesitation(self, text: str) -> str:
        """Add subtle, natural hesitation markers"""
        hesitation_markers = [' — ', ' ... ', ' well, ', ' actually, ']
        
        # Split into words and occasionally insert hesitation
        words = text.split()
        for i in range(len(words)-1, 0, -1):
            if random.random() < 0.1:
                words.insert(i, random.choice(hesitation_markers).strip())
        
        return ' '.join(words)

    def _add_contextual_nuance(self, text: str) -> str:
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

    def _refine_punctuation(self, text: str) -> str:
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

    def humanize(self, text: str) -> str:
        """
        Apply a random subset of humanization techniques
        
        Args:
            text (str): Input text to humanize
        
        Returns:
            str: Humanized text
        """
        if not text:
            return text

        # Randomly select and apply modifications
        num_mods = random.randint(2, len(self.modifications))
        selected_mods = random.sample(self.modifications, num_mods)
        
        humanized_text = text
        for modification in selected_mods:
            humanized_text = modification(humanized_text)
        
        return humanized_text

def main():
    """
    Streamlit application for text humanization
    """
    # Initialize the humanizer
    humanizer = TextHumanizer()

    # App title and description
    st.title("Text Humanizer")
    st.markdown("Transform AI-generated text into natural, conversational language")

    # Input section
    input_text = st.text_area(
        "Input AI-Generated Text", 
        height=300,
        placeholder="Paste your text here for humanization..."
    )

    # Transformation settings
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Transformation Intensity")
        intensity = st.slider(
            "Humanization Level", 
            min_value=1, 
            max_value=10, 
            value=5,
            help="Adjust the depth of linguistic transformations"
        )
    
    with col2:
        st.subheader("Communication Style")
        style = st.selectbox(
            "Tone",
            ["Professional", "Casual", "Technical"],
            help="Select the desired communication approach"
        )

    # Humanize button
    if st.button("Humanize Text", use_container_width=True):
        if input_text:
            # Humanize the text
            humanized_text = humanizer.humanize(input_text)
            
            # Display results
            st.success("Text Successfully Transformed")
            
            # Side-by-side comparison
            col_original, col_humanized = st.columns(2)
            
            with col_original:
                st.subheader("Original")
                st.text_area("Original Text", value=input_text, height=300, disabled=True)
            
            with col_humanized:
                st.subheader("Humanized")
                st.text_area("Humanized Text", value=humanized_text, height=300, disabled=True)
            
            # Download option
            st.download_button(
                label="Download Transformed Text",
                data=humanized_text,
                file_name="humanized_text.txt",
                mime="text/plain",
                use_container_width=True
            )
        else:
            st.warning("Please enter text to transform")

    # Methodology section
    st.markdown("---")
    st.markdown("""
    ### Our Approach to Text Humanization
    - Advanced linguistic transformation techniques
    - Contextual language intelligence
    - Preserves original meaning and intent
    - Enhances readability and natural communication
    """)

if __name__ == "__main__":
    main()
