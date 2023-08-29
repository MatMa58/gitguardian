#Pobieranie listy agentów - zwykłe podejście
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
access_key = 'AKIAIOSFODNN7EXAMPLE'
secret_key = 'bPxRfiCYEXAMPLEKEY' 

agents = get_nessus_agents(api_url, access_key, secret_key)
if agents is not None:
    print(agents)
else:
    print('The agent list could not be retrieved')
