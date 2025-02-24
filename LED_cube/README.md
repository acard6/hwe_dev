# 3D animated LED cube
## personal project to turn LED's into a programmable 3d cube



## TODO and project notes
plan on making an 3d n*n*n  LED matrix from wsb2112 LED strip. using this as a base to theorize what functions to implement on it once cube can handle it.

Things to note:
    I plan to start with a samller n x n test out LED. From there expand to play around with a 3d concept. After that move onto using 4 or 5 32x32 LED panels and make 3d graphics with that

TODO
- convert the base case where z=0 and points snake
- consider how the points will differ at different height and how to deal with them
- add to this template page to help understand my progress


*The \LED_driver folder contains the code for the mcu hardware to be programmed on
The \src folder is where the python for previewing and converting animations is*



## About


## Initial stages/Preplanning
After some careful consideration the physical LED set up has 2 options the standard thought of how pixels work where LED's =[0, 1,...,n] translates to a 2d array of

    LED-2d-arr =  [ 0       >>  ...  >>   7
               v    8       >>  ...  >>  15
               v    16      >>  ...  >>
               v            >>  ...  >>
               v    56      >>  ...  >>  63]

However, running wires all the way from one side to the other would make it more work and possibly slower on timing ive gone with what many others typically do and use the "snake" method.

    z = [0   >>  ...  >> 7      v
         15  <<  ...  << 8      v
         16  >>  ...  >> 23     v
                 ...
         63  <<  ...  << 56]

where every other row alternates in direction. Another key note is how each floor/level will connect to one another given that the next point must lie physically as close to the previous point to ensure least resistance, best time, and most efficient wiring on the led layout. For level=0, the first 64(8x8) leds, the start is at (x,y,z) of (0,0) and ends at (0,7,0) or the same row but opposite end. Therefore the next 64 points will start above this point at (0,7,1) and if we follow backwards in reverse order the 128th point will lie above the 1st point of the array at (0,0,1). Knowing that the levels would alternate is a simple fix that can be done. 
