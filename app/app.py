from flask import Flask, render_template,request
import requests
import base64
import cognitive_face as CF
import urllib
import os,json
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename
import insert_log
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/albinpaulose/blood_group_detection/app/static/img/faces'

@app.route("/log",methods=['GET', 'POST'])
def log():
    data = insert_log.get_all_logs()
    return render_template('logs.html',data = data)

@app.route("/home",methods=['GET', 'POST'])
def home():
   return render_template('detect_blood.html',data = "")


@app.route("/detect_group",methods=['GET', 'POST'])
def enroll_new():
    image = request.files['pic']
    #with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "rb") as f:
    #    image = f.read()
    print("writing done")
    filename = "122345"    
    name = request.form["name"]
    gender = request.form["gender"]
    dob = request.form["dob"]
    print ("image saved")
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename+".jpg"))
    print ("image saved")
    blood_group = insert_log.detect_group(name,gender,dob,filename)
    print ("Rendering template")
    return render_template('detect_blood.html',data = blood_group)



@app.route("/history",methods=['GET', 'POST'])
def history():
    data = insert_log.get_all_logs()
    return render_template("history.html",data=data)
    


app.run()
