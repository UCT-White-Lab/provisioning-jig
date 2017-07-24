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
LIBS:stm_jig_lib
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
U 1 1 5975A1E1
P 3500 1450
F 0 "U?" H 3250 650 60  0000 C CNN
F 1 "ST_LINK" H 3300 1950 60  0000 C CNN
F 2 "" H 3300 1950 60  0001 C CNN
F 3 "" H 3300 1950 60  0001 C CNN
	1    3500 1450
	1    0    0    -1  
$EndComp
$Comp
L ST_LINK U?
U 1 1 5975A32B
P 6500 3850
F 0 "U?" H 6250 3050 60  0000 C CNN
F 1 "ST_LINK" H 6300 4350 60  0000 C CNN
F 2 "" H 6300 4350 60  0001 C CNN
F 3 "" H 6300 4350 60  0001 C CNN
	1    6500 3850
	1    0    0    -1  
$EndComp
$Comp
L USB_B J?
U 1 1 5975A2BF
P 1150 1400
F 0 "J?" H 950 1850 50  0000 L CNN
F 1 "USB_B" H 950 1750 50  0000 L CNN
F 2 "" H 1300 1350 50  0001 C CNN
F 3 "" H 1300 1350 50  0001 C CNN
	1    1150 1400
	1    0    0    -1  
$EndComp
$Comp
L LCD-016N002L DS?
U 1 1 5975A4A1
P 9750 1300
F 0 "DS?" H 8950 1700 50  0000 C CNN
F 1 "LCD-016N002L" H 10450 1700 50  0000 C CNN
F 2 "WC1602A" H 9750 1250 50  0001 C CIN
F 3 "" H 9750 1300 50  0001 C CNN
	1    9750 1300
	1    0    0    -1  
$EndComp
$Comp
L TARGET U?
U 1 1 5975A82C
P 10150 4350
F 0 "U?" H 9300 5600 60  0000 C CNN
F 1 "TARGET" H 9550 3200 60  0000 C CNN
F 2 "STM32F051C6" H 9900 4250 60  0000 C CNN
F 3 "" H 9900 4400 60  0001 C CNN
	1    10150 4350
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5975AA9E
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
U 1 1 5975AB71
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
U 1 1 5975AC02
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
U 1 1 5975AC26
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
U 1 1 5975B752
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
U 1 1 5975B758
P 1200 3750
F 0 "J?" H 1000 4200 50  0000 L CNN
F 1 "USB_B" H 1000 4100 50  0000 L CNN
F 2 "" H 1350 3700 50  0001 C CNN
F 3 "" H 1350 3700 50  0001 C CNN
	1    1200 3750
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5975B75E
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
U 1 1 5975B771
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
U 1 1 5975BDE4
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
SWDIO
Text Label 4100 4250 0    60   ~ 0
SWDIO
Text Label 4100 4400 0    60   ~ 0
SWCLK
Text Label 2100 3850 0    60   ~ 0
USB_B_D-
Text Label 2100 4000 0    60   ~ 0
USB_B_D+
Text Label 5250 3900 0    60   ~ 0
USB_B_D-
Text Label 5250 4050 0    60   ~ 0
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
Wire Wire Line
	5900 3900 5250 3900
Wire Wire Line
	5900 4050 5250 4050
$Comp
L GND #PWR?
U 1 1 5975C5A5
P 5700 4450
F 0 "#PWR?" H 5700 4200 50  0001 C CNN
F 1 "GND" H 5700 4300 50  0000 C CNN
F 2 "" H 5700 4450 50  0001 C CNN
F 3 "" H 5700 4450 50  0001 C CNN
	1    5700 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 4200 5700 4200
Wire Wire Line
	5700 4200 5700 4450
Wire Wire Line
	5600 3600 5900 3600
Wire Wire Line
	5600 3350 5600 3600
Text Label 5600 3350 0    60   ~ 0
V_Debug
Text Notes 3550 4900 0    60   ~ 0
Two of these - one pogo pin one female header.
Text Label 9900 2500 0    60   ~ 0
V_Target
Wire Wire Line
	9600 2850 9600 2500
