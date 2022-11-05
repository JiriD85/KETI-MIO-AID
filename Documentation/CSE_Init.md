# CSE Step by Step
**MQTT Topic** 
Topic: /oneM2M/req/aqm/id-in/json
Request: /oneM2M/req/+/id-in/json
Response: /oneM2M/resp/aqm/id-in/json

## Creating AE "airQualityMonitoring"
**cse-in/airQualityMonitoring**
Resource ID / URL: id-in
Request Header:
```
Content-Type: application/json;ty=2
Accept: application/json
X-M2M-Origin: Caqm
X-M2M-RI: h3r50jwbemk
X-M2M-RVI: 3
```
Request Body:
```
{
    "m2m:ae": {
        "api": "Naqm",
        "rn": "airQualityMonitoring",
        "srv": [
            "3"
        ],
        "rr": true
    }
}
```
Response Header:
```
connection: close
content-length: 232
content-type: application/json
date: Thu, 03 Nov 2022 18:33:15 GMT
server: Werkzeug/2.2.2 Python/3.8.14, ACME 0.10.2
x-m2m-ot: 20221103T183315,323656
x-m2m-ri: 84e04p9x7vx
x-m2m-rsc: 2001
x-m2m-rvi: 3
```
Response Body:
```
{
    "m2m:ae": {
        "api": "Naqm",
        "rn": "airQualityMonitoring",
        "srv": [
            "3"
        ],
        "rr": true,
        "ri": "Caqm",
        "pi": "id-in",
        "ct": "20221103T183314,694286",
        "lt": "20221103T183314,694286",
        "et": "20231103T183314,694383",
        "ty": 2,
        "aei": "Caqm"
    }
}
```

## Creating Container "room1" inside AE "airQualityMonitoring"
**cse-in/airQualityMonitoring/room1**
Ressource ID / URL: Caqm
Request Header:
```
Content-Type: application/json;ty=3
Accept: application/json
X-M2M-Origin: aid
X-M2M-RI: iztdjlbech
X-M2M-RVI: 3
```
Request Body:
```
{
    "m2m:cnt": {
        "mbs": 10000,
        "mni": 10,
        "rn": "room1"
    }
}
```

**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/Caqm",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "id": "ab",
    "srn": "as",
    "pc": {
        "m2m:cnt": {
            "rn": "room10"
        }
    },
    "ty": 3
}
```

Response Header:
```
connection: close
content-length: 233
content-type: application/json
date: Thu, 03 Nov 2022 18:41:22 GMT
server: Werkzeug/2.2.2 Python/3.8.14, ACME 0.10.2
x-m2m-ot: 20221103T184122,822423
x-m2m-ri: iztdjlbech
x-m2m-rsc: 2001
x-m2m-rvi: 3
```
Response Body:
```
{
    "m2m:cnt": {
        "mbs": 10000,
        "mni": 10,
        "rn": "room1",
        "ri": "cnt5647192724075432334",
        "pi": "Caqm",
        "ct": "20221103T184121,447427",
        "lt": "20221103T184121,447427",
        "et": "20231103T184121,447526",
        "ty": 3,
        "cni": 0,
        "cbs": 0,
        "st": 0
    }
}
```

## Creating flexcontainer "room1_deviceSmartLed" inside container "room1"
**cse-in/airQualityMonitoring/room1/room1_deviceSmartLed**
Ressource ID / URL: cnt1016724803076668936
Request Header:
```
Content-Type: application/json;ty=28
Accept: application/json
X-M2M-Origin: aid
X-M2M-RI: kxevz4abq9
X-M2M-RVI: 3
```
Request Body:
```
{
    "mio:devSd": {
        "cnd": "org.fhtwmio.common.device.mioDeviceSmartLed",
        "rn": "led"
    }
}
```
**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/<cnt-URI>",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "pc": {
        "mio:devSd": {
            "cnd": "org.fhtwmio.common.device.mioDeviceSmartLed",
            "rn": "led"
        }
    },
    "ty": 28
}
```

