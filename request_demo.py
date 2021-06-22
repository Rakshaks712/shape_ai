import  requests

r = requests.get('https://imgs.xkcd.com/comics/python.png')


print(r.content)

#Requests is successful and we received the corresponding response

...
with open('console.png','wb') as f:
    f.write(r.content)