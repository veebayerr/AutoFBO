''' This will be the main class for the AutoFBO project and will watch for a 
carrier signal, decide whether to perform a radio check or transmit weather, 
perform the radio check, and call the weather function.
'''
import WeatherPolling
import time
import math
from time import gmtime, strftime                #import gmttime, use strftime for proper format
from math import exp, expm1
from tkinter.constants import CURRENT

class Main:
    #gap = time between groups of clicks
    #dwell = time between individual clicks
    #on = time a click lasts
    GAP_MAX = 0.5
    GAP_MIN = 0.4
    DWELL_MAX = 0.1
    DWELL_MIN = 0.05
    ON_MAX = 0.01
    ON_MIN = 0.005
    #instead of defining vals, need to pull from web interface

    def __init__(self):
    
        while(True):
            #some kind of timer limit the calls to a certain interval
            #enough time to complete
            
            weather = WeatherPolling()
        
            command = countClicks()
        
            if(command == 1):
                TransmitRadioCheck()
                '''transmit radio check'''
            elif(command == 2):
                TransmitWeather()
                '''transmit weather'''
            else:
                continue

    def countClicks():
        #if pattern matches radio = return 1
        #if pattern matches weather = return 2
        #if pattern does not match, end and return 0
        pattern = None
        while(found == False): #while a pattern hasn't been found, continue to loop
            length = carrier.SignalLength()
            if(length > ON_MIN and length < ON_MAX): #active low
                
                length = carrier.SignalLength()  
                if(length > DWELL_MIN and length < DWELL_MAX):
                     
                    length = carrier.SignalLength()
                    if (length > ON_MIN and length < ON_MAX):
                        
                        length = carrier.SignalLength()  
                        if(length > GAP_MIN and length < GAP_MAX):
                        
                            length = carrier.SignalLength()
                            if (length > ON_MIN and length < ON_MAX):
                        
                                length = carrier.SignalLength()  
                                if(length > DWELL_MIN and length < DWELL_MAX):
                                    
                                    length = carrier.SignalLength()  
                                    if(length > ON_MIN and length < ON_MAX): #active low
                
                                        length = carrier.SignalLength()  
                                        if(length > DWELL_MIN and length < DWELL_MAX):
                        
                                            length = carrier.SignalLength()  
                                            if(length > ON_MIN and length < ON_MAX): #active low
                
                                                length = carrier.SignalLength()  
                                                if(length > GAP_MIN):
                                                    found = True
                                                    pattern = 2
                                                else:
                                                    continue
                                        elif(length > GAP_MIN):
                                            found = True
                                            pattern = 1
                                        else:
                                            continue
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue         
                    else:
                        continue
                else:
                    continue          
            else:
                continue
            return pattern
            
        

    def TransmitRadioCheck():
        #Play tune
        
        #ptt & record
        
        #playback
        
        #getSignal strength
        None

    def TransmitWeather():
        #Format: XXXXX weather information, XXXX zulu, Wind XXX at XX (gust XX), Temperature XX, Dew Point XX, Altimeter XXXX, Density Altitude XXXX, Remarks…    
        
        #obtain current airport location
        loc = "Orlando Apopka"
        
        #obtain current time zulu (GMT) ALready set as current time in pi
        current_time = strftime("%H:%M", gmtime())
        #seperate numbers for playback 
        true_time = current_time[0]+ ' '+ current_time[1]+ ' '+ current_time[3] + ' ' +current_time[4]
        
        #winddirection
        find = WeatherPolling()
        windir = find.windDirection
        if(len(windir) == 1):
            true_dir = '0 ' + '0 ' + str(windir[0])
        elif(len(windir) == 2):
            true_dir = '0 ' + str(windir[0])+ ' '+ str(windir[1])
        elif(len(windir) == 3):
            true_dir = str(windir[0]) + ' ' + str(windir[1]) + ' ' + str(windir[2])
        
        #WindSpeed
        windspeed = find.windSpeed
        if(len(windspeed) == 1):
            true_speed = '0 '+ str(windspeed[0])
        elif(len(windspeed) == 2):
            true_speed = str(windspeed[0]) +' ' +str(windspeed[1])
        
        #Gust
        gust = find.gust
        if(len(gust) == 2):
            true_gust = str(gust[0]) +' ' + str(gust[1])
        else:
            true_gust = 0
            
        #Temperature 
        ctemp = find.temperature
        rank_temp = ctemp*(493.47)
        if(len(ctemp) == 1):
            true_ctemp = ctemp
        elif(len(ctemp) == 2):
            true_ctemp = str(ctemp[0]) + ' ' + str(ctemp[1])
        
        #Altimeter barometric pressure
        pressure = find.pressure
        pressure_inch = "%.2f" % (pressure*(.02953))
        if(len(pressure_inch) <=3):
            true_pressure = '0 ' + str(pressure_inch[0])+ ' '+ str(pressure_inch[2])+ ' ' + str(pressure_inch[3])
        else:
            true_pressure = str(pressure_inch[0])+ ' '+ str(pressure_inch[1])+ ' '+ str(pressure_inch[3])+ ' '+ str(pressure_inch[4])

        #Humidity
        humidity = find.humidity
        
        #Dew Point
        dewPoint = ctemp - ((100 - humidity)/5)
        if(len(dewPoint) == 1):
            true_dew = '0 '+ str(dewPoint[0])
        else:
            true_dew = str(dewPoint[0]) + ' ' + str(dewPoint[1])
        
        #Density Altitude
        pval = (7.5*dewPoint)/(237.7+ dewPoint)
        vaporP = (6.11*(10*exp(pval)))
        vTemp = (ctemp)/(1-(vaporP/pressure)*(1-0.622))
        vTemp_rank = vTemp*(493.47)
        densAlt = 145366 *( 1-(17.326*pressure_inch/vTemp_rank)*exp(.235))
        densAlt = int(round(densAlt))
        if(len(densAlt)==3):
            true_dens = '0 '+ str(densAlt[0])+ ' '+ str(densAlt[1]) + ' ' + str(densAlt[2])
        else:
            true_dens = str(densAlt[0]) +' '+ str(densAlt[1]) +' '+ str(densAlt[2]) +' '+ str(densAlt[3])
        
        #Format: XXXXX weather information, XXXX zulu, Wind XXX at XX (gust XX), Temperature XX, Dew Point XX, Altimeter XXXX, Density Altitude XXXX, Remarks…    
        if(gust == 0):
            mytext = loc + " weather information "+ true_time+ " zulu, wind "+ true_dir+" at "+ true_speed+ ", temperature " + true_ctemp+ ", Dew point "+true_dew+ ", Altimeter " + true_pressure+ ", Density Altitude "+true_dens     
        else:
            mytext = loc + " weather information "+ true_time+ " zulu, wind "+ true_dir+" at "+ true_speed+" gust "+ true_gust+ ", temperature " + true_ctemp+ ", Dew point "+true_dew+ ", Altimeter " + true_pressure+ ", Density Altitude "+true_dens
    
    def SignalLength(self):
        if(carrier.g=GetSignal() == 0): #active low
                start = time.now 
                while(carrier.GetSignal() == 0):
                    continue
                end = time.now
                timer = end-start
                return timer
        else:
            return 0
    
    def GetSignal(self):
        '''communicate with pi to get carrier detect'''
        None
        
    def converter(self):
        None
        
