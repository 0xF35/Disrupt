## Disrupt - A Wifi Deauther That Supports 2.4GHZ and 5GHZ Networks

Requirements
```
sudo apt install mdk4
```
```
sudo apt install aircrack-ng
```

### How To Use

Run Program Using Sudo
```
┌──(user㉿kali)-[~/Desktop]
└─$ sudo python disrupt.py
```
Then Select Wifi Adapter You Want To Use
```
Select Adapter
[0] - wlan0
[1] - wlan1

Select Adapter : 0
```
It Gives You Wifi Networks Sorted By Signal, Both 2.4GHZ and 5GHZ
Choose Network You Want To Deauth
```
NO.    BSSID                SSID                    SIG    CHANNEL
------------------------------------------------------------------
0      A0:A2:4A:A3:AC:AB    Alpha_5G                75     157
1      BC:B2:B2:B3:BC:BA    Beta_4G                 72     2
2      CC:C3:C9:CF:C6:C0    Crispy_14               70     6
3      DC:D3:D9:DF:D6:D1    Dolphin_01              42     36
4      EC:E3:E9:E9:EF:E7    Easter_4G               30     3
5      FC:F3:F9:F4:F2:F7    Fourty_Lives            29     11
6      08:08:0C:04:08:00    Home_WIFI               27     11
7      14:12:16:16:11:1F    Coffee                  25     1

Select Network : 2
```
Then The Attack Will Start On Selected Network, Press `ctrl+c` To Exit
```
BSSID : CC:C3:C9:CF:C6:C0
SSID : Crispy_14
CHANNEL : 6
SIGNAL : 70

Flooding Crispy_14 - CC:C3:C9:CF:C6:C0 with Deauth Packets
[+] Packets sent:      1 - Speed:    1 packets/sec
[+] Packets sent:     41 - Speed:   40 packets/sec
[+] Packets sent:     86 - Speed:   45 packets/sec
[+] Packets sent:    131 - Speed:   45 packets/sec
[+] Packets sent:    196 - Speed:   65 packets/sec
[+] Packets sent:    218 - Speed:   22 packets/sec
[+] Packets sent:    269 - Speed:   51 packets/sec
[+] Packets sent:    333 - Speed:   64 packets/sec
```
At Last The Program Turns Off Monitor Mode Of Adapter
```
Disabling Monitor Mode On wlan0
```
That's It.

### Disclaimer

This tool is for testing purposes only and should only be used with consent. Do not use it for illegal activities. The end user is responsible for complying with all applicable laws. I am not liable for any misuse or damage caused by this tool and software.

### IMPORTANT NOTES
- This script is designed for Linux based operating systems. Using this script in another operating system may cause errors.
- The use of two wireless cards is highly recommended to avoid errors and complications.
