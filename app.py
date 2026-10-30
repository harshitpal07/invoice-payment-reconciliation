import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Smart Reconciliation",
    page_icon="💰",
    layout="wide"
)

# Main heading
st.title("💰 Smart Invoice & Payment Reconciliation")

# Description
st.write(
    "Manage invoices, payments and automatically "
    "identify matching transactions."
)

# Divider
st.divider()

# Upload section
st.subheader("Upload Financial Records")

col1, col2 = st.columns(2)

with col1:
    invoice_file = st.file_uploader(
        "Upload Invoice CSV",
        type=["csv"]
    )

with col2:
    payment_file = st.file_uploader(
        "Upload Payment CSV",
        type=["csv"]
    )

# Upload confirmation
if invoice_file is not None and payment_file is not None:
    st.success("Both files uploaded successfully!")

else:
    st.info("Please upload both CSV files to continue.")