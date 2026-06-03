\# PathWise AI: Personalized Learning Path Recommender for University Students



PathWise AI is a machine learning-based decision-support dashboard that predicts student academic risk, identifies likely learning gaps, and recommends personalized learning pathways for university students.



\## Project Overview



The system uses student academic records, assessment activity, previous education, and virtual learning environment engagement data to classify students into low, medium, and high-risk groups.



It then recommends support pathways such as foundation revision modules, tutor support, academic advising, VLE engagement targets, time management resources, and accessibility support.



\## Key Features



\- Student academic risk prediction

\- Low, medium, and high-risk classification

\- Skill gap identification

\- Personalized support pathway recommendation

\- Interactive Streamlit dashboard

\- Student-level recommendation lookup



\## Dataset



The project uses the Open University Learning Analytics Dataset, which contains student demographics, assessment records, course information, and virtual learning environment activity.



\## Models Trained



Three machine learning models were trained and compared:



\- Logistic Regression

\- Random Forest

\- Gradient Boosting



The final dashboard uses the recommendation-ready output generated from the best-performing model.



\## Dashboard Pages



\- Overview

\- Risk Analytics

\- Skill Gap Analysis

\- Student Recommendation

\- About the Project



\## Deployment Note



The model was first trained on full academic and engagement records to understand key risk patterns. For real-time university use, the system can later be restricted to early-semester data so support teams can identify and assist students before failure or withdrawal occurs.



\## Tools Used



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- Streamlit

\- Plotly

