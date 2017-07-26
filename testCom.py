
import time    
import Adafruit_ADS1x15
import smbus

class testCom:
    
    
                                                                                # create an ADS1015 ADC (12-bit) instance.
    adc = Adafruit_ADS1x15.ADS1015()
    bus = smbus.SMBus(1)
    def __init__(self):                                                         # tests to read data from sensors in different ways
        self.testbusbyte= test(1)
        self.testarray= test(2)
        self.testbyte= test(3)
        self.testblock= test(4)
        self.testword= test(5)
                                                                                
    def test1():
        address = 0x76                                                          # Address (1110110) = 0x76
        data = bus.read_byte(address)                                           # Temp+pressure
        #e_dev1= read_i2c_block_data(address,char cmd) 
        print data                
    
    def test2():
        address = 0x76

        data = ""
        for i in range(0, 5):
            data += chr(bus.read_byte(address))
        print data
    
    def test3():
        address = 0x76
        cmd = '0x00'
        data = read_byte_data(address,cmd)
        print data
        
    def test4():
        address = 0x76
        cmd = '0x00'
        data = read_block_data(address, cmd)
        print data
    
    def test5():
        address = 0x76
        cmd = '0x00'
        data = read_word_data(address, cmd)
        
        
    time.sleep(0.5)
    