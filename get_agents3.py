#Pobieranie listy agentów - zwykłe podejście 3!
import requests
import urllib3


def get_nessus_agents(api_url, access_key, secret_key):
    headers = {
        'X-ApiKeys': f'accessKey={access_key}; secretKey={secret_key}',
        'Content-Type': 'application/json',
    }

    response = requests.get(api_url, headers=headers, verify=False)

    if response.status_code == 200:
        agents = response.json()
        return agents
    else:
        return None

api_url = 'https://example.ing.com/scanners/1/agents'
access_key = 'MAMA59SFODNN7EXAMPLE'
secret_key = 'T7ehjUJmk1DYdhu5HVQYbpe9nc417HHZTzHYUFW2yIKbPLvGvBJARF1H9UISfpTD'

agents = get_nessus_agents(api_url, access_key, secret_key)
if agents is not None:
    print(agents)
else:
    print('The agent list could not be retrieved')
