import requests as req


def userGet(name):
    return (
        (req.get(url='https://api.github.com/users/'+str(name))).json()
    )

