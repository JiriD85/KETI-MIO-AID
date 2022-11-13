
#define ASYNC_TCP_SSL_ENABLED 1
#include <WiFi.h>
#include <Ticker.h>
#include <Adafruit_SCD30.h>
#include <string.h>


extern "C"
{
  #include "freertos/FreeRTOS.h"
  #include "freertos/timers.h"
}

//##################################################################################
//##################################################################################
#define WIFI_SSID ""
#define WIFI_PASSWORD ""


#define ASYNC_TCP_SSL_ENABLED       true
//#define ASYNC_TCP_SSL_ENABLED       false

#include <AsyncMqtt_Generic.h>

//#define MQTT_HOST         IPAddress(192, 168, 2, 110)
#define MQTT_HOST         "192.168.0.135"        // Broker address

#if ASYNC_TCP_SSL_ENABLED

  #define MQTT_SECURE     true
  
  const uint8_t MQTT_SERVER_FINGERPRINT[] = {0xBD,0x0F,0x36,0xDC,0x1C,0x05,0xB8,0xBB,0xD1,0x6C,0xA5,0xC1,0x99,0xD9,0xFA,0xE8,0x0B,0xCD,0x8E,0x85,0xF8,0xF4,0xA5,0x7C,0x3E,0x98,0x1D,0x5E,0x82,0x3D,0xD2,0xB5};
  const char *PubTopic  = "async-mqtt/ESP32_SSL_Pub";               // Topic to publish
  
  #define MQTT_PORT       9883
  
#else

  const char *PubTopic  = "async-mqtt/ESP32_Pub";                   // Topic to publish
  
  #define MQTT_PORT       1883
  
#endif

AsyncMqttClient mqttClient;
TimerHandle_t mqttReconnectTimer;
TimerHandle_t wifiReconnectTimer;

//#########################################################################
//OneM2M MQTT Default mgf

#define NEW_ROOM_MSG "{\"fr\": \"aid\",\"to\": \"cse-in/airQualityMonitoring_test\",\"op\": 1,\"rvi\": \"3\",\"rqi\": \"1234562\",\"id\": \"ab\",\"srn\": \"as\",\"pc\": {\"m2m:cnt\":{\"rn\": \"room%i\"}},\"ty\": 3}"
#define NEW_FlexContainer_devAir  "{\"fr\":\"aid\",\"to\":\"cse-in/airQualityMonitoring_test/room%i\",\"op\":1,\"rvi\":\"3\",\"rqi\":\"1234562\",\"pc\":{\"mio:devAir\":{\"acpi\":[\"cse-in/acr_room%i\"],\"cnd\":\"org.fhtwmio.common.device.mioDeviceAirQualitySensor\",\"rn\":\"sensor\"}},\"ty\":28}"
#define NEW_FlexContainer_mio_aiQSr "{\"fr\":\"aid\",\"to\":\"cse-in/airQualityMonitoring_test/room%i/sensor\",\"op\":1,\"rvi\":\"3\",\"rqi\":\"1234562\",\"pc\":{\"mio:aiQSr\":{\"acpi\":[\"cse-in/acr_room%i\"],\"cnd\":\"org.fhtwmio.common.moduleclass.mioAirqualitySensor\",\"rn\":\"value\",\"co2\":0,\"temp\":0,\"hum\":0}},\"ty\":28}"
#define UPDATE_SENSOR "{\"fr\":\"aid\",\"to\":\"cse-in/airQualityMonitoring_test/room%i/sensor/value\",\"op\":3,\"rvi\":\"3\",\"rqi\":\"1234562\",\"pc\":{\"mio:aiQSr\":{\"co2\":%f,\"temp\":%f,\"hum\":%f}},\"ty\":28}"







#define dip0 25
#define dip1 33
#define dip2 32
#define dip3 35
uint8_t roomnr = 0b0;

//##################################################################################
//##################################################################################

// SCD30 Arduino IDE Example
Adafruit_SCD30  scd30;




// MQTT Arduino IDE Example##############################################################
void connectToWifi()
{
  Serial.println("Connecting to Wi-Fi...");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
}

void connectToMqtt()
{
  Serial.println("Connecting to MQTT...");
  mqttClient.connect();
}

void WiFiEvent(WiFiEvent_t event)
{
  switch (event)
  {
#if USING_CORE_ESP32_CORE_V200_PLUS
    case ARDUINO_EVENT_WIFI_READY:
      Serial.println("WiFi ready");
      break;
    case ARDUINO_EVENT_WIFI_STA_START:
      Serial.println("WiFi STA starting");
      break;
    case ARDUINO_EVENT_WIFI_STA_CONNECTED:
      Serial.println("WiFi STA connected");
      break;
    case ARDUINO_EVENT_WIFI_STA_GOT_IP6:
    case ARDUINO_EVENT_WIFI_STA_GOT_IP:
      Serial.println("WiFi connected");
      Serial.print("IP address: "); Serial.println(WiFi.localIP());
      connectToMqtt();
      break;
    case ARDUINO_EVENT_WIFI_STA_LOST_IP:
      Serial.println("WiFi lost IP");
      break;
    case ARDUINO_EVENT_WIFI_STA_DISCONNECTED:
      Serial.println("WiFi lost connection");
      xTimerStop(mqttReconnectTimer, 0); // ensure we don't reconnect to MQTT while reconnecting to Wi-Fi
      xTimerStart(wifiReconnectTimer, 0);
      break;
#else
    case SYSTEM_EVENT_STA_GOT_IP:
      Serial.println("WiFi connected");
      Serial.println("IP address: "); Serial.println(WiFi.localIP());
      connectToMqtt();
      break;
    case SYSTEM_EVENT_STA_DISCONNECTED:
      Serial.println("WiFi lost connection");
      xTimerStop(mqttReconnectTimer, 0); // ensure we don't reconnect to MQTT while reconnecting to Wi-Fi
      xTimerStart(wifiReconnectTimer, 0);
      break;
#endif
      default:
      break;
  }
}

void printSeparationLine()
{
  Serial.println("************************************************");
}

void onMqttConnect(bool sessionPresent) 
{
  Serial.print("Connected to MQTT broker: "); Serial.print(MQTT_HOST);
  Serial.print(", port: "); Serial.println(MQTT_PORT);
  Serial.print("PubTopic: "); Serial.println(PubTopic);
  
  printSeparationLine();
  Serial.print("Session present: "); Serial.println(sessionPresent);
  
  uint16_t packetIdSub = mqttClient.subscribe(PubTopic, 2);
  Serial.print("Subscribing at QoS 2, packetId: "); Serial.println(packetIdSub);

  
  mqttClient.publish(PubTopic, 0, true, "ESP32 Test");
  Serial.println("Publishing at QoS 0");
  
  uint16_t packetIdPub1 = mqttClient.publish(PubTopic, 1, true, "test 2");
  Serial.print("Publishing at QoS 1, packetId: "); Serial.println(packetIdPub1);
  
  uint16_t packetIdPub2 = mqttClient.publish(PubTopic, 2, true, "test 3");
  Serial.print("Publishing at QoS 2, packetId: "); Serial.println(packetIdPub2);

  create_room();

  printSeparationLine();
}

void onMqttDisconnect(AsyncMqttClientDisconnectReason reason)
{
  (void) reason;
  
  Serial.println("Disconnected from MQTT.");

  if (WiFi.isConnected())
  {
    xTimerStart(mqttReconnectTimer, 0);
  }
}

void onMqttSubscribe(const uint16_t& packetId, const uint8_t& qos)
{
  Serial.println("Subscribe acknowledged.");
  Serial.print("  packetId: "); Serial.println(packetId);
  Serial.print("  qos: ");      Serial.println(qos);
}

void onMqttUnsubscribe(const uint16_t& packetId)
{
  Serial.println("Unsubscribe acknowledged.");
  Serial.print("  packetId: "); Serial.println(packetId);
}

void onMqttMessage(char* topic, char* payload, const AsyncMqttClientMessageProperties& properties, 
                   const size_t& len, const size_t& index, const size_t& total)
{
  (void) payload;
  
  Serial.println("Publish received.");
  Serial.print("  topic: ");  Serial.println(topic);
  Serial.print("  qos: ");    Serial.println(properties.qos);
  Serial.print("  dup: ");    Serial.println(properties.dup);
  Serial.print("  retain: "); Serial.println(properties.retain);
  Serial.print("  len: ");    Serial.println(len);
  Serial.print("  index: ");  Serial.println(index);
  Serial.print("  total: ");  Serial.println(total);

}

