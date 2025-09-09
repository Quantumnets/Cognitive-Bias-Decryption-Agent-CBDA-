import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.bias_engine.inference import detect_bias

# Page configuration
st.set_page_config(
    page_title="CBDA Dashboard",
    page_icon="🧠",
    layout="wide"
)

# Title and description
st.title("🧠 Cognitive Bias Decryption Agent")
st.markdown("Real-time analysis of cognitive biases in text content")

# Input section
col1, col2 = st.columns([2, 1])

with col1:
    text_input = st.text_area(
        "Enter text to analyze for cognitive biases:",
        height=200,
        placeholder="Paste text here to analyze for confirmation bias, anchoring, Dunning-Kruger effect, etc..."
    )

with col2:
    st.markdown("### Supported Bias Types")
    st.markdown("""
    - Confirmation Bias
    - Anchoring Bias  
    - Dunning-Kruger Effect
    - Sunk Cost Fallacy
    - Bandwagon Effect
    """)

if st.button("Analyze Text", type="primary"):
    if text_input.strip():
        with st.spinner("Analyzing for cognitive biases..."):
            result = detect_bias(text_input)
        
        # Display results
        st.subheader("Analysis Results")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Detected Bias",
                result["bias_type"].replace("_", " ").title(),
                f"{result['confidence']*100:.1f}% confidence"
            )
        
        with col2:
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = result["confidence"] * 100,
                title = {'text': "Confidence Level"},
                gauge = {'axis': {'range': [0, 100]}}
            ))
            st.plotly_chart(fig, use_container_width=True)
        
        # Show original text with highlights
        st.subheader("Original Text")
        st.text_area("", text_input, height=150)
    
    else:
        st.warning("Please enter some text to analyze")

# Sample data visualization
st.subheader("Bias Distribution in Sample Data")
sample_data = pd.DataFrame({
    'Bias Type': ['Confirmation', 'Anchoring', 'Dunning-Kruger', 'Sunk Cost', 'Bandwagon'],
    'Frequency': [45, 30, 15, 25, 35]
})

fig = px.bar(sample_data, x='Bias Type', y='Frequency', color='Bias Type')
st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("### About CBDA")
st.markdown("""
The Cognitive Bias Decryption Agent uses advanced NLP to identify and analyze 
cognitive biases in human decision-making processes across various domains.
""")
