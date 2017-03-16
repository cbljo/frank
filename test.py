# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:03:17 2017

@author: yuweili
"""

import requests
import os
import os.path

def dl(url):
    req=requests.get(url)
    if req.status_code==404:
        print('no such file found at %s' %url)
        return
    filename=url.split('/')[-1]
    with open(filename,'wb') as fobj:
        fobj.write(req.content)
    print('download over.')
    
if __name__=='__main__':
    url=input('enter a url:')
    dl(url)