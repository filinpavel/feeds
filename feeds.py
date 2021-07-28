import streamlit as st
import feedparser

dict = {'НКЦКИ':'https://safe-surf.ru/rss/',
        'Checkpoint':'https://research.checkpoint.com/feed/',
        'CISA':'https://us-cert.cisa.gov/ncas/current-activity.xml',
        'NSA':'https://www.nsa.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=1&Site=920&max=20',
        'Securelist':'https://securelist.com/feed',
        'ESET':'https://www.welivesecurity.com/feed/'}
r = st.slider('',1,5,1)
d = len(dict)
for i in range(d) :
    for n in range(r):
      id = list(dict)[i]
      url = list(dict.values())[i]
      article = feedparser.parse(url)
      datesplit = (article.entries[n].published).split()
      date = datesplit[1]+' '+datesplit[2]
      articlelink =' '+article.entries[n].title+' '+article.entries[n].link
      a = id +' '+ date +' '+ articlelink
      st.write(a)
  
