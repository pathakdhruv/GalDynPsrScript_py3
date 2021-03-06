import math
from galpy.potential import MWPotential2014
from galpy.potential import PowerSphericalPotentialwCutoff
from galpy.potential import MiyamotoNagaiPotential
from galpy.potential import NFWPotential
from galpy.util import bovy_conversion
from galpy.potential import evaluatezforces
from astropy import units
from galpy.potential import KeplerPotential
import parameters as par
from Excesspl import Rpkpcfunc



def MWBHZfo(bdeg,ldeg,dkpc):

    b = bdeg*par.degtorad
    l = ldeg*par.degtorad
    Rskpc = par.Rskpc
    Vs = par.Vs
    conversion = par.conversion
    Rpkpc = Rpkpcfunc(dkpc,b,l,Rskpc)
    zkpc = dkpc*math.sin(b)
    '''
    bp= PowerSphericalPotentialwCutoff(alpha=1.8,rc=1.9/8.,normalize=0.05)
    mp= MiyamotoNagaiPotential(a=3./8.,b=0.28/8.,normalize=.6)
    np= NFWPotential(a=16./8.,normalize=.35)
    kp = KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(par.Vs,par.Rskpc))
    MWBH = [bp,mp,np,kp]
    zf1 = evaluatezforces(MWBH, Rpkpc/Rskpc,zkpc/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)
    '''
    MWPotential2014wBH= [MWPotential2014,KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(par.Vs,par.Rskpc))]
    zf1 = evaluatezforces(MWPotential2014wBH, Rpkpc/Rskpc,zkpc/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)

    Excz = zf1*conversion*math.sin(b)#s-1

    return Excz;
