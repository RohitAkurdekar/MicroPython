'''
Name        : WiFi_AP.py
Date        : 29/Apr/2023
Brief       : Configure ESP32 as AccessPoint and host a web page using web socket.
Tested      : --
Developer   : Rohit Akurdekar
Note        :
   * WDT issue... Not solved.
   * Works fine when thonny IDE is closed. 

'''

try:
    print("Importing")
    from machine import WDT
    wdt = WDT(timeout=20000)  # enable it with a timeout of 20s
    wdt.feed()

    import socket
    import network            #importing network
    import esp                 #importing ESP
    esp.osdebug(None)
    import gc
    gc.collect()
    print("Import complete")
except:
   print("import error")
   while True:
      pass

ssid = 'ESP_AP'                  #Set your own 
password = '12345678'      #Set your own password

try:
    print("setting up as AP")
    wdt.feed()

    ap = network.WLAN(network.AP_IF)
    ap.active(True)            #activating
    ap.config(essid=ssid, password=password)

    print("AP settup complete")

except:
    print("Error in AP setup")
    while True:
       pass
while ap.active() == False:
  print(".",end=" ")
  pass
print('Connection is successful')
print(ap.ifconfig())

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Welcome to microcontrollerslab!</h1></body></html>"""
  return html
try:
    print("binding")
    wdt.feed()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
    s.bind(('', 80))
    s.listen(5)
    print("bind complete")
except:
   print("bind error")
   while True:
      pass

while True:
    try:
        print("accepting connection")
        wdt.feed()
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        print('Content = %s' % str(request))
        response = web_page()
        conn.send(response)
        conn.close()
        print("Conncection closed")
    except:
       print("Error in connection")