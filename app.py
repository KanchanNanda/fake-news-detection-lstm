
import streamlit as st
import tensorflow as tf
from pathlib import Path

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="🔎",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #151b33);
    color: #f4f6ff;
}
h1, h2, h3, p, label {
    color: #f4f6ff !important;
}
.hero {
    padding: 28px;
    border: 1px solid #343d60;
    border-radius: 20px;
    background: #171f38;
    text-align: center;
}
.result {
    padding: 22px;
    border-radius: 16px;
    background: #202a45;
    border: 1px solid #3c496b;
}
.stButton > button {
    width: 100%;
    border-radius: 10px;
    font-weight: 600;
    min-height: 48px;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    path = Path(__file__).parent / "fake_news_lstm.keras"
    return tf.keras.models.load_model(path)

st.markdown("""
<div class="hero">
    <h1>🔎 Fake News Detector</h1>
    <p>AI-powered news text classification using LSTM</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("Paste a news article below to get a model prediction.")

try:
    model = load_model()
except Exception as e:
    st.error("Model could not be loaded. Check that the model file is included.")
    st.stop()

news = st.text_area(
    "News article",
    height=220,
    placeholder="Paste the complete news article here..."
)

if st.button("Analyze News", type="primary"):
    if len(news.strip()) < 30:
        st.warning("Please enter a longer news article (at least 30 characters).")
    else:
        with st.spinner("Analyzing text..."):
            probability = float(
                model(tf.constant([news]), training=False).numpy()[0][0]
            )

        label = "REAL NEWS" if probability >= 0.5 else "FAKE NEWS"
        confidence = probability if probability >= 0.5 else 1 - probability

        st.markdown("---")
        st.subheader("Analysis Result")

        st.markdown(
            f'<div class="result"><h2>{label}</h2>'
            f'<p>Model confidence score: {confidence:.2%}</p></div>',
            unsafe_allow_html=True
        )

        st.write("Real news score")
        st.progress(probability)

        st.write("Fake news score")
        st.progress(1 - probability)

        st.caption(
            "This is a model prediction, not proof of authenticity. "
            "Dataset bias and writing patterns can affect the result. "
            "Verify important claims using reliable sources."
        )

st.markdown("---")
st.caption(
    "Built with Python, Streamlit and TensorFlow | LSTM text classifier"
)
