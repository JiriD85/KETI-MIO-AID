## Configuration for the use ofe TLS/SSL certificates ##

The certificates are stored in:
```
/home/pi/ACME/certificates
```

The files *ca.crt*, *mio_aid.crt* and *mio_aid.key* have to be moved to the specific directories of:
1. Mosquitto
2. ACME CSE
3. Zigbee2MQTT

Furthermore the configuration of the applications has to be adapted.

### 1. Mosquitto ###
Copy files to:
```
/var/lib/docker/volumes/acme_mosquittoConfigVolume/_data/
```

Add lines to configuration file *mosquitto.conf*:
```
listener 8883                                 # listening on Port 8883
cafile /mosquitto/config/ca.crt               # Path to the CA.crt file
certfile /mosquitto/config/mio_aid.crt        # Path to the PEM encoded server certificate.
keyfile /mosquitto/config/mio_aid_public.pem  # Path to the PEM encoded keyfile.

```

Further information: https://mosquitto.org/man/mosquitto-conf-5.html

### 2. ACME CSE ###
Copy files to:
```
/var/lib/docker/volumes/acme_cseVolume/_data/cert/
```

Add/change lines in *acme.ini*:
```
[server.http.security]
useTLS=true
tlsVersion=auto
verifyCertificate=false
caCertificateFile=/opt/ACME-oneM2M-CSE/cert/mio_aid.crt
caPrivateKeyFile=/opt/ACME-oneM2M-CSE/cert/mio_aid.key

[client.mqtt]
port=8883

[client.mqtt.security]
useTLS=true
verifyCertificate=false
caCertificateFile=/opt/ACME-oneM2M-CSE/cert/ca.crt
```

Further information: https://github.com/ankraft/ACME-oneM2M-CSE/blob/master/docs/Configuration.md

### 3. Zigbee2MQTT ###
Copy files to:
```
/var/lib/docker/volumes/acme_zigbee2mqttVolume/_data/
```

Add/change lines to configuration file *configuration.yaml*:
```
mqtt:
  base_topic: zigbee2mqtt
  server: mqtt://mosquitto:8883
  ca: /app/data/ca.crt
  key: /app/data/mio_aid.key
  cert: /app/data/mio_aid.crt
```

Further information: https://www.zigbee2mqtt.io/guide/configuration/mqtt.html#server-connection

### 4. Node Red ###
Edit the settings for "mosquitto" MQTT-Broker

1. Change the port to 8333:

![Change the Port to 8333](Node_Red_MQTT_TLS_1.png)

2. Upload certificates:

![Upload Certificates](Node_Red_MQTT_TLS_2.png)