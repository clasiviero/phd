
import galpy.potential
import galpy.orbit
import numpy as np
import matplotlib.pyplot as plt
from galpy.potential import MiyamotoNagaiPotential
from galpy.potential import plotDensities
from galpy.potential import DoubleExponentialDiskPotential
from galpy.potential import TriaxialNFWPotential
from galpy.potential import SCFPotential
from galpy.orbit import Orbit


# ----- Potentials and orbits

# Initial conditions

ic = [1.,0.1,1.1,0.1,0.3,0.] # Initial conditions [R, vR, vT, z, vz, phi]
ts= np.linspace(0.,100.,10001) # Integrate the orbit for 100 time units

print('\nMathematical Expression for the gravitational potential \n')
print(TriaxialNFWPotential.__doc__)

# Prolate NFW potential (b=1, c=1)
np1= TriaxialNFWPotential(normalize=1.,c=1.4,a=1.)
o1 = Orbit(ic); o1.integrate(ts, np1)
#o1.plot(d1='x', d2='y', label='Prolate NFW (c=1.4)')


# Spherical NFW potential (b=1, c=1)
np2 = TriaxialNFWPotential(normalize=1.,amp=1.0, a=1.0)
o2 = Orbit(ic); o2.integrate(ts, np2)
#o2.plot(d1='x', d2='y', overplot=True, label='Spherical NFW (c=1.0)')


# Triaxial NFW potential ---- NOT WORKING
np3 = TriaxialNFWPotential(amp=1.0, a=1.0, b=0.6, c=0.4)
o3 = Orbit(ic); o3.integrate(ts, np3)
#o3.plot(d1='x', d2='y', overplot=True, label='Triaxial NFW (b=0.8, c=0.6)')
#plt.legend()
#plt.savefig('XYview.pdf', bbox_inches='tight', format = 'pdf')


# SCFPotential ---- NOT WORKING
a_SCF= 50.
#sp= SCFPotential.from_density(np1.dens,80,L=40,a=a_SCF,symmetry='axisymmetry')
#o4 = Orbit(ic); o4.integrate(ts,sp)





# ----- Plots
'''
plt.close('all')
# XY view 
plt.figure(figsize=(6, 6)) 
o1.plot(d1='x', d2='y', label='Prolate NFW (c=1.4)')
o2.plot(d1='x', d2='y', overplot=True,label='Spherical NFW (c=1.0)')
#o3.plot(d1='x', d2='y', overplot=True,label='Triaxial NFW (b=0.8, c=0.6)')
#o4.plot(d1='x', d2='y', overplot=True,label='SCFPotential')
#plt.gca().set_aspect('equal')
plt.legend(loc = 'upper left')
plt.savefig('XYview.pdf', bbox_inches='tight', format='pdf')
'''

# XZ view 
plt.figure(figsize=(6, 6))
o1.plot(label='Prolate NFW (c=1.4)')
o2.plot(overplot=True,label='Spherical NFW (c=1.0)')
#o3.plot(d1='x', d2='z', overplot=True,label='Triaxial NFW (b=0.8, c=0.6)')
#o4.plot(d1='x', d2='z', overplot=True,label='SCFPotential')
#plt.gca().set_aspect('equal')
plt.legend(loc = 'upper left')
#plt.savefig('XZview.pdf', bbox_inches='tight', format='pdf')
plt.savefig('RZview.pdf', bbox_inches='tight', format='pdf')

'''
# 3D
plt.figure(figsize=(6, 6))
o1.plot3d(d1='x', d2='y', d3='z', label='Prolate NFW (c=1.4)')
o2.plot3d(d1='x', d2='y', d3='z', overplot=True,label='Spherical NFW (c=1.0)')
#o3.plot3d(d1='x', d2='y', d3='z', overplot=True,label='Triaxial NFW (b=0.8, c=0.6)')
#o4.plot(d1='x', d2='y', d3 = 'z', overplot=True,label='SCFPotential')
plt.gca().view_init(elev=30, azim=45)
plt.legend(loc = 'upper left')
plt.savefig('3D_orbits.pdf', bbox_inches='tight', format='pdf')
'''

plt.show()

#plt.close('all')



''' 
# ----- draft
#print(TriaxialNFWPotential.__dict__)  # inspecting the potential
mp= MiyamotoNagaiPotential(a=0.5,b=0.0375,normalize=1.)
# print(MiyamotoNagaiPotential.__dict__) to see everything inside of the class
print(MiyamotoNagaiPotential.__doc__) ## it shows the gravitational potential
mp.plot()
#plt.show()

dp= DoubleExponentialDiskPotential(hr=1./4.,hz=1./20.,normalize=1.)
dp.plotDensity(rmin=0.1,zmax=0.25,zmin=-0.25,nrs=101,nzs=101)
plt.show()
'''
