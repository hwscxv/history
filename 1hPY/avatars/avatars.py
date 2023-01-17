import requests
import random
from pathlib import Path
Path('./awatars').mkdir(exist_ok=True)

response = requests.get(f'https://avatars.dicebear.com/api/male/{random.random()}.svg')

with open('./awatars/avatar.svg', 'wb') as file:
    file.write(response.content)



