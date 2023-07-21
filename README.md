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

