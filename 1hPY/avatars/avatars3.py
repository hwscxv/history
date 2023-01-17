import requests
import random
from pathlib import Path






response = requests.get(f'https://avatars.dicebear.com/api/male/{random.random()}.svg')

with open('./avatars/avatar.svg', 'wb') as file:
    file.write(response.content)

Path('./avatars').mkdir(exist_ok=True)




