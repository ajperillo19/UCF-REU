import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np
# load data
def data_loader(fname):
    import numpy as np

    data = np.loadtxt(fname)
    energy = data[:, 0]
    pdos_up = data[:, 1]  # ldos col, total contribution for a given orbital
    pdos_down = data[:,2]
    return energy, pdos_up

energy, Mo_s= data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#1(Mo)_wfc#1(s)')
_, Mo2_s = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#1(Mo)_wfc#2(s)')
_, Mo_p = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#1(Mo)_wfc#3(p)')
_, Mo_d = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#1(Mo)_wfc#4(d)')
_, S_s  = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#2(S)_wfc#1(s)')
_, S_p = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#2(S)_wfc#2(p)')
_, S2_s  = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#3(S)_wfc#1(s)')
_, S2_p  = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#3(S)_wfc#2(p)')
efermi = .486


# make plots
plt.figure()

# plot Mo contribution
plt.plot(energy -efermi, Mo_s, linewidth=2, color='black', label='Mo (s)')


plt.plot(energy -efermi, Mo2_s, linewidth=2, color='black')




plt.plot(energy -efermi, Mo_p, linewidth=2, color='red', label='Mo (p)')



plt.plot(energy -efermi, Mo_d , linewidth=2, color='blue', label='Mo (d)')



#plot S contribution
plt.plot(energy -efermi, S_s , linewidth=2, color='green', label='1S (s)')



plt.plot(energy -efermi, S2_s, linewidth=2, color='magenta', label='2S (s)')



plt.plot(energy -efermi, S_p, linewidth =2, color = 'cyan', label='1S (p)')



plt.plot(energy -efermi, S2_p, linewidth =2, color = '#ffd713', label = '2S (p)')


plt.axvline(x=0, linewidth=0.5, color='k', linestyle=(0,(8,10)))

plt.yticks()
plt.xlabel('E - E$_f$ (eV)')
plt.ylabel('PDOS (states/eV)')
plt.title('Monolayer MoS$_2$ PDOS')
plt.xlim(-4, 4)
plt.ylim(0,4 )
plt.legend(loc = 'best')
plt.savefig('MoS2_PDOS.png')
plt.show()
