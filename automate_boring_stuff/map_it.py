# map_it.py - Launches a map in the browser using an address from 
# the command line or clipboard 

import webbrowser, sys
# import pyperclip

if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
else:
    address = '' 

print(address) 
webbrowser.open('https://www.google.com/maps/place/' + address)
