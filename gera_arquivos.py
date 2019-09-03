import time
import matplotlib.pyplot as plt
from ambientev3 import *
#from ddqnv2 import *
from copy import copy
import numpy as np

startTime = time.time()

env = Env()
#agente = Agente()
#agente.model.load_weights("modeldense.h5")

i = 0

arquivo_tasks = open("tasks75epc.log", "w")
arquivo_dc = open("datacenter75epc.log", "w")
observation = env.reset()
done = False
tempos = []

"""
while not done:
    startTime = time.time()
    acao = agente.prever(observation)
    endTime = float(time.time() - startTime)
    tempos.append(endTime)
    observation, reward, done, info = env.step(acao)

    if info[0] != "no containers":
        ativos = 0.0
        for server in env.lista_servers:
            if server.ativo:
                ativos += 1.0

        if info[0] == "accepted":
            fragmentacao = ativos/len(env.lista_servers)
            fp_cpu = float(np.sum([x.bckp_cpu - x.cpu for x in env.lista_servers])/np.sum([x.bckp_cpu for x in env.lista_servers]))
            fp_ram = float(np.sum([x.bckp_ram - x.ram for x in env.lista_servers])/np.sum([x.bckp_ram for x in env.lista_servers]))
            fp_epc = float(np.sum([x.bckp_crypto - x.crypto for x in env.lista_servers])/np.sum([x.bckp_crypto for x in env.lista_servers]))
            env.temp_dc.append(str(i) + " " + str(fragmentacao) + " " + str(fp_cpu) + " " + str(fp_ram) + " " + str(fp_epc))

            i += 1

"""

rr = 0
while not done:
    acao = np.zeros(shape=(1, 60))[0]
    cpu_min = env.lista_containers[env.contIndice].cpu[0]
    ram_min = env.lista_containers[env.contIndice].ram[0]
    epc_min = env.lista_containers[env.contIndice].epc[0]
    cpu = env.lista_containers[env.contIndice].cpu[1]
    ram = env.lista_containers[env.contIndice].ram[1]
    epc = env.lista_containers[env.contIndice].epc[1]
    rr_cap = 0
    for subserver in env.lista_subservers:
        if subserver.id_server == rr:
            if subserver.vcpu > (cpu_min + cpu)/2 and subserver.vram > (ram_min + ram)/2 and subserver.vcrypto > (epc_min + epc)/2:
                break
            rr_cap += 1

    if rr_cap >= 4:
        rr_cap = 3

    acao[4*rr + rr_cap] = 1
    observation, reward, done, info = env.step(acao)

    rr += 1
    if rr >= 15:
        rr = 0

    if info[0] != "no containers":
        ativos = 0.0
        for server in env.lista_servers:
            if server.ativo:
                ativos += 1.0

        if info[0] == "accepted":
            fragmentacao = ativos/len(env.lista_servers)
            fp_cpu = float(np.sum([x.bckp_cpu - x.cpu for x in env.lista_servers])/np.sum([x.bckp_cpu for x in env.lista_servers]))
            fp_ram = float(np.sum([x.bckp_ram - x.ram for x in env.lista_servers])/np.sum([x.bckp_ram for x in env.lista_servers]))
            fp_epc = float(np.sum([x.bckp_crypto - x.crypto for x in env.lista_servers])/np.sum([x.bckp_crypto for x in env.lista_servers]))
            env.temp_dc.append(str(i) + " " + str(fragmentacao) + " " + str(fp_cpu) + " " + str(fp_ram) + " " + str(fp_epc))

arquivo_tasks.write("\n".join(env.temp_infos))
arquivo_dc.write("\n".join(env.temp_dc))
env.temp_infos = []
env.temp_dc = []

'''print(np.mean(tempos))
print(np.std(tempos))'''

arquivo_dc.close()
arquivo_tasks.close()
