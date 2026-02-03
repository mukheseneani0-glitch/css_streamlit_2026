# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 14:22:28 2026

@author: 22001691
"""
import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Grade 10 Practical Tools Impact", layout="wide")
st.title("Grade 10 – Practical Tools Impact Dashboard")
st.markdown("Compare how different practical approaches affect performance and understanding.")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame([
        {"Group": "Traditional (no practical)", "Students": 30, "Pre (%)": 55.0, "Post (%)": 60.0, "Understanding (1-10)": 5.2, "Practical Hours": 0.0},
        {"Group": "Physical Labs",              "Students": 30, "Pre (%)": 55.0, "Post (%)": 78.0, "Understanding (1-10)": 8.0, "Practical Hours": 20.0},
        {"Group": "Virtual Labs",               "Students": 30, "Pre (%)": 55.0, "Post (%)": 82.0, "Understanding (1-10)": 8.7, "Practical Hours": 15.0},
        {"Group": "Combined (Phys + Virt)",     "Students": 30, "Pre (%)": 55.0, "Post (%)": 86.0, "Understanding (1-10)": 9.3, "Practical Hours": 25.0},
    ])

df = st.session_state.df.copy()

with st.sidebar:
    st.header("Add or Update Group")
    group = st.text_input("Group / Tool name", "New Group")
    students = st.number_input("Number of students", 1, 200, 30)
    pre = st.number_input("Average Pre-test %", 0.0, 100.0, 55.0)
    post = st.number_input("Average Post-test %", 0.0, 100.0, 75.0)
    understand = st.number_input("Avg Understanding (1–10)", 1.0, 10.0, 7.0, 0.1)
    hours = st.number_input("Practical hours", 0.0, 100.0, 10.0, 1.0)

    if st.button("Add / Update", type="primary"):
        mask = df["Group"] == group
        if mask.any():
            df.loc[mask, ["Students", "Pre (%)", "Post (%)", "Understanding (1-10)", "Practical Hours"]] = [students, pre, post, understand, hours]
        else:
            new_row = pd.DataFrame([{"Group": group, "Students": students, "Pre (%)": pre, "Post (%)": post, "Understanding (1-10)": understand, "Practical Hours": hours}])
            df = pd.concat([df, new_row], ignore_index=True)
        st.session_state.df = df
        st.success(f"Group '{group}' added/updated!")

st.subheader("Your Data")
edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
st.session_state.df = edited_df

if len(edited_df) >= 2:
    improve = edited_df["Post (%)"] - edited_df["Pre (%)"]
    corr = edited_df[['Practical Hours', 'Post (%)']].corr().iloc[0, 1]

    cols = st.columns(4)
    cols[0].metric("Avg Improvement", f"{improve.mean():+.1f}%")
    cols[1].metric("Avg Post-test", f"{edited_df['Post (%)'].mean():.1f}%")
    cols[2].metric("Avg Practical Hours", f"{edited_df['Practical Hours'].mean():.1f} h")
    cols[3].metric("Correlation (hours ↔ score)", f"{corr:.2f}", help="> 0.7 = strong positive")

    tab1, tab2, tab3 = st.tabs(["Post-test Performance", "Improvement", "Hours vs Score"])

    with tab1:
        fig1 = px.bar(edited_df, x="Group", y="Post (%)", title="Post-test Scores", color="Post (%)", range_y=[0, 100])
        st.plotly_chart(fig1, use_container_width=True)

    with tab2:
        fig2 = px.bar(edited_df.assign(Improvement=improve), x="Group", y="Improvement", title="Improvement (Post - Pre)", color="Improvement")
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        fig3 = px.scatter(edited_df, x="Practical Hours", y="Post (%)", size="Students", hover_name="Group", trendline="ols", title="Practical Hours vs Post-test Score")
        st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("Add at least 2 groups to see statistics and charts.")