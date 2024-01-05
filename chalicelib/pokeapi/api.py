import requests

basepath = 'https://pokeapi.co/api/v2/berry/'

def get_berries_list():
    """
    Retrieves all the berries' names by iterating through list berries API.
    """
    
    names = []

    url = basepath

    while True:

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f'failed to fetch berries list, status_code: {response.status_code}')
        
        data = response.json()
        names.extend([berry['name'] for berry in data.get('results', [])])
        url = data.get('next')

        if url is None:
            break

    return names


def get_berries_detail(names: list[str]) -> list[dict]:
    """
    Retrieves detailed information for each berry in the provided list of names.
    """
    
    details = []
    for name in names:
        
        url = f"{basepath}{name}/"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"failed to fetch berries detail, status_code: {response.status_code}")
        
        data = response.json()
        details.append(data)

    
    return details