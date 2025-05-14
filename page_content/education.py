import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master in Marketing
    **The Chinese University of Hong Kong** | *August 2024 - July 2025*
    
    - GPA: 3.9/4.0
    - Relevant Coursework: Machine Learning, Customer Analytics, Social Media Analytics, Marketing Management, Digital Marketing, Big Data Analytics
    
    ### Bachelor of Management
    **Sun Yat-sen University** | *September 2020 - June 2024*
    
    - GPA: 3.6/4.0
    - Graduated with Honors
    - Relevant Coursework: Customer Behavior, International Marketing, Financial Management, Business Analytics, Marketing Research, Marketing Management
    """)
    
    st.markdown("---")
    
    st.markdown("## In-campus Projects")
    
    proj1, proj2 = st.columns(2)
    
    with proj1:
        st.markdown("""
        ### Swimming Team of Lingnan College - Leader
        **School Swimming Group** | *September 2021 - June 2023*
                    
        Won the 1st prize in the school swimming competition.
        """)
        
    with proj2:
        st.markdown("""
        ### Student Union of Sun Yat-sen University - Marketing President
        **Sun Yat-sen University** | *September 2021 - June 2023*
        
        Responsible for the marketing and promotion of the school events such as Christmas Party and Graduation Ceremony.
        """)
        
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### The impact of consumer ethnocentrism on brand preference: Taking Tesla as an example
    - Analyzed the impact of consumer ethnocentrism on brand preference using machine learning techniques
    - Found out the factors that influence the consumer ethnocentrism
    - Gave some suggestions to new energy companies to improve their brand preference in the Chinese market
    """)
    
    st.markdown("---") 