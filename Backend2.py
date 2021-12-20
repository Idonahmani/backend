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
    return render_template('index.html')


if __name__== '__main__':
    app.run(debug=True)

