import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Product Manager Intern
    **Jumper Medical Inc.** | *September 2023 - June 2024*
    
    - Analyzed customer data to identify patterns and trends using Python and SQL
    - Based on the data, I improved the product roadmap for the company
    - Implemented the product roadmap and achieved the goal
    """)
    
    st.markdown("""
    ### Financial Analyst Intern
    **Guotaijunan Securities Co., Ltd.** | *July 2022 - October 2022*
    
    - Analyzed the financial data of the company and gave some suggestions to the company
    - Analyzed the industry data and gave some suggestions to the company
    - Improved the efficiency of the team by 20%
    - Tied the relationship between company and customers
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Brand Preference of New Energy Car Companies in China",
            "description": "Used machine learning techniques to analyze the brand preference of new energy car companies in China.",
            "skills": ["Python", "scikit-learn", "Pandas", "Matplotlib"],
            "outcome": "Gave some suggestions to new energy companies to improve their brand preference in the Chinese market."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL
        - **Machine Learning:** scikit-learn
        - **Data Processing:** Pandas, NumPy
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** Google Cloud, Baidu Cloud
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 