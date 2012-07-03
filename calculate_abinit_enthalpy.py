#! /usr/bin/python

"""
grep etotal, pressure, and ucvol. then calculate the enthalpy
output information to file
"""

import os, sys, commands

def main():

    try:
        fname = sys.argv[1]
        verbose = sys.argv[2]
    except IndexError:
        try:
            fname = sys.argv[1]
            verbose = False
        except IndexError:
            print '\nPlease provide the path to the abinit output file.\n'
            sys.exit(0)

    # Obtain data from given abinit output file
    etotal = commands.getoutput("grep etotal "+fname+" | awk '{print $2}'").split()   ### Hartree
    P = commands.getoutput("grep GPa "+fname+" | awk '{print $8}'").split()        ####### GPa
    ucvol = commands.getoutput("grep ucvol "+fname+" | awk '{print $5}'").split()     #### bohr^3

    # Convert pressure from GPa to Ha/bohr^3 for ease of calculations
    pres = [str(float(p)/29356.889) for p in P]

    if len(pres) == len(ucvol) == len(etotal):
        
        # Open output file and write header information
        out_fname = fname.rstrip('.out')+'.EPVH'
        out = open(out_fname,'w')
        out.write('# Data obatined from '+fname+'\n')
        out.write('# pres (GPa)\tucvol (bohr^3)\tetotal (Ha)\t\tenthalpy (Ha) \n')

        for i in range(len(etotal)):

            # Calculate the enthalpy
            H = str( float(etotal[i]) + float(pres[i])*float(ucvol[i]) )
            out.write(P[i]+'\t'+ucvol[i]+'\t'+etotal[i]+'\t'+H+'\n')

            if verbose:
                print etotal[i]+' + '+pres[i]+' * '+ucvol[i]+' = '+H

        out.close()
    
if __name__ == '__main__':
    main()
