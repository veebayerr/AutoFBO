''' This will be the main class for the AutoFBO project and will watch for a 
carrier signal, decide whether to perform a radio check or transmit weather, 
perform the radio check, and call the weather function.
'''
import WeatherPolling

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
        None

    def TransmitWeather():
        None
        
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