import requests

def get_data(data):
    try:
        url = f'https://cruviana.ifpi.edu.br/oeiras/api/v1/leituras/?Data={data}'
        respose = requests.get(url)
        return respose.json()['results']
    except:
         requests.exceptions.RequestException()

