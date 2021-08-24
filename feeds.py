import streamlit as st
import feedparser

dict = {'НКЦКИ':'https://safe-surf.ru/rss/',
        'Checkpoint':'https://research.checkpoint.com/feed/',
        'CISA':'https://us-cert.cisa.gov/ncas/current-activity.xml',
        'NSA':'https://www.nsa.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=1&Site=920&max=20',
        'Securelist':'https://securelist.com/feed',
        'ESET':'https://www.welivesecurity.com/feed/',
        'NCSC':'https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml',
        'CISA':'https://us-cert.cisa.gov/ncas/analysis-reports.xml',
       'MSFT SRC':'https://msrc-blog.microsoft.com/feed/',
       'CERT FR':'https://www.cert.ssi.gouv.fr/feed/',
       'Sec7':'https://sector7.computest.nl/index.xml',
       'EE':'https://www.ria.ee/en/news-feed/all/feed'}
#r = st.slider('',1,5,1)
depth = 3
dictlen = len(dict)
for i in range(dictlen) :
    for n in range(depth):
      url = list(dict.values())[i]
      article = feedparser.parse(url)
      datesplit = (article.entries[n].published).split()
      date = datesplit[1] + ' ' + datesplit[2]
      articlelink = ' ' + article.entries[n].title + ' ' + article.entries[n].link
      id = list(dict)[i]
      a = id + ' ' + date + ' ' + articlelink
      st.write(a)
