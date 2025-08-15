import streamlit as st
import pandas as pd
from datetime import datetime, date
import plotly.express as px

# Streamlit page configuration
st.set_page_config(page_title="Task Prioritizer", layout="wide")

# Title and description
st.title("Task Prioritizer")
st.write("Enter your tasks, deadlines, and importance to prioritize them effectively.")

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to calculate priority score
def calculate_priority_score(deadline, importance):
    # Convert deadline to days remaining
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
        days_remaining = (deadline_date - date.today()).days
    except ValueError:
        days_remaining = 365  # Default for invalid dates
    days_remaining = max(1, days_remaining)  # Avoid division by zero

    # Importance weights
    importance_weights = {"High": 3, "Medium": 2, "Low": 1}
    importance_score = importance_weights.get(importance, 1)

    # Priority score: higher importance and closer deadlines get higher scores
    score = (importance_score * 100) / days_remaining
    return round(score, 2)

# Task input form
with st.form("task_form"):
    task_description = st.text_input("Task Description")
    deadline = st.date_input("Deadline", min_value=date.today())
    importance = st.selectbox("Importance", ["High", "Medium", "Low"])
    submit = st.form_submit_button("Add Task")

    if submit and task_description:
        # Add task to session state
        task = {
            "Description": task_description,
            "Deadline": deadline.strftime("%Y-%m-%d"),
            "Importance": importance,
            "Priority Score": calculate_priority_score(deadline.strftime("%Y-%m-%d"), importance)
        }
        st.session_state.tasks.append(task)
        st.success("Task added!")

# Display tasks
if st.session_state.tasks:
    # Convert tasks to DataFrame
    df = pd.DataFrame(st.session_state.tasks)
    
    # Sort by priority score (descending)
    df = df.sort_values(by="Priority Score", ascending=False).reset_index(drop=True)
    
    # Display task list
    st.subheader("Prioritized Task List")
    st.dataframe(df, use_container_width=True)
    
    # Plot priority scores
    fig = px.bar(df, x="Description", y="Priority Score", color="Importance",
                 title="Task Priority Visualization",
                 color_discrete_map={"High": "red", "Medium": "orange", "Low": "green"})
    st.plotly_chart(fig, use_container_width=True)

    # Clear tasks button
    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
        st.rerun()

else:
    st.info("No tasks added yet. Use the form above to add tasks.")

# Instructions
st.markdown("""
### How it works:
- **Add Tasks**: Enter a task, select a deadline, and choose importance (High, Medium, Low).
- **Priority Score**: Calculated based on importance and days until deadline (higher score = more urgent).
- **Visualization**: Tasks are sorted by priority and displayed in a bar chart.
""")