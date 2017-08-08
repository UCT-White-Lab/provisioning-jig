EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:probe_pcb-cache
EELAYER 25 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L ST_LINK U?
U 1 1 5989D23C
P 3500 1450
F 0 "U?" H 3250 650 60  0000 C CNN
F 1 "ST_LINK" H 3300 1950 60  0000 C CNN
F 2 "" H 3300 1950 60  0001 C CNN
F 3 "" H 3300 1950 60  0001 C CNN
	1    3500 1450
	1    0    0    -1  
$EndComp
$Comp
L USB_B J?
U 1 1 5989D23E
P 1150 1400
F 0 "J?" H 950 1850 50  0000 L CNN
F 1 "USB_B" H 950 1750 50  0000 L CNN
F 2 "Connectors:USB_B" H 1300 1350 50  0001 C CNN
F 3 "" H 1300 1350 50  0001 C CNN
	1    1150 1400
	1    0    0    -1  
$EndComp
$Comp
L TARGET U?
U 1 1 5989D240
P 7000 2700
F 0 "U?" H 6150 3950 60  0000 C CNN
F 1 "TARGET" H 6400 1550 60  0000 C CNN
F 2 "" H 6750 2600 60  0000 C CNN
F 3 "" H 6750 2750 60  0001 C CNN
	1    7000 2700
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5989D241
P 1100 2000
F 0 "#PWR?" H 1100 1750 50  0001 C CNN
F 1 "GND" H 1100 1850 50  0000 C CNN
F 2 "" H 1100 2000 50  0001 C CNN
F 3 "" H 1100 2000 50  0001 C CNN
	1    1100 2000
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR?
U 1 1 5989D242
P 1550 1000
F 0 "#PWR?" H 1550 850 50  0001 C CNN
F 1 "+5V" H 1550 1140 50  0000 C CNN
F 2 "" H 1550 1000 50  0001 C CNN
F 3 "" H 1550 1000 50  0001 C CNN
	1    1550 1000
	1    0    0    -1  
$EndComp
Text Notes 750  700  0    60   ~ 0
USB 1 - Connects to ST-LINK for flashing target and debugger
$Comp
L +5V #PWR?
U 1 1 5989D243
P 2650 1000
F 0 "#PWR?" H 2650 850 50  0001 C CNN
F 1 "+5V" H 2650 1140 50  0000 C CNN
F 2 "" H 2650 1000 50  0001 C CNN
F 3 "" H 2650 1000 50  0001 C CNN
	1    2650 1000
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5989D244
P 2650 2000
F 0 "#PWR?" H 2650 1750 50  0001 C CNN
F 1 "GND" H 2650 1850 50  0000 C CNN
F 2 "" H 2650 2000 50  0001 C CNN
F 3 "" H 2650 2000 50  0001 C CNN
	1    2650 2000
	1    0    0    -1  
$EndComp
$Comp
L ST_LINK U?
U 1 1 5989D245
P 3550 3800
F 0 "U?" H 3300 3000 60  0000 C CNN
F 1 "ST_LINK" H 3350 4300 60  0000 C CNN
F 2 "" H 3350 4300 60  0001 C CNN
F 3 "" H 3350 4300 60  0001 C CNN
	1    3550 3800
	1    0    0    -1  
$EndComp
$Comp
L USB_B J?
U 1 1 5989D246
P 1200 3750
F 0 "J?" H 1000 4200 50  0000 L CNN
F 1 "USB_B" H 1000 4100 50  0000 L CNN
F 2 "Connectors:USB_B" H 1350 3700 50  0001 C CNN
F 3 "" H 1350 3700 50  0001 C CNN
	1    1200 3750
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5989D247
P 1150 4350
F 0 "#PWR?" H 1150 4100 50  0001 C CNN
F 1 "GND" H 1150 4200 50  0000 C CNN
F 2 "" H 1150 4350 50  0001 C CNN
F 3 "" H 1150 4350 50  0001 C CNN
	1    1150 4350
	1    0    0    -1  
$EndComp
Text Notes 800  3050 0    60   ~ 0
USB 2 - For firmware upgrade of DEBUG
$Comp
L GND #PWR?
U 1 1 5989D248
P 2700 4350
F 0 "#PWR?" H 2700 4100 50  0001 C CNN
F 1 "GND" H 2700 4200 50  0000 C CNN
F 2 "" H 2700 4350 50  0001 C CNN
F 3 "" H 2700 4350 50  0001 C CNN
	1    2700 4350
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR?
U 1 1 5989D249
P 2300 1000
F 0 "#PWR?" H 2300 850 50  0001 C CNN
F 1 "+5V" H 2300 1140 50  0000 C CNN
F 2 "" H 2300 1000 50  0001 C CNN
F 3 "" H 2300 1000 50  0001 C CNN
	1    2300 1000
	1    0    0    -1  
