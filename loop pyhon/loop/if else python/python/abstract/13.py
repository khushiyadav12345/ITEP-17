# 13. Smart Device System

# Device
# SmartDevice(Device)
# SmartTV(SmartDevice)

# Add WiFi support.

class Device:
    def powerOn(self):
        print("Device is ON")

class SmartDevice(Device):
    def wifiSupport(self):
        print("WiFi connected")

class SmartTV(SmartDevice):
    def watchTV(self):
        print("Watching Smart TV")
        

tv = SmartTV()

tv.powerOn()
tv.wifiSupport()
tv.watchTV()


# class Device:
#     def support(self):
#         print("device")

# class SmartDevice(Device):
#     def support(self):
#         print("smartdevice")

# class SmartTV(SmartDevice):
#     def support(self):
#         print("smartTV")
        
#     def wifi(self):
#         print("wifi")
        
# s = SmartTV()
# s.support()
# s.wifi()