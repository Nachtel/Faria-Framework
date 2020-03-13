import numpy as np


def sig(x):
	return 1/(1+np.exp(-x))


layer1 = 10
layer2 = 40

total_weights = layer1*layer2

P_all = []
W_all = []
F_all = []
V_all = []
I_all = []
NW_all = []
weights1 = []
weights2 = []

#REMINDER: REPLACE ALL [] in the appends with normal paranthesis
#
#
#
#
#
#
#
#

##
def setup_p():
	if len(P_all) == 0:
		for i in range(layer2):
			P_all.append(np.random.random())
			#print("Successfully setup second-to-last layer")
def setup_w():
	if len(W_all) == 0:
		for i in range(total_weights):
			W_all.append(np.random.random())
			#print("Successfully setup weights")
def setup_i():
	if len(I_all) == 0:
		for i in range(layer1):
			I_all.append(float(input("Insert {} ideals as the finals:".format(layer1))))
'''def st():
	F = 0
	weightmove = 0
	for final in range(layer1):
		for previous in range(layer2):
			F += (P_all[previous]*W_all[weightmove])
			weightmove += 1
	F_all.append(F)'''
def sig_f(x):
	V_all.append(sig(x))
def cost(t):
	return (V_all[t]-I_all[t])**2
def setup_f():
	measure_of_weight = 0
	for final in range(layer1):	
		summ = 0.0
		for previous in P_all:
			summ += previous*W_all[measure_of_weight]
			measure_of_weight +=1
				#print(measure_of_weight)
				#print(summ)
			#print(summ)
			#print(measure_of_weight)
			#print("Successfuly setup final layer.")
		F_all.append(summ)

def deri(p, f):
	return (2*(sig(F_all[f])-I_all[f])*sig(F_all[f])*(1-sig(F_all[f]))*P_all[p])


def setup_v():
	for final in F_all:
		V_all.append(sig(final))
def update_values():
	for weight in range(total_weights):
		W_all.append(W_all[weight]-NW_all[weight])
	del W_all[:total_weights]
	del F_all[:layer1]
	del NW_all[:]
	del V_all[:]
def process_weights():
	setup_p()
	setup_w()
	setup_i()
	setup_f()
	setup_v()
	for final in range(layer1):
		for previous in range(layer2):
			NW_all.append(deri(previous, final))
		#V_all.append(deri(previous, final)
	cost_all()

def train(cycles):
	for cycle in range(cycles):
		process_weights()
		update_values()
def cost_all():
	total = 0
	for challenger in range(len(I_all)):
		print("individual final cost function: {}".format((V_all[challenger]-I_all[challenger])**2))
		total += (I_all[challenger]-V_all[challenger])**2
	print("The cost function is: {}.".format(total))
