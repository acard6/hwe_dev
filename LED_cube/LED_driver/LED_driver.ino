#include <stdio.h>
#include <FastLED.h>
#include <stdlib.h>
#include <EEPROM.h>
// #include <LiteLED.h>
// #include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>  // Required for 16 MHz Adafruit Trinket
#endif

#define BAUD_RATE 115200
#define NUM_LEDS 300
#define DATA_PIN 2 // blue jumper wire
#define SEC 1000
#define INPUT1 4
#define INPUT2 15

CRGB leds[NUM_LEDS];  // setup for FastLED
const int row = 15;
const int col = 20;

typedef struct{
  uint8_t r;
  uint8_t g;
  uint8_t b;
}colors;


typedef struct coords
{
  int x,y,z;
}coords;

coords plane[64] = {0};

colors ColorArr[row][col] ={ {0} };


void setup() {
  delay(2 * SEC);
  Serial.begin(BAUD_RATE);
  
  pinMode(INPUT1, INPUT);
  pinMode(INPUT2, INPUT);


  // Initialize and begin the LED
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(64);  // setting brightness to 25% max is 255

  // draw_circle(1);
  // draw_square(2);

  Serial.println("Flashed & Running. Now Runnig LED_Driver 1.1.0");
  Serial.println("ESP32 is ready for use :)");

  for (int i=0; i<64; i++){
    plane[i].x = i/8;
    int temp = i%16;
    plane[i].y = (temp>=8)?(15-temp):temp
  }
}



void loop() {
  // put your main code here, to run repeatedly:
  int read1 = digitalRead(INPUT1);
  int read2 = digitalRead(INPUT2);
  
  if ((read1 == 1) && (read2 == 1)){
    draw_circle(4);
    clear();
    display_image();
    delay(2*SEC);
  }
  
  if ((read1 == 1) && (read2 == 0)){
    draw_square(2);
    clear();
    display_image();
    delay(2*SEC);
  }
  if ((read1 == 0) && (read2 == 1)){
    loop_led();
  }
  else{
    clear();
    FastLED.show();
  }
}


void clear(){
  for (int i=0; i<NUM_LEDS; i++){
    leds[i] = CRGB::Black;
  }
}

// FastLED blink
void loop_led(){
  for (int i=0; i<NUM_LEDS; i++){
    leds[i] = CRGB::Red;
    FastLED.show();
    delay(10);
    leds[i] = CRGB::Black;

  }

}

/*
 *  
 *  convert the 2d array that describes an image to the 1d LED matrix
 *  
 */
void display_image(){
  for (int i = 0; i < row; i++) {
    for (int j=0; j < col; j++){
      leds[i*col+j] = CRGB(ColorArr[i][j].r, ColorArr[i][j].g, ColorArr[i][j].b);
    }
    FastLED.show();

  }
}

/*
 *  draws a circle in a 2d array 
 */
void draw_circle(int radius){
    int x0 = row/2;
    int y0  =col/2;
    int dist;
    for (int i = 0; i < row; i++){
      for (int j = 0; j < col; j++){
        dist = sqrt(sq(i-x0) + sq(j-y0));
        if (dist <= radius){
          ColorArr[i][j].r = 128;
          ColorArr[i][j].g = 0;
          ColorArr[i][j].b = 0;
        }
      }
    }
    ColorArr[x0][y0].r = 0;
    ColorArr[x0][y0].g = 128;
    ColorArr[x0][y0].b = 0;

}


/*
 *  draws a square in a 2d array
 */
void draw_square(int width){
    int x0 = row/2;
    int y0  =col/2;
    for (int i = 0; i < row; i++){
      for (int j = 0; j < col; j++){
        if ( (abs(i-x0) <=width) && (abs(j-y0) <= width) ){
          ColorArr[i][j].r = 0;
          ColorArr[i][j].g = 128;
          ColorArr[i][j].b = 0;
        }
      }
    }
    ColorArr[x0][y0].r = 0;
    ColorArr[x0][y0].g = 0;
    ColorArr[x0][y0].b = 128;

}