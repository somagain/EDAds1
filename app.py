import numpy as np
import pandas as pd
import streamlit as st
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from PIL import Image    


# Web App Title
img = Image.open("eda_pic.gif")
st.sidebar.image("eda_pic.gif")

st.markdown('''
# **The EDAds App**

EDAds-Exploratory Data Analysis for Data Scientist's App **EDAds** created in Streamlit using the **pandas-profiling** library.
App built in `Python` + `Streamlit` By: [Ndukwe James](https://www.linkedin.com/in/ndukwe-ijioma-james-6313371aa/)
                    
EDAds App generates profile reportsfrom a Pandas DataFrame. It provides a detailed report about the 
dataframe such as its missing values, correlations,  histograms,etc. is required. Thus DSeaT gives the
user these details about the pandas DataFramewith df.profile_report(), which automatically generates a 
standardized univariate and multivariate report for a deeper understanding of data, and sets the pace for 
further indepth analysis. The final output of the DSAT is HTML report


            
            

---
''')


# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")
st.sidebar.markdown("""**Credit:**:
                    """)
st.sidebar.markdown("""[Chanin Nantasenamat](http://youtube.com/dataprofessor) 
                    """)
st.sidebar.markdown("[Aka Einwanne](https://www.linkedin.com/in/ezinwanne-chinemelu-aka/?trk=public_profile_browsemap&originalSubdomain=ng)")
# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache_data
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
