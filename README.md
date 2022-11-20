# KETI-MIO-AID
Raspberry Pi based air quality monitoring system connecting ESP32-S sensor nodes, actuators and Smart LEDs via Zigbee and MQTT to a ACME CSE.

## High Level Architecture
Every room is equipped with the following devices:
- Sensor Node with ESP32-S and a SCD30 sensor measuring the CO2 concentration (ppm), temperature (°C) and humidity (% r.H.)
- Zigbee Smart LED
- Zigbee Actuator that controls a fan or a window drive

The Raspberry Pi runs a Docker environment with following applications:
- Portainer
- Zigbee2MQTT
- Node Red
- Mosquitto MQTT Broker
- ACME-oneM2M-CSE

**Description of the process**
- Sensor Nodes are sending their measurements via MQTT to the ACME-oneM2M-CSE
- The payload of the sensor nodes MQTT message is a OneM2M request and the MQTT topic is /oneM2M/req/aqm/id-in/json
- Through the definition of specific messages and topics it is ensured, that the information gets through to the ACME-oneM2M-CSE
- The sensor nodes are getting updated by the sensor messages in the OneM2M CSE
- The OneM2M CSE sends a response message to the sensor with the MQTT topic /oneM2M/resp/aqm/id-in/json
- Every response message is processed in Node Red function nodes
- One function node is creating a OneM2M request to change the state of the actuator (controling a fan or window drive), depending on the measured CO2 concentration level
- Another function node is creating a OneM2M request to change the color of the smart LED, depending on the measured CO2 concentration level
- Then there is a function node, that is translating the OneM2M response message to control the smart LEDs and actuators via Zigbee
- All measured values are visualized with Node Red dashboards
- Simple control functions are implemented with Node Red dashboards

![Architecture](Pictures/High_Level_Architecture.png)

## Raspberry Pi Config
### Network
- **IP-Address:** <your IP address>
- **Hostname:** <your hostname>
- **User:** <your user>
- **Password:** <your pw>

### Grafana
- **Port:** 3000
- http://192.168.1.121:3000/
- not in use / Dashboards and Widgets were created with Node Red

### Zigbee2MQTT
- **Ports:** 8883, 8081
- http://192.168.1.121:8081/#/

### NodeRed
- **Port:** 1880
- http://192.168.1.121:1880/

### Acme CSE
- **Port:** 8080
- http://192.168.1.121:8080/webui/index.html?ri=id-in&or=aid

### Portainer: https://192.168.1.121:9443/#!/auth
Username: admin
Password: PORTAINER@MIO

### Installation via docker-compose
`docker-compose up -d`
[Link to Docker Compose file](Docker/docker-compose.yml)

![Running Containers](Pictures/Portainer_Containers.png)

## Sensor Node Config
### SCD30 Sensor

