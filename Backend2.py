from flask import Flask, redirect,url_for
from flask import render_template
from flask import request
from flask import session
app=Flask(__name__)
app.secret_key = '12321'

@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():
    #DB
    found=True
    if found:
        return render_template('index.html',name='Ido Nahmani')
    else:
        return render_template('index.html')

def hello_world():  # put application's code here
    # TODO
    return redirect(url_for('assignment8.html'))

@app.route('/assignment8')
def assignment8_func():
    profile={'Name':'Ido','Last Name':'Nahmani'}
    uni='bgu'
    degrees=['BSc','Msc']
    hobbies=('art','sport','music','flask')
    return render_template('assignment8.html',fullname=profile,University=uni,degress=degrees,hobbies=hobbies)

@app.route('/assignment9',methods=['GET','POST'])
def assignment9_func():
    users = {'user1': {'name': 'Oren', 'email':'Oren@gmail.com'},
             'user2':{'name': 'Ido', 'email':'Ido@gmail.com'},
             'user3': {'name': 'Dana', 'email': 'Dana@gmail.com'},
             'user4': {'name': 'Itzik', 'email': 'Itzik@gmail.com'},
             'user5': {'name': 'Reut', 'email': 'Reut@gmail.com'}}
    if request.method == 'GET':
        if 'usersearch' in request.args:
            search_user = request.args['usersearch']
            return render_template('assignment9.html',users=users,search_user=search_user)
        return render_template('assignment9.html',users=users)
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        session['username']=username
        session['email']=email
        return render_template('assignment9.html')

@app.route('/catalog')
def catalog_func():
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        return render_template('catalog.html',product=product,size=size)
    return render_template('catalog.html')

@app.route('/login',methods=['GET','POST'])
def login_fun():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        #DB
        username = request.form['username']
        password=request.form['password']
        session['username']=username
        session['password']=password
        return redirect(url_for('home_func'))




@app.route('/logout')
def logout_func():
    session['username']=''
    return render_template('assignment9.html')


if __name__== '__main__':
    app.run(debug=True)

