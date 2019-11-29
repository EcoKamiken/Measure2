import time
from measure import powermeter


ob = powermeter.Powermeter()

for i in range(10):
    ob.get_bus_voltage()
    ob.insert()
    time.sleep(0.1)
