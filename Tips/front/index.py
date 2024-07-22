import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Assertividade")
st.title('Assertividade')

url = "http://tips-api:8000"

@st.cache_data
def get_tips_data():
    try:
        response = requests.get(f'{url}/tips')
        response.raise_for_status()  # Verifica se houve algum erro na requisição
        games = response.json()
    except requests.exceptions.HTTPError as http_err:
        st.error(f'HTTP error occurred: {http_err}')
        return
    except requests.exceptions.RequestException as err:
        st.error(f'Error occurred: {err}')
        return
    except ValueError as json_err:
        st.error(f'JSON decode error: {json_err}')
        return

    df = pd.DataFrame(games)
    
    df['Percentage'] = (df['Percentage']).round(2).astype(str) + '%'
    
    column_order=('Under', 'Green', 'Red', 'Total', 'Percentage')
  
    
    st.dataframe(df, column_order=column_order, width= 900)

get_tips_data()