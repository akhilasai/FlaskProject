from flask import *
from flask_pymongo import PyMongo

app=Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb+srv://athumma:Akhila%40123@cluster0.iiybw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        db.user.find(dict(request.form))
        email=request.form['email']
        password=request.form['password']
        print("Email:",email)
        print("Password:",password)
        return redirect(url_for('success'))
    return render_template('login.html')

    
@app.route('/success')
def success():
    return "success"    
    
   

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        name=request.form['name']
        print("Email:",email)
        print("Password:",password)
        print("Name:",name)
        if (len(email)>=0 and len(password)>=0 and len(name)>=0):
            db.user.insert_one(dict(request.form))
            return redirect(url_for('success'))
        else:
            return redirect(url_for('error')) 
    else:
        return render_template('signup.html')
 
@app.route('/error')
def error():
    return "error"
    
@app.route('/forgot',methods=['GET','POST'])
def forgot():
    if request.method=='POST':
        db.user.insert_one(dict(request.form))
        email=request.form['email']
        password=request.form['password']
        newpassword=request.form['newpassword']
        print("Email:",email)
        print("Password:",password)
        print("New password:",newpassword)
        return redirect(url_for('success'))
    return render_template('forgot.html')  

@app.route('/landing')
def landing():
    return render_template('landing.html')     


if __name__ == '__main__':
    app.run(debug = True)