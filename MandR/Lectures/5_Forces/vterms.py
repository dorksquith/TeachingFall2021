# How to solve a problem properly, using python

import numpy as np


g = 9.81 # m/s^2
rho = 1.225 # kg/m^3
C_D = 0.5

def diameter_to_area(d):
	return np.pi*pow((d/2),2)

def vterm( m, A ):
	return np.sqrt( (2 * m * g) / (rho * A * C_D) )

def dens( d, m ):
	r = d/2
	V = (4/3)*np.pi*pow(r,3)
	return m/V

m_m = 2e-3 # kg
d_m = 1.42e-2 # m
A_m = diameter_to_area(d_m)
vterm_m = vterm(m_m,A_m)
rho_m = dens( d_m, m_m )


m_fr = 12.5e-3 # kg
d_fr = 3.2e-2 # m
A_fr = diameter_to_area(d_fr)
vterm_fr = vterm(m_fr,A_fr)
rho_fr = dens( d_fr, m_fr )

m_ta = 200e-3 # kg
d_ta = 6e-2 # m
A_ta = diameter_to_area(d_ta)
vterm_ta = vterm(m_ta,A_ta)
rho_ta = dens( d_ta, m_ta )


print("Terminal Velocities:")
print("Malteser: %3.2f"%(vterm_m))
print("Ferrero Rocher: %3.2f"%(vterm_fr))
print("Toffee Apple: %3.2f"%(vterm_ta))

# print("Densities:")
# print("Malteser: %3.2f"%(rho_m))
# print("Ferrero Rocher: %3.2f"%(rho_fr))
# print("Toffee Apple: %3.2f"%(rho_ta))
