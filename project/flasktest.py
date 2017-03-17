# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:49:23 2017

@author: yuweili
"""

from flask import  Flask,request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'
    
@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action=''/signin'' method=''post''>
          <p><input name=''username''></p>
          <p><input name=''password'' type=''password''></p>
          <p><button type=''submit''>Sign In</button></p>
          </form>'''
    
@app.route('/in',methods=['GET'])
def ind():
    return '<h3>Bad Username or password.</h3>'
    

@app.route('/signin',methods=['GET','POST'])
def signin():
    try:
        if request.form['username']=='admin' and request.form['password']=='pass':
            return '<h3>Hello,admin</h3>'
        return '<h3>Bad Username or password.</h3>'
    except:
        print 'this is wrong'

    

if __name__=='__main__':
    app.run(debug=True)