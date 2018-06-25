#!/usr/bin/python

import commands,time

option='''

Press 1 to check Internet cable on your machine:
Press 2 to check Internet access
Press 3 to check for google access
'''

print option

choice=raw_input()

if choice == '1':
    print "plz wait...internet cable is being checked by the current OS..."
    time.sleep(3)
    cable_check=commands.getoutput('sudo mii-tool  eno1')

    if 'link ok' in cable_check:
       print "lan cable is connected"

    else:
       print "cable is not connected"
  


elif choice=='2':
    print "internet connectivity is checking in a while"


elif choice=='3':
    print "loading google web page//"


else:
    print "wrong option"

