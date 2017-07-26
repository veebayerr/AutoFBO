import time    
import math


class dirtest:
    
    #use arctan of sin and cos sum of total angles
    #just get actual values
    averageDir = 0  
    total_sin = 0
    total_cos = 0
    angle = [1,30,40]
    
    for angle in angle:
        rad = math.radians(angle)
        total_sin += math.sin(rad)
        total_cos += math.cos(rad)
        

    len_angles = len(str(angle))
    avg_sin = total_sin/len_angles
    avg_cos = total_cos/len_angles
    arc_tan = math.degrees(math.atan(avg_sin/avg_cos))
    avg=0

    if avg_sin >0 and avg_cos > 0:
        averageDir = arc_tan
    elif avg_sin < 0 and avg_cos>0:
        averageDir = arc_tan +360
    elif avg_cos <0:
        averageDir =arc_tan +180
        
    
    print(averageDir)