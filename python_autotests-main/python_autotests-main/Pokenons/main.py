import requests

token = 'b99913f43581f1e54cf07a796a516963'
host = 'https://pokemonbattle.me:9104'

answer_t = requests.post(f'{host}/trainers/reg', json = 
                       { 'trainer_token': token, 
                        'email': 'ind-dmitrij-chernyshev@qa.studio', 
                        'password': '3SWzLpWTzC1udQKmc0Ud'
                        }, headers = {'Content-Type': 'application/json'})
print (answer_t.text) 


answer_reg = requests.post(f'{host}/trainers/confirm_email', json = {    
                          'trainer_token': token
                        },headers = {'Content-Type': 'application/json'} )
print (answer_reg.text)

pokemon_new = requests.post(f'{host}/pokemons', json = {
                            'name': 'Dimit',
                            'photo': 'https://dolnikov.ru/pokemons/albums/001.png',                            
                            },headers = {'Content-Type': 'application/json', 'trainer_token': token})

print (pokemon_new.text)

pokemon_name = requests.put(f'{host}/pokemons', json = {
    'pokemon_id': '1058',
    'name': 'DM',
    'photo': 'https://dolnikov.ru/pokemons/albums/002.png'
}, headers = {'Content-Type': 'application/json', 'trainer_token': token}) 

print (pokemon_name.text)

pokemon_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {"pokemon_id": "1058"}, 
                                 headers = {'Content-Type': 'application/json', 'trainer_token': token} )
print (pokemon_pokeball.text)

answer = requests.get(f'{host}/trainers', json = {'trainer_token': token}, params= {'trainer_id' : '237'})
print (answer.text, answer.status_code)
