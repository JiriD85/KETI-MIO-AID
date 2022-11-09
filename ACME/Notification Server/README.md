### Starting Notification Server with MQTTS Support
```
python3 notificationServer.py --mqtt --mqtt-address mosquitto --mqtt-port 8883 --mqtt-useTLS --mqtt-caFile ca.crt --mqtt-certfile mio_aid.crt --mqtt-keyfile mio_aid.key --mqtt-topic /oneM2M/req/id-in/+/# --mqtt-logging

```