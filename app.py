import streamlit as st

# Page configuration
st.set_page_config(
    page_title="ReconX | Smart Reconciliation",
    page_icon="💰",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.block-container {
    padding-top: 2rem;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] * {
    color: white;
}

.metric-card {
    background-color: white;
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
}

.metric-title {
    color: #64748b;
    font-size: 14px;
}

.metric-value {
    color: #111827;
    font-size: 27px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# Sidebar
st.sidebar.title("💰 ReconX")

st.sidebar.write("Smart Financial Reconciliation")

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Upload Records",
        "Reconciliation",
        "Review Transactions",
        "Reports"
    ]
)

st.sidebar.divider()

st.sidebar.caption("Smart Invoice Management System")


# Dashboard
if page == "Dashboard":

    st.title("Dashboard")

    st.write(
        "Welcome to ReconX. Manage your invoices "
        "and payment reconciliation."
    )

    st.divider()

    # Summary cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Total Invoices</div>
            <div class="metric-value">₹0</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Total Payments</div>
            <div class="metric-value">₹0</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Matched</div>
            <div class="metric-value">0</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Outstanding</div>
            <div class="metric-value">₹0</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Getting Started")

    st.info(
        "Upload your invoice and payment CSV files "
        "to begin reconciliation."
    )


# Upload Records
elif page == "Upload Records":

    st.title("Upload Financial Records")

    st.write("Import your invoice and payment CSV files.")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Invoice Records")

        invoice_file = st.file_uploader(
            "Upload Invoice CSV",
            type=["csv"],
            key="invoice"
        )

    with col2:

        st.subheader("Payment Records")

        payment_file = st.file_uploader(
            "Upload Payment CSV",
            type=["csv"],
            key="payment"
        )

    if invoice_file and payment_file:

        st.success("Both files uploaded successfully!")


# Reconciliation
elif page == "Reconciliation":

    st.title("Reconciliation")

    st.info("Suggested invoice-payment matches will appear here.")


# Review Transactions
elif page == "Review Transactions":

    st.title("Review Transactions")

    st.info("Review and approve suggested matches here.")


# Reports
elif page == "Reports":

    st.title("Reconciliation Reports")

    st.info("Your reconciliation reports will appear here.")