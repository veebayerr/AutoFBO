
import time    
import Adafruit_ADS1x15
import smbus

class testCom:
    
    
    # create an ADS1015 ADC (12-bit) instance.
    adc = Adafruit_ADS1x15.ADS1015()
    bus = smbus.SMBus(1)
    
    #Test for reading values of the pressure and temperature sensor
    def test1():
        address = 0x76                                                          #1110110
        data = bus.read_byte(address)                                           #temp+pressure
        #e_dev1= read_i2c_block_data(address,char cmd) 
        print data                
    
    def test2():
        address = 0x76

        data = ""
        for i in range(0, 5):
            data += chr(bus.read_byte(address));
        print data
    
    def test3():
        address = 0x76
        cmd = '0x00'
        data = read_byte_data(address,cmd)
        print data
        
    def test4():
        address = 0x76
        cmd = '0x00'
        data[] = read_block_data(address, cmd)
        print data
        
    time.sleep(0.5)
    