[Seeedstudio Grove SCD30](https://wiki.seeedstudio.com/Grove-CO2_Temperature_Humidity_Sensor-SCD30/)

## Brainstorming CSE
### Data Management
- application AE: aqm (air quality management)
- container: room1, room2
- flex container: device classes (devAct, devSd, devAir), module classes (cod:binSh, cod:sigSh, mio:coSLd, mio:aiQSr)

### Authorization
- access control policies: acp_admin, acp_room1, acp_room2

### Subscription/Notification
- Notification Server on Port 9999
- <subscription> resource: CRUD

**Notification**
- Attributes: eventNotifocationCriteria, notificationURI, ...
- Notification Target: ```localhost:9999 (ContentType = JSON)``` 

**Subscription**
- Event Type: target update, target delete, child creation, ...

**Aggregated Notification**
- subscription reference
- notification event: notification event type, representation
- content instance: name, type, content

### AE Registration <AE> Resource
- Attributes: appName, App-ID, AE-ID, etc.
- AE-ID Uniqueness: ```cse-in/airQualityMonitoring```

### Container and contentInstance
- Attributes: maxNrOfInstances, maxByteSize, locationID, creator, ...
- Child Resources: container, subscription, latest, oldest, ...
```cse-in/airQualityMonitoring/room1 #resource: content, creationTime, stateTag``` 

### Rescource Discovery
- Filter conditions: createdBefore, createdAfter, modifiedSince, labels, resourceType, ...
- Discover resources created after a specific time: ```{URL}?fu=1&cra=20221008T122321```

### Group
- group of resources and its management
- attributes: memberIDs (ID of group member resources)
- e.g. Group of actuators:
```
cse-in/airQualityMonitoring/gractuator
cse-in/airQualityMonitoring/grsled
```

### Procedure
1. Registration: Devices and user app (AEs) registers to the platform (CSE)
2. Initial resource creation: <acp>, <container>, <flexcontainer>, <subscription>
3. Target container discovery: group creation
4. Retrieve current sensor data (CO2, temperature, humidity) and status of the actuators (Smart LED, fan)
5. Single switch on/off Smart LED / Change Smart LED color / Activate fan --> watching notification event
6. Multiple switch on/off: group fan-out

**1. Registration**
- Sensor Node 1, Sensor Node 2, Smart LED 1, Smart LED 2, Actuator 1, Actuator 2 ```<AE>``` create request

**2. Initial resource creation**
- Sensor Node 1, Sensor Node 2, Smart LED 1, Smart LED 2, Actuator 1, Actuator 2 ```<container>, <contantInstance>, <subscription>```create request

**3. Traget container discovery**
- User app (AE): discovery request for Smart LED and Actuator control, ```<group>``` create request

**Resource Tree**
```
CSE<CSEBase>
    airQualityMonitoring<AE> *cse-in/airQualityMonitoring*
        room1<container> *cse-in/airQualityMonitoring/room1*
            mio:devAct<flexContainer> *cse-in/airQualityMonitoring/room1/actuator*
               cod:sigSh<flexContainer> *cse-in/airQualityMonitoring/room1/actuator/lqi*
               cod:binSh<flexContainer> *cse-in/airQualityMonitoring/room1/actuator/status*
            mio:devSd<flexContainer> *cse-in/airQualityMonitoring/room1/led*
               cod:sigSh<flexContainer> *cse-in/airQualityMonitoring/room1/led/lqi*
               cod:binSh<flexContainer> *cse-in/airQualityMonitoring/room1/led/status*
               cod:brigs<flexContainer> *cse-in/airQualityMonitoring/room1/led/brigs*
               mio:coSLd<flexContainer> *cse-in/airQualityMonitoring/room1/led/color*
            mio:devAir<flexContainer> *cse-in/airQualityMonitoring/room1/sensor*
               mio:aiQSr<flexContainer> *cse-in/airQualityMonitoring/room1/sensor/value*
        room2<container> *cse-in/airQualityMonitoring/room2*
            mio:devAct<flexContainer> *cse-in/airQualityMonitoring/room2/actuator*
               cod:sigSh<flexContainer> *cse-in/airQualityMonitoring/room2/actuator/lqi*
               cod:binSh<flexContainer> *cse-in/airQualityMonitoring/room2/actuator/status*
            mio:devSd<flexContainer> *cse-in/airQualityMonitoring/room2/led*
               cod:sigSh<flexContainer> *cse-in/airQualityMonitoring/room2/led/lqi*
               cod:binSh<flexContainer> *cse-in/airQualityMonitoring/room2/led/status*
               cod:brigs<flexContainer> *cse-in/airQualityMonitoring/room2/led/brigs*
               mio:coSLd<flexContainer> *cse-in/airQualityMonitoring/room2/led/color*
            mio:devAir<flexContainer> *cse-in/airQualityMonitoring/room2/sensor*
               mio:aiQSr<flexContainer> *cse-in/airQualityMonitoring/room2/sensor/value*
    userApp<AE> *tbd*
        gractuator<group> *cse-in/userApp/gractuator*
        grsled<group> *cse-in/userApp/gractuator*
```

**4. Retrieve current status**
- User app (AE): group fan-out retrieve request

**5. Single on/off**
- watching notification event
- User app (AE): ```<contenetInstance> create request``` to CSE
- CSE: ```notification request``` to actuatorControl1

**6. Multiple on/off**
- group fan-out
- User app (AE): ```group fan-out <contentInstance> create request``` to CSE
- CSE: ```notification request``` to actuatorControl1, actuatorcontrol2
