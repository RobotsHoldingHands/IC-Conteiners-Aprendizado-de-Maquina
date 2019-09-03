import time
import matplotlib.pyplot as plt
from ambientev3 import *
from ddqnv2 import *
from copy import copy

startTime = time.time()

env = Env()
agente = Agente()
agente.model.load_weights("model.h5")

i = 0

arquivo_tasks = open("tasks.log", "w")
arquivo_dc = open("datacenter.log", "w")

observation = env.reset()
done = False

while not done:
    acao = agente.prever(observation)
    observation, reward, done, info = env.step(acao)

    if info[0] != "no containers":
        ativos = 0.0
        for server in env.lista_servers:
            if server.ativo:
                ativos += 1.0

        fragmentacao = ativos/len(env.lista_servers)
        env.temp_dc.append(str(i) + "    " + str(fragmentacao) + "    " + info[0])
        if i % 5000 == 0 and i > 0:
            arquivo_tasks.write("\n".join(env.temp_infos))
            arquivo_dc.write("\n".join(env.temp_dc))
            env.temp_infos = []
            env.temp_dc = []
            print("%d de %d concluidos." % (i, len(env.lista_containers)))

        i += 1

arquivo_tasks.write("\n".join(env.temp_infos))
arquivo_dc.write("\n".join(env.temp_dc))
env.temp_infos = []
env.temp_dc = []

arquivo_dc.close()
arquivo_tasks.close()
