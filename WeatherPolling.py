'''
This class will handle all the communications with the sensors and will 
store readings into an object to be passed to the main class.
'''
import time
import math
import Adafruit_ADS1x15
from test.test_statistics import AverageMixin
import temp

adc = Adafruit_ADS1x15.ADS1015()
GAIN = 1
MAX = 1649

class WeatherPolling:
    
    verifyGust = False                                                          #initialize global variables
    gust = False                                                                #reset to avoid unexpected behavior at reboot
    gust_val = 0
    INTERVAL = 50                                                               #global to set interval to find wind speed and wind direction
    SPEEDTHRESHOLD = 10                                                         #global for speed change threshold to report gusts
    
    def __init__(self):                                                         #initialize weather object
                                                                                #calls each function to collect each reading from the sensors
        self.windSpeed = findWindSpeed()                                        #stores each reading into object to return to main function
        self.gust = findGust()                                                  #findGust compares gust and verifyGust flags to make sure gust exists and returns boolean
        self.windDirection = findWindDirection()                                #calls function to compute average wind direction over interval
        tp = findTempPressure()                                                 #temperature and pressure are read on the same I2C adr so
        self.temperature = tp[0]                                                #findTempPressure function collects both at the same time and returns a list (pair)
        self.pressure = tp[1]                                                   #with both measurements
        self.humidity = tp[2]
    
    def findWindSpeed():                                                        #This function will call the anemometer and find current wind speed then
                                                                                #store the new value to an array and calculate the average
        print 'Initializing speed test:'
        adc = Adafruit_ADS1x15.ADS1015()
        speedList = [0]*5                                                        
        currentSpeed = 0
        lastSpeed = 0
        averageSpeed = 0
        counter =0
    
        for j in range(0, 5):
            for i in range(0, 3300):
                pulse =  adc.read_adc(0,1,3300)    
                if pulse < 1000:
                    counter= counter+1
    
            speed = (counter*2.25)/5.0
            speed = speed*0.868976        
        speedList[j] = speed
        print 'Average = ', speed, "Knot\n"
        
                                                                 #reset function variables to avoid undesirable behavior each time it's called
        currentSpeed = 0
        lastSpeed = 0
        averageSpeed = 0
        SPEEDTHRESHOLD = 10
        
        for i in range(0, INTERVAL):                                            #loop - iterate for period of time to collect readings
            currentSpeed = speedList[4]
            lastSpeed = speedList[0]                                            #get last stored reading from list
        
            if((currentSpeed + SPEEDTHRESHOLD > lastSpeed) and (gust = False)): #compare last and most recent speeds to check for a gust
                gust = True                                                     #if the current speed + the threshold is greater than the last speed that was 
                                                                                #recorded, then 1st gust flag is true
            elif((currentSpeed + SPEEDTHRESHOLD > lastSpeed) and (gust = True)):#compare last and most recent speeds and the 1st gust flag to verify if a gust exists
                verifyGust = True
            
    gust_val = currentSpeed        
            
        return speed

    def findWindDirection():                                                    #This function will call the anemometer and compute the
                                                                               #average wind direction over the interval
        print 'Initializing direction test:'
        averageDir = 0
        total_sin = 0
        total_cos = 0
        i=0
        current_val = [0]*20
        angle= []
        
        while i<20:
        
            current_val[i] = adc.read_adc(1, gain=GAIN, data_rate=3300)
            #print current_val[i]
            current_val[i] = (current_val[i]/ 1649.0) *360.0
            #print(current_val[i])        
            angle.append(current_val[i])
            i= i+1
            time.sleep(1)
            
            i=0    
        for angle in angle:
            rad = math.radians(angle)
            total_sin += math.sin(rad)
            total_cos += math.cos(rad)

        len_angles = len(str(angle))
        avg_sin = total_sin/ len_angles
        avg_cos = total_cos/ len_angles
        arc_tan = math.degrees(math.atan(avg_sin/avg_cos))

        if avg_sin > 0 and avg_cos >0:
            averageDir = arc_tan
        elif avg_sin <0 and avg_cos >0:
            averageDir = arc_tan+360
        elif avg_cos <0:
            averageDir = arc_tan+180
        
        print 'Average direction = ', "%.2f" % averageDir, 'degrees\n'           
        return averageDir        

    def findGust():                                                             #This function will check the gust booleans and return a final boolean
        
                                                                                #determining whether or not to report a gust
        if(verifyGust  and gust):                                               #if both the gust flags are true then report gust, else no gust
            #reportGust = True
            return gust_val
        else:
            #reportGust = False
            return 0
        #return reportGust                                                       #return boolean for object to be passed to main

    def findTempPressure():                                                     #This function will call the temperature/pressure address on the temp sensor to 
                                                                                #collect the current temperature and pressure reading
        currentTemp, currentPres, currenthum =  temperature()                   #call the sensor and store both readings
        
    
        return [currentTemp, currentPres, currenthum]                           #return the current temperature and pressure readings (as list)

