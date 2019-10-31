from flask import Flask, render_template, json, request
from pprint import pprint
from socketserver.go import Go

host = 'localhost'
port = 3010

def cb(fut):
  print('RESULT ----------')
  (header, body) = fut.result()
  print('header:')
  pprint(header)
  print('')
  print('body:')
  pprint(body)
  print('----------')

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImNpIjoyMjU0MDgyMCwiZW1haWwiOiJlcmljQG1haWwuY29tIn0sImV4cCI6MTU3MjQ2MzA5Mn0.37RYLjikjTol0wRKfoxMGlIdQe8B2nlUcLDaVkmoOCI'

body = {
  'ci': 22540820,
  'email': 'eric@mail.com',
  'phone': '04241234567',
  'name': 'eric',
  'last_name': 'vdd'
}
Go('POST', '/signup', host_port = (host, port), body=body).with_callback(cb)

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
    
