import matplotlib.pyplot as plt
import numpy as np
import math
import random
def gaus(x,un,sigm):
    result = math.exp(-0.5 * math.pow((x-un) / sigm, 2)) / (sigm * math.sqrt(2*math.pi))
    return result
def getME(array):
    sum = 0
    for element in array:
        sum += element
    return sum / len(array)
def getSigma(array,mathExp):
    sum = 0
    for element in array:
        sum += math.pow(element - mathExp, 2)
    return math.sqrt(sum / len(array))
elementsNum = 10000
conPropFist = 0.5
conPropSecond = 0.5
print("Априорная вероятность для первого класса: " + str(conPropFist))
print("Априорная вероятность для второго класса: " + str(conPropSecond))
arrayControl = np.random.uniform(-100,1000,elementsNum)
arrayControl.sort()
arrayFist = np.random.uniform(-100,500,elementsNum)
arraySecond = np.random.uniform(400,1000,elementsNum)

mathExpFist = getME(arrayFist)
mathExpSecond = getME(arraySecond)

sigmaFist = getSigma(arrayFist,mathExpFist)
sigmaSecond = getSigma(arraySecond,mathExpSecond)

pFist = []
pSecond = []

for i in range(1000):
    fistEl = gaus(i, mathExpFist, sigmaFist) * conPropFist
    secondEl = gaus(i, mathExpSecond, sigmaSecond) * conPropSecond
    pFist.append(fistEl)
    pSecond.append(secondEl)

''' for element in arrayControl:
    fistEl = gaus(element,mathExpFist,sigmaFist)*conPropFist
    secondEl = gaus(element, mathExpSecond, sigmaSecond)*conPropSecond
    pFist.append(fistEl)
    pSecond.append(secondEl)
'''
propFalseAlarm = 0
propSkipDetect = 0
i = 0
while pFist[i]>pSecond[i]:
    propFalseAlarm += pSecond[i]
    i += 1
plt.axvline(x = i, c = 'm')
while i < 1000:
    propSkipDetect += pFist[i]
    i += 1

print("Вероятность ложной тревоги: " + str(propSkipDetect))
print("Вероятность пропуска обнаружения ошибки: " + str(propFalseAlarm))
print("Суммарная ошибка классификации: " + str(propFalseAlarm+propSkipDetect))
plt.plot(pFist, c = 'b')
plt.plot(pSecond, c = 'c')
plt.show()