# netSpy
Scapy-based Wi-Fi scanner utility in Python that sniffs, captures, and decodes 802.11 frames to display nearby wireless networks and extra information. 


<br>

## Instructions

1. install requirements
```
pip install scapy
pip install pandas
```
3. Enable monitor mode in your network interface

```
$ airmon-ng start [interface name]
```

3. Verify your interface name

```
$ iwconfig
```

4. run the code
```
$./netSpy.py -h 
```

<br>

## Usage

```
$ ./netSpy.py -s
$ ./netSpy.py --scan
```

**Example**

```
$ ./netSpy.py --scan

#### DISPLAY NEARBY WIRELESS NETWORKS ####
___________________________________________________________________________________________________________________________
                       [SSID]                    [Strength -dBm format]  [Channel]  [Crypto]              [Supported Rates]            
[BSSID]  
0  12:34:56:78:90:ab   MyNetwork                 -50                      1          WPA/PSK | WAP2/PSK    100  
1  34:56:78:90:ab:cd   GuestNetwork123           -80                      6          WPA/PSK               100
2  56:78:90:ab:cd:ef   CorporateWirelessNetwork  -65                      6          WPA/PSK               100
3  78:90:ab:cd:ef:12   TestNetwork123            -75                      11         WPA/PSK | WAP2/PSK    100
4  90:ab:cd:ef:12:34   BNHOME                    -70                      1          WAP2/PSK              100

```

<br>

