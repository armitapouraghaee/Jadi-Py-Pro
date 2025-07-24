import os
class Device:
    count = 0
    def __init__(self,ip,mac,name):
        self.ip = ip
        self.mac_address = mac
        self.name=name
        Device.count +=1

        self.result = os.system(f"ping -n 1 {self.ip}") == 0
        self.status = 'active' if self.result else 'unknown'
    def get_status(self):
        return self.status

class TV(Device):
    def turn_on(self):
        if self.status == 'active':
            print(f"Turning on {self.name}")
        else:
            print("Device is offline!")

class Thermo(Device):
    def get_degree(self):
        if self.status == 'active':
            return 24.5  
        return None
    
class SmartTV(TV):
    def turn_on(self):
        #turn on the smart tv from self.ip
        pass



# تست دستگاه‌ها
tv1 = TV("192.168.1.100", "00:11:22:33:44", "Living Room TV")
thermo1 = Thermo("192.168.1.101", "00:AA:BB:CC:DD", "Kitchen Thermo")

print(tv1.get_status())
tv1.turn_on()

print(thermo1.get_degree())