Wire Wire Line
	9600 2500 9900 2500
Wire Wire Line
	9800 2850 9800 2500
Connection ~ 9800 2500
Wire Wire Line
	10000 2850 10000 2650
Wire Wire Line
	10000 2650 9800 2650
Connection ~ 9800 2650
Wire Wire Line
	10200 2850 10200 2750
Wire Wire Line
	10200 2750 10000 2750
Connection ~ 10000 2750
Wire Wire Line
	10050 5750 10050 6200
Wire Wire Line
	10200 5950 10200 5750
Wire Wire Line
	9900 5950 10200 5950
Connection ~ 10050 5950
Wire Wire Line
	9900 5750 9900 5950
$Comp
L GND #PWR?
U 1 1 5975CCAC
P 10050 6200
F 0 "#PWR?" H 10050 5950 50  0001 C CNN
F 1 "GND" H 10050 6050 50  0000 C CNN
F 2 "" H 10050 6200 50  0001 C CNN
F 3 "" H 10050 6200 50  0001 C CNN
	1    10050 6200
	1    0    0    -1  
$EndComp
Text Label 10850 4150 0    60   ~ 0
SWCLK
Text Label 10850 4450 0    60   ~ 0
SWDIO
$Comp
L LED D?
U 1 1 5975D07A
P 2000 5900
F 0 "D?" H 2000 6000 50  0000 C CNN
F 1 "LED" H 2000 5800 50  0000 C CNN
F 2 "" H 2000 5900 50  0001 C CNN
F 3 "" H 2000 5900 50  0001 C CNN
	1    2000 5900
	-1   0    0    1   
$EndComp
$Comp
L LED D?
U 1 1 5975D142
P 2000 6800
F 0 "D?" H 2000 6900 50  0000 C CNN
F 1 "LED" H 2000 6700 50  0000 C CNN
F 2 "" H 2000 6800 50  0001 C CNN
F 3 "" H 2000 6800 50  0001 C CNN
	1    2000 6800
	-1   0    0    1   
$EndComp
$Comp
L LED D?
U 1 1 5975D175
P 2000 7700
F 0 "D?" H 2000 7800 50  0000 C CNN
F 1 "LED" H 2000 7600 50  0000 C CNN
F 2 "" H 2000 7700 50  0001 C CNN
F 3 "" H 2000 7700 50  0001 C CNN
	1    2000 7700
	-1   0    0    1   
$EndComp
$Comp
L R R?
U 1 1 5975D1B1
P 1150 6800
F 0 "R?" V 1230 6800 50  0000 C CNN
F 1 "220" V 1150 6800 50  0000 C CNN
F 2 "" V 1080 6800 50  0001 C CNN
F 3 "" H 1150 6800 50  0001 C CNN
	1    1150 6800
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 5975D3A9
P 1150 5900
F 0 "R?" V 1230 5900 50  0000 C CNN
F 1 "220" V 1150 5900 50  0000 C CNN
F 2 "" V 1080 5900 50  0001 C CNN
F 3 "" H 1150 5900 50  0001 C CNN
	1    1150 5900
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 5975D755
P 1150 7700
F 0 "R?" V 1230 7700 50  0000 C CNN
F 1 "220" V 1150 7700 50  0000 C CNN
F 2 "" V 1080 7700 50  0001 C CNN
F 3 "" H 1150 7700 50  0001 C CNN
	1    1150 7700
	0    1    1    0   
$EndComp
Wire Wire Line
	1300 7700 1850 7700
Wire Wire Line
	1300 6800 1850 6800
Wire Wire Line
	1300 5900 1850 5900
Wire Wire Line
	1000 5700 1000 7700
Connection ~ 1000 6800
Connection ~ 1000 5900
$Comp
L +5V #PWR?
U 1 1 5975D9B0
P 1000 5700
F 0 "#PWR?" H 1000 5550 50  0001 C CNN
F 1 "+5V" H 1000 5840 50  0000 C CNN
F 2 "" H 1000 5700 50  0001 C CNN
F 3 "" H 1000 5700 50  0001 C CNN
	1    1000 5700
	1    0    0    -1  
