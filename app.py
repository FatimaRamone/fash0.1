from flask import Flask, render_template , request , session

import random
import json


app = Flask(__name__)

app.config["SECRET_KEY"] = "-FCKQV8YGQF1xFX6Qf_TVw"


words = json.load(open ('words.json'))


@app.route('/')
def index():
  selected = random.choice(words["words"]) 
  session["english"] = selected["english"]
  session["spanish"] = selected["spanish"]
  
  return render_template ('index.html' , palabra= session["spanish"])



@app.route('/', methods=['POST'])
def respuesta():
  respuesta = request.form['respuesta']

  if respuesta == session["english"]: 
      return render_template('right.html', palabra= session["spanish"]) 
  else:
      return render_template('wrong.html', palabra= session["english"])

     

#if __name__ == '__main__':
    #flask app.run(debug=True)

  






