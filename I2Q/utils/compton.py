# Intro to Quantum : Compton scattering solutions
# consistent units are everything!
import numpy as np

# GIVEN:
theta    = 85 # degrees (angle between incoming and outgoing photon)
lambda_i = 2.2e-11 # metres (wavelegth of incoming photon)

# KNOWN: 
hc    = 1240e-9 # eV m (planck's constant x speed of light)
mc2   = 511e3 # eV (mass of electron x speed of light squared)
m0    = 0 # (mass of photon)
c     = 3e8 # m/s (speed of light)

# numpy assumes radians, so we must convert to radians 
theta_rads = np.radians(theta) 

# part 1 : what is delta lambda between incoming and outgoing photons?

# define a little function that calculates the Compton wavelength shift from hc, mc2, and theta
def wavelengthShift(hc,mc2,theta_rads):                       
	return (hc/mc2 * (1-np.cos(theta_rads)) ) 

# actually call the function
deltaLambda = wavelengthShift(hc,mc2,theta_rads)

# print the answer
print("unformatted (safe!) deltaLambda (metres)= ",deltaLambda)
# the formatter .2e gives the answer in scientific notation with 2 decimal places
print("unformatted with .2e, deltaLambda = %.2e m "%(deltaLambda))
# BEWARE! look what happens if we try to print it as a float with 2 decimal places
print("unformatted with .2f,deltaLambda = %.2f m "%(deltaLambda))

# part 2 : what is the energy difference between incoming and outgoing photon?

# get the outgoing photon's wavelength 
lambda_f = lambda_i + deltaLambda

# define a little function that calculates the Energy from hc and wavelength
def E(hc,wavelength):
        return hc/wavelength

# call the function to get the incoming photon energy from incoming photon wavelength
E_i = E(hc,lambda_i) 

# call the function to get the outgoing photon energy from outgoing photon wavelength
E_f = E(hc,lambda_f) 

# get the difference in outgoing and incoming photon energies
deltaE = E_f - E_i

# print the answer
print("deltaE: %.2e eV"%( deltaE ))

# part 3 : what is KE of outgoing electron?
# we use cons of KE (elastic collision!): KE_i = KE_f + KE_el
KE_el = E_i - E_f 
print("KE_el: %.2e eV"%(KE_el) )

# part 4 : what is the angle phi of the outgoing electron?

# define a little function that calculates the Momentum (actually, pc = Momentum x speed of light) from KE and "rest energy", mc2

# this method calculates the momentum from KE and mc2
def Momentum(KE,mc2):
        E = KE + mc2 # total energy = KE plus rest energy
        E2 = pow(E,2) # total energy squared
        m2c4 = pow(mc2,2) # rest energy squared
        pc = np.sqrt( (E2 - m2c4) ) # rearrangement of E2 = m2c4 + p2c2
        return pc

# call the function to get the incoming photon momentum from incoming photon KE, and noting photon mass is zero
p_i = Momentum(E_i,0) 
# call the function to get the outgoing photon momentum from outgoing photon KE, and noting photon mass is zero
p_f = Momentum(E_f,0) 
# call the function to get the outgoing electron momentum from outgoing electron KE and mc2 (=511 keV/c^2)
p_el = Momentum(KE_el,mc2) # momentum of outgoing 

# we use cons of momentum:
# p_i = p_f + p_el
# the y-components of the momentum:
# 0 = p_f*sin(theta) - p_el*sin(phi)
# so sin(phi) = p_f*sin(theta)/p_e
phi = np.arcsin((p_f*np.sin(theta_rads))/p_el)
# don't forget, numpy works in rads, so convert back to degrees if we want degrees
phi_degrees = np.degrees(phi)

print("phi: %2.0f degrees"%(phi_degrees))



