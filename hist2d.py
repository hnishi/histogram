##### SETTING
"""Please put parameters in this section.
"""
fn_potential_rmsd = 'sample/potential_rmsd.dat' #input file name
num_bin = 40



##### IMPORT
from matplotlib.colors import LogNorm  #for log scale
#from pylab import *   #matplotlib, numpy, scipy

from matplotlib.pyplot import *   #matplotlib, numpy, scipy
#from matplotlib import *   #matplotlib, numpy, scipy
#from numpy import *   #matplotlib, numpy, scipy
#from scipy import *   #matplotlib, numpy, scipy

##### MAIN
print "hist2d v1.0"

##### READING FILE
f1 = open(fn_potential_rmsd,'r')
pot = []
rmsd = []
for line in f1:
    pot.append(line.split()[0])
    rmsd.append(line.split()[1])
f1.close()

x = np.array(pot,dtype=float)
y = np.array(rmsd,dtype=float)
#print pot
#print rmsd

clf()  #clear figure
#figsize=(10,10)  #size of figure
#subplot(1,1,1,aspect=1)  #keep ratio of figsize, even adding colorbar

title(r"Histogram",fontsize=20)
xlabel(r"Potential energy (kacl/mol)",fontsize=15)
ylabel(r"RMSD ($\AA$)",fontsize=15)
#hist2d(x,y,(200,200).norm=LogNorm())

# normal dist x=0 and y=5
#x = np.random.randn(100000) * 100
#y = np.random.randn(100000) + 5
#print x

hist2d(x, y, bins=num_bin, norm=LogNorm())
colorbar()

savefig("histogram.png")
savefig("histogram.eps")
#savefig("histogram.pdf")
#show()

