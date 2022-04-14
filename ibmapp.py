from flask import Flask, render_template, request # Flask is a application
# used to run/serve our application
# request is used to access the file which is uploaded by the user in out application
# render_template is used for rendering the html pages
import pickle # pickle is used for serializing and de-serializing Python object structures

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "LfZSAOLV-4j3WOLkhPiH9l51ZsABBnUr-mWDhBLS-s1a"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


app=Flask(__name__) # our flask app

@app.route('/') # rendering the html template
def home():
    return render_template('home.html')
@app.route('/predict') # rendering the html template
def index() :
    return render_template("index.html")

@app.route('/data_predict', methods=['POST']) # route for our prediction
def predict():
    at = request.form['at'] # requesting for at data
    v = request.form['v'] # requesting for v data
    ap = request.form['ap'] # requesting for ap data
    rh = request.form['rh'] # requesting for rh data
    
    # coverting data into float format
    data = [[float(at), float(v), float(ap), float(rh)]]  
    payload_scoring = {"input_data":[{"field": [['at', 'v', 'ap', 'rh',]],"values": data}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/fceca4bb-5665-47f6-bb69-0d91eb60e1b4/predictions?version=2021-11-17', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print(data)
    print("Scoring response")
    print(response_scoring.json())
    predictions =response_scoring.json()
    print(predictions)
    print('Final Prediction Result',predictions['predictions'][0]['values'][0][0])
    pred = predictions['predictions'][0]['values'][0][0]
    print(pred)
    


    
    # loading model which we saved
    #model = pickle.load(open('CCPP.pkl', 'rb'))
    
    #prediction= model.predict(data)[0]
    return render_template('predict.html', prediction=pred)

if __name__ == '__main__':
    app.run()