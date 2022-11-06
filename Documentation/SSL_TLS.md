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

Edit configuration file *mosquitto.conf*:

