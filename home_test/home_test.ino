#include <WiFi.h>

#define BAUD_RATE 115200
#define LED      15
#define in        2

const char* ssid = "HOME-5E95-2.4";
const char* password = "fasten0179brace";

void initWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  //Serial.println(WiFi.localIP());
}

void setup() {
  // WiFi.mode(WIFI_STA)	// station mode: the ESP32 connects to an access point
  // WiFi.mode(WIFI_AP)	// access point mode: stations can connect to the ESP32
  // WiFi.mode(WIFI_AP_STA)	// access point and a station connected to another access point

  
  Serial.begin(BAUD_RATE);


  pinMode(in, INPUT);
  pinMode(LED, OUTPUT);
  Serial.println("Flashed & Running.");

  initWiFi();
  Serial.print("EPS32 IP: ");
  Serial.println(WiFi.localIP());

  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());
}

void loop() {
  // put your main code here, to run repeatedly:
  int read = Serial.parseInt();
  if (read == 1){
    digitalWrite(LED, HIGH);
    Serial.println("Turning LED on");
    delay(2000);
    Serial.println("Turning LED off");
    digitalWrite(LED, LOW);
  }

}
