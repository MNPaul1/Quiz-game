import requests
NUMBER_OF_QUESTION = 10
TYPE = 'boolean'
parameters = {
    'amount' : NUMBER_OF_QUESTION,
    'type' : TYPE
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()['results']
# print(question_data)