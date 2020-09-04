# No 1
def isPointInCircle(x,y,r,center=(0,0)):
    a = (x-center[0])**2 + (y- center[1])**2
    b = r**2
    if a == b:
        return True
    if a < b:
        return True
    else:
        return False

print(isPointInCircle(1,1,1,center=(0,0)),isPointInCircle(1,0,1,center=(0,0)),
      isPointInCircle(1,1,1,center=(1,0)),isPointInCircle(0,0,1,center=(1,1)))


# No 2
import random

def generateRandomSquarePoints(n,length,center=(0,0)):
    minx = center[0]-length/2
    miny = center[1]-length/2
    points = [[random.uniform(minx, center[0]+length/2),random.uniform(miny, center[1]+length/2)] for i in range(n)]
    
    return points
  
random.seed(0)

points = generateRandomSquarePoints(100,1)
print(points[10:15])

import matplotlib.pyplot as plt
x,y = zip(*points)

# persegi dengan panjang sisi 1 dan berpusat di (0,0)
r1 = plt.Rectangle((-0.5,-0.5),1,1,color='r', fill=False)
c1 = plt.Circle((0,0), 0.5, color='b', fill=False)
fig, ax = plt.subplots(figsize=(9,9)) 
ax.add_artist(r1)
ax.add_artist(c1)
plt.xlim(-0.6,0.6)
plt.ylim(-0.6,0.6)
plt.scatter(x,y,s=100,marker='x')
plt.show()


# No 3
def MCCircleArea(r,n=100,center=(0,0)):
    length = r*2
    count = 0

    points = generateRandomSquarePoints(n, length, center)
    for x, y in points:
        if isPointInCircle(x, y, r, center) is True:
            count += 1
        else:
            count *= 1
    
    luas_ling = count/n*(length**2)
    return(luas_ling)


random.seed(0)
print(MCCircleArea(1,100),MCCircleArea(1,10,center=(10,10)))


# No 4
def LLNPiMC(nsim,nsample):
    r = 1
    center = (0,0)
    
    test = [MCCircleArea(r, nsample, center) for i in range (nsim)]
    total = sum(test)/nsim
        
    return total
     
import math
random.seed(0)
estpi = LLNPiMC(10000,500)

print('est_pi:',estpi)
print('act_pi:',math.pi)


# No 5
def relativeError(act,est):
    
    total = ((est-act)/act)*100
    return abs(total)

print('error relatif:',relativeError(math.pi,estpi),'%')

