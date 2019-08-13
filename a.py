import requests



string = 'dqw'
font = 'qwd'
url = 'http://artii.herokuapp.com/make?text='
url += string
url += '&'+font
response = requests.get(url)
print(response.text)
print(url)