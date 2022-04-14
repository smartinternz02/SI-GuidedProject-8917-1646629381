import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "LfZSAOLV-4j3WOLkhPiH9l51ZsABBnUr-mWDhBLS-s1a"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['at','v','ap','rh']], "values": [[14.96,41.76,1024.07,73.17]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/a5d0e278-5944-497a-bfb8-d9131d8fcf36/predictions?version=2021-11-18', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")

print(response_scoring.json())
predictions =response_scoring.json()
print(predictions)
print('Final Prediction Result',predictions['predictions'][0]['values'][0][0])
