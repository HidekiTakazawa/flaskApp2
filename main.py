# coding: UTF-8
from flask import Flask, render_template, request, url_for
from google.appengine.ext import ndb
app = Flask(__name__)

class User(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()


@app.route('/')
def toppage():
    return render_template('toppage.html')
@app.route('/database_all', methods=['get', 'post'])
def database_all():
    users = User.query().fetch()
   # users = ndb.Query(User)
    #return users
    return render_template('databaseAll.html', users=users)

@app.route('/database_new', methods=['get', 'post'])
def database_new():
    
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    user = User(name=name, email=email, password=password)
    user.put()
    return render_template('databaseAdd.html', name=name, email=email, password=password)
    

@app.route('/database_read', methods=['get', 'post'])
def database_read():
    name = request.form['name2']
    #email = request.form['email2']
    password = request.form['password2']
    message = ''
    
    
    query = User.query(ndb.AND(User.name == name, User.password == password))
    result = query.get()
    if result is None:
        message = 'name,password error'
        email = ''
        return render_template('databaseRead.html', name2=name, email2=email, password2=password, message=message)
    else:
        email = result.email
        #return result.email
        return render_template('databaseRead.html', name2=name, email2=email, password2=password, message=message)
    
