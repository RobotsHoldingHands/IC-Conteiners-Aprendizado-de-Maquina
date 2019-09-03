import matplotlib.pyplot as plt
plt.rcParams.update({'font.weight' : 'bold', 'font.size': 13})
from collections import Counter
import numpy as np

def carrega_dados():
    ###################### 0epc #####################################
    for line in nn_0epc_tasks:
        id, delay, utility = line.split(" ")
        dados_nn_0epc_tasks['id'].append(int(id))
        dados_nn_0epc_tasks['delay'].append(int(delay))
        dados_nn_0epc_tasks['utility'].append(float(utility))

    for line in nn_0epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_nn_0epc_dc['clock'].append(int(clock))
        dados_nn_0epc_dc['fragmentacao'].append(float(frag))
        dados_nn_0epc_dc['fp_cpu'].append(float(fpcpu))
        dados_nn_0epc_dc['fp_ram'].append(float(fpram))
        dados_nn_0epc_dc['fp_epc'].append(float(fpepc))

    for line in rr_0epc_tasks:
        id, delay, utility = line.split(" ")
        dados_rr_0epc_tasks['id'].append(int(id))
        dados_rr_0epc_tasks['delay'].append(int(delay))
        dados_rr_0epc_tasks['utility'].append(float(utility))

    for line in rr_0epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_rr_0epc_dc['clock'].append(int(clock))
        dados_rr_0epc_dc['fragmentacao'].append(float(frag))
        dados_rr_0epc_dc['fp_cpu'].append(float(fpcpu))
        dados_rr_0epc_dc['fp_ram'].append(float(fpram))
        dados_rr_0epc_dc['fp_epc'].append(float(fpepc))

    for line in milp_0epc_tasks:
        _, id, delay, utility = line.split(" ")
        dados_milp_0epc_tasks['id'].append(int(id))
        dados_milp_0epc_tasks['delay'].append(float(delay))
        dados_milp_0epc_tasks['utility'].append(float(utility))

    for line in milp_0epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_milp_0epc_dc['clock'].append(int(float(clock)))
        dados_milp_0epc_dc['fragmentacao'].append(float(frag))
        dados_milp_0epc_dc['fp_cpu'].append(float(fpcpu))
        dados_milp_0epc_dc['fp_ram'].append(float(fpram))
        dados_milp_0epc_dc['fp_epc'].append(float(fpepc))

    ##############################################################################################
    ########################## 25 epc ############################################################
    for line in nn_25epc_tasks:
        id, delay, utility = line.split(" ")
        dados_nn_25epc_tasks['id'].append(int(id))
        dados_nn_25epc_tasks['delay'].append(int(delay))
        dados_nn_25epc_tasks['utility'].append(float(utility))

    for line in nn_25epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_nn_25epc_dc['clock'].append(int(clock))
        dados_nn_25epc_dc['fragmentacao'].append(float(frag))
        dados_nn_25epc_dc['fp_cpu'].append(float(fpcpu))
        dados_nn_25epc_dc['fp_ram'].append(float(fpram))
        dados_nn_25epc_dc['fp_epc'].append(float(fpepc))

    for line in rr_25epc_tasks:
        id, delay, utility = line.split(" ")
        dados_rr_25epc_tasks['id'].append(int(id))
        dados_rr_25epc_tasks['delay'].append(int(delay))
        dados_rr_25epc_tasks['utility'].append(float(utility))

    for line in rr_25epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_rr_25epc_dc['clock'].append(int(clock))
        dados_rr_25epc_dc['fragmentacao'].append(float(frag))
        dados_rr_25epc_dc['fp_cpu'].append(float(fpcpu))
        dados_rr_25epc_dc['fp_ram'].append(float(fpram))
        dados_rr_25epc_dc['fp_epc'].append(float(fpepc))

    for line in milp_25epc_tasks:
        _, id, delay, utility = line.split(" ")
        dados_milp_25epc_tasks['id'].append(int(id))
        dados_milp_25epc_tasks['delay'].append(float(delay))
        dados_milp_25epc_tasks['utility'].append(float(utility))

    for line in milp_25epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_milp_25epc_dc['clock'].append(int(float(clock)))
        dados_milp_25epc_dc['fragmentacao'].append(float(frag))
        dados_milp_25epc_dc['fp_cpu'].append(float(fpcpu))
        dados_milp_25epc_dc['fp_ram'].append(float(fpram))
        dados_milp_25epc_dc['fp_epc'].append(float(fpepc))
    ##############################################################################################
    ########################## 50 epc ############################################################
    for line in nn_50epc_tasks:
        id, delay, utility = line.split(" ")
        dados_nn_50epc_tasks['id'].append(int(id))
        dados_nn_50epc_tasks['delay'].append(int(delay))
        dados_nn_50epc_tasks['utility'].append(float(utility))

    for line in nn_50epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_nn_50epc_dc['clock'].append(int(clock))
        dados_nn_50epc_dc['fragmentacao'].append(float(frag))
        dados_nn_50epc_dc['fp_cpu'].append(float(fpcpu))
        dados_nn_50epc_dc['fp_ram'].append(float(fpram))
        dados_nn_50epc_dc['fp_epc'].append(float(fpepc))

    for line in rr_50epc_tasks:
        id, delay, utility = line.split(" ")
        dados_rr_50epc_tasks['id'].append(int(id))
        dados_rr_50epc_tasks['delay'].append(int(delay))
        dados_rr_50epc_tasks['utility'].append(float(utility))

    for line in rr_50epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_rr_50epc_dc['clock'].append(int(clock))
        dados_rr_50epc_dc['fragmentacao'].append(float(frag))
        dados_rr_50epc_dc['fp_cpu'].append(float(fpcpu))
        dados_rr_50epc_dc['fp_ram'].append(float(fpram))
        dados_rr_50epc_dc['fp_epc'].append(float(fpepc))

    for line in milp_50epc_tasks:
        _, id, delay, utility = line.split(" ")
        dados_milp_50epc_tasks['id'].append(int(id))
        dados_milp_50epc_tasks['delay'].append(float(delay))
        dados_milp_50epc_tasks['utility'].append(float(utility))

    for line in milp_50epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_milp_50epc_dc['clock'].append(int(float(clock)))
        dados_milp_50epc_dc['fragmentacao'].append(float(frag))
        dados_milp_50epc_dc['fp_cpu'].append(float(fpcpu))
        dados_milp_50epc_dc['fp_ram'].append(float(fpram))
        dados_milp_50epc_dc['fp_epc'].append(float(fpepc))
    ##############################################################################################
    ########################## 75 epc ############################################################
    for line in nn_75epc_tasks:
        id, delay, utility = line.split(" ")
        dados_nn_75epc_tasks['id'].append(int(id))
        dados_nn_75epc_tasks['delay'].append(int(delay))
        dados_nn_75epc_tasks['utility'].append(float(utility))

    for line in nn_75epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_nn_75epc_dc['clock'].append(int(clock))
        dados_nn_75epc_dc['fragmentacao'].append(float(frag))
        dados_nn_75epc_dc['fp_cpu'].append(float(fpcpu))
        dados_nn_75epc_dc['fp_ram'].append(float(fpram))
        dados_nn_75epc_dc['fp_epc'].append(float(fpepc))

    for line in rr_75epc_tasks:
        id, delay, utility = line.split(" ")
        dados_rr_75epc_tasks['id'].append(int(id))
        dados_rr_75epc_tasks['delay'].append(int(delay))
        dados_rr_75epc_tasks['utility'].append(float(utility))

    for line in rr_75epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_rr_75epc_dc['clock'].append(int(clock))
        dados_rr_75epc_dc['fragmentacao'].append(float(frag))
        dados_rr_75epc_dc['fp_cpu'].append(float(fpcpu))
        dados_rr_75epc_dc['fp_ram'].append(float(fpram))
        dados_rr_75epc_dc['fp_epc'].append(float(fpepc))

    for line in milp_75epc_tasks:
        _, id, delay, utility = line.split(" ")
        dados_milp_75epc_tasks['id'].append(int(id))
        dados_milp_75epc_tasks['delay'].append(float(delay))
        dados_milp_75epc_tasks['utility'].append(float(utility))

    for line in milp_75epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_milp_75epc_dc['clock'].append(int(float(clock)))
        dados_milp_75epc_dc['fragmentacao'].append(float(frag))
        dados_milp_75epc_dc['fp_cpu'].append(float(fpcpu))
        dados_milp_75epc_dc['fp_ram'].append(float(fpram))
        dados_milp_75epc_dc['fp_epc'].append(float(fpepc))
    ##############################################################################################
    ########################## 100 epc ############################################################
    for line in nn_100epc_tasks:
        id, delay, utility = line.split(" ")
        dados_nn_100epc_tasks['id'].append(int(id))
        dados_nn_100epc_tasks['delay'].append(int(delay))
        dados_nn_100epc_tasks['utility'].append(float(utility))

    for line in nn_100epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_nn_100epc_dc['clock'].append(int(clock))
        dados_nn_100epc_dc['fragmentacao'].append(float(frag))
        dados_nn_100epc_dc['fp_cpu'].append(float(fpcpu))
        dados_nn_100epc_dc['fp_ram'].append(float(fpram))
        dados_nn_100epc_dc['fp_epc'].append(float(fpepc))

    for line in rr_100epc_tasks:
        id, delay, utility = line.split(" ")
        dados_rr_100epc_tasks['id'].append(int(id))
        dados_rr_100epc_tasks['delay'].append(int(delay))
        dados_rr_100epc_tasks['utility'].append(float(utility))

    for line in rr_100epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_rr_100epc_dc['clock'].append(int(clock))
        dados_rr_100epc_dc['fragmentacao'].append(float(frag))
        dados_rr_100epc_dc['fp_cpu'].append(float(fpcpu))
        dados_rr_100epc_dc['fp_ram'].append(float(fpram))
        dados_rr_100epc_dc['fp_epc'].append(float(fpepc))

    for line in milp_100epc_tasks:
        _, id, delay, utility = line.split(" ")
        dados_milp_100epc_tasks['id'].append(int(id))
        dados_milp_100epc_tasks['delay'].append(float(delay))
        dados_milp_100epc_tasks['utility'].append(float(utility))

    for line in milp_100epc_dc:
        clock, frag, fpcpu, fpram, fpepc = line.split(" ")
        dados_milp_100epc_dc['clock'].append(int(float(clock)))
        dados_milp_100epc_dc['fragmentacao'].append(float(frag))
        dados_milp_100epc_dc['fp_cpu'].append(float(fpcpu))
        dados_milp_100epc_dc['fp_ram'].append(float(fpram))
        dados_milp_100epc_dc['fp_epc'].append(float(fpepc))
    ##############################################################################################

############ Abrindo os arquivos ############
nn_0epc_tasks = open("logs nn/tasks0epc.log", "r")
nn_0epc_dc = open("logs nn/datacenter0epc.log", "r")
nn_25epc_tasks = open("logs nn/tasks25epc.log", "r")
nn_25epc_dc = open("logs nn/datacenter25epc.log", "r")
nn_50epc_tasks = open("logs nn/tasks50epc.log", "r")
nn_50epc_dc = open("logs nn/datacenter50epc.log", "r")
nn_75epc_tasks = open("logs nn/tasks75epc.log", "r")
nn_75epc_dc = open("logs nn/datacenter75epc.log", "r")
nn_100epc_tasks = open("logs nn/tasks100epc.log", "r")
nn_100epc_dc = open("logs nn/datacenter100epc.log", "r")

rr_0epc_tasks = open("logs rr/rr_tasks0epc.log", "r")
rr_0epc_dc = open("logs rr/rr_datacenter0epc.log", "r")
rr_25epc_tasks = open("logs rr/rr_tasks25epc.log", "r")
rr_25epc_dc = open("logs rr/rr_datacenter25epc.log", "r")
rr_50epc_tasks = open("logs rr/rr_tasks50epc.log", "r")
rr_50epc_dc = open("logs rr/rr_datacenter50epc.log", "r")
rr_75epc_tasks = open("logs rr/rr_tasks75epc.log", "r")
rr_75epc_dc = open("logs rr/rr_datacenter75epc.log", "r")
rr_100epc_tasks = open("logs rr/rr_tasks100epc.log", "r")
rr_100epc_dc = open("logs rr/rr_datacenter100epc.log", "r")

