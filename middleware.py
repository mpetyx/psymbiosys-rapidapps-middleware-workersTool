import requests
import json

def post_to_rapidapps(body):
    url = "https://rapid-apps-2475.eu-gb.mybluemix.net/services/2984dcb289ef8da69bfdc2442546d334"

    payload = {
        "iduser":body['iduser'],
        "firstname":body['firstname'],
        "lastname":body['lastname'],
        "height":body['height'],
        "weight":body['weight'],
        "position":body['position'],
        "isPublic":body['isPublic'],
        "username":body['username'],
        "lengthOfFemur":body['lengthOfFemur'],
        "lengthOfTibia":body['lengthOfTibia'],
        "distanceElbowBottom":body['distanceElbowBottom'],
        "defaultWorkplace":body['defaultWorkplace'],
        "email": body.get('email','')
    }
    headers = {
        'content-type': "application/json"
        # 'cache-control': "no-cache",
        # 'postman-token': "ad231e44-444e-510e-ea43-811235517205"
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    print(response.text)

def retrieve_from_aidima():
    url = "http://83.136.188.223/PSYReport/rest/userlist/get"

    headers = {
        'cache-control': "no-cache",
        'postman-token': "fc91ddf4-df82-198a-b876-b53ad11647b0"
    }

    response = requests.request("GET", url, headers=headers)
    print "ok"

    for user in response.json():
        post_to_rapidapps(user)
        print user


retrieve_from_aidima()
