import streamlit as st
import re
import random
from datetime import datetime

# ---------------------- EnhancedTextHumanizer Class ----------------------
class EnhancedTextHumanizer:
    def __init__(self):
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
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        varied_sentences = []
        for sentence in sentences:
            if random.random() < 0.5:
                interjections = [
                    'Strategically speaking,', 
                    'Core insights suggest,', 
                    'From an operational standpoint,'
                ]
                if not any(sentence.startswith(interj) for interj in interjections):
                    sentence = f"{random.choice(interjections)} {sentence}"
            varied_sentences.append(sentence)
        return ' '.join(varied_sentences)

    def _introduce_professional_hesitation(self, text):
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
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        nuanced_sentences = []
        for sentence in sentences:
            if random.random() < 0.4:
                sentence = f"{random.choice(self.enterprise_qualifiers)} {sentence}"
            nuanced_sentences.append(sentence)
        return ' '.join(nuanced_sentences)

    def _refine_enterprise_punctuation(self, text):
        text = re.sub(r'(!{2,})', '!', text)
        text = re.sub(r'(\?{2,})', '?', text)
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        refined_sentences = []
        for sentence in sentences:
            if random.random() < 0.3:
                parts = sentence.split(',')
                if len(parts) > 1:
                    sentence = f"{parts[0]} — {','.join(parts[1:])}"
            refined_sentences.append(sentence)
        return ' '.join(refined_sentences)

    def humanize(self, text, style='Professional', intensity=5):
        if not text:
            return text
        style_modifiers = {
            'Professional': {'factor': 1.2, 'mods': 4},
            'Casual': {'factor': 0.9, 'mods': 3},
            'Technical': {'factor': 1.5, 'mods': 5}
        }
        style_config = style_modifiers.get(style, {'factor': 1.0, 'mods': 3})
        num_mods = max(2, min(len(self.modifications), 
                               round(style_config['mods'] * (intensity/5) * style_config['factor'])))
        selected_mods = random.sample(self.modifications, num_mods)
        humanized_text = text
        for modification in selected_mods:
            humanized_text = modification(humanized_text)
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

# ---------------------- Main App ----------------------
def main():
    st.set_page_config(
        page_title="Enterprise Text Intelligence", 
        page_icon="🏢",
        layout="wide"
    )

    ENTERPRISE_BLUE = {
        'primary': '#0D47A1',
        'secondary': '#1565C0',
        'accent': '#2196F3',
        'background': '#F1F8E9',
        'text': '#212121',
        'white': '#FFFFFF'
    }

    # CSS
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
        white-space: pre-wrap;
    }}
    </style>
    """, unsafe_allow_html=True)

    if 'humanizer' not in st.session_state:
        st.session_state.humanizer = EnhancedTextHumanizer()

    st.title("🏢 Enterprise Text Intelligence Platform")
    st.markdown("<p class='big-font'>Transform Your Communication with AI-Powered Insights</p>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        input_text = st.text_area("Enter Your Text", height=250, 
                                  placeholder="Paste the text you want to transform...",
                                  help="Input the text you'd like to elevate to enterprise-level communication")
    with col2:
        style = st.selectbox("Communication Style", ["Professional", "Casual", "Technical"])
        intensity = st.slider("Transformation Intensity", 1, 10, 5)

    col_button = st.columns(3)[1]
    with col_button:
        humanize_button = st.button("Humanize Text", type="primary")

    if humanize_button and input_text:
        humanized_text = st.session_state.humanizer.humanize(
            input_text, style=style, intensity=intensity
        )

        st.markdown("### 📊 Transformation Summary")
        st.markdown(f"- Original Length: **{len(input_text)} characters**")
        st.markdown(f"- Humanized Length: **{len(humanized_text)} characters**")
        st.markdown(f"- Word Count Difference: **{len(humanized_text.split()) - len(input_text.split())} words**")

        col_orig, col_human = st.columns(2)

        with col_orig:
            st.markdown("### 📝 Original Text")
            st.markdown(f"<div class='result-box'>{input_text}</div>", unsafe_allow_html=True)
            st.download_button("📥 Download Original", input_text, file_name="original_text.txt")
            st.code(input_text, language="markdown")

        with col_human:
            st.markdown("### 🚀 Humanized Text")
            st.markdown(f"<div class='result-box'>{humanized_text}</div>", unsafe_allow_html=True)
            st.download_button("📥 Download Humanized", humanized_text, file_name="humanized_text.txt")
            st.code(humanized_text, language="markdown")

        with st.expander("Transformation Insights"):
            last_transformation = st.session_state.humanizer.transformation_history[-1]
            st.json(last_transformation)

    elif humanize_button and not input_text:
        st.warning("Please enter some text to transform!")

    st.markdown("---")
    st.markdown(f"<p style='color:{ENTERPRISE_BLUE['primary']}'>Powered by Enterprise AI Communication Solutions</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
