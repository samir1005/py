import wget
import mechanize
from wget import bar_thermometer

import urllib
i=1
while i<=114:
    urls='http://audio3.islamweb.net/quran/Abdulrashid/abu_alhareth_k/'
    url = '{}{:03d}'.format(urls,i)+'.mp3'
    #print url
    print '......'
    file=wget.download(url, bar=bar_thermometer)
    print 'surrat {:03d}:'.format(i)+' is done'
    i+=1
