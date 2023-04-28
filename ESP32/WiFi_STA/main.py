import network

station = network.WLAN(network.STA_IF)

station.active(True)

station.connect("rohit", "12345678")

station.isconnected()
print(station.ifconfig())


while True:
    station.isconnected()

    # cd /media/rohit/Shared/Projects/ESP_projects/ESP_Python/WiFi_STA/