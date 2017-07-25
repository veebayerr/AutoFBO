'''
This class will handle all the communications with the sensors and will 
store readings into an object to be passed to the main class.
'''
from test.test_statistics import AverageMixin
import Adafruit_ADS1x15
import math
import time

class WeatherPolling:
    
    verifyGust = False                                                          #initialize global variables
    gust = False                                                                #reset to avoid unexpected behavior at reboot
    
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
        self.humidity = findHumidity()
    
    def findWindSpeed():                                                        #This function will call the anemometer and find current wind speed then
                                                                                #store the new value to an array and calculate the average
        speedList = ''                                                          #reset function variables to avoid undesirable behavior each time it's called
        currentSpeed = 0
        lastSpeed = 0
        averageSpeed = 0
    
        for i in range(0, INTERVAL):                                            #loop - iterate for period of time to collect readings
            currentSpeed = adc.read_adc(0, gain = GAIN, data_rate = 3300)
        
            lastSpeed = speedList[-1:]                                          #get last stored reading from list
            speedList.append(currentSpeed)                                      #append most recent reading to list
        
            if((currentSpeed + SPEEDTHRESHOLD > lastSpeed) and (gust = False)): #compare last and most recent speeds to check for a gust
                gust = True                                                     #if the current speed + the threshold is greater than the last speed that was 
                                                                                #recorded, then 1st gust flag is true
            elif((currentSpeed + SPEEDTHRESHOLD > lastSpeed) and (gust = True)):#compare last and most recent speeds and the 1st gust flag to verify if a gust exists
                verifyGust = True
        averageSpeed = sum(speedList)/len(speedList)                            #compute and return average speed over the interval
        return averageSpeed

    def findWindDirection():                                                    #This function will call the anemometer and compute the
                                                                                #average wind direction over the interval
        dirList = ''                                                            #reset function variables to avoid undesirable behavior
        currentDir = 0
        averageDir = 0
    
        for j in range(0, INTERVAL):                                            #loop - iterate for period of time to collect readings on direction
            currentDir = '''call anemomenter'''                                 #get current wind direction reading from the anemometer
        
            dirList.append(currentDir)                                          #append most recent reading to the list
    
        averageDir = '''LOGIC'''                                                #compute and return the average wind direction on the list over the interval
        return averageDir
        
    def findGust():                                                             #This function will check the gust booleans and return a final boolean
                                                                                #determining whether or not to report a gust
        if(verifyGust  and gust):                                               #if both the gust flags are true then report gust, else no gust
            reportGust = True
        else:
            reportGust = False
    
        return reportGust                                                       #return boolean for object to be passed to main

    def findTempPressure():                                                     #This function will call the temperature/pressure address on the temp sensor to 
                                                                                #collect the current temperature and pressure reading
        currentTemp = '''call temp'''                                           #call the sensor and store both readings
        currentPressure = '''call pres'''
    
        return [currentTemp, currentPressure]                                   #return the current temperature and pressure readings (as list)

    def findHumidity():                                                         #This function will call the humidity address on the temp sensor
                                                                                #to collect the current humidity reading
        currentHumidty = '''call humidity'''                                    #call humidity address on temp sensor for current reading
    
        return currentHumidty                                                   #return current humidity value