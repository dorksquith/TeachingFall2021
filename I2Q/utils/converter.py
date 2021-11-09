# Intro to Quantum : Joules to eV converter
# consistent units are everything!
import numpy as np

def JoulesToElectronVolts(E_joules):
	return E_joules*6.242e+18
	
E_joules = float(input("Quantity in Joules:"))

print("E : %.2e Joules -> %.2e eV"%(E_joules, JoulesToElectronVolts(E_joules)))