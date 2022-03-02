from turtle import ht
from urllib.request import urlopen

link='http://python.org/'

def get_html():
    try:
        http_rsp=urlopen(link)
        print(http_rsp)
        html=http_rsp.read()
        print(html)
        html_decoded=html.decode()
        print(html_decoded)
    except Exception as ex:
        print('*** Failed to get Html! ***\n\n'+str(ex))
    else:
        return html_decoded