
#2020 Ashkan Rezaee
#visit gumroad.com/ashkanism for more material
import rhinoscriptsyntax as rs
import Rhino as R


selectedLayer = []
a = []
j = 0
selectedLayer = rs.GetLayers("Select Layer")



def rgbtohsv(rgb):
    R = rgb[0]/255
    G = rgb[1]/255
    B = rgb[2]/255
    colMax = max(R,G,B)
    colMin = min(R,G,B)
    delta = colMax - colMin
    #Writing Hue
    if(delta == 0):
        hue = 0
    elif(colMax == R):
        hue = (G-B)/delta
    elif(colMax ==G):
        hue = (B-R)/delta + 2
    elif(colMax ==B):
        hue = (R-G)/delta + 4
    else:
        hue = 0
    hue = hue/6
    #Value
    value = colMax
    #Saturation
    if(value ==0):
        saturation = 0
    else:
        saturation = delta/value
    color = (hue, saturation, value )
    return color
def hsvtorgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q

a = []
b = []
c = []
numbers = len(selectedLayer)
#Convert RGB to HSV
colorA = rgbtohsv(rs.GetColor())
colorB = rgbtohsv(rs.GetColor())

#Hue
minHue = min(colorA[0],colorB[0])

if(minHue == colorA[0]):
    HueStep = (colorB[0] - colorA[0]) / numbers
    
    minSaturation = colorA[1]
    satStep = (colorB[1] - colorA[1])/ numbers
    
    minValue = colorA[2]
    valStep = (colorB[2] - colorA[2]) / numbers
    
elif(minHue == colorB[0]):
    HueStep = (colorA[0] - colorB[0]) / numbers
    
    minSaturation = colorB[1]
    satStep = (colorA[1] - colorB[1]) / numbers
    
    minValue = colorB[2]
    valStep = (colorA[2] - colorB[2]) / numbers



    
for i in selectedLayer:
    a = (minHue + j*HueStep) 
    b = (minSaturation +j*satStep)
    c = (minValue + j*valStep)
    ncolor = hsvtorgb(a,b,c)
    rs.LayerColor(i,(ncolor[0] * 255,ncolor[1]*255,ncolor[2]*255))
    j = j+1
    