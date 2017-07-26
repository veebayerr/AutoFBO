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
            
            #command = countClicks()
            com = input('Enter command:\n')
            print(com + '\n')
            
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
        print "\a"
        
        #ptt & record
        
        #playback
        
        #getSignal strength
        powerlvl = 0
        adc_str = 0
        adc_str = adc.read_adc(0,2,3300)
        sig = (adc_str/1649.00)
        if(sig<.38):
            powerlvl = 10
        elif(sig<.40):
            powerlvl = 9
        elif(sig<.42):
            powerlvl = 8
        elif(sig<.44):
            powerlvl = 7
        elif(sig<.46):
            powerlvl = 6
        elif(sig<.5):
            powerlvl = 5
        elif(sig<.62):
            powerlvl = 4
        elif(sig<.77):
            powerlvl =3
        elif(sig<.89):
            powerlvl =2
        elif(sig<.96):
            powerlvl =1
        else:
            powerlvl = 0

    def TransmitWeather(): 
        
        #obtain current airport location
        loc = "Orlando Apopka"
        
        #obtain current time zulu (GMT) ALready set as current time in pi
        current_time = strftime("%H:%M", gmtime())
        #seperate numbers for playback 
        true_time = current_time[0]+ ' '+ current_time[1]+ ' '+ current_time[3] + ' ' +current_time[4]
        
        #winddirection
        find = WeatherPolling()
        windir = find.windDirection
        windir = str(windir)

        if(len(windir) == 1):
            true_dir = '0 ' + '0 ' + windir[0]
        elif(len(windir) == 2):
            true_dir = '0 ' + windir[0]+ ' '+ windir[1]
        elif(len(windir) == 3):
            true_dir = windir[0] + ' ' + windir[1] + ' ' + windir[2]
        
        #WindSpeed
        windspeed = find.windSpeed
        windspeed = str(windspeed)
        if(len(windspeed) == 1):
            true_speed = '0 '+ windspeed[0]
        elif(len(windspeed) == 2):
            true_speed = windspeed[0] +' ' + windspeed[1]
        
        #Gust
        gust = find.gust
        gust = str(gust)
        if(len(gust) == 2):
            true_gust = gust[0] +' ' + gust[1]
        else:
            true_gust = 0
            
        #Temperature 
        ctemp = find.temperature
        rank_temp = ctemp*(493.47)
        ctemp = str(ctemp)
        if(len(ctemp) == 1):
            true_ctemp = '0 ' + ctemp[0]
        elif(len(ctemp) == 2):
            true_ctemp = ctemp[0] + ' ' + ctemp[1]
            
        #Altimeter barometric pressure
        pressure = find.pressure
        pressure_inch = "%.2f" % (pressure*(.02953))
        pressure_inch = str(pressure_inch)

        if(len(pressure_inch) <=4):
            true_pressure = '0 ' + pressure_inch[0]+ ' '+ pressure_inch[2]+ ' ' + pressure_inch[3]
        else:
            true_pressure = pressure_inch[0]+ ' '+ pressure_inch[1]+ ' '+ pressure_inch[3]+ ' '+ pressure_inch[4]

        #Humidity
        humidity = find.humidity
        
        #Dew Point
        dewPoint = int(ctemp) - ((100 - humidity)/5)
        dewPoint = str(dewPoint)
        if(len(dewPoint) == 1):
            true_dew = '0 '+ dewPoint[0]
        else:
            true_dew = dewPoint[0] + ' ' + dewPoint[1]
        
        #Density Altitude
        pval = (7.5*int(dewPoint))/(237.7+ int(dewPoint))
        vaporP = (6.11*(10*exp(pval)))
        vTemp = int(ctemp)/(1-(vaporP/pressure)*(1-0.622))
        vTemp_rank = vTemp*(493.47)
        densAlt = 145366 *( 1-(17.326*float(pressure_inch)/vTemp_rank)*exp(.235))
        densAlt = int(round(densAlt))
        densAlt = str(densAlt)

        if(len(densAlt)==3):
            true_dens = '0 '+ densAlt[0]+ ' '+ densAlt[1] + ' ' + densAlt[2]
        else:
            true_dens = densAlt[0] +' '+ densAlt[1] +' '+ densAlt[2] +' '+ densAlt[3]
            
        if(gust == 0):
            mytext = loc + " weather information, , "+ true_time+ " zulu, wind, "+ true_dir+" at, "+ true_speed+ ", temperature, " + true_ctemp+ ",, Dew point,, "+true_dew+ ",, Altimeter,, " + true_pressure+ ", Density Altitude "+true_dens     
        else:
            mytext = loc + " weather information, , "+ true_time+ " zulu, wind, "+ true_dir+" at, "+ true_speed+" ,gust, "+ str(true_gust)+ ", temperature, " + true_ctemp+ ",, Dew point,, "+true_dew+ ",, Altimeter,, " + true_pressure+ ", Density Altitude "+true_dens

    
    #def SignalLength(self):
     #   if(carrier.g=GetSignal() == 0): #active low
      #          start = time.now 
       #         while(carrier.GetSignal() == 0):
        #            continue
         #       end = time.now
          #      timer = end-start
           #     return timer
        #else:
         #   return 0
    
   # def GetSignal(self):
    #    '''communicate with pi to get carrier detect'''
     #   None
        
    #def converter(self):
     #   None
        