$EndComp
Text Label 2700 3350 0    60   ~ 0
V_Debug
Text Label 4050 1200 0    60   ~ 0
NRST
Text Label 4050 1350 0    60   ~ 0
SWCLK
Text Label 4050 1500 0    60   ~ 0
SWDIO_SWITCH
Text Label 4100 4250 0    60   ~ 0
SWDIO_DEBUG
Text Label 4100 4400 0    60   ~ 0
SWCLK
Text Label 2100 3850 0    60   ~ 0
USB_B_D-
Text Label 2100 4000 0    60   ~ 0
USB_B_D+
Wire Wire Line
	1050 1800 1150 1800
Wire Wire Line
	1100 1800 1100 2000
Wire Wire Line
	1550 1000 1550 1200
Wire Wire Line
	1550 1200 1450 1200
Wire Wire Line
	2650 1000 2650 1200
Wire Wire Line
	2650 1200 2900 1200
Wire Wire Line
	2300 1000 2300 1350
Wire Wire Line
	2300 1350 2900 1350
Wire Wire Line
	1450 1500 2900 1500
Wire Wire Line
	1450 1400 1850 1400
Wire Wire Line
	1850 1400 1850 750 
Wire Wire Line
	1850 750  700  750 
Wire Wire Line
	700  750  700  2200
Wire Wire Line
	700  2200 1500 2200
Wire Wire Line
	1500 2200 1500 1650
Wire Wire Line
	1500 1650 2900 1650
Wire Wire Line
	2900 1800 2650 1800
Wire Wire Line
	2650 1800 2650 2000
Wire Wire Line
	1100 4150 1200 4150
Wire Wire Line
	1150 4150 1150 4350
Wire Wire Line
	2700 3350 2700 3550
Wire Wire Line
	2700 3550 2950 3550
Wire Wire Line
	1500 3850 2950 3850
Wire Wire Line
	1500 3750 1900 3750
Wire Wire Line
	1900 3750 1900 3100
Wire Wire Line
	1900 3100 750  3100
Wire Wire Line
	750  3100 750  4550
Wire Wire Line
	750  4550 1550 4550
Wire Wire Line
	1550 4550 1550 4000
Wire Wire Line
	1550 4000 2950 4000
Wire Wire Line
	2950 4150 2700 4150
Wire Wire Line
	2700 4150 2700 4350
Text Label 6750 850  0    60   ~ 0
V_Target
Wire Wire Line
	6450 1200 6450 850 
Wire Wire Line
	6450 850  6750 850 
Wire Wire Line
	6650 850  6650 1200
Connection ~ 6650 850 
Wire Wire Line
	6850 1000 6850 1200
Wire Wire Line
	6850 1000 6650 1000
Connection ~ 6650 1000
Wire Wire Line
	7050 1200 7050 1100
Wire Wire Line
	7050 1100 6850 1100
Connection ~ 6850 1100
Wire Wire Line
	6900 4100 6900 4550
Wire Wire Line
	7050 4300 7050 4100
Wire Wire Line
	6750 4300 7050 4300
Connection ~ 6900 4300
Wire Wire Line
	6750 4100 6750 4300
$Comp
L GND #PWR?
U 1 1 5989D24B
P 6900 4550
F 0 "#PWR?" H 6900 4300 50  0001 C CNN
F 1 "GND" H 6900 4400 50  0000 C CNN
F 2 "" H 6900 4550 50  0001 C CNN
F 3 "" H 6900 4550 50  0001 C CNN
	1    6900 4550
	1    0    0    -1  
