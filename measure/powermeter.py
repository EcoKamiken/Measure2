import time
import random
import subprocess
import redis
from walrus import Database


class Powermeter:
    I2C_BUS: int = 1
    I2C_ADDR: int = 0x7a
    I2C_VOLT_REGISTER: int = 0x02

    def __init__(self):
        self.bus_voltage: float = 0.0

    def get_bus_voltage(self):
        """Get bus-voltage from sensors
        """
        # self.bus_voltage = subprocess.getoutput(
        #     "/usr/sbin/i2cget -y {bus} {addr} {reg}".format(bus=self.I2C_BUS, addr=self.I2C_ADDR, reg=self.I2C_VOLT_REGISTER))
        self.bus_voltage = random.random()

    def insert(self):
        """Insert data
        """
        db = Database()
        stream = db.Stream('log-stream')
        stream.add({time.time(): self.bus_voltage})
