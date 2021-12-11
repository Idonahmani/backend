from flask import Flask, redirect,url_for
from flask import render_template
app=Flask(__name__)

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
    return redirect(url_for('about.html'))

@app.route('/about')
def about_func():
    profile={'Name':'Ido','Last Name':'Nahmani'}
    uni='bgu'
    degrees=['BSc','Msc']
    hobbies=('art','sport','music','flask')
    return render_template('about.html',fullname=profile,University=uni,degress=degrees,hobbies=hobbies)


@app.route('/catalog')
def catalog_func():
    return render_template('catalog.html')

if __name__== '__main__':
    app.run(debug=True)

