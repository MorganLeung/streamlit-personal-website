import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Morgan_Leung_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Morgan Leung")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** timing_leung@outlook.com
    - **Phone:** (86) 135 3755 2343
    - **LinkedIn:** [linkedin.com/in/morgan-leung14](https://linkedin.com/in/morgan-leung14)
    - **GitHub:** [github.com/MorganLeung](https://github.com/MorganLeung)
    - **Address:** 12 Chak Cheung St., Ma Liu Shui, HKSAR
    """)

    st.header("Professional Summary")
    st.markdown("""
    Highly skilled Product Manager with over 5 years of experience in customer-centric marketing. Proven ability to lead teams, manage products, and improve performance.
    """)

    st.header("Work Experience")
    st.markdown("""
    **Product Manager, Jumper Medical Inc.**
    - *September 2023 – June 2024*
    - Analyzed customer data to identify patterns and trends using Python and SQL
    - Based on the data, I improved the product roadmap for the company
    - Implemented the product roadmap and achieved the goal

    **Financial Analyst, Guotaijunan Securities Co., Ltd.**
    - *July 2022 – October 2022*
    - Analyzed the financial data of the company and gave some suggestions to the company
    - Analyzed the industry data and gave some suggestions to the company
    - Improved the efficiency of the team by 20%
    - Tied the relationship between company and customers
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - Chinese University of Hong Kong
    - *Graduated: June 2025*
    - GPA: 3.9/4.0
                
    **Bachelor of Management**
    - Sun Yat-sen University
    - *Graduated: June 2024*
    - GPA: 3.6/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Communication:** Excellent written and verbal communication
    - **Teamwork:** Collaborative team player with experience in Agile environments
    - **Problem-solving:** Strong analytical and critical thinking abilities
    - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
    - **Leadership:** Experience leading small teams and mentoring junior colleagues
    - **Adaptability:** Quick learner who thrives in dynamic environments
    """)

    st.header("In-campus Projects")
    st.markdown("""
    **Swimming Team of Lingnan College - Leader**
    - Won the 1st prize in the school swimming competition.

    **Student Union of Sun Yat-sen University - Marketing President**
    - Responsible for the marketing and promotion of the school events such as Christmas Party and Graduation Ceremony.
    """)

    st.header("Languages")
    st.markdown("""
    - **Chinese:** Native
    - **English:** Fluent
    """)

    st.header("Interests")
    st.markdown("""
    - Swimming
    - Hiking
    - Reading
    - Traveling
    """)

    st.markdown("---") 