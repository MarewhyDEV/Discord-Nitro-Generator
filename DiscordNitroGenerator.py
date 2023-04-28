import random
import requests

file = open("valid_codes.txt","a",encoding="utf-8")

def generate_code():
    code = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(24):
        code += random.choice(characters)
    return code

def test_code(code):
    headers = {
        'Authorization': 'YourBotTokenHere'
    }
    response = requests.post(f'https://discord.com/api/v9/entitlements/gift-codes/{code}/redeem', headers=headers)
    if response.status_code == 200:
        print(f'Valid code found: {code}')
        return True
    else:
        print(f'Invalid code: {code}')
        print(response.status_code)
        return False

while True:
    code = generate_code()
    if test_code(code):
        file.write(code)
        