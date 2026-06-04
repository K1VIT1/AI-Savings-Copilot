import streamlit as st
from datetime import datetime
import calendar
import pandas as pd
from ai_agent import ask_gemini

st.set_page_config(
    page_title="AI Savings Copilot",
    page_icon="💰",
    layout="wide"
)

st.title("💰 AI Savings Copilot")

st.subheader("Savings Goal Setup")

income = st.number_input(
    "Monthly Income (₹)",
    min_value=0,
    value=50000
)

goal = st.number_input(
    "Monthly Savings Goal (₹)",
    min_value=0,
    value=15000
)

transactions = []

num_transactions = st.number_input(
    "Number of Transactions",
    min_value=1,
    value=3
)

for i in range(num_transactions):

    col1, col2, col3 = st.columns(3)

    with col1:
        merchant = st.text_input(
            f"Merchant {i+1}",
            key=f"merchant_{i}"
        )

    with col2:
        amount = st.number_input(
            f"Amount {i+1}",
            min_value=0,
            value=0,
            key=f"amount_{i}"
        )

    with col3:
        category = st.selectbox(
            f"Category {i+1}",
            [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Subscription",
            "Other"
            ],
            key=f"category_{i}"
        )

    transactions.append(
        {
            "merchant": merchant,
            "amount": amount,
            "category": category
        }
    )

spent = sum(
    t["amount"]
    for t in transactions
)

st.subheader("Transaction Summary")

with st.expander("📊 View Spending Analytics"):

    st.subheader("Transactions")

    df = pd.DataFrame(transactions)

    st.dataframe(
        df,
        use_container_width=True
    )

    if not df.empty:

        category_summary = (
            df.groupby("category")["amount"]
            .sum()
            .reset_index()
        )

        st.subheader(
            "Category Breakdown"
        )

        st.bar_chart(
            category_summary.set_index(
                "category"
            )
        )

st.write(
    f"Total Transactions: {len(transactions)}"
)

st.write(
    f"Total Spent: ₹{spent:,.0f}"
)

remaining_budget = income - goal - spent

today = datetime.today()

days_in_month = calendar.monthrange(
    today.year,
    today.month
)[1]

days_left = max(
    days_in_month - today.day,
    1
)

safe_daily_spend = remaining_budget / days_left

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Remaining Budget",
        f"₹{remaining_budget:,.0f}"
    )

with col2:
    st.metric(
        "Days Left",
        days_left
    )

with col3:
    st.metric(
        "Safe Daily Spend",
        f"₹{safe_daily_spend:,.0f}"
    )

st.divider()

st.subheader("AI Insights")

if st.button("Generate AI Advice"):
    prompt = f"""
    Monthly income: ₹{income}

    Savings goal: ₹{goal}

    Total spent: ₹{spent}

    Remaining budget: ₹{remaining_budget}

    Safe daily spend: ₹{safe_daily_spend}

    Give:
    1. A savings health score out of 10
    2. One warning if needed
    3. Three practical suggestions
    """

    advice = ask_gemini(prompt)

    st.subheader("AI Financial Coach")

    st.write(advice)