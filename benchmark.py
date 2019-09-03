# -*- coding: utf-8 -*-

import time
import matplotlib.pyplot as plt
from ambientev3 import *
from ddqnv2 import *
from copy import copy

startTime = time.time()

env = Env()
env_rr = Env()
env.limite = 500
env_rr.limite = 500
agente = Agente()
agente.model.load_weights("model.h5")
agente.e = 0
linhaScores = []
linhaTimespam = []
linhaScores_rr = []
linhaTimespam_rr = []
for i in range(10):
	state = env.reset()
	env_rr.reset()
	score = 0
	score_rr = 0

	while True:
		acao = agente.prever(state)
		observation, reward, done, info = env.step(acao)

		if info[0] != "no containers":
			score += reward

			if done:
				print ("NN -- Iteracao:", i+1,"Score:", score)
				env.offset += env.limite
				linhaScores.append(score)
				linhaTimespam.append(env.makespam)
				break


	rr = 0
	while True:
		acao = np.zeros(shape=(1, 20))[0]
		cpu = env_rr.lista_containers[env_rr.contIndice].cpu[1]
		ram = env_rr.lista_containers[env_rr.contIndice].ram[1]
		epc = env_rr.lista_containers[env_rr.contIndice].epc[1]
		rr_cap = 0
		for subserver in env_rr.lista_subservers:
			if subserver.id_server == rr:
				if subserver.vcpu > cpu and subserver.vram > ram and subserver.vcrypto > epc:
					break
				rr_cap += 1

		acao[4*rr + rr_cap] = 1
		rr += 1
		if rr >= 5:
			rr = 0
		observation, reward, done, info = env_rr.step(acao)

		if info[0] != "no containers":
			score_rr += reward

			if done:
				print ("RR -- Iteracao:", i+1,"Score:", score_rr)
				env_rr.offset += env_rr.limite
				linhaScores_rr.append(score_rr)
				linhaTimespam_rr.append(env_rr.makespam)
				break
	print("Infos -- Iteracao:", i+1, "Media CPU", np.mean([x.cpu[1] for x in env.lista_containers[env.offset:env.offset + env.limite]]),
			"Media RAM", np.mean([x.ram[1] for x in env.lista_containers[env.offset:env.offset + env.limite]]),
			"Media EPC", np.mean([x.epc[1] for x in env.lista_containers[env.offset:env.offset + env.limite]]),
			"Media Duracao", np.mean([x.duration for x in env.lista_containers[env.offset:env.offset + env.limite]]))


print(("%s segundos de execução." % (time.time() - startTime)))

plt.plot(list(range(len(linhaScores))), linhaScores, c='b', label='NN')
plt.plot(list(range(len(linhaScores_rr))), linhaScores_rr, c='r', label='RR')
plt.xlabel('Iteracao')
plt.ylabel('Reward')
plt.legend(loc='upper left')
plt.show()

plt.plot(list(range(len(linhaTimespam))), linhaTimespam, c = 'b', label='NN')
plt.plot(list(range(len(linhaTimespam_rr))), linhaTimespam_rr, c = 'r', label='RR')
plt.xlabel('Iteracao')
plt.ylabel('Timespam')
plt.legend(loc='upper left')
plt.show()
