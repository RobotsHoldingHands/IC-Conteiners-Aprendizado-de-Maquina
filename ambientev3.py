import json, re, random, time
import numpy as np
from copy import copy, deepcopy

#Classe servidor mestre
class Server():
    def __init__(self, id, n_vcpu, n_vram, n_crypto):
        self.id = id
        self.cpu = n_vcpu
        self.bckp_cpu = n_vcpu
        self.ram = n_vram
        self.bckp_ram = n_vram
        self.crypto = n_crypto
        self.bckp_crypto = n_crypto
        self.ativo = False
        self.nTasksAtivas = 0

#Classe de subservidor, servidor dividido
class SubServer():
    def __init__(self, id_server, cpu, ram, crypto):
        self.id_server = id_server
        self.vcpu = cpu
        self.vram = ram
        self.vcrypto = crypto

    def possui_carga(self, lista_servers, cpu, ram, epc):
        return (cpu <= lista_servers[self.id_server].cpu and
                ram <= lista_servers[self.id_server].ram and
                epc <= lista_servers[self.id_server].crypto)

class Container():
    def __init__(self, id, subtime, duration, cpu, ram, epc):
        self.id = id
        self.subtime = subtime
        self.duration = duration
        self.cpu = cpu
        self.ram = ram
        self.epc = epc
        self.id_server = "NaN"
        self.actual_cpu = "NaN"
        self.actual_ram = "NaN"
        self.actual_epc = "NaN"
        self.delay = 0

