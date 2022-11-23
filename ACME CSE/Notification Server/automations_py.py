from __future__ import annotations
from automations import *
from http.client import HTTPMessage
from typing import cast
from http.server import HTTPServer, BaseHTTPRequestHandler
import email.parser
import json, argparse, sys, ssl, signal
import cbor2
from rich.console import Console
from rich.syntax import Syntax
import paho.mqtt.client as mqtt
import pathlib, os
parent = pathlib.Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(f'{parent}')
from acme.helpers.MQTTConnection import *
from acme.helpers.TextTools import toHex
from acme.etc.RequestUtils import serializeData
from acme.etc.DateUtils import getResourceDate
from acme.etc.Types import ContentSerializationType
from acme.etc.Constants import Constants as C

###MQTT Data to publish
topic = "/oneM2M/req/aqm/id-in/json"

actuatorStatusTrue={"fr":"room1","to":"cse-in/airQualityMonitoring/room1/actuator/status","op":3,"rvi":"3","rqi":"1234562","pc":{"cod:binSh":{"powSe":True}},"ty":28}
actuatorStatusFalse={"fr": "room1","to": "cse-in/airQualityMonitoring/room1/actuator/status","op": 3,"rvi": "3","rqi": "1234562","pc": {"cod:binSh": {"powSe": False}},"ty": 28}
colorLedRed={"fr":"room1","to":"cse-in/airQualityMonitoring/room1/led/color","op":"3","rvi":3,"rqi":"1234562","pc":{"mio:coSLd":{"hue":3,"sat":96,"x":0.6307692307692307,"y":0.3230769230769231,"colT":319}},"ty":28}
colorLedOrange={"fr":"room1","to":"cse-in/airQualityMonitoring/room1/led/color","op":"3","rvi":3,"rqi":"1234562", "pc": {"mio:coSLd": {"hue": 12,"sat": 97,"x": 0.5945945945945946,"y": 0.36486486486486486,"colT": 454}},"ty":28}
colorLedYellow={"fr":"room1","to":"cse-in/airQualityMonitoring/room1/led/color","op":"3","rvi":3,"rqi":"1234562","pc":{"mio:coSLd":{"hue":66,"sat":93,"x":0.41847826086956524,"y":0.5054347826086957,"colT":255}},"ty":28}
colorLedLightGreen={"fr":"room1","to":"cse-in/airQualityMonitoring/room1/led/color","op":"3","rvi":3,"rqi":"1234562","pc":{"mio:coSLd":{"hue":98,"sat":93,"x":0.3203125,"y":0.578125,"colT":250}},"ty":28}
colorLedDarkGreen={"fr":"room1","to":"cse-in/airQualityMonitoring/room1/led/color","op":"3","rvi":3,"rqi":"1234562","pc":{"mio:coSLd":{"hue":104,"sat":93,"x":0.2962962962962963,"y":0.5925925925925926,"colT":250}},"ty":28}
colorLedOff={"fr":"room1","to":"cse-in/airQualityMonitoring/room1/led/color","op":"3","rvi":3,"rqi":"1234562","pc":{"mio:coSLd":{"powSe":False}},"ty":28}
###threshold values
ledDarkGreen = 1000
ledLightGreen = 1500
ledYellow = 2000
ledOrange = 3000
actuatorOnTh = 2000
actuatorOffTh = 1000
###automation code ###
def automation(mqttClient,post_data):### function needs MQTT Client and received Sensor data from ACME
    ###retrieve CO2,Temperature and Humidity values
    y = json.loads(post_data)
    sensorCo2=float(y["m2m:sgn"]["nev"]["rep"]["mio:aiQSr"]["co2"])
    sensorHum=float(y["m2m:sgn"]["nev"]["rep"]["mio:aiQSr"]["hum"])
    sensorTemp=float(y["m2m:sgn"]["nev"]["rep"]["mio:aiQSr"]["temp"])

    ###automation States
    green=sensorCo2 < ledDarkGreen
    lightGreen= ledDarkGreen <= sensorCo2 <ledLightGreen
    yellow = ledLightGreen <= sensorCo2 <ledYellow
    orange = ledYellow <= sensorCo2 < ledOrange
    red = sensorCo2>ledOrange
    aktuatorOn = sensorCo2>actuatorOnTh
    actuatorOff =sensorCo2<actuatorOffTh

    ###automation process
    if red:
        print("Luft Qualitt sehr schlecht: " + "Co2: " +str(sensorCo2)+"ppm " +"Temp: "+str(sensorTemp )+" " +"Hum: "+str(sensorHum)+"%")
        mqttClient.publish(topic,json.dumps(colorLedRed))
    if orange:
        print("Luft Qualitt schlecht: " + "Co2: " +str(sensorCo2)+"ppm " +"Temp: "+str(sensorTemp )+" " +"Hum: "+str(sensorHum)+"%")
        mqttClient.publish(topic,json.dumps(colorLedOrange))
    if yellow:
        print("Luft Qualitt mittelmig: " + "Co2: " +str(sensorCo2)+"ppm " +"Temp: "+str(sensorTemp )+" " +"Hum: "+str(sensorHum)+"%")
        mqttClient.publish(topic,json.dumps(colorLedYellow))
    if lightGreen:
        print("Luft Qualitt gut: " + "Co2: " +str(sensorCo2)+"ppm " +"Temp: "+str(sensorTemp )+" " +"Hum: "+str(sensorHum)+"%")
        mqttClient.publish(topic,json.dumps(colorLedLightGreen))
    if green:
        print("Luft Qualitt sehr gut: " + "Co2: " +str(sensorCo2)+"ppm " +"Temp: "+str(sensorTemp )+" " +"Hum: "+str(sensorHum)+"%")
        mqttClient.publish(topic,json.dumps(colorLedDarkGreen))
    if aktuatorOn:
        mqttClient.publish(topic,json.dumps(actuatorStatusTrue))
    if actuatorOff:
        mqttClient.publish(topic,json.dumps(actuatorStatusFalse))