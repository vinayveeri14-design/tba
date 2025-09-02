user_ids = df['user_id'].unique()
selected_user = st.selectbox("Filter by User", user_ids)
filtered_df = df[df['user_id'] == selected_user]
