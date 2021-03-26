from flask import Flask, render_template,request
from flask_pymongo import PyMongo
from decouple import config

app = Flask(__name__)
app.config['MONGO_URI'] = config("MONGO_URI")
mongo= PyMongo(app)
access=mongo.db.table

@app.route('/',methods=["POST","GET"])
def hello_world():
    return render_template("index.html", title="registration form")

@app.route('/add_details',methods=["POST","GET"])
def add_details():
    user_data={
            "firstname": request.values.get("first"),
            "lastname" : request.values.get("last"),
            "password" : request.values.get("pass"),
            "gender"   : request.values.get("gender")
            }
    print(user_data)        
    access.insert_one(user_data)          
    return "user data added successfully!"
    
if __name__=="__main__":
    app.run(debug=True,port="5000")