#include <stdio.h>
// #include <FastLED.h>
#include <LiteLED.h>
// #include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>  // Required for 16 MHz Adafruit Trinket
#endif

#define BAUD_RATE 115200
#define LED_PIN 23
#define NUM_LED 1
#define SEC 1000

#define LED_TYPE  LED_STRIP_APA106
#define LED_TYPE_IS_RGBW 0   // if the LED is an RGBW type, change the 0 to 1
#define LED_BRIGHT 168   // sets how bright the LED is. O is off; 255 is burn your eyeballs out (not recommended)

// Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, LED_PIN, NEO_RGB + NEO_KHZ800);
// CRGB leds[NUMPIXELS];
static const crgb_t L_RED = 0xff0000;
static const crgb_t L_GREEN = 0x00ff00;
static const crgb_t L_BLUE = 0x0000ff;
LiteLED myLED( LED_TYPE, LED_TYPE_IS_RGBW );

void setup() {
  Serial.begin(BAUD_RATE);
  // Initialize and begin the LED
  // pixels.begin();
  // FastLED.addLeds<APA106, LED_PIN, RGB>(leds, NUMPIXELS);
  myLED.begin(LED_PIN, NUM_LED);         // initialze the myLED object. Here we have 1 LED attached to the LED_GPIO pin
  myLED.brightness(LED_BRIGHT);     // set the LED photon intensity level
  myLED.setPixel(0, L_GREEN, 1);    // set the LED colour and show it
  delay(SEC);

  Serial.println("Flashed & Running. Now Runnig LED_Driver 1.00.4");
  Serial.println("ESP32 is ready for use :)");
}

int loop_var = 0;
crgb_t color = 0x0;

void loop() {
  // put your main code here, to run repeatedly:
  
  // FastLED blink
  // leds[0] = CRGB::Red;
  // FastLED.show();
  // delay(50);
  // // Now turn the LED off, then pause
  // leds[0] = CRGB::Black;
  // FastLED.show();
  
  // adafruit blink
  // pixels.setPixelColor(0, pixels.Color(0, 0, 160));
  // pixels.show();
  // delay(SEC);
  // pixels.setPixelColor(0, pixels.Color(0, 0, 0));
  // pixels.show();
  // delay(SEC);

  // LiteLED blink
  if (loop_var == 1){
    color = L_BLUE;    
  }
  else if (loop_var == 2){
    color = L_GREEN;    
  }
  else{
    color = L_RED;
  }
  loop_var++;
  loop_var = loop_var % 3;


  myLED.setPixel( 0, color, 1);           // turn the LED off (brightness, 1=show )
  delay(SEC);

  myLED.clear(1);  // clear LED buffer and show
  delay(SEC);

}


// // thanks to http://forum.arduino.cc/index.php?topic=307655.5
// void setLedColorHSV(int h, double s, double v) {

//   double r = 0;
//   double g = 0;
//   double b = 0;
//   double hf = h / 60.0;

//   int i = (int)floor(h / 60.0);
//   double f = h / 60.0 - i;
//   double pv = v * (1 - s);
//   double qv = v * (1 - s * f);
//   double tv = v * (1 - s * (1 - f));

//   switch (i) {
//     case 0:
//       r = v;
//       g = tv;
//       b = pv;
//       break;
//     case 1:
//       r = qv;
//       g = v;
//       b = pv;
//       break;
//     case 2:
//       r = pv;
//       g = v;
//       b = tv;
//       break;
//     case 3:
//       r = pv;
//       g = qv;
//       b = v;
//       break;
//     case 4:
//       r = tv;
//       g = pv;
//       b = v;
//       break;
//     case 5:
//       r = v;
//       g = pv;
//       b = qv;
//       break;
//   }

//   //set each component to a integer value between 0 and 255
//   int red = constrain((int)255 * r, 0, 255);
//   int green = constrain((int)255 * g, 0, 255);
//   int blue = constrain((int)255 * b, 0, 255);

//   pixels.setPixelColor(0, pixels.Color(red, green, blue));
//   pixels.show();
// }