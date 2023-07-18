import jwt
import datetime
import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

import schedule
import time

# Define a global variable for the token
token = None

#prerequisite values
connectedAppClientId = '0a9faf71-d52e-4a17-a52a-24a0d5ad694c'
connectedAppSecretId = '6dac74d9-65d6-48bc-b5f7-259a23b8bd5d'
connectedAppSecretKey = '2Yh9wbplndBzimew1ZZ0wU+q8k0NnKuRdnnTiyD8GSk='

#email address for TOL; username for Tableau Server
username = "m.setit@gmail.com"

#TOL or Tableau server name. SSL is highly recommeded
tableauservername = "https://10ax.online.tableau.com/t/setitsandboxdev427435/"

# Define a function to refresh the token
def refresh_token():
    global token
    # Refresh the token content here
    token = jwt.encode(
  {
    'iss': connectedAppClientId,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
    'jti': str(uuid.uuid4()),
    'aud': 'tableau',
    'sub': username,
    'scp': ['tableau:views:embed']
  },
  connectedAppSecretKey,
  algorithm='HS256',
  headers={
    'kid': connectedAppSecretId,
    'iss': connectedAppClientId
  })

# Function to demonstrate using the token
def another_function(token):
    return token

# Schedule the token refresh every 8 minutes
schedule.every(8).minutes.do(refresh_token)

#########
app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
#@app.route('/get_string')
def get_string():

  # Call your Python function and get the string result
  text = str(request.args.get('input')) # Requests the ?input= 1
  # result = your_python_function(data)
  # Add a loop to run the scheduled tasks
  i=0
  while True:
    schedule.run_pending()
    time.sleep(8*60+30)
    # Return the result as JSON
    #print('Here')
    #return jsonify({'result': token})
    another_function(token)
    i+=1
    print(i)
    #return('<p>Hello</p>')


#app.run(host='0.0.0.0', port = 8080)

if __name__ == '__main__':
   #print('Here1')
   #app.debug = True
   # Schedule the function to run every 8 minutes
   #schedule.every(8).minutes.do(app.run(host='0.0.0.0', port = 8080))
   app.run()
   #while True:
    #schedule.run_pending()
    #time.sleep(8*60+30)

