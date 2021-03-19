# '''Importing Streamlit''''

import streamlit as st
st.subheader("Name Entity Recognition (Wikipedia)") 

#'''CSS Content'''

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    
def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)
local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
icon("search")

'''Search below'''

#'''Python NLP libraries'''

import spacy
import wikipedia
nlp = spacy.load("en_core_web_sm")
from spacy import displacy
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

#'''Funcation for Analyzing Text'''

def analyze_text(text):
    	return nlp(text)
raw_text = st.text_input("","Search....")
s = wikipedia.summary(raw_text, sentences =50)
if st.button("Ok"):
    doc = analyze_text(s)
    html = displacy.render(doc,style="ent")
    html = html.replace("\n\n","\n")
    st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)

