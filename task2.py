import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
import MIMO


SNRdB = np.arange(-10,10,1); 
SNR = 10**(SNRdB/10); 
numBlocks = 100; 
Capacity_OPT = np.zeros(len(SNRdB));  
Capacity_EQ = np.zeros(len(SNRdB));
r = 4; 
t = 4; 



for L in range(numBlocks): 
    H = (nr.normal(0.0, 1.0,(r,t))+1j*nr.normal(0.0, 1.0,(r,t)))/np.sqrt(2)
    for kx in range(len(SNRdB)): 
        

                                                           

Capacity_OPT = Capacity_OPT/numBlocks;
Capacity_EQ = Capacity_EQ/numBlocks;


plt.plot(SNRdB,Capacity_OPT,'b-s');
plt.plot(SNRdB,Capacity_EQ,'r-.o');
plt.grid(1,which='both')
plt.legend(["OPT","Equal"], loc ="upper left");
plt.suptitle('MIMO Capacity vs SNR(dB)')
plt.xlabel('SNR (dB)')
plt.ylabel('Capacity (b/s/Hz)') 

