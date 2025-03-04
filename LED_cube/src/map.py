''' 
    trying to figure out how to mathematically convert given 3d-space coordniates to indecies on a snaking array is more work than id like to do.
    so instead here is a giant dictionary for an nxnxn matrix that will map things out. this will also be faster than computing because LUT :).
    its easier to take the index and find its coordinates then the opposite so thank you to coding and god for that.
'''
#format is data_map[(x,y,z)] = index of the led in the LED array
data_map = {
            # z = 7
(0,0,0):0,
(0,1,0):1,
(0,2,0):2,
(0,3,0):3,
(0,4,0):4,
(0,5,0):5,
(0,6,0):6,
(0,7,0):7,
(1,7,0):8,
(1,6,0):9,
(1,5,0):10,
(1,4,0):11,
(1,3,0):12,
(1,2,0):13,
(1,1,0):14,
(1,0,0):15,
(2,0,0):16,
(2,1,0):17,
(2,2,0):18,
(2,3,0):19,
(2,4,0):20,
(2,5,0):21,
(2,6,0):22,
(2,7,0):23,
(3,7,0):24,
(3,6,0):25,
(3,5,0):26,
(3,4,0):27,
(3,3,0):28,
(3,2,0):29,
(3,1,0):30,
(3,0,0):31,
(4,0,0):32,
(4,1,0):33,
(4,2,0):34,
(4,3,0):35,
(4,4,0):36,
(4,5,0):37,
(4,6,0):38,
(4,7,0):39,
(5,7,0):40,
(5,6,0):41,
(5,5,0):42,
(5,4,0):43,
(5,3,0):44,
(5,2,0):45,
(5,1,0):46,
(5,0,0):47,
(6,0,0):48,
(6,1,0):49,
(6,2,0):50,
(6,3,0):51,
(6,4,0):52,
(6,5,0):53,
(6,6,0):54,
(6,7,0):55,
(7,7,0):56,
(7,6,0):57,
(7,5,0):58,
(7,4,0):59,
(7,3,0):60,
(7,2,0):61,
(7,1,0):62,
(7,0,0):63,
            # z = 1
(7,0,1):64,
(7,1,1):65,
(7,2,1):66,
(7,3,1):67,
(7,4,1):68,
(7,5,1):69,
(7,6,1):70,
(7,7,1):71,
(6,7,1):72,
(6,6,1):73,
(6,5,1):74,
(6,4,1):75,
(6,3,1):76,
(6,2,1):77,
(6,1,1):78,
(6,0,1):79,
(5,0,1):80,
(5,1,1):81,
(5,2,1):82,
(5,3,1):83,
(5,4,1):84,
(5,5,1):85,
(5,6,1):86,
(5,7,1):87,
(4,7,1):88,
(4,6,1):89,
(4,5,1):90,
(4,4,1):91,
(4,3,1):92,
(4,2,1):93,
(4,1,1):94,
(4,0,1):95,
(3,0,1):96,
(3,1,1):97,
(3,2,1):98,
(3,3,1):99,
(3,4,1):100,
(3,5,1):101,
(3,6,1):102,
(3,7,1):103,
(2,7,1):104,
(2,6,1):105,
(2,5,1):106,
(2,4,1):107,
(2,3,1):108,
(2,2,1):109,
(2,1,1):110,
(2,0,1):111,
(1,0,1):112,
(1,1,1):113,
(1,2,1):114,
(1,3,1):115,
(1,4,1):116,
(1,5,1):117,
(1,6,1):118,
(1,7,1):119,
(0,7,1):120,
(0,6,1):121,
(0,5,1):122,
(0,4,1):123,
(0,3,1):124,
(0,2,1):125,
(0,1,1):126,
(0,0,1):127,
            # z = 2
(0,0,2):128,
(0,1,2):129,
(0,2,2):130,
(0,3,2):131,
(0,4,2):132,
(0,5,2):133,
(0,6,2):134,
(0,7,2):135,
(1,7,2):136,
(1,6,2):137,
(1,5,2):138,
(1,4,2):139,
(1,3,2):140,
(1,2,2):141,
(1,1,2):142,
(1,0,2):143,
(2,0,2):144,
(2,1,2):145,
(2,2,2):146,
(2,3,2):147,
(2,4,2):148,
(2,5,2):149,
(2,6,2):150,
(2,7,2):151,
(3,7,2):152,
(3,6,2):153,
(3,5,2):154,
(3,4,2):155,
(3,3,2):156,
(3,2,2):157,
(3,1,2):158,
(3,0,2):159,
(4,0,2):160,
(4,1,2):161,
(4,2,2):162,
(4,3,2):163,
(4,4,2):164,
(4,5,2):165,
(4,6,2):166,
(4,7,2):167,
(5,7,2):168,
(5,6,2):169,
(5,5,2):170,
(5,4,2):171,
(5,3,2):172,
(5,2,2):173,
(5,1,2):174,
(5,0,2):175,
(6,0,2):176,
(6,1,2):177,
(6,2,2):178,
(6,3,2):179,
(6,4,2):180,
(6,5,2):181,
(6,6,2):182,
(6,7,2):183,
(7,7,2):184,
(7,6,2):185,
(7,5,2):186,
(7,4,2):187,
(7,3,2):188,
(7,2,2):189,
(7,1,2):190,
(7,0,2):191,
            # z = 3
(7,0,3):192,
(7,1,3):193,
(7,2,3):194,
(7,3,3):195,
(7,4,3):196,
(7,5,3):197,
(7,6,3):198,
(7,7,3):199,
(6,7,3):200,
(6,6,3):201,
(6,5,3):202,
(6,4,3):203,
(6,3,3):204,
(6,2,3):205,
(6,1,3):206,
(6,0,3):207,
(5,0,3):208,
(5,1,3):209,
(5,2,3):210,
(5,3,3):211,
(5,4,3):212,
(5,5,3):213,
(5,6,3):214,
(5,7,3):215,
(4,7,3):216,
(4,6,3):217,
(4,5,3):218,
(4,4,3):219,
(4,3,3):220,
(4,2,3):221,
(4,1,3):222,
(4,0,3):223,
(3,0,3):224,
(3,1,3):225,
(3,2,3):226,
(3,3,3):227,
(3,4,3):228,
(3,5,3):229,
(3,6,3):230,
(3,7,3):231,
(2,7,3):232,
(2,6,3):233,
(2,5,3):234,
(2,4,3):235,
(2,3,3):236,
(2,2,3):237,
(2,1,3):238,
(2,0,3):239,
(1,0,3):240,
(1,1,3):241,
(1,2,3):242,
(1,3,3):243,
(1,4,3):244,
(1,5,3):245,
(1,6,3):246,
(1,7,3):247,
(0,7,3):248,
(0,6,3):249,
(0,5,3):250,
(0,4,3):251,
(0,3,3):252,
(0,2,3):253,
(0,1,3):254,
(0,0,3):255,
            # z = 4
(0,0,4):256,
(0,1,4):257,
(0,2,4):258,
(0,3,4):259,
(0,4,4):260,
(0,5,4):261,
(0,6,4):262,
(0,7,4):263,
(1,7,4):264,
(1,6,4):265,
(1,5,4):266,
(1,4,4):267,
(1,3,4):268,
(1,2,4):269,
(1,1,4):270,
(1,0,4):271,
(2,0,4):272,
(2,1,4):273,
(2,2,4):274,
(2,3,4):275,
(2,4,4):276,
(2,5,4):277,
(2,6,4):278,
(2,7,4):279,
(3,7,4):280,
(3,6,4):281,
(3,5,4):282,
(3,4,4):283,
(3,3,4):284,
(3,2,4):285,
(3,1,4):286,
(3,0,4):287,
(4,0,4):288,
(4,1,4):289,
(4,2,4):290,
(4,3,4):291,
(4,4,4):292,
(4,5,4):293,
(4,6,4):294,
(4,7,4):295,
(5,7,4):296,
(5,6,4):297,
(5,5,4):298,
(5,4,4):299,
(5,3,4):300,
(5,2,4):301,
(5,1,4):302,
(5,0,4):303,
(6,0,4):304,
(6,1,4):305,
(6,2,4):306,
(6,3,4):307,
(6,4,4):308,
(6,5,4):309,
(6,6,4):310,
(6,7,4):311,
(7,7,4):312,
(7,6,4):313,
(7,5,4):314,
(7,4,4):315,
(7,3,4):316,
(7,2,4):317,
(7,1,4):318,
(7,0,4):319,
            # z = 5
(7,0,5):320,
(7,1,5):321,
(7,2,5):322,
(7,3,5):323,
(7,4,5):324,
(7,5,5):325,
(7,6,5):326,
(7,7,5):327,
(6,7,5):328,
(6,6,5):329,
(6,5,5):330,
(6,4,5):331,
(6,3,5):332,
(6,2,5):333,
(6,1,5):334,
(6,0,5):335,
(5,0,5):336,
(5,1,5):337,
(5,2,5):338,
(5,3,5):339,
(5,4,5):340,
(5,5,5):341,
(5,6,5):342,
(5,7,5):343,
(4,7,5):344,
(4,6,5):345,
(4,5,5):346,
(4,4,5):347,
(4,3,5):348,
(4,2,5):349,
(4,1,5):350,
(4,0,5):351,
(3,0,5):352,
(3,1,5):353,
(3,2,5):354,
(3,3,5):355,
(3,4,5):356,
(3,5,5):357,
(3,6,5):358,
(3,7,5):359,
(2,7,5):360,
(2,6,5):361,
(2,5,5):362,
(2,4,5):363,
(2,3,5):364,
(2,2,5):365,
(2,1,5):366,
(2,0,5):367,
(1,0,5):368,
(1,1,5):369,
(1,2,5):370,
(1,3,5):371,
(1,4,5):372,
(1,5,5):373,
(1,6,5):374,
(1,7,5):375,
(0,7,5):376,
(0,6,5):377,
(0,5,5):378,
(0,4,5):379,
(0,3,5):380,
(0,2,5):381,
(0,1,5):382,
(0,0,5):383,
            # z = 6
(0,0,6):384,
(0,1,6):385,
(0,2,6):386,
(0,3,6):387,
(0,4,6):388,
(0,5,6):389,
(0,6,6):390,
(0,7,6):391,
(1,7,6):392,
(1,6,6):393,
(1,5,6):394,
(1,4,6):395,
(1,3,6):396,
(1,2,6):397,
(1,1,6):398,
(1,0,6):399,
(2,0,6):400,
(2,1,6):401,
(2,2,6):402,
(2,3,6):403,
(2,4,6):404,
(2,5,6):405,
(2,6,6):406,
(2,7,6):407,
(3,7,6):408,
(3,6,6):409,
(3,5,6):410,
(3,4,6):411,
(3,3,6):412,
(3,2,6):413,
(3,1,6):414,
(3,0,6):415,
(4,0,6):416,
(4,1,6):417,
(4,2,6):418,
(4,3,6):419,
(4,4,6):420,
(4,5,6):421,
(4,6,6):422,
(4,7,6):423,
(5,7,6):424,
(5,6,6):425,
(5,5,6):426,
(5,4,6):427,
(5,3,6):428,
(5,2,6):429,
(5,1,6):430,
(5,0,6):431,
(6,0,6):432,
(6,1,6):433,
(6,2,6):434,
(6,3,6):435,
(6,4,6):436,
(6,5,6):437,
(6,6,6):438,
(6,7,6):439,
(7,7,6):440,
(7,6,6):441,
(7,5,6):442,
(7,4,6):443,
(7,3,6):444,
(7,2,6):445,
(7,1,6):446,
(7,0,6):447,
            # z = 7
(7,0,7):448,
(7,1,7):449,
(7,2,7):450,
(7,3,7):451,
(7,4,7):452,
(7,5,7):453,
(7,6,7):454,
(7,7,7):455,
(6,7,7):456,
(6,6,7):457,
(6,5,7):458,
(6,4,7):459,
(6,3,7):460,
(6,2,7):461,
(6,1,7):462,
(6,0,7):463,
(5,0,7):464,
(5,1,7):465,
(5,2,7):466,
(5,3,7):467,
(5,4,7):468,
(5,5,7):469,
(5,6,7):470,
(5,7,7):471,
(4,7,7):472,
(4,6,7):473,
(4,5,7):474,
(4,4,7):475,
(4,3,7):476,
(4,2,7):477,
(4,1,7):478,
(4,0,7):479,
(3,0,7):480,
(3,1,7):481,
(3,2,7):482,
(3,3,7):483,
(3,4,7):484,
(3,5,7):485,
(3,6,7):486,
(3,7,7):487,
(2,7,7):488,
(2,6,7):489,
(2,5,7):490,
(2,4,7):491,
(2,3,7):492,
(2,2,7):493,
(2,1,7):494,
(2,0,7):495,
(1,0,7):496,
(1,1,7):497,
(1,2,7):498,
(1,3,7):499,
(1,4,7):500,
(1,5,7):501,
(1,6,7):502,
(1,7,7):503,
(0,7,7):504,
(0,6,7):505,
(0,5,7):506,
(0,4,7):507,
(0,3,7):508,
(0,2,7):509,
(0,1,7):510,
(0,0,7):511,
}