$EndComp
Text Label 7700 2500 0    60   ~ 0
SWCLK
Text Label 7700 2800 0    60   ~ 0
SWDIO_TARGET
Text Notes 5250 1100 0    60   ~ 0
Target:
Text Notes 13050 11050 0    60   ~ 0
2017/08/08
$Comp
L PWR_FLAG #FLG?
U 1 1 5989D296
P 2050 10500
F 0 "#FLG?" H 2050 10575 50  0001 C CNN
F 1 "PWR_FLAG" H 2050 10650 50  0000 C CNN
F 2 "" H 2050 10500 50  0001 C CNN
F 3 "" H 2050 10500 50  0001 C CNN
	1    2050 10500
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG?
U 1 1 5989D297
P 2650 10500
F 0 "#FLG?" H 2650 10575 50  0001 C CNN
F 1 "PWR_FLAG" H 2650 10650 50  0000 C CNN
F 2 "" H 2650 10500 50  0001 C CNN
F 3 "" H 2650 10500 50  0001 C CNN
	1    2650 10500
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5989D298
P 2050 10500
F 0 "#PWR?" H 2050 10250 50  0001 C CNN
F 1 "GND" H 2050 10350 50  0000 C CNN
F 2 "" H 2050 10500 50  0001 C CNN
F 3 "" H 2050 10500 50  0001 C CNN
	1    2050 10500
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR?
U 1 1 5989D299
P 2650 10500
F 0 "#PWR?" H 2650 10350 50  0001 C CNN
F 1 "+5V" H 2650 10640 50  0000 C CNN
F 2 "" H 2650 10500 50  0001 C CNN
F 3 "" H 2650 10500 50  0001 C CNN
	1    2650 10500
	-1   0    0    1   
$EndComp
$Comp
L MCP1703A-3302/MB U?
U 1 1 5989E316
P 7500 6000
F 0 "U?" H 7650 5750 50  0000 C CNN
F 1 "MCP1703A-3302/MB" H 7500 6150 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT89-3_Housing" H 7550 6250 50  0001 C CNN
F 3 "" H 7500 5950 50  0001 C CNN
	1    7500 6000
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5989E4B7
P 7500 6300
F 0 "#PWR?" H 7500 6050 50  0001 C CNN
F 1 "GND" H 7500 6150 50  0000 C CNN
F 2 "" H 7500 6300 50  0001 C CNN
F 3 "" H 7500 6300 50  0001 C CNN
	1    7500 6300
	1    0    0    -1  
$EndComp
Text Label 7800 6000 0    60   ~ 0
V_Target
$Comp
L CONN_01X03_MALE J?
U 1 1 5989E64D
P 5050 5800
F 0 "J?" H 5050 6075 50  0000 C CNN
F 1 "CONN_01X03_MALE" H 5075 5525 50  0000 C CNN
F 2 "" H 5050 6000 50  0001 C CNN
F 3 "" H 5050 6000 50  0001 C CNN
	1    5050 5800
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X03_MALE J?
U 1 1 5989E680
P 1300 5700
F 0 "J?" H 1300 5975 50  0000 C CNN
F 1 "CONN_01X03_MALE" H 1325 5425 50  0000 C CNN
F 2 "" H 1300 5900 50  0001 C CNN
F 3 "" H 1300 5900 50  0001 C CNN
	1    1300 5700
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X03_MALE J?
U 1 1 5989E6CD
P 5050 6600
F 0 "J?" H 5050 6875 50  0000 C CNN
F 1 "CONN_01X03_MALE" H 5075 6325 50  0000 C CNN
F 2 "" H 5050 6800 50  0001 C CNN
F 3 "" H 5050 6800 50  0001 C CNN
	1    5050 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 6000 7200 6000
Text Label 5350 5600 0    60   ~ 0
V_Debug
$Comp
L +5V #PWR?
U 1 1 5989EB4F
P 5350 5800
F 0 "#PWR?" H 5350 5650 50  0001 C CNN
F 1 "+5V" H 5350 5940 50  0000 C CNN
F 2 "" H 5350 5800 50  0001 C CNN
F 3 "" H 5350 5800 50  0001 C CNN
	1    5350 5800
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR?
U 1 1 5989EB7E
P 1600 5700
F 0 "#PWR?" H 1600 5550 50  0001 C CNN
F 1 "+5V" H 1600 5840 50  0000 C CNN
F 2 "" H 1600 5700 50  0001 C CNN
F 3 "" H 1600 5700 50  0001 C CNN
	1    1600 5700
	1    0    0    -1  
$EndComp
Text Label 5350 6600 0    60   ~ 0
SWDIO_SWITCH
Text Label 5350 6400 0    60   ~ 0
SWDIO_Target
Text Label 5350 6800 0    60   ~ 0
SWDIO_Debug
Text Notes 2650 5700 2    60   ~ 0
These go to the pi\n
Text Notes 3200 5800 2    60   ~ 0
so it can sense where the switch is\n
Text Notes 6850 6250 2    60   ~ 0
The switch connects SWDIO and 5V to one of the two sides of these connectors\n
Text Label 1600 5500 0    60   ~ 0
V_Debug
Text Label 1600 5900 0    60   ~ 0
V_Reg_In
Text Label 6050 6000 0    60   ~ 0
V_Reg_In
$EndSCHEMATC
