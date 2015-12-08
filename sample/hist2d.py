from matplotlib.colors import LogNorm  #for log scale
#from pylab import *   #matplotlib, numpy, scipy

from matplotlib.pyplot import *   #matplotlib, numpy, scipy
#from matplotlib import *   #matplotlib, numpy, scipy
#from numpy import *   #matplotlib, numpy, scipy
#from scipy import *   #matplotlib, numpy, scipy


clf()  #clear figure
#figsize=(10,10)  #size of figure
subplot(1,1,1,aspect=1)  #keep ratio of figsize, even adding colorbar

title(r"Histogram",fontsize=20)
xlabel(r"Potential energy (kacl/mol)",fontsize=15)
ylabel(r"RMSD ($\AA$)",fontsize=15)
#hist2d(x,y,(200,200).norm=LogNorm())


# normal dist x=0 and y=5
x = np.random.randn(100000)
y = np.random.randn(100000) + 5

print x
print hist2d(x, y, bins=40, norm=LogNorm())
colorbar()

savefig("histogram.png")
savefig("histogram.eps")
#savefig("histogram.pdf")
#show()

