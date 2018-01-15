from rechner import *
def choose():
	"""Auswahl der Funktion"""
	print("1: Würfelversuch")
	print("2: Hypergeometrische Verteilung")
	print("3: Binomialverteilung/Bernoulli-Kette")
	print("4: pq-Formel")
	print("5: Erwartungswert")
	print("6: Standardabweichung")
	print("7: Wurzel ziehen")
	print("8: e-Funktion")
	print("9: Binom. Erwartungswert")
	print("10: Binom. Standardabweichung")
	print("11: Integralannäherung für 1+x^-2")
	print("12: Vektorlänge")
	print("13: Skalarprodukt")
	print("14: Kreuzprodukt")
	options = {1: dice,
	2: hypGeo,
	3: bin,
	4: pq,
	5: erw,
	6: abweichung,
	7: sqroot,
	8: e,
	9: binErw,
	10: binAbweichung,
	11: integral,
	12: vectorLength,
	13: scaleProduct,
	14: crossProduct}
	num = int(input("Welche Funktion soll ausgeführt werden? "))
	options[num]()


while True:

	choose()

	again = input("Wollen Sie weitermachen? [Y/N]: ")
	if again.lower() == "y":
		continue
	elif again.lower() == "n":
		quit() 
