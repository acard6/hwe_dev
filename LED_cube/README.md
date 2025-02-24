plan on making an 3d n*n*n  LED matrix from wsb2112 LED strip. using this as a base to theorize what functions to implement on it once cube can handle it.

Things to note:
    I plan to start with a samller n x n test out LED. From there expand to play around with a 3d concept. After that move onto using 4 or 5 32x32 LED panels and make 3d graphics with that

TODO
- convert the base case where z=0 and points snake
- consider how the points will differ at different height and how to deal with them

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

where every other row alternates in direction. Another key note is how each floor/level will connect to one another given that the next point must lie physically as close to the previous point to ensure least resistance, best time, and most efficient wiring on the led layout




*The \LED_driver folder contains the code for the mcu hardware to be programmed on
The \src folder is where the python for previewing and converting animations is*