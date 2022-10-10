import json

import requests
import time


def delete():
    headers = {
        'X-M2M-Origin': "aid",
        'X-M2M-RI': '123',
        'X-M2M-RVI': '3',
        'Content-Type': 'application/json;ty=2',
        'Accept': 'application/json'
    }

    send_delete_request("/aid", "", headers)

def register_an_AE_Resource(xm2morigin,rn):
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")

    #print(current_time)

    headers = {
        'X-M2M-Origin': str(xm2morigin),
        'X-M2M-RI': '123',
        'X-M2M-RVI': '3',
        'Content-Type': 'application/json;ty=2',
        'Accept': 'application/json'
    }

    # resourceName = rn, App-ID = api, requestReachability = rr, supportedReleaseVersions = srv
    api = "N"+str(rn)
    raw = {"m2m:ae":{"rn": str(rn), "api": str(api), "rr": True, "srv": ["3"]}}

    data = json.dumps(raw)

    url = 'http://localhost:8080/id-in'
    print(headers)
    print(data)
    print(url)
    response = requests.post(url, data=data, headers=headers)
    print(response)
    print(response.text)


def create_a_container_Resource(room,xm2morigin,contname):
    print("----------Create Container-------")
    print(xm2morigin)
    print(contname)
    headers = {
        'X-M2M-Origin': str(xm2morigin),
        'X-M2M-RI': '123',
        'X-M2M-RVI': '3',
        'Content-Type': 'application/json;ty=3',
        'Accept': 'application/json'
    }

    raw = {"m2m:cnt": {"mbs": 10000, "mni": 10, "rn": str(contname)}}
    data = json.dumps(raw)

    url = 'http://localhost:8080/cse-in/' + str(room)
    print(headers)
    print(data)
    print(url)
    response = requests.post(url, data=data, headers=headers)
    print(response)
    print(response.text)

# def create_a_flex_container_Resource(room,xm2morigin,contname):
#     print("----------Create Flex Container-------")
#     print(xm2morigin)
#     print(contname)
#     headers = {
#         'X-M2M-Origin': str(xm2morigin),
#         'X-M2M-RI': '123',
#         'X-M2M-RVI': '3',
#         'Content-Type': 'application/json;ty=3',
#         'Accept': 'application/json'
#     }
#
#     raw = {"cod:color": {"resourceName": "Colour",
#         "containerDefinition": "org.onem2m.common.moduleclass.colour",
#         "red": 0,
#        "green": 255,
#        "blue": 0}
#            }
#
#     data = json.dumps(raw)
#
#     url = 'http://localhost:8080/cse-in/' + str(room)
#     print(headers)
#     print(data)
#     print(url)
#     response = requests.post(url, data=data, headers=headers)
#     print(response)
#     print(response.text)

def send_delete_request(cseBaseName, data, headers):
    url = 'http://localhost:8080/id-in' + cseBaseName

    response = requests.delete(url, data=data, headers=headers)
    print(response)
    print(response.text)


if __name__ == '__main__':
    #delete()

    #-------------------------------Create AE Resoucre Room1 and Containers-----------------------
    #AE Parameter
    xm2morigin = "Cmatthias"
    rn = "Room1"

    #Container Parameter
    contname = "ESPStation1"
    room = "Room1"

    register_an_AE_Resource(xm2morigin, rn)
    create_a_container_Resource(room,xm2morigin,contname)
    contname = "SmartLED1"
    create_a_container_Resource(room, xm2morigin, contname)
    contname = "Actuator1"
    create_a_container_Resource(room, xm2morigin, contname)
    #create_a_flex_container_Resource(room, xm2morigin, contname)

    # -------------------------------Create AE Resoucre Room2 and Containers-----------------------
    xm2morigin = "Cmatthias1"
    rn = "Room2"

    # Container Parameter
    contname = "ESPStation2"
    room = "Room2"

    register_an_AE_Resource(xm2morigin, rn)
    create_a_container_Resource(room, xm2morigin, contname)
    contname = "SmartLED2"
    create_a_container_Resource(room, xm2morigin, contname)
    contname = "Actuator1"
    create_a_container_Resource(room, xm2morigin, contname)