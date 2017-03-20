import urllib3
from bs4 import BeautifulSoup
import re


SCHOLAR_SITE = 'http://scholar.google.com'

def main(phrase):
    '''
    phrase is formatted with +s instead of spaces, I only wrote a portion of the code and that is how the other part
    needed it
    '''
    output = []
    output.append(gettitle(phrase))
    output.append(getlink(phrase))
    output.append(getabstract(phrase))
    return output


def gs_urlbuild(phrase):
    phrasedef = '&as_epq=' + phrase
    SCHOLAR_QUERY_URL = SCHOLAR_SITE + '/scholar?' + 'as_q=' +phrasedef + '&as_oq=&as_eq=&as_occt=any&as_sauthors=&as_publication=&as_ylo=&as_yhi=&btnG=&hl=en&as_sdt=0%2C40'
    return SCHOLAR_QUERY_URL

def grabhtml(phrase):
    http = urllib3.PoolManager()
    url = gs_urlbuild(phrase)
    request = http.request('GET', url)
    html = request.data.decode('latin1')
    return(html)

def parsehtml(phrase):
    html = grabhtml(phrase)
    children = []
    soup = BeautifulSoup(html)
    div = soup("div", {"class" : "gs_ri"})
    for z in range(0,9):
        child = div[z].findChildren()
        children.append(child)
    return children

def getlink(phrase):
    parse1 = parsehtml(phrase)
    Link = []
    for z in range(0,9):
        raw = str((parse1[z])[0])
        split1 = (raw.split('href='))[1]
        split2 = (split1.split('\"'))[1]
        Link.append(split2)
    return Link #list

def gettitle(phrase):
    parse1 = parsehtml(phrase)
    Title = []
    for z in range(0,9):
        raw = str((parse1[z])[0])
        split0 = (raw.split('href='))[1]
        split1 = (split0.split('\">'))[1]
        split2 = (split1.split('</a>'))[0]
        split2_notags = re.sub('<[^<]+?>', '', split2)
        Title.append(split2_notags)
    return Title #list

def getabstract(phrase):
    parse1 = parsehtml(phrase)
    Abstract = []
    for z in range(0,9):
        for y in range(0,20):
            if "gs_rs" in str((parse1[z])[y]):
                raw = str((parse1[z])[y])
        split1 = (raw.split('\gs_rs">'))[0]
        split2 = (split1.split('</div>'))[0]
        split2_notags = re.sub('<[^<]+?>', '', split2)
        Abstract.append(split2_notags)
    return Abstract #list

print(main("hello+world"))