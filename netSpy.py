from scapy.all import Dot11Beacon, Dot11, Dot11Elt, sniff
from threading import Thread
import pandas as pd
import time
import os


# interface name, change this based on iwconfig result 
interface = "wlan0mon"
    
# initialize the network dataframe to display the nerbay network information in table format 
networks = pd.DataFrame(columns=["[BSSID]", "[SSID]", "[Strength -dBm format]", "[Channel]", "[Crypto]", "[Supported Rates]"])

# set the table index as the MAC address of the AP (BSSID)
networks.set_index("[BSSID]", inplace=True)


# the callback function to be passed to the sniff function 
def packetInfo(packet):
    if packet.haslayer(Dot11Beacon):

        # extract the MAC address of the network
        bssid = packet[Dot11].addr2
        
        # get the name of the access point  
        ssid = packet[Dot11Elt].info.decode()

        # get the strength of the access point in dBm
        try:
            signalStrength  = packet.dBm_AntSignal
        except:
            signalStrength  = "N/A"

        # extract network stats to get channel, crypto and rate information 
        stats = packet[Dot11Beacon].network_stats()

        # get the channel of the access point  
        channel = stats.get("channel")

        # get the encryption method of the access point  
        crypto = stats.get("crypto")

        # get Supported rates of the access point  
        rates = stats.get("rates")

        # assign extracted network information to rows and columns 
        networks.loc[bssid] = (ssid, signalStrength , channel, crypto, rates)


# Thread 01 
def display():
    while True:
        os.system("clear")
        print ("#### DISPLAY NEARBY WIRELESS NETWORKS ####")
        print ("____________________________________________________________________")
        print(networks)
        time.sleep(0.5)


# Thread 02
def channelSwitcher():

    channel = 1

    while True:
        # check available channels using iwconfig
        os.system(f"iwconfig {interface} channel {channel}")
        
        # switch channel from 1 to 14 each 0.5s
        channel = channel % 14 + 1
        time.sleep(0.5)


