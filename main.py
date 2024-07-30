from flask import Flask, request, render_template,redirect,session, url_for
import sqlite3 as sql
import os
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static\\images')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

@app.route("/")
def route():
    return render_template("login.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/cartitems")
def cartitems():
    return render_template("cartitems.html")

@app.route("/signup")
def sign():
    return render_template("signup.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/book")
def book():
    return render_template("book.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/bharath", methods = ["GET","POST"])
def regAction():
    msg=None
    if(request.method=="POST"):
        if (request.form["username"]!="" and request.form["email"]!=""and request.form["password"]!=""and request.form["phone"]!="" ):
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            phone = request.form["phone"]
                       
            with sql.connect("demo.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  raj(username,email,password,phone) VALUES('"+username+"','"+email+"','"+password+"','"+phone+"')")
                msg = "Register Details submitted successfully "

                con.commit()
        else:
            msg="Something went wrong"
        
        return render_template("login.html", msg=msg)
    
@app.route('/loginAction',methods=['GET','POST'])
def loginAction():
    msg=None
    if (request.method == "POST"):
        email = request.form['email']
      
        password = request.form['password']
        
        with sql.connect("demo.db") as con:
            c=con.cursor()
            c.execute("SELECT email, password  FROM raj WHERE email = '"+email+"' and password ='"+password+"'")
            r=c.fetchall()
            for i in r:
                if(email==i[0] and password==i[1]):
                    session["logedin"]=True
                    session["email"]=email
                    session["password"]=password
                    return redirect(url_for("index"))
                else:
                    msg= "please enter valid username and password"
    
    
    return render_template("login.html",msg=msg)




@app.route("/booking", methods = ["GET","POST"])
def manasa():
    msg=None
    if(request.method=="POST"):
        if (request.form["name"]!="" and  request.form["phone"]!=""and request.form["email"]!=""and request.form["person"]!=""):
            name = request.form["name"]
            
            phone = request.form["phone"]
            email = request.form["email"]
            person = request.form["person"]
                       
            with sql.connect("demo.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  bookings(name,phone,email,person) VALUES('"+name+"','"+email+"','"+phone+"','"+person+"')")
                msg = "Register Details submitted successfully"

                con.commit()
        else:
            msg="Something went wrong"
        
        return render_template("success.html", msg=msg)




if __name__ == "__main__":
    app.run(debug=True)
