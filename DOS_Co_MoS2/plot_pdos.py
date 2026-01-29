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
    return energy, pdos_up, pdos_down 

energy, Mo_s, Mo_s_down = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#1(Mo)_wfc#1(s)')
_, Mo2_s, Mo2_s_down = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#1(Mo)_wfc#2(s)')
_, Mo_p, Mo_p_down = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#1(Mo)_wfc#3(p)')
_, Mo_d, Mo_d_down = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#1(Mo)_wfc#4(d)')
_, S_s, S_s_down  = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#2(S)_wfc#1(s)')
_, S_p, S_p_down  = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#2(S)_wfc#2(p)')
_, S2_s, S2_s_down  = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#3(S)_wfc#1(s)')
_, S2_p, S2_p_down  = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#3(S)_wfc#2(p)')
_, Co_s, Co_s_down  = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#4(Co)_wfc#1(s)')
_, Co_p, Co_p_down  = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#4(Co)_wfc#2(p)')
_, Co_d, Co_d_down  = data_loader('/home/antonio/PROJ_MetalTMD/antonio/DOS_Co_MoS2/pdos.dat.pdos_atm#4(Co)_wfc#3(d)')


efermi = .004 


# make plots
plt.figure()

# plot Mo contribution
plt.plot(energy -efermi, Mo_s, linewidth=2, color='black', label='Mo (s)')
plt.plot(energy -efermi, Mo_s_down*-1, ls='--', linewidth=2, color='black')

plt.plot(energy -efermi, Mo2_s, linewidth=2, color='black')
plt.plot(energy -efermi, Mo2_s_down*-1,ls='--',  linewidth=2, color='black')



plt.plot(energy -efermi, Mo_p, linewidth=2, color='red', label='Mo (p)')
plt.plot(energy -efermi, Mo_p_down*-1,ls='--',  linewidth=2, color='red')


plt.plot(energy -efermi, Mo_d , linewidth=2, color='blue', label='Mo (d)')
plt.plot(energy -efermi, Mo_d_down*-1 ,ls='--',  linewidth=2, color='blue')


#plot S contribution
plt.plot(energy -efermi, S_s , linewidth=2, color='green', label='1S (s)')
plt.plot(energy -efermi, S_s_down*-1 ,ls='--',  linewidth=2, color='green')


plt.plot(energy -efermi, S2_s, linewidth=2, color='magenta', label='2S (s)')
plt.plot(energy -efermi, S2_s_down*-1 ,ls='--',  linewidth=2, color='magenta')


plt.plot(energy -efermi, S_p, linewidth =2, color = 'cyan', label='1S (p)')
plt.plot(energy -efermi, S_p_down*-1,ls='--',  linewidth =2, color = 'cyan')


plt.plot(energy -efermi, S2_p, linewidth =2, color = '#ffd713', label = '2S (p)')
plt.plot(energy -efermi, S2_p_down*-1, ls='--', linewidth =2, color = '#ffd713')

#plot Co contribution
plt.plot(energy -efermi, Co_s, linewidth =2, color = '#691500', label='Co (s)')
plt.plot(energy -efermi, Co_s_down*-1, ls='--', linewidth =2, color = '#691500')



plt.plot(energy -efermi, Co_p, linewidth =2, color = '#69e600', label='Co (p)')
plt.plot(energy -efermi, Co_p_down*-1, ls='--', linewidth =2, color = '#69e600')


plt.plot(energy -efermi, Co_d, linewidth =2, color = '#697f9c', label='Co (d)')
plt.plot(energy -efermi, Co_d_down*-1, ls='--', linewidth =2, color = '#697f9c')


plt.yticks()
plt.xlabel('E - E$_f$ (eV)')
plt.ylabel('PDOS (states/eV)')
plt.title('Co hcp Adsorbed on Monolayer MoS$_2$ PDOS')
plt.xlim(-4, 4)
plt.ylim(-5,5 )
plt.legend(loc = 'best')
plt.savefig('hcp_PDOS.png')
plt.show()