milp_0epc_tasks = open("logs milp/req0.txt", "r")
milp_0epc_dc = open("logs milp/dc0.txt", "r")
milp_25epc_tasks = open("logs milp/req25.txt", "r")
milp_25epc_dc = open("logs milp/dc25.txt", "r")
milp_50epc_tasks = open("logs milp/req50.txt", "r")
milp_50epc_dc = open("logs milp/dc50.txt", "r")
milp_75epc_tasks = open("logs milp/req75.txt", "r")
milp_75epc_dc = open("logs milp/dc75.txt", "r")
milp_100epc_tasks = open("logs milp/req100.txt", "r")
milp_100epc_dc = open("logs milp/dc100.txt", "r")
#############################################

dados_nn_0epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_nn_0epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}
dados_rr_0epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_rr_0epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}
dados_milp_0epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_milp_0epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}

dados_nn_25epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_nn_25epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}
dados_rr_25epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_rr_25epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}
dados_milp_25epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_milp_25epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}

dados_nn_50epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_nn_50epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}
dados_rr_50epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_rr_50epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}
dados_milp_50epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_milp_50epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}

dados_nn_75epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_nn_75epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}
dados_rr_75epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_rr_75epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}
dados_milp_75epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_milp_75epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}

