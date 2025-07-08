import requests
def myrequest(username):
    data=requests.get (f"https://api.github.com/users/{username}")
    if data.status_code==200:
        mydata= data.json()
        print(mydata)
myrequest('khushi1452')