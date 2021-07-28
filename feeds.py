import streamlit as st
import feedparser
nkcki = feedparser.parse('https://safe-surf.ru/rss/')
st.markdown('### NKCKI feed')
r = 5
for n in range(r) :
  datesplit = (nkcki.entries[n].published).split()
  date = datesplit[1]+' '+datesplit[2]
  #articlelink =' '+ nkcki.entries[n].title +' '+ nkcki.entries[n].link
  #articlelink =' '+nkcki.entries[n].title+' '+nkcki.entries[n].link
  #a = data + articlelink
  #st.write(a)
  st.markdown('date')