class Env():
    def __init__(self):
        # Criando lista de servers
        self.lista_servers = [
            Server(0, 8, 64, 0),
            Server(1, 8, 64, 0),
            Server(2, 8, 64, 0),
            Server(3, 8, 8, 93.5),
            Server(4, 8, 8, 93.5),
            Server(5, 8, 64, 0),
            Server(6, 8, 64, 0),
            Server(7, 8, 64, 0),
            Server(8, 8, 8, 93.5),
            Server(9, 8, 8, 93.5),
            Server(10, 8, 64, 0),
            Server(11, 8, 64, 0),
            Server(12, 8, 64, 0),
            Server(13, 8, 8, 93.5),
            Server(14, 8, 8, 93.5)
        ]

        self.lista_subservers = [
            # Sub servers do servidor 0
            SubServer(0, 2, 8, 0),
            SubServer(0, 4, 16, 0),
            SubServer(0, 6, 32, 0),
            SubServer(0, 8, 64, 0),
            # Sub servers do servidor 1
            SubServer(1, 2, 8, 0),
            SubServer(1, 4, 16, 0),
            SubServer(1, 6, 32, 0),
            SubServer(1, 8, 64, 0),
            # Sub servers do servidor 2
            SubServer(2, 2, 8, 0),
            SubServer(2, 4, 16, 0),
            SubServer(2, 6, 32, 0),
            SubServer(2, 8, 64, 0),
            # Sub servers do servidor 3
            SubServer(3, 2, 1, 16),
            SubServer(3, 4, 2, 32),
            SubServer(3, 6, 4, 64),
            SubServer(3, 8, 8, 93.5),
            # Sub servers do servidor 4
            SubServer(4, 2, 1, 16),
            SubServer(4, 4, 2, 32),
            SubServer(4, 6, 4, 64),
            SubServer(4, 8, 8, 93.5),
            # Sub servers do servidor 0
            SubServer(5, 2, 8, 0),
            SubServer(5, 4, 16, 0),
            SubServer(5, 6, 32, 0),
            SubServer(5, 8, 64, 0),
            # Sub servers do servidor 1
            SubServer(6, 2, 8, 0),
            SubServer(6, 4, 16, 0),
            SubServer(6, 6, 32, 0),
            SubServer(6, 8, 64, 0),
            # Sub servers do servidor 2
            SubServer(7, 2, 8, 0),
            SubServer(7, 4, 16, 0),
            SubServer(7, 6, 32, 0),
            SubServer(7, 8, 64, 0),
            # Sub servers do servidor 3
            SubServer(8, 2, 1, 16),
            SubServer(8, 4, 2, 32),
            SubServer(8, 6, 4, 64),
            SubServer(8, 8, 8, 93.5),
            # Sub servers do servidor 4
            SubServer(9, 2, 1, 16),
            SubServer(9, 4, 2, 32),
            SubServer(9, 6, 4, 64),
            SubServer(9, 8, 8, 93.5),
            # Sub servers do servidor 0
            SubServer(10, 2, 8, 0),
            SubServer(10, 4, 16, 0),
            SubServer(10, 6, 32, 0),
            SubServer(10, 8, 64, 0),
            # Sub servers do servidor 1
            SubServer(11, 2, 8, 0),
            SubServer(11, 4, 16, 0),
            SubServer(11, 6, 32, 0),
            SubServer(11, 8, 64, 0),
            # Sub servers do servidor 2
            SubServer(12, 2, 8, 0),
            SubServer(12, 4, 16, 0),
            SubServer(12, 6, 32, 0),
            SubServer(12, 8, 64, 0),
            # Sub servers do servidor 3
            SubServer(13, 2, 1, 16),
            SubServer(13, 4, 2, 32),
            SubServer(13, 6, 4, 64),
            SubServer(13, 8, 8, 93.5),
            # Sub servers do servidor 4
            SubServer(14, 2, 1, 16),
            SubServer(14, 4, 2, 32),
            SubServer(14, 6, 4, 64),
            SubServer(14, 8, 8, 93.5)
        ]

        self.offset = 0
        self.limite = 100
        self.lista_containers = []
        i = 0
        with open("data-75.json", "r") as arq_json:
            data = json.load(arq_json)
            data = data['tasks']
            min_time = min([int(x['submission']) for x in data])
            for task in data:
                self.lista_containers.append(Container(task['id'], int(task['submission'] - min_time), task['duration'],
                                                [task['containers'][0]['vcpu_min'], task['containers'][0]['vcpu_max']],
                                                [task['containers'][0]['ram_min'],  task['containers'][0]['ram_max']],
                                                [task['containers'][0]['epc_min'], task['containers'][0]['epc_max']]))
                i += 1


        self.lista_containers_backup = deepcopy(self.lista_containers)


        self.temp_infos = []
        self.temp_dc = []

    def reset(self):
        self.lista_containers = deepcopy(self.lista_containers_backup)

        # Criando lista de servers
        self.lista_servers = [
            Server(0, 8, 64, 0),
            Server(1, 8, 64, 0),
            Server(2, 8, 64, 0),
            Server(3, 8, 8, 93.5),
            Server(4, 8, 8, 93.5),
            Server(5, 8, 64, 0),
            Server(6, 8, 64, 0),
            Server(7, 8, 64, 0),
            Server(8, 8, 8, 93.5),
            Server(9, 8, 8, 93.5),
            Server(10, 8, 64, 0),
            Server(11, 8, 64, 0),
            Server(12, 8, 64, 0),
            Server(13, 8, 8, 93.5),
            Server(14, 8, 8, 93.5)
        ]
        self.contIndice = 0

        # Inicializa a contagem de eventos
        self.evento = 0
        self.eventopassado = 0



        self.makespam = 0
        for contain in self.lista_containers:
            self.makespam += contain.duration

        observation = []
        # Incluindo os status dos servidores
        #############################################################
        for server in self.lista_servers:
            cpu = float(server.cpu)
            ram = float(server.ram)
            crypto = float(server.crypto)

            if NORMALIZE:
                cpu /= MAX_CPU
                ram /= MAX_RAM
                crypto /= MAX_CRYPTO

            observation.append(cpu)
            observation.append(ram)
            observation.append(crypto)
        #############################################################

        # Incluindo informações dos containeres
        #############################################################
        mincpu = float(self.lista_containers[self.contIndice + self.offset].cpu[0])
        maxcpu = float(self.lista_containers[self.contIndice + self.offset].cpu[1])
        minram = float(self.lista_containers[self.contIndice + self.offset].ram[0])
        maxram = float(self.lista_containers[self.contIndice + self.offset].ram[1])
        mincrypto = float(self.lista_containers[self.contIndice + self.offset].epc[0])
        maxcrypto = float(self.lista_containers[self.contIndice + self.offset].epc[1])
        ttl = float(self.lista_containers[self.contIndice + self.offset].duration)

        if NORMALIZE:
            mincpu /= MAX_VCPU
            maxcpu /= MAX_VCPU
            minram /= MAX_VRAM
            maxram /= MAX_VRAM
            mincrypto /= MAX_VCRYPTO
            maxcrypto /= MAX_VCRYPTO
            ttl /= MAX_TTL

        observation.append(mincpu)
        observation.append(maxcpu)
        observation.append(minram)
        observation.append(maxram)
        observation.append(mincrypto)
        observation.append(maxcrypto)
        observation.append(ttl)
        #############################################################

        return observation

    # Metodo de iteracao, cada ciclo toma uma acao (que eh o servidor a ser alocado) e entao retorna [observacao, reward, done, info]
    def step(self, acao):
        self.passarTempo()

        ind = np.argmax(acao)
        # Recuperando as informações do subserver
        id_server = self.lista_subservers[ind].id_server
        cpu = self.lista_subservers[ind].vcpu
        ram = self.lista_subservers[ind].vram
        crypto = self.lista_subservers[ind].vcrypto
        cpu = min(cpu, self.lista_containers[self.contIndice + self.offset].cpu[1])
        ram = min(ram, self.lista_containers[self.contIndice + self.offset].ram[1])
        crypto = min(crypto, self.lista_containers[self.contIndice + self.offset].epc[1])
        #############################################
        rewardEnergia = 1.0
        rewardTempo = 1.0
        rewardRequisicao = 1.0
        info = []

        # Caso não haja nenhum container com esse submission time
        if self.lista_containers[self.contIndice + self.offset].subtime > self.evento:
            self.eventopassado = self.evento
            self.evento += 1
            info.append("no containers")
        # Caso o subserver seja incompativel
        elif cpu < self.lista_containers[self.contIndice + self.offset].cpu[0] or ram < self.lista_containers[self.contIndice + self.offset].ram[0] or crypto < self.lista_containers[self.contIndice + self.offset].epc[0]:
            #print("ID:", self.lista_containers[self.contIndice].id, " indice:", ind)
            info.append("incompatible subserver")
            #print("Estado do servidor 3:", self.lista_servers[3].cpu, self.lista_servers[3].ram, self.lista_servers[3].crypto, self.lista_servers[3].nTasksAtivas)
            #print("Estado do servidor 4:", self.lista_servers[4].cpu, self.lista_servers[4].ram, self.lista_servers[4].crypto, self.lista_servers[4].nTasksAtivas)
            '''if ind == 19 or ind == 15:
                print(self.lista_subservers[ind].id_server)
                print(self.lista_containers[self.contIndice + self.offset].cpu[0], self.lista_servers[id_server].cpu)
                print(self.lista_containers[self.contIndice + self.offset].ram[0],  self.lista_servers[id_server].ram)
                print(self.lista_containers[self.contIndice + self.offset].epc[0],  self.lista_servers[id_server].crypto)'''

            self.eventopassado = self.evento
            self.evento += 1
            self.makespam += 1
            # Posterga os containers
            tamanho_fila = 0
            subtime_post = self.lista_containers[self.contIndice + self.offset].subtime
            for i in range(len(self.lista_containers)):
                if self.lista_containers[i].subtime == subtime_post:
                    self.lista_containers[i].subtime += 1
                    self.lista_containers[i].delay += 1
                    tamanho_fila += 1

            rewardRequisicao = 0.0
            rewardTempo = 1.0/(tamanho_fila + 1) # Reward proporcional ao tamanho da fila
            rewardEnergia = 0.0
        # Caso o servidor aguente o container
        elif self.lista_subservers[ind].possui_carga(self.lista_servers[:], cpu, ram, crypto):
            # Reduzindo da capacidade do server cpu, ram e crypto do subserver escolhido
            self.lista_servers[id_server].cpu -= cpu
            self.lista_servers[id_server].ram -= ram
            self.lista_servers[id_server].crypto -= crypto
            self.lista_servers[id_server].nTasksAtivas += 1
            self.lista_containers[self.contIndice + self.offset].id_server = id_server
            self.lista_containers[self.contIndice + self.offset].actual_cpu = cpu
            self.lista_containers[self.contIndice + self.offset].actual_ram = ram
            self.lista_containers[self.contIndice + self.offset].actual_epc = crypto

            # Checa se há o ligamento de um servidor
            if self.lista_servers[id_server].ativo == False:
                n_servers_aproveitaveis = 0
                for server in self.lista_servers:
                    if server.cpu >= cpu and server.ram >= ram and server.crypto >= crypto and server.ativo == True:
                        n_servers_aproveitaveis += 1
                rewardEnergia = 1.0/(n_servers_aproveitaveis + 1)

            # Seta o servidor para ativo
            self.lista_servers[id_server].ativo = True

            if self.lista_containers[self.contIndice + self.offset].epc[1] > 0:
                utilidade = (self.lista_containers[self.contIndice + self.offset].actual_cpu / self.lista_containers[self.contIndice + self.offset].cpu[1] +
                            self.lista_containers[self.contIndice + self.offset].actual_ram / self.lista_containers[self.contIndice + self.offset].ram[1] +
                            self.lista_containers[self.contIndice + self.offset].actual_epc / (self.lista_containers[self.contIndice + self.offset].epc[1] + 0.0001)) / 3.0
            else:
                utilidade = (self.lista_containers[self.contIndice + self.offset].actual_cpu / self.lista_containers[self.contIndice + self.offset].cpu[1] +
                            self.lista_containers[self.contIndice + self.offset].actual_ram / self.lista_containers[self.contIndice + self.offset].ram[1]) / 2.0

            linha_task = str(self.lista_containers[self.contIndice + self.offset].id) + " " + str(self.lista_containers[self.contIndice + self.offset].delay) + " " + str(utilidade)
            self.temp_infos.append(linha_task)

            info.append("accepted")

            # Calculando o reward da requisição
            rewardRequisicao = (0.25 * max(0, cpu/self.lista_containers[self.contIndice + self.offset].cpu[1]) +
                                0.25 * max(0, ram/self.lista_containers[self.contIndice + self.offset].ram[1]) +
                                0.50 * max(0, crypto/(self.lista_containers[self.contIndice + self.offset].epc[1] + 0.0001)))

            self.contIndice += 1
            if self.lista_containers[self.contIndice + self.offset].subtime > self.evento:
                self.eventopassado = self.evento
                self.evento += 1

        # Caso o servidor não aguente o container
        else:
            n_servers_aproveitaveis = 0
            self.makespam += 1
            for server in self.lista_servers:
                if server.cpu >= cpu and server.ram >= ram and server.crypto >= crypto and server.ativo == True:
                    n_servers_aproveitaveis += 1
            rewardEnergia = 1.0/(n_servers_aproveitaveis + 1)
            rewardRequisicao = 0.0

            # Posterga os containers
            tamanho_fila = 0
            subtime_post = self.lista_containers[self.contIndice + self.offset].subtime
            for i in range(len(self.lista_containers)):
                if self.lista_containers[i].subtime == subtime_post:
                    self.lista_containers[i].subtime += 1
                    self.lista_containers[i].delay += 1
                    tamanho_fila += 1

            rewardTempo = 1.0/(tamanho_fila + 1) # Reward proporcional ao tamanho da fila

            info.append("rejected")

        #done = self.contIndice >= self.limite
        done = self.contIndice >= len(self.lista_containers) - 1

        observation = []
        # Incluindo os status dos servidores
        #############################################################
        for server in self.lista_servers:
            cpu = float(server.cpu)
            ram = float(server.ram)
            crypto = float(server.crypto)

            if NORMALIZE:
                cpu /= MAX_CPU
                ram /= MAX_RAM
                crypto /= MAX_CRYPTO

            observation.append(cpu)
            observation.append(ram)
            observation.append(crypto)
        #############################################################

        # Incluindo informações dos containeres
        #############################################################
        mincpu = float(self.lista_containers[self.contIndice + self.offset].cpu[0])
        maxcpu = float(self.lista_containers[self.contIndice + self.offset].cpu[1])
        minram = float(self.lista_containers[self.contIndice + self.offset].ram[0])
        maxram = float(self.lista_containers[self.contIndice + self.offset].ram[1])
        mincrypto = float(self.lista_containers[self.contIndice + self.offset].epc[0])
        maxcrypto = float(self.lista_containers[self.contIndice + self.offset].epc[1])
        ttl = float(self.lista_containers[self.contIndice + self.offset].duration)

        if NORMALIZE:
            mincpu /= MAX_VCPU
            maxcpu /= MAX_VCPU
            minram /= MAX_VRAM
            maxram /= MAX_VRAM
            mincrypto /= MAX_VCRYPTO
            maxcrypto /= MAX_VCRYPTO
            ttl /= MAX_TTL

        observation.append(mincpu)
        observation.append(maxcpu)
        observation.append(minram)
        observation.append(maxram)
        observation.append(mincrypto)
        observation.append(maxcrypto)
        observation.append(ttl)
        #############################################################

        # Apendendo as rewards separadamente
        info.append(rewardTempo)
        info.append(rewardEnergia)
        info.append(rewardRequisicao)
        info.append(ind)

        # Calculando a média
        reward = (rewardTempo + rewardEnergia + rewardRequisicao)/3.0

        return observation, reward, done, info

    # Função que decresce o duration e verifica a finalização de execução de um container
    def passarTempo(self):
        for i in range(self.contIndice):
            if self.lista_containers[i + self.offset].id_server != "NaN":
                self.lista_containers[i + self.offset].duration -= 1
                # Container finalizou sua execução
                if self.lista_containers[i + self.offset].duration == 0:
                    self.lista_servers[self.lista_containers[i + self.offset].id_server].cpu += self.lista_containers[i + self.offset].actual_cpu
                    self.lista_servers[self.lista_containers[i + self.offset].id_server].ram += self.lista_containers[i + self.offset].actual_ram
                    self.lista_servers[self.lista_containers[i + self.offset].id_server].crypto += self.lista_containers[i + self.offset].actual_epc
                    self.lista_servers[self.lista_containers[i + self.offset].id_server].nTasksAtivas -= 1

                    # Caso o servidor não tenha mais containers ativos ele é "desligado"
                    if self.lista_servers[self.lista_containers[i + self.offset].id_server].nTasksAtivas == 0:
                        self.lista_servers[self.lista_containers[i + self.offset].id_server].ativo = False

                    self.lista_containers[i + self.offset].id_server = "NaN"


NORMALIZE = True
MAX_CPU = 8
MAX_RAM = 64
MAX_CRYPTO = 128

MAX_VCPU = 8
MAX_VRAM = 64
MAX_VCRYPTO = 128
MAX_TTL = 300