void onMqttPublish(const uint16_t& packetId)
{
  Serial.println("Publish acknowledged");
  Serial.print("  packetId: "); Serial.println(packetId);
}// MQTT Arduino IDE Example##############################################################

// OneM2M 


void create_room(){

  char msg [350]; 

  sprintf(msg,NEW_ROOM_MSG,roomnr);                
  mqttClient.publish("/oneM2M/req/aqm/id-in/json",1,true,msg);

  delay(500);

  sprintf(msg,NEW_FlexContainer_devAir,roomnr,roomnr);                
  mqttClient.publish("/oneM2M/req/aqm/id-in/json",1,true,msg);

  delay(500);

  sprintf(msg,NEW_FlexContainer_mio_aiQSr,roomnr,roomnr);                
  mqttClient.publish("/oneM2M/req/aqm/id-in/json",1,true,msg);



}


void setup() {
  Serial.begin(115200);
  while (!Serial && millis() < 5000);

  Serial.print("\nStarting Sensornode"); Serial.println(ARDUINO_BOARD);  

    // Try to initialize!
  if (!scd30.begin()) {
    Serial.println("Failed to find SCD30 chip");
    while (1) { delay(10); }
  }

  pinMode(dip0, INPUT_PULLUP);
  pinMode(dip1, INPUT_PULLUP);
  pinMode(dip2, INPUT_PULLUP);
  pinMode(dip3, INPUT_PULLUP);

  if (digitalRead(dip0))  roomnr |= 1 ;
  if (digitalRead(dip1))  roomnr |= 2 ; 
  if (digitalRead(dip2))  roomnr |= 4 ; 
  if (digitalRead(dip3))  roomnr |= 8 ;

  Serial.print("Room nr: "); Serial.println(roomnr); 
  Serial.println(digitalRead(dip0));
  Serial.println(digitalRead(dip1));
  Serial.println(digitalRead(dip2));
  Serial.println(digitalRead(dip3));

  Serial.println("SCD30 Found!");

  mqttReconnectTimer = xTimerCreate("mqttTimer", pdMS_TO_TICKS(2000), pdFALSE, (void*)0, reinterpret_cast<TimerCallbackFunction_t>(connectToMqtt));
  wifiReconnectTimer = xTimerCreate("wifiTimer", pdMS_TO_TICKS(2000), pdFALSE, (void*)0, reinterpret_cast<TimerCallbackFunction_t>(connectToWifi));

  WiFi.onEvent(WiFiEvent);

  mqttClient.onConnect(onMqttConnect);
  mqttClient.onDisconnect(onMqttDisconnect);
  mqttClient.onSubscribe(onMqttSubscribe);
  mqttClient.onUnsubscribe(onMqttUnsubscribe);
  mqttClient.onMessage(onMqttMessage);
  mqttClient.onPublish(onMqttPublish);

  mqttClient.setServer(MQTT_HOST, MQTT_PORT);

#if ASYNC_TCP_SSL_ENABLED
  mqttClient.setSecure(MQTT_SECURE);
  
  if (MQTT_SECURE) 
  {
    //mqttClient.addServerFingerprint((const uint8_t[])MQTT_SERVER_FINGERPRINT);
    mqttClient.addServerFingerprint((const uint8_t *)MQTT_SERVER_FINGERPRINT);
  }
#endif

  connectToWifi();


  

}



void readSCD30(){

    if (scd30.dataReady()){
    Serial.println("Data available!");

    if (!scd30.read()){ Serial.println("Error reading sensor data"); return; }

    Serial.print("Temperature: ");
    Serial.print(scd30.temperature);
    Serial.println(" degrees C");
    
    Serial.print("Relative Humidity: ");
    Serial.print(scd30.relative_humidity);
    Serial.println(" %");
    
    Serial.print("CO2: ");
    Serial.print(scd30.CO2, 3);
    Serial.println(" ppm");
    Serial.println("");

    char msg[350];
    sprintf(msg,UPDATE_SENSOR,scd30.CO2,scd30.temperature,scd30.relative_humidity);
    mqttClient.publish("/oneM2M/req/aqm/id-in/json",1,true,msg);
    Serial.print(msg);





    
  } else {
    //Serial.println("No data");
  }
  
}




void loop() {

  
  
  readSCD30();
  delay(5000);

 
  
}
