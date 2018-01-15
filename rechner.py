from math import *
from random import randint
import numpy as np 

def dice():
	results = []
	result_count = {}
	durch = int(input("Anzahl der Durchgänge:"))
	for i in range(durch):
		count = 0
		for i in range(100):
			number = 0
			number = randint(1, 6)
			if number == 6:
				count += 1
		results.append(count)
	for i in range(100):
		num = results.count(i)
		result_count[i] = num
	for key, value in result_count.items():
		print(str(key) + " : " + str(value))
	results.sort()
	ave = sum(results) / durch
	print(ave)

def erw():
	lang = int(input("Geben Sie die Anzahl an Ergebnissen an: "))		#Wie viele mögliche Ergebnisse sind vorhanden?
	werte = {}
	ergebnis = []
	for i in range(lang):
		ereig = float(input("Zufallswert: "))							#Abfrage der Ergebnisse und der jeweiligen Wahrscheinlichkeit
		werte[ereig] = float(input("Wahrscheinlichkeit: "))

	for key, value in werte.items():									#Gewichtung durch Multiplikation von Ergebnis und Wahrscheinlichkeit
		erg = key * value
		ergebnis.append(erg)

	result = sum(ergebnis)												#Ergebnisse der Gewichtung zusammenrechnen												
	return werte
	print(result)

def hypGeo():
	n = int(input("Spezifizieren sie die Gesamtmenge:"))
	m = int(input("Spezifizieren Sie die Menge der Treffer:"))
	z = int(input("Spezifizieren Sie die Anzahl der Ziehungen:"))
	k = int(input("Spezifizieren Sie die gewünschte Trefferanzahl:"))
	#Aussortierung aller unmöglichen Ergebnisse
	if m > n:
		print("Error: Treffermenge ist größer als Gesamtmenge")
	elif k > z:
		print("Error: Gewünschte Trefferanzahl ist größer als die Anzahl der Ziehungen")
	elif k > m:
		print("Error: Die gewünschte Trefferzahl ist größer als Treffermenge")
	elif z > n:
		print("Error: So viele Ziehungen sind nicht möglich")
	#Formel
	else:
		ol = factorial(m) / (factorial(k) * factorial(m - k))						#Oben links in der Gleichung (M über k)
		obr = factorial(n - m) / (factorial(z - k) * factorial((n - m) - (z - k)))	#Oben Rechts in der Gleichung (N - M über n - k)
		un = factorial(n) / (factorial(z) * factorial(n - z))						#Unten in der Gleichung (N über n)
		result = (ol * obr) / un
		print(str(result * 100) + "%")
		print(result)

def pq():
	p = float(input("Geben Sie p an: "))
	q = float(input("Geben Sie q an: "))
	if (p / 2) ** 2 - q < 0:
		return "Die Formel hat keine Lösung. Damit hat der Graph keine Nullstellen!"
	else:
		root = sqrt((p / 2) ** 2 - q)
		x1 = (p / 2) + root
		x2 = (p / 2) - root

		print(x1)
		print(x2)

def bin():
	n = int(input("Geben Sie die Länge der Kette an: "))
	k = int(input("Geben Sie die gewünschte Ergebnismenge an: "))
	p = float(input("Geben Sie die Wahrscheinlichkeit für das gewünschte Ereignis an: "))
	#Unmögliche Ergebnisse aussortieren
	if k > n:
		return "Dies ist nicht möglich. k kann nicht größer sein als die Kettenlänge."
	elif p >= 1:
		return "Dies ist nicht möglich. P muss kleiner als 1 sein."
	#Formel
	else:
		q = 1 - p
		cr = factorial(n) / (factorial(k) * factorial(n - k))
		result = cr * p ** k * q ** (n - k)
		print(result)

def sqroot():
	number = float(input("Zahl: "))
	result = sqrt(number)
	print(result)

def e():
	"""Berechnet entweder e^x oder e^x von 1-10"""
	try:
		expo = float(input("Exponent: "))
	except SyntaxError:
		expo = None
	if expo is None:		
		for i in range(1, 10):
			result = e ** i
			print(str(i) + str(result))
	else: 
		res = exp(expo)
		print(res)

def abweichung():
	"""Berechnet die Standardabweichung"""
	liste = {}
	liste = erw()
	for key, value in liste.items():									#Gewichtung durch Multiplikation von Ergebnis und Wahrscheinlichkeit
		erg = key * value
		ergebnis.append(erg)
	result = sum(ergebnis)

	liste2 = []
	for key, value in liste.items():
		first = (key * result) ** 2
		gesamt = first * value
		liste2.append(gesamt)

	ergeb = sum(liste2)
	ergebnis = sqrt(ergeb)
	print(ergebnis)

def binErw():
	n = int(input("Geben Sie die Anzahl der Wiederholungen ein: "))
	p = int(input("Geben Sie die Wahrscheinlichkeit an: "))
	if p == 1:
		print(n)
	elif p > 1:
		print("p kann nicht größer als 1 sein")
	else:
		result = n * p
		print(result)

def binAbweichung():
	n = float(input("Geben Sie die Anzahl der Wiederholungen an: "))
	p = float(input("Geben Sie die Wahrscheinlichkeit an: "))
	if p > 1:
		print("p kann nicht größer als 1 sein.")
	else:
		var = n * p * (1 - p)
		result = sqrt(var)
		print(result)


def integral():
	lowerEnd = float(input("Geben Sie die untere Grenze an:"))
	upperEnd = float(input("Geben Sie die obere Grenze an:"))
	stepCount = int(input("Geben sie die Anzahl an Schritten an:"))
	integralSize = upperEnd - lowerEnd
	stepSize = integralSize / stepCount
	fValues = []
	start = lowerEnd + stepSize
	end = upperEnd - stepSize
	while start < end:
		fValues.append(2 * f(start))
		start += stepSize

	fValues.append(f(lowerEnd))
	fValues.append(f(upperEnd))
	result = ((upperEnd - lowerEnd) / (2 * stepCount)) * sum(fValues) 
	print(result)

def f(pos):
	return 1 / (1 + pos ** 2)

def veclen(vector):							#calculates the length of the vector given 
	vector = vector ** 2
	result = 0
	for i in vector:
		result += sqrt(i)
	return result

def scaleProduct():							#calculates the scalar product of the two vectors given when running
	avec = vectorCreation()
	bvec = vectorCreation()

	alen = veclen(avec)
	blen = veclen(bvec)
	result = alen * blen * angle
	return result

def vectorLength():						#takes the input for a vector and passes it to the veclen() function
	result = veclen(vectorCreation())
	return result

def crossProduct():
	veca = vectorCreation()
	vecb = vectorCreation()
	a = veca[2] * vecb[3] - veca[3] * vecb[2]
	b = veca[3] * vecb[1] - veca[1] * vecb[2]
	c = veca[1] * vecb[2] - veca[2] * vecb[1]
	return np.array( (a, b, c) )

def vectorCreation():
	print("Just use 3-dimensional vectors. To transform a 2-dimensional vector to a 3D one, just set the last coordinate to 0")
	veclist = []
	for i in range(2):
		veclist.append(float(input("Please enter coordinate number " + str(i + 1))))
	vec = np.array(veclist)
	return vec

