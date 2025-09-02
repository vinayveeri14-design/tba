from logic.analyser import summary_stats, top_users, call_type_distribution

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Summary")
    stats = summary_stats(df)
    st.write(stats)

    st.subheader("🏅 Top 5 Users by Cost")
    st.bar_chart(top_users(df))

    st.subheader("📞 Call Type Distribution")
    st.bar_chart(call_type_distribution(df))
