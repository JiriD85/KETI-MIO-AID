# Description of creation of flexcontainer #
(see TS-0023-Home_Appliances_Information_Model_and_Mapping-V3_7_3.pdf)

ACME CSE creates the flexcontainers described in imported fcp-File:
1. mio:devAct (Actuator) - device class
2. mio:devSLd (Smart LED) - device class
3. mio:devAir (Air Quality Sensor) - device class
4. mio:coSLd (Color Smart LED) - module class containing datapoints for Smart LED control
5. mio:aiQSr (Air Quality Sensor values) - module class containing datapoints of the air quality sensor (co2, humidity, temperature)

## Instructions
1. Copy mio_flex.fcp to /var/lib/docker/volumes/acme_cseVolume/_data/init
2. Restart ACME CSE