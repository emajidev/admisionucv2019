from flask import Flask, render_template, json, request
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def dashboard_admin():
    lista = {'A','B','C','D'}

    return render_template('admin.html',lista=data["student"]['name'])
    
@app.route('/showSignUp',methods=['GET','POST'])
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    # create user code will be here !!
    ci = request.form['inputCi']
    email = request.form['inputEmail']
    phone = request.form['inputPhone']
    name = request.form['inputName']
    lastName= request.form['inputlastName']
    # create json for singUp
    data = {
       "student":
           {"ci":ci,
            "email":email,
            "phone":phone,
            "name":name,
            "lastName":lastName,
            }
    }
   
  
  
    jsonSingUp = json.dumps(data)
    DecoSingUp = json.loads(jsonSingUp)

    print("json: "+ jsonSingUp)
    print("json decodificado, estraccion data name: "+ str(DecoSingUp["student"]['name']))
    return ci + email + phone + name +lastName

@app.route('/signIn',methods=['POST'])
def signIn():
    # create user code will be here !!
    ci = request.form['inputCi']
    email = request.form['inputEmail']
    # create json for singUp
    data = {
       "student":
           {"ci":ci,
            "email":email,
            }
    }
   
  
  
    jsonSingUp = json.dumps(data)
    DecoSingUp = json.loads(jsonSingUp)

    print("json: "+ jsonSingUp)
    print("json decodificado, estraccion data name: "+ str(DecoSingUp["student"]['ci']))
    return ci + email 
    
app.run(debug =True)
    
