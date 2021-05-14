import numpy as np

def Regularize(RGB):
    return RGB/255

def RGB2HSV(RGB):
    R,G,B = RGB
    Max = np.max(RGB)
    Min = np.min(RGB)
    V = Max
    Delta = Max - Min
    S = Delta/Max
    if Delta == 0:
        H=0
        return np.array([H,S,V])

    else:
        if Max == R and Min == B:
            H = 1/6*(G-B)/Delta

        elif Max == G and Min == B:
            H = 1/6*(1+(R-B)/Delta)

        elif Max == G and Min == R: 
            H = 1/6*(2+(B-R)/Delta)

        elif Max == B and Min == R:
            H = 1/6*(3+(G-R)/Delta)

        elif Max == B and Min == G:
            H = 1/6*(4+(R-G)/Delta)
            
        elif Max == B and Min == G:
            H = 1/6*(5+(B-G)/Delta)
            
    return np.array([H,S,V])


def RGB2YIQ(RGB):
    YIQTranformation = np.array([[0.299,0.587,0.114],[0.595716,-0.274453,-0.321263],[0.211456,-0.522591,0.311135]])
    RGB = RGB.reshape(-1,1)
    
    return (YIQTranformation.dot(RGB)).flatten()

def YIQ2RGB(YIQ):
    RGBTranformation = np.array([[1,0.9563,0.6210],[1,-0.2721,-0.6474],[1,-1.1070,1.7046]])
    YIQ = YIQ.reshape(-1,1)
    return np.round((RGBTranformation.dot(YIQ)).flatten(),decimals=2)

def RGB2XYZ(RGB):
    XYZTranformation = np.array([[0.5767309,0.1855540,0.1881852],[0.29273769,0.6273491,0.0752741],[0.0270343,0.0706872,0.9911085]])
    XYZ = (RGB**2.2).reshape(-1,1)
    return (XYZTranformation@XYZ).flatten()

def RGB2LAB(RGB):
    XYZ = RGB2XYZ(RGB)
    XYZn = XYZ/np.array([0.9505,1,1.0888])

    P = np.zeros_like(XYZn)
    for pi in range(0,P.__len__()):
        if XYZn[pi] > 0.008856:
            P[pi] = XYZn[pi]**(1/3)
        elif XYZn[pi] < 0.008856:
             P[pi] = 7.787*XYZn[pi] + 16/116

    LAB = np.array([116*P[1]-16,500*(P[0]-P[1]),200*(P[1]-P[2])])   
    
    return LAB


def RGB2HSI(RGB):
    R,G,B = RGB
    eps = 2.2204E-16
    num = 0.5*((R - G)+(R - B))
    den = np.sqrt((R - G)**2 + (R - B)*(G - B))
    angle = np.arccos(num/(den + eps))
    if B <=G:
        H = angle
    else:
        H = 2*pi -  angle
    
    H = H/(2*np.pi)
    num = np.min(RGB)
    den = R + G + B
    
    if den == 0:
        den = eps
        
    S = 1 - 3*num/den
    
    if S == 0:
        H = eps
    
    
    I = (R + G + B)/3
    
    return np.array([H,S,I])
    
    
def GetColors(vec):
    try:
        HSV  = RGB2HSV(vec)
        print(f"HSV: {HSV}")
    except:
        print("could not retrive HSV")
        
    try:
        YIQ  = RGB2YIQ(vec)
        print(f"YIQ: {YIQ}")
    except:
        print("could not retrive YIQ")

    try:
        XYZ = RGB2XYZ(vec)
        print(f"XYZ: {XYZ}")
    except:
        print("could not retrive XYZ")

    try:
        LAB = RGB2LAB(vec)
        print(f"LAB: {LAB}")
    except:
        print("could not retrive LAB")

    try:
        HSI = RGB2HSI(vec)
        print(f"HSI: {HSI}")
    except:
        print("could not retrive HSI")
