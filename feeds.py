import streamlit as st
import feedparser
nkcki = feedparser.parse('https://safe-surf.ru/rss/')
st.markdown('### NKCKI feed')
r = 5
for n in range(r) :
  datesplit = (nkcki.entries[n].published).split()
  a = datesplit[1]+' '+datesplit[2] +' '+ nkcki.entries[n].title +' '+ nkcki.entries[n].link
  st.write(a)
