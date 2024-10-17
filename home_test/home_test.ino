#include <WiFi.h>
#include <stdio.h>
#include <string.h>
#include <WebServer.h>

#define BAUD_RATE 115200
#define LED       15
#define IN        2
#define SEC       1000

const char* ssid = "SweetHome";
const char* password = "Fasten017!";
IPAddress local_ip(192,168,1,1);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);
bool wifi_stat = false;

WiFiServer server(80);

// Current time
unsigned long currentTime = millis();
// Previous time
unsigned long previousTime = 0; 
// Define timeout time in milliseconds (example: 2000ms = 2s)
const long timeoutTime = 2000;
String header;
String LED_state = "off";

void initWiFi() {
  // WiFi.mode(WIFI_AP);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(SEC);
  }
  Serial.println();
  Serial.println("WiFi Connected");
  Serial.print("EPS32 IP: ");
  Serial.println(WiFi.localIP());
  server.begin();
  wifi_stat = true;
}

void setup() {
  // WiFi.mode(WIFI_STA)	// station mode: the ESP32 connects to an access point
  // WiFi.mode(WIFI_AP)	// access point mode: stations can connect to the ESP32
  // WiFi.mode(WIFI_AP_STA)	// access point and a station connected to another access point

  
  Serial.begin(BAUD_RATE);

  Serial.println("Flashed & Running.");

  pinMode(IN, INPUT); // input pin to read data
  pinMode(LED, OUTPUT); // output to LED for testing

  // initWiFi();
  

  Serial.println("ESP32 is ready for use :)");

}

void loop() {
  // put your main code here, to run repeatedly:
  int read = Serial.parseInt();   // read from serial monitor
  if (read == 1){                 // if 1 in serial monitor turn on and off an LED on breadboard
    digitalWrite(LED, HIGH);      // used for testing software to hardware compatability
    Serial.println("Turning LED on");
    delay(2*SEC);
    digitalWrite(LED, LOW);
    Serial.println("Turning LED off");
  }

  if (read == 2){
    Serial.println("Type into the Message line.");
    delay(6*SEC);
    String s = Serial.readString();
    Serial.printf("You typed:%s", s);
  }

  if (wifi_stat){
    run_server();
  }
  if (digitalRead(IN)){
    digitalWrite(LED, HIGH);
  }
  else if (!digitalRead(IN)){
    digitalWrite(LED, LOW);
  }

}


void run_server(){
  WiFiClient client = server.available();  // listen for incoming clients
  if (client) {                     // if you get a client,
    Serial.println("New Client.");  // print a message out the serial port
    String currentLine = "";        // make a String to hold incoming data from the client
    while (client.connected()) {    // loop while the client's connected
      if (client.available()) {     // if there's bytes to read from the client,
        char c = client.read();     // read a byte, then
        Serial.write(c);            // print it out the serial monitor
        header += c;
        if (c == '\n') {            // if the byte is a newline character

          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();

            if (header.indexOf("GET /15/on") >= 0) {
              Serial.println("GPIO 15 on");
              LED_state = "on";
              digitalWrite(LED, HIGH);
            } else if (header.indexOf("GET /15/off") >= 0) {
              Serial.println("GPIO 15 off");
              LED_state = "off";
              digitalWrite(LED, LOW);
            }
            // Display the HTML web page
            client.println("<!DOCTYPE html><html>");
            client.println("<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
            client.println("<link rel=\"icon\" href=\"data:,\">");
            // CSS to style the on/off buttons 
            // Feel free to change the background-color and font-size attributes to fit your preferences
            client.println("<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}");
            client.println(".button { background-color: #4CAF50; border: none; color: white; padding: 16px 40px;");
            client.println("text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}");
            client.println(".button2 {background-color: #555555;}</style></head>");
            
            // Web Page Heading
            client.println("<body><h1>ESP32 Web Server</h1>");

            // Display current state, and ON/OFF buttons for GPIO 26  
            client.println("<p>GPIO 15 - State " + LED_state + "</p>");
            // If the output26State is off, it displays the ON button       
            if (LED_state=="off") {
              client.println("<p><a href=\"/15/on\"><button class=\"button\">ON</button></a></p>");
            } else {
              client.println("<p><a href=\"/15/off\"><button class=\"button button2\">OFF</button></a></p>");
            } 

            client.println("<body><\html>");

            // The HTTP response ends with another blank line:
            client.println();
            // break out of the while loop:
            break;
          } else {  // if you got a newline, then clear currentLine:
            currentLine = "";
          }
        } else if (c != '\r') {  // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }
      }
    }
    header = "";
    // close the connection:
    client.stop();
    Serial.println("Client Disconnected.");
    Serial.println();
  }  
}