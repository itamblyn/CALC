#!/usr/bin/python
"""
Utility Script to calculate the wavenumber for a given period in picoseconds
"""

def main():

    f = float(input('\nFrequency in picoseconds^-1:   '))
    k = f/1E-12*(8.0655E+03/2.41796E+14)

    print '\nFor a frequency of '+str(f)+' ps^-1 the wavenumber is:'
    print 'k = '+str(k)+' cm^-1\n'


if __name__ == '__main__':
    main()
