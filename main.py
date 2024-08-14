from art import logo
import json

with open('morse-code.json', 'r') as file:
    data = json.load(file)

print(logo)

str_message = input('Enter message: ').lower()

encoded_message = [data[char] if char in data else '#' for char in str_message]

print(f'\nThe encoded message appear here with "#" indicating unencoded string and "/" indicating whitespace between words.\n {' '.join(encoded_message)}')