Response Header:
```
connection: close
content-length: 233
content-type: application/json
date: Thu, 03 Nov 2022 18:41:22 GMT
server: Werkzeug/2.2.2 Python/3.8.14, ACME 0.10.2
x-m2m-ot: 20221103T184122,822423
x-m2m-ri: iztdjlbech
x-m2m-rsc: 2001
x-m2m-rvi: 3
```
Response Body:
```
{
    "m2m:cnt": {
        "mbs": 10000,
        "mni": 10,
        "rn": "room1",
        "ri": "cnt5647192724075432334",
        "pi": "Caqm",
        "ct": "20221103T184121,447427",
        "lt": "20221103T184121,447427",
        "et": "20231103T184121,447526",
        "ty": 3,
        "cni": 0,
        "cbs": 0,
        "st": 0
    }
}
```

## Creating flexcontainer "room1_deviceActuator" inside container "room1"
**cse-in/airQualityMonitoring/room1/room1_deviceActuator**
Ressource ID / URL: cnt1016724803076668936
Request Header:
```
Content-Type: application/json;ty=28
Accept: application/json
X-M2M-Origin: aid
X-M2M-RI: kxevz4abq9
X-M2M-RVI: 3
```
Request Body:
```
{
    "mio:devAct": {
        "cnd": "org.fhtwmio.common.device.mioDeviceActuator",
        "rn": "actuator"
    }
}
```
**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/<cnt-URI>",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "pc": {
        "mio:devAct": {
            "cnd": "org.fhtwmio.common.device.mioDeviceActuator",
            "rn": "actuator10"
        }
    },
    "ty": 28
}
```

## Creating flexcontainer "room1_deviceAirQualitySensor" inside container "room1"
**cse-in/airQualityMonitoring/room1/room1_deviceAirQualitySensor**
Ressource ID / URL: cnt1016724803076668936
Request Header:
```
Content-Type: application/json;ty=28
Accept: application/json
X-M2M-Origin: aid
X-M2M-RI: kxevz4abq9
X-M2M-RVI: 3
```
Request Body:
```
{
    "mio:devAir": {
        "cnd": "org.fhtwmio.common.device.mioDeviceAirQualitySensor",
        "rn": "sensor"
    }
}
```
**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/<cnt-URI>",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "pc": {
        "mio:devAir": {
            "cnd": "org.fhtwmio.common.device.mioDeviceAirQualitySensor",
            "rn": "sensor"
        }
    },
    "ty": 28
}
```

