#!/usr/bin/python
# -*- coding: utf-8 -*-

import keras
from keras.models import Sequential
from keras.layers import Dense, CuDNNGRU, Embedding, Dropout,Flatten, Activation, RepeatVector, Activation
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.callbacks import TensorBoard
import matplotlib.pyplot as plt
from collections import deque
import numpy as np
import copy
import random
import json

class Agente():
	def __init__(self):
		self.memory = deque(maxlen=2000)
		self.gamma = 0.9
		self.e = 1
		self.e_decay = 0.95
		self.e_min = 0
		self.LR = 7e-3
		self.n_servers = 15
		self.model = self.build_model()

	def build_model(self):
		model = Sequential()
		'''model.add(CuDNNGRU(512, input_shape=(3*self.n_servers + 7, 1), return_sequences=False))
		model.add(Dropout(0.5))
		model.add(Activation('softmax'))
		model.add(Dense(4*self.n_servers, activation='softmax', activity_regularizer=l2(0.0001)))'''
		model.add(Dense(3*self.n_servers + 7 + 4*self.n_servers, input_dim = 3*self.n_servers+7, activation="relu"))
		model.add(Dense(3*self.n_servers + 7 + 4*self.n_servers, activation="relu"))
		model.add(Dense(4*self.n_servers, activation='softmax'))
		model.compile(optimizer=Adam(lr=self.LR), loss="categorical_crossentropy")
		return model

	def save(self, apendice):
		filename = "model" + apendice +".h5"
		self.model.save(filename)

	def remember(self, estado, acao, reward, proxEstado, done):
		self.memory.append((estado, acao, reward, proxEstado, done))

	def prever(self, estado):
		if(np.random.rand() < self.e):
			return np.random.rand(4*self.n_servers)
		else:
			estado = np.reshape(estado, [1, 3*self.n_servers + 7])
			return self.model.predict(estado)[0]

	def replay(self, batchSize):
		amostra = random.sample(self.memory, batchSize)
		for estado, acao, reward, proxEstado, done in amostra:
			target = reward
			if not done:
				proxEstado = np.reshape(proxEstado, [1, 3*self.n_servers + 7])
				target = reward + self.gamma * (np.amax(self.model.predict(proxEstado)[0]))

			estado = np.reshape(estado, [1, 3*self.n_servers + 7])
			target_f = self.model.predict(estado)
			target_f = np.reshape(target_f, [1, 4*self.n_servers])
			acao = np.reshape(acao, [1, 4*self.n_servers])
			target_f[0][np.argmax(acao)] = target
			target_f = np.reshape(target_f, [1, 4*self.n_servers])
			self.model.fit(estado, target_f, epochs=3, verbose=0)

		if self.e > self.e_min:
			self.e *= self.e_decay
