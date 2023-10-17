import math

arc_angle = lambda r,angle: 2*math.pi*r*(angle/360)
chord_angle = lambda r,angle: r*math.sin((angle*math.pi)/2*180)

arc_min = lambda r,angle: 2*math.pi*r*(angle/(360*60))
chord_min = lambda r,angle: r*math.sin((angle*math.pi)/2*80*60)
print(arc_min(700,60))