$EndComp
$Comp
L PN2222A Q?
U 1 1 5975DA2C
P 2250 6150
F 0 "Q?" H 2450 6225 50  0000 L CNN
F 1 "PN2222A" H 2450 6150 50  0000 L CNN
F 2 "TO_SOT_Packages_THT:TO-92_Molded_Narrow" H 2450 6075 50  0001 L CIN
F 3 "" H 2250 6150 50  0001 L CNN
	1    2250 6150
	1    0    0    -1  
$EndComp
$Comp
L PN2222A Q?
U 1 1 5975DAA9
P 2250 7950
F 0 "Q?" H 2450 8025 50  0000 L CNN
F 1 "PN2222A" H 2450 7950 50  0000 L CNN
F 2 "TO_SOT_Packages_THT:TO-92_Molded_Narrow" H 2450 7875 50  0001 L CIN
F 3 "" H 2250 7950 50  0001 L CNN
	1    2250 7950
	1    0    0    -1  
$EndComp
$Comp
L PN2222A Q?
U 1 1 5975DD76
P 2250 7050
F 0 "Q?" H 2450 7125 50  0000 L CNN
F 1 "PN2222A" H 2450 7050 50  0000 L CNN
F 2 "TO_SOT_Packages_THT:TO-92_Molded_Narrow" H 2450 6975 50  0001 L CIN
F 3 "" H 2250 7050 50  0001 L CNN
	1    2250 7050
	1    0    0    -1  
$EndComp
Wire Wire Line
	2150 5900 2350 5900
Wire Wire Line
	2350 5900 2350 5950
Wire Wire Line
	2150 6800 2350 6800
Wire Wire Line
	2150 7700 2350 7700
Wire Wire Line
	2350 7700 2350 7750
Wire Wire Line
	2350 6800 2350 6850
Text Label 1750 7050 2    60   ~ 0
LED_BUSY
Text Label 1750 6150 2    60   ~ 0
LED_FAIL
Text Label 1750 7950 2    60   ~ 0
LED_SUCCESS
$Comp
L GND #PWR?
U 1 1 5975E39F
P 2350 6350
F 0 "#PWR?" H 2350 6100 50  0001 C CNN
F 1 "GND" H 2350 6200 50  0000 C CNN
F 2 "" H 2350 6350 50  0001 C CNN
F 3 "" H 2350 6350 50  0001 C CNN
	1    2350 6350
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5975E443
P 2350 7250
F 0 "#PWR?" H 2350 7000 50  0001 C CNN
F 1 "GND" H 2350 7100 50  0000 C CNN
F 2 "" H 2350 7250 50  0001 C CNN
F 3 "" H 2350 7250 50  0001 C CNN
	1    2350 7250
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5975E69B
P 2350 8150
F 0 "#PWR?" H 2350 7900 50  0001 C CNN
F 1 "GND" H 2350 8000 50  0000 C CNN
F 2 "" H 2350 8150 50  0001 C CNN
F 3 "" H 2350 8150 50  0001 C CNN
	1    2350 8150
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 5975F7CC
P 1900 6150
F 0 "R?" V 1980 6150 50  0000 C CNN
F 1 "10K" V 1900 6150 50  0000 C CNN
F 2 "" V 1830 6150 50  0001 C CNN
F 3 "" H 1900 6150 50  0001 C CNN
	1    1900 6150
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 5975F87C
P 1900 7050
F 0 "R?" V 1980 7050 50  0000 C CNN
F 1 "10K" V 1900 7050 50  0000 C CNN
F 2 "" V 1830 7050 50  0001 C CNN
F 3 "" H 1900 7050 50  0001 C CNN
	1    1900 7050
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 5975F8F1
P 1900 7950
F 0 "R?" V 1980 7950 50  0000 C CNN
F 1 "10k" V 1900 7950 50  0000 C CNN
F 2 "" V 1830 7950 50  0001 C CNN
F 3 "" H 1900 7950 50  0001 C CNN
	1    1900 7950
	0    1    1    0   
$EndComp
Text Notes 2250 5600 2    60   ~ 0
Pi controls status LEDs
$EndSCHEMATC