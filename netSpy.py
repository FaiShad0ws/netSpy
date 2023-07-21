#!/usr/bin/env python3

from Scanner import *
from threading import Thread
import getopt
import sys

def main(invisible = None ,visible = None, verbose = False):

      usage = ''' 
        usage: ./wifi_scanner.py  -s  
               ./wifi_scanner.py  --scan     
           
        
        Informative option:
        -h, --help                print help menu and exit
                                
        '''


      # option menu
      try:
          opts, args = getopt.getopt(sys.argv[1:], 'hs', ['help','scan'])

      except getopt.GetoptError as e:
          print(usage)
          print(str(e) + '\n')
          sys.exit(1)

      for opt, args in opts: 

          if opt in ('-h', '--help'):
                print(usage)
                sys.exit(0)

          elif opt in ('-s', '--wifi-scan'):
   
                # interface name, check/modify this using iwconfig
                interface = "wlan0mon"
                
                # start the printer thread to print all the networks info.
                t1_printer = Thread(target=display, deamon=True)
                t1_printer.start()
                
                # start the channel switcher thread to loop through channels
                t2_Switcher = Thread(target=channelSwitcher, daemon=True)
                t2_Switcher.start()
                
                # start sniffing, by calling the callback function every time a packet is sniffed
                sniff(prn=packetInfo, iface=interface) 
                # or 
                # sniff(prn=packetInfo, iface="wlan0", monitor=True)

          elif opt in ('-v', '--visible'):
                print(usage)
                sys.exit(0)

    
   
if __name__=="__main__":
    main()
