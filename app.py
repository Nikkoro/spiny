import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://freegametips.com/coin-master-free-spins-new-links-daily/'

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col3:
    st.write(' ')


entries = soup.find('figure', class_='wp-block-table')
multi_entries = entries.findChildren('tr')


for multi in multi_entries:
    link = multi.find('a', href=True)
    text = multi.find('td', class_='has-text-align-left')
    if text:
        st.code(multi.text)
    if link:
        #st.button("Spin dla igorka", link['href'])
        st.markdown(link,
                    unsafe_allow_html=True)
