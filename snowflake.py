import random, time

allFlakes = []

def makeSnowflakes():
    print('creating 100,000 unique snowflakes')
    for x in range(100000):
        tempSnowflake = []
        for i in range(6):
            tempSnowflake.append(random.randint(1, 50))
        allFlakes.append(tempSnowflake)

    print('finished creating snowflakes')

    timeStart = time.time()

    print('checking for identicals')
    identifyIdentical(allFlakes)

    timeEnd = time.time()
    print(timeEnd - timeStart)
        
def identicalRight(snow1, snow2, start):
        for i in range(len(snow1)):
             if(snow1[i] != snow2[(start + i) % 6]):
                  return False
        return True

def identicalLeft(snow1, snow2, start):
    for i in range(len(snow1)):
        snow2Index = start - i
        if snow2Index < 0:
            snow2Index += 6
        if(snow1[i] != snow2[snow2Index]):
             return False
    return True

def areIdentical(snow1, snow2):        
    for x in range(6):
        if identicalRight(snow1, snow2, x):
            return True
        if identicalLeft(snow1, snow2, x):
            return True
    return False

def identifyIdentical(arr):
    for i in range(len(arr)):
        print(str(i) + '/' + str(len(arr)))

        for j in range(len(arr) - (i + 1)):
            if(areIdentical(arr[i], arr[j+i+1])):
                print(arr[i])
                print(arr[j+1+i])
                print('identical found')
                return
    print('no identicals found')

makeSnowflakes()