#!/usr/bin/python
"""
Utility Script to calculate the wavenumber for a given period in picoseconds
"""

def main():

    k = float(input('\nWavenumber in cm^-1:   '))
    f = k*(1/1E-12*(8.0655E+03/2.41796E+14))**-1
    T = 1 / f

    print '\nFor a wavenumber of '+str(k)+' cm^-1 the period and freqency are:'
    print '\nT = '+str(T)+' ps   =   '+str(T*1000.0)+' fs'
    print 'f = '+str(f)+' ps^-1\n'


if __name__ == '__main__':
    main()