dados_nn_100epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_nn_100epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}
dados_rr_100epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_rr_100epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}
dados_milp_100epc_tasks = {'id': [], 'delay': [], 'utility': []}
dados_milp_100epc_dc = {'clock': [], 'fragmentacao': [], 'fp_cpu': [], 'fp_ram': [], 'fp_epc': []}

carrega_dados()

####################### EDITAR AQUI ##############################
classe = "100"
nn_tasks = dados_nn_100epc_tasks
nn_dc = dados_nn_100epc_dc
rr_tasks = dados_rr_100epc_tasks
rr_dc = dados_rr_100epc_dc
milp_tasks = dados_milp_100epc_tasks
milp_dc = dados_milp_100epc_dc
##################################################################

#x = dados_nn_0epc_tasks['id']
x = range(len(nn_tasks['delay']))

y_nn = [nn_tasks['delay'][i] for i in x]
y_rr = [rr_tasks['delay'][i] for i in x]
y_milp = [milp_tasks['delay'][i] for i in x]

contador_nn = sorted(Counter(y_nn).items())
contador_rr = sorted(Counter(y_rr).items())
contador_milp = sorted(Counter(y_milp).items())

x_nn = [x[0] for x in contador_nn]
y_nn = np.cumsum([x[1] for x in contador_nn])
y_nn = y_nn/max(y_nn)

x_rr = [x[0] for x in contador_rr]
y_rr = np.cumsum([x[1] for x in contador_rr])
y_rr = y_rr/max(y_rr)

x_milp = [x[0] for x in contador_milp]
y_milp = np.cumsum([x[1] for x in contador_milp])
y_milp = y_milp/max(y_milp)

x_nn = np.insert(x_nn, 0, np.min(x_nn), axis=0)
y_nn = np.insert(y_nn, 0, 0., axis=0)
x_rr = np.insert(x_rr, 0, np.min(x_nn), axis=0)
y_rr = np.insert(y_rr, 0, 0., axis=0)
x_milp = np.insert(x_milp, 0, np.min(x_nn), axis=0)
y_milp = np.insert(y_milp, 0, 0., axis=0)

plt.plot(x_nn, y_nn, c='b', label='DQN')
plt.plot(x_rr, y_rr, c='g', label='Round Robin')
plt.plot(x_milp, y_milp, c='r', label='MILP')
plt.scatter([x_nn[0], x_nn[-1]], [y_nn[0], y_nn[-1]], c='b')
plt.scatter([x_rr[0], x_rr[-1]], [y_rr[0], y_rr[-1]], c='g')
plt.scatter([x_milp[0], x_milp[-1]], [y_milp[0], y_milp[-1]], c='r')
plt.xlabel("Delay (ms)")
plt.ylabel("CDF")
plt.legend(loc='best')
#plt.ylim(0, 25)
plt.savefig(classe+' EPC/delay.jpg', dpi=200)
plt.clf()

y_nn = [nn_tasks['utility'][i] for i in x]
y_rr = [rr_tasks['utility'][i] for i in x]
y_milp = [milp_tasks['utility'][i] for i in x]

contador_nn = sorted(Counter(y_nn).items())
contador_rr = sorted(Counter(y_rr).items())
contador_milp = sorted(Counter(y_milp).items())


x_nn = [x[0] for x in contador_nn]
y_nn = np.cumsum([x[1] for x in contador_nn])
y_nn = y_nn/max(y_nn)

x_rr = [x[0] for x in contador_rr]
y_rr = np.cumsum([x[1] for x in contador_rr])
y_rr = y_rr/max(y_rr)

x_milp = [x[0] for x in contador_milp]
y_milp = np.cumsum([x[1] for x in contador_milp])
y_milp = y_milp/max(y_milp)

x_nn = np.insert(x_nn, 0, np.min(x_nn), axis=0)
y_nn = np.insert(y_nn, 0, 0., axis=0)
x_rr = np.insert(x_rr, 0, np.min(x_nn), axis=0)
y_rr = np.insert(y_rr, 0, 0., axis=0)
x_milp = np.insert(x_milp, 0, np.min(x_nn), axis=0)
y_milp = np.insert(y_milp, 0, 0., axis=0)

