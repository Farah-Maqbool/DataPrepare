# app.py
import streamlit as st
import pandas as pd
from analyzer import analyze_dataset
from agent import analyze_with_agent
from backend import execute_preprocessing

# ------------------------------
# Streamlit Page Setup
# ------------------------------
st.set_page_config(page_title="AI Data Preprocessing Tool", layout="wide")
st.title("🧠 AI-Powered Data Preprocessing Tool")
st.markdown(
    "Upload a CSV file, view dataset summary, get AI preprocessing suggestions, "
    "apply them, and download the processed dataset."
)

# ------------------------------
# File Upload
# ------------------------------
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")

    # ------------------------------
    # Step 1: Analyze Dataset
    # ------------------------------
    st.info("Analyzing dataset...")
    summary = analyze_dataset(df)
    st.success("Dataset analyzed!")

    # Show dataset preview
    with st.expander("📄 Dataset Preview"):
        st.dataframe(df.head(10))

    # Show dataset summary
    with st.expander("📊 Dataset Summary"):
        for key, value in summary.items():
            st.write(f"**{key}:** {value}")

    # ------------------------------
    # Step 2: Get AI Agent Decisions
    # ------------------------------
    st.info("Getting AI preprocessing suggestions...")
    decisions = analyze_with_agent(summary)
    st.success("AI suggestions generated!")

    # ------------------------------
    # Step 2a: Display AI Suggestions with Multiple Actions
    # ------------------------------
    st.subheader("🤖 AI Preprocessing Suggestions")
    user_overrides = {}

    for col, col_decision in decisions.get("columns", {}).items():
        actions = col_decision.get("actions", ["keep"])
        reasons = col_decision.get("reasons", ["No explanation provided."])

        # Display actions & reasons clearly
        st.markdown(f"**{col}**")
        for i, action in enumerate(actions):
            reason_text = reasons[i] if i < len(reasons) else ""
            st.write(f"- Action: `{action}` → Reason: {reason_text}")

        # Allow user to override each column action (single-select override for simplicity)
        all_options = [
            "keep", "fill_median", "fill_mean", "fill_mode", "fill_unknown",
            "drop", "one_hot", "label", "standard", "minmax",
            "drop_outliers", "cap_outliers", "log_transform", "sqrt_transform", "none"
        ]

        # Default index
        default_index = 0
        if actions[0] in all_options:
            default_index = all_options.index(actions[0])

        user_choice = st.selectbox(
            f"Override first action for {col} (optional)",
            all_options,
            index=default_index
        )

        if user_choice != actions[0]:
            user_overrides[col] = col_decision.copy()
            user_overrides[col]["actions"][0] = user_choice

    # Merge overrides
    if user_overrides:
        for k, v in user_overrides.items():
            decisions["columns"][k] = v

    # ------------------------------
    # Step 3: Apply Preprocessing
    # ------------------------------
    if st.button("✅ Confirm and Apply Preprocessing"):
        st.info("Applying preprocessing...")
        df_processed, action_log = execute_preprocessing(df, decisions)
        st.success("Preprocessing completed!")

        # Convert boolean columns to 0/1 for display & download
        for col in df_processed.select_dtypes(include='bool').columns:
            df_processed[col] = df_processed[col].astype(int)

        # ------------------------------
        # Display Action Log
        # ------------------------------
        with st.expander("📝 Action Log"):
            for col, log in action_log.items():
                st.write(f"**{col}:**")
                st.json(log)

        # ------------------------------
        # Display Processed Dataset
        # ------------------------------
        st.subheader("📄 Processed Dataset Preview")
        st.dataframe(df_processed.head(10))

        # ------------------------------
        # Download Processed Dataset
        # ------------------------------
        csv = df_processed.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Processed CSV",
            data=csv,
            file_name="processed_dataset.csv",
            mime="text/csv"
        )
