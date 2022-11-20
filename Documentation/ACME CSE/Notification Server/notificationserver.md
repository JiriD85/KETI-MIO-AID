# Starting Notification Server with MQTTS Support
```
python3 notificationServer.py --mqtt --mqtt-address mosquitto --mqtt-port 8883 --mqtt-useTLS --mqtt-caFile ca.crt --mqtt-certfile mio_aid.crt --mqtt-keyfile mio_aid.key --mqtt-topic /oneM2M/req/id-in/+/# --mqtt-logging

```

## Instructions
1. Copy notificationServer.py to /var/lib/docker/volumes/acme_cseVolume/_data/tools/notificationServer (replace old file)
2. Copy MQTTConnection.py to /var/lib/docker/volumes/acme_cseVolume/_data/acme/helpers (replace old file)
3. Copy automations.py to /var/lib/docker/volumes/acme_cseVolume/_data/tools/notificationServer