#!/usr/bin/python

# backlib.py

import math

# constants

a0 = 0.5291772108E-10  # Bohr radius 
e = 1.60219E-19
m = 91,09
pi = math.pi


# inputs

rs = input('For what value of rs? ')

volume = (1.0/3)*(4*N*pi)*(Rs*a0)**3
length = volume**(1.0/3)

print '\n For ' + repr(N) + ' particles and Rs of ' + str(Rs) + ','
print 'cell must have a volume of ' + repr(volume) + ' cm^3 (' + repr(volume*(1/a0)**3) + ' A.U.)'
print 'which cooresponds to a length of ' + repr(length/1E-8) + ' A (' + repr(length/a0) + ' A.U.),' 
#print 'and a density of ' + repr(density) + ' cm^-3'
