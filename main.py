''' This will be the main class for the AutoFBO project and will watch for a 
carrier signal, decide whether to perform a radio check or transmit weather, 
perform the radio check, and call the weather function.
'''
import WeatherPolling

class Main:

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
        None
        #if pattern matches radio = return 1
        #if pattern matches weather = return 2
        #if pattern does not match, end and return 0

    def TransmitRadioCheck():
        None

    def TransmitWeather():
        None