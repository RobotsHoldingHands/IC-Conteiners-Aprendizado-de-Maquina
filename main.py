import time
import matplotlib.pyplot as plt
from ambientev3 import *
from ddqnv2 import *
from copy import copy, deepcopy

startTime = time.time()

env = Env()
agente = Agente()
tAmostra = 512
linhaScores = []
linhaRewTempo = []
linhaRewEnergia = []
linhaRewRequisicao = []
linhaTimespam = []
maior = 0
for i in range(500):
    state = env.reset()
    score = 0
    r_tempo = 0
    r_energia = 0
    r_requisicao = 0
    timespam = 0

    #start_time = time.time()
    while True:
        acao = agente.prever(state)
        observation, reward, done, info = env.step(acao)
        if info[0] != "no containers":
            if info[0] == "rejected" or info[0] == "incompatible subserver":
                timespam += 1
            agente.remember(state, acao, reward, observation, done)
            score += reward
            r_tempo += info[1]
            r_energia += info[2]
            r_requisicao += info[2]
            timespam += 1

            if done:
                print("Iteração:", i + 1, "Score:", score)
                print("Makespam:", env.makespam)
                #env.offset += env.limite
                #linhaScores.append(score)
                #linhaRewTempo.append(r_tempo)
                #linhaRewEnergia.append(r_energia)
                #linhaRewRequisicao.append(r_requisicao)
                #linhaTimespam.append(env.makespam)
                break

        state = copy(observation)

    if score > maior:
        agente.save("dense")
        maior = score
        print("Salvando modelo...")

    #elapsed_time = time.time() - start_time
    #print("Iteração levou ", elapsed_time)

    if len(agente.memory) > tAmostra:
        agente.replay(tAmostra)
        #agente.updateTargetModel()

print(("%s segundos de execução." % (time.time() - startTime)))

plt.plot(list(range(len(linhaScores))), linhaScores)
plt.xlabel('Iteração')
plt.ylabel('Reward')
plt.show()

plt.plot(list(range(len(linhaRewTempo))), linhaRewTempo)
plt.xlabel('Iteração')
plt.ylabel('Reward Tempo')
plt.show()

plt.plot(list(range(len(linhaRewEnergia))), linhaRewEnergia)
plt.xlabel('Iteração')
plt.ylabel('Reward Energia')
plt.show()

plt.plot(list(range(len(linhaRewRequisicao))), linhaRewRequisicao)
plt.xlabel('Iteração')
plt.ylabel('Reward Requisição')
plt.show()

plt.plot(list(range(len(linhaTimespam))), linhaTimespam)
plt.xlabel('Iteração')
plt.ylabel('Timespam')
plt.show()