## Creating datapoints inside "room1_deviceAirQualitySensor"
**cse-in/airQualityMonitoring/room1/sensor**
Ressource ID / URL: cnt1016724803076668936
Request Header:
```
Content-Type: application/json;ty=28
Accept: application/json
X-M2M-Origin: aid
X-M2M-RI: kxevz4abq9
X-M2M-RVI: 3
```
Request Body:
```
{
    "mio:aiQSr": {
        "cnd": "org.fhtwmio.common.moduleclass.mioAirqualitySensor",
        "rn": "sensor",
        "co2": 0,
        "temp": 0,
        "hum": 0
    }
}
```
**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/<devAir-URI>",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "pc": {
        "mio:aiQSr": {
            "cnd": "org.fhtwmio.common.moduleclass.mioAirqualitySensor",
            "rn": "sensor",
            "co2": 0,
            "temp": 0,
            "hum": 0
        }
    },
    "ty": 28
}
```

## Creating datapoints inside "room1_deviceSmartLed"
**cse-in/airQualityMonitoring/room1/led**
Ressource ID / URL: cnt1016724803076668936
Request Header:
```
Content-Type: application/json;ty=28
Accept: application/json
X-M2M-Origin: aid
X-M2M-RI: kxevz4abq9
X-M2M-RVI: 3
```
<!--- Color -->
Request Body:
```
{
    "mio:coSLd": {
        "cnd": "org.fhtwmio.common.moduleclass.mioColorSmartLed",
        "rn": "color",
        "hue": 0,
        "sat": 0,
        "x": 0,
        "y": 0,
        "colT": 0
    }
}
```
**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/<devSd-URI>",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "pc": {
        "mio:coSLd": {
            "cnd": "org.fhtwmio.common.moduleclass.mioColorSmartLed",
            "rn": "color",
            "hue": 0,
            "sat": 0,
            "x": 0,
            "y": 0,
            "colT": 0
        }
    },
    "ty": 28
}
```
<!--- Status (Switch on/off) -->
Request Body:
```
{
    "cod:binSh": {
        "cnd": "org.onem2m.common.moduleclass.binarySwitch",
        "rn": "status",
        "powSe": false
    }
}
```
**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/<devSd-URI>",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "pc": {
        "cod:binSh": {
            "cnd": "org.onem2m.common.moduleclass.binarySwitch",
            "rn": "status",
            "powSe": false
        }
    },
    "ty": 28
}
```
<!--- Brightness -->
Request Body:
```
{
    "cod:brigs": {
        "cnd": "org.onem2m.common.moduleclass.brightness",
        "rn": "brightness",
        "brigs": 254
    }
}
```
**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/<devSd-URI>",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "pc": {
        "cod:brigs": {
            "cnd": "org.onem2m.common.moduleclass.brightness",
            "rn": "brightness",
            "brigs": 254
        }
    },
    "ty": 28
}
```
<!--- Signal Strength -->
Request Body:
```
{
    "cod:sigSh": {
        "cnd": "org.onem2m.common.moduleclass.signalStrength",
        "rn": "lqi",
        "lqi": 0
    }
}
```
**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/<devSd-URI>",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "pc": {
        "cod:sigSh": {
            "cnd": "org.onem2m.common.moduleclass.signalStrength",
            "rn": "lqi",
            "lqi": 0
        }
    },
    "ty": 28
}
```

## Creating datapoints inside "room1_deviceActuator"
**cse-in/airQualityMonitoring/room1/actuator**
Ressource ID / URL: cnt1016724803076668936
Request Header:
```
Content-Type: application/json;ty=28
Accept: application/json
X-M2M-Origin: aid
X-M2M-RI: kxevz4abq9
X-M2M-RVI: 3
```
<!--- Status (Switch on/off) -->
Request Body:
```
{
    "cod:binSh": {
        "cnd": "org.onem2m.common.moduleclass.binarySwitch",
        "rn": "status",
        "powSe": false
    }
}
```
**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/<devAct-URI>",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "pc": {
        "cod:binSh": {
            "cnd": "org.onem2m.common.moduleclass.binarySwitch",
            "rn": "status",
            "powSe": false
        }
    },
    "ty": 28
}
```
<!--- Signal Strength -->
Request Body:
```
{
    "cod:sigSh": {
        "cnd": "org.onem2m.common.moduleclass.signalStrength",
        "rn": "lqi",
        "lqi": 0
    }
}
```

**MQTT**
```
{
    "fr": "aid",
    "to": "/id-in/<devAct-URI>",
    "op": 1,
    "rvi": "3",
    "rqi": "1234562",
    "pc": {
        "cod:sigSh": {
            "cnd": "org.onem2m.common.moduleclass.signalStrength",
            "rn": "lqi",
            "lqi": 0
        }
    },
    "ty": 28
}
```


## Templates from ACME CSE
**Template AE ACME CSE**
Request Header:
```
Content-Type: application/json;ty=2
Accept: application/json
X-M2M-Origin: aid
X-M2M-RI: rpyu1dccs7
X-M2M-RVI: 3
```
Request Body:
```
{
    "m2m:ae": {
        "acpi": [
            "==> fill or remove <=="
        ],
        "api": "==> fill (must start with N or R) <==",
        "nl": "==> fill or remove <==",
        "poa": [
            "==> fill or remove <=="
        ],
        "rn": "==> fill or remove <==",
        "srv": [
            "3"
        ],
        "rr": false
    }
}
```

**Template Container ACME CSE**
Request Header:
```
Content-Type: application/json;ty=3
Accept: application/json
X-M2M-Origin: aid
X-M2M-RI: ldjye9n1fhe
X-M2M-RVI: 3
```
Request Body:
```
{
    "m2m:cnt": {
        "acpi": [
            "==> fill or remove <=="
        ],
        "mbs": 10000,
        "mni": 10,
        "rn": "==> fill <=="
    }
}
```

**Template Flexcontainer ACME CSE**
Request Header:
```
Content-Type: application/json;ty=28
Accept: application/json
X-M2M-Origin: aid
X-M2M-RI: dqnho8zg21t
X-M2M-RVI: 3
```
Request Body:
```
{
    "==> fill <==": {
        "acpi": [
            "==> fill or remove <=="
        ],
        "cnd": "==> fill <==",
        "rn": "==> fill <==",
        "==> custom attributes <==": "==> fill <=="
    }
}
```
