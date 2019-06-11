#Author:S M Abdullah Ferdous as a Part of CM2540 final coursework
from werkzeug.utils import secure_filename
from flask import Flask, render_template
import datetime
import time
import os


app = Flask(__name__)

@app.route("/")
def pictures_taken():
   #the location of the pictures
   files=os.listdir('/home/pi/Desktop/Home_security/static')
   #creating a array for todays image and useing a for loop to sort the out
   today_images = []
   for f in files:
      if f.startswith(time.strftime("%Y%m%d-")):
          today_images.append(f)
   #Useing the templetes
   templateData = {
      'title' : 'Intruder/visitors pictures',
      'file': today_images
      }
   return render_template('web_template.html', **templateData)

if __name__ == "__main__":
  
   try:
      app.run(host='0.0.0.0', port=8080, debug=True)
   except KeyboardInterrupt:
      pass
print("Shutting down web app ", __name__)
