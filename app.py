from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_pymongo import PyMongo
from decouple import config
from bson.json_util import dumps


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
    #return "user data added successfully!"
    return redirect(url_for('show_details'))

@app.route('/show_details',methods=["POST","GET"])
def show_details():
    data = access.find()
   # print (data)
   # print (dumps(data))
    return render_template("show.html",result = data)
    
if __name__=="__main__":
    app.run(debug=True,port="5000")









#  '''<pymongo.cursor.Cursor object at 0x7fab30283f90> for data
# [
#   {"_id": {"$oid": "605dce25efff33c2e7453d29"}, 
#   "firstname": "Sharon",
#   "lastname": "Abishek",
#   "password": "passwod",
#   "gender": "male"}
# ]
# for dumps(data)
#  '''   


# [
# {"_id": {"$oid": "605dce25efff33c2e7453d29"},
# "firstname": "Sharon",
# "lastname": "Abishek",
# "password": "passwod",
# "gender": "male"}, 

# {"_id": {"$oid": "605dd4f4cdf6ebcb6b8d4642"},
#  "firstname": "bairavi",
#  "lastname": "sowmya",
#  "password": "oassword",
#  "gender": "female"}
#  ]