plt.plot(x_nn, y_nn, c='b', label='DQN')
plt.plot(x_rr, y_rr, c='g', label='Round Robin')
plt.plot(x_milp, y_milp, c='r', label='MILP')
plt.scatter([x_nn[0], x_nn[-1]], [y_nn[0], y_nn[-1]], c='b')
plt.scatter([x_rr[0], x_rr[-1]], [y_rr[0], y_rr[-1]], c='g')
plt.scatter([x_milp[0], x_milp[-1]], [y_milp[0], y_milp[-1]], c='r')
plt.xlabel("Utilidade")
plt.ylabel("CDF")
plt.legend(loc='best')
#plt.ylim(0, 25)
plt.savefig(classe+' EPC/util.jpg', dpi=200)
plt.clf()

y_nn = [nn_dc['fragmentacao'][i] for i in x]
y_rr = [rr_dc['fragmentacao'][i] for i in x]
y_milp = [milp_dc['fragmentacao'][i] for i in x]

contador_nn = sorted(Counter(y_nn).items())
contador_rr = sorted(Counter(y_rr).items())
contador_milp = sorted(Counter(y_milp).items())

x_nn = [x[0] for x in contador_nn]
y_nn = np.cumsum([x[1] for x in contador_nn])
y_nn = y_nn/max(y_nn)

x_rr = [x[0] for x in contador_rr]
y_rr = np.cumsum([x[1] for x in contador_rr])
y_rr = y_rr/max(y_rr)

x_milp = [x[0] for x in contador_milp]
y_milp = np.cumsum([x[1] for x in contador_milp])
y_milp = y_milp/max(y_milp)

x_nn = np.insert(x_nn, 0, np.min(x_nn), axis=0)
y_nn = np.insert(y_nn, 0, 0., axis=0)
x_rr = np.insert(x_rr, 0, np.min(x_nn), axis=0)
y_rr = np.insert(y_rr, 0, 0., axis=0)
x_milp = np.insert(x_milp, 0, np.min(x_nn), axis=0)
y_milp = np.insert(y_milp, 0, 0., axis=0)

plt.plot(x_nn, y_nn, c='b', label='DQN')
plt.plot(x_rr, y_rr, c='g', label='Round Robin')
plt.plot(x_milp, y_milp, c='r', label='MILP')
plt.scatter([x_nn[0], x_nn[-1]], [y_nn[0], y_nn[-1]], c='b')
plt.scatter([x_rr[0], x_rr[-1]], [y_rr[0], y_rr[-1]], c='g')
plt.scatter([x_milp[0], x_milp[-1]], [y_milp[0], y_milp[-1]], c='r')
plt.xlabel("Fragmentação")
plt.ylabel("CDF")
plt.legend(loc='best')
#plt.ylim(0, 25)
plt.savefig(classe+' EPC/frag.jpg', dpi=200)
plt.clf()



'''
y_nn = [nn_dc['fp_cpu'][i] for i in x]
y_rr = [rr_dc['fp_cpu'][i] for i in x]
y_milp = [milp_dc['fp_cpu'][i] for i in x]

plt.plot(x, y_nn, c='b', label='DQN')
plt.plot(x, y_rr, c='g', label='Round Robin')
plt.plot(x, y_milp, c='r', label='MILP')
plt.xlabel("Clock")
plt.ylabel("FP CPU")
plt.legend(loc='best')
plt.ylim(0, 1.1)
plt.savefig(classe+' EPC/fpcpu.jpg', dpi=200)
plt.clf()

y_nn = [nn_dc['fp_ram'][i] for i in x]
y_rr = [rr_dc['fp_ram'][i] for i in x]
y_milp = [milp_dc['fp_ram'][i] for i in x]

plt.plot(x, y_nn, c='b', label='DQN')
plt.plot(x, y_rr, c='g', label='Round Robin')
plt.plot(x, y_milp, c='r', label='MILP')
plt.xlabel("Clock")
plt.ylabel("FP RAM")
plt.legend(loc='best')
plt.ylim(0, 1.1)
plt.savefig(classe+' EPC/fpram.jpg', dpi=200)
plt.clf()

y_nn = [nn_dc['fp_epc'][i] for i in x]
y_rr = [rr_dc['fp_epc'][i] for i in x]
y_milp = [milp_dc['fp_epc'][i] for i in x]

plt.plot(x, y_nn, c='b', label='DQN')
plt.plot(x, y_rr, c='g', label='Round Robin')
plt.plot(x, y_milp, c='r', label='MILP')
plt.xlabel("Clock")
plt.ylabel("FP EPC")
plt.legend(loc='best')
plt.ylim(0, 1.1)
plt.savefig(classe+' EPC/fpepc.jpg', dpi=200)
plt.clf()
'''
