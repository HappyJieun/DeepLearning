import random
import matplotlib.pyplot as plt
import math
import numpy as np
# f_nQ
f_nQ_set = open('C:/Users/ABC/Desktop/기말대비/1분반 기말/data/f_nQ.txt')
f_nQ = [float(i) for i in f_nQ_set]
f_nQ_set.close()
# f_study
f_study_set = open('C:/Users/ABC/Desktop/기말대비/1분반 기말/data/f_study.txt')
f_study = [float(i) for i in f_study_set]
f_study_set.close()
# p_nQ
p_nQ_set = open('C:/Users/ABC/Desktop/기말대비/1분반 기말/data/p_nQ.txt')
p_nQ = [float(i) for i in p_nQ_set]
p_nQ_set.close()
# p_study
p_study_set = open('C:/Users/ABC/Desktop/기말대비/1분반 기말/data/p_study.txt')
p_study = [float(i) for i in p_study_set]
p_study_set.close()


f_nQ_values = np.array(f_nQ)
p_nQ_values = np.array(p_nQ)
f_study_values = np.array(f_study)
p_study_values = np.array(p_study)
# Assign 0 to f_nQ and 1 to p_nQ
f_nQ_labels = np.zeros_like(f_nQ_values)
p_nQ_labels = np.ones_like(p_nQ_values)
# Combine the arrays
nQ = np.concatenate((f_nQ_values, p_nQ_values))
study = np.concatenate((f_study_values, p_study_values))
y_data = np.concatenate((f_nQ_labels, p_nQ_labels))

#############################################################
def w_initial(x, y):
    w = np.random.rand(x, y)
    return w

def cross_entropy(y_data, x_data, w_set_cros):
    y_error = 0
    for i in range(len(y_data)):
        y_error += -sum(y_data[i] * np.log(softmax(np.dot(w_set_cros, x_data[i]))))
    return y_error / len(y_data)

def softmax(x):
    e_x = np.exp(x)
    return e_x / np.sum(e_x)

def partial_differentiation(y_data, x_data, w_set_t, c_ce, delta):
    grad_set = [[0 for col in range(len(w_set_t[0]))] for row in range(len(w_set_t))]
    for i in range(len(w_set_t)):
        for j in range(len(w_set_t[0])):
            w_set_t[i][j] += delta
            grad_set[i][j] = (cross_entropy(y_data, x_data, w_set_t) - c_ce) / delta
    return grad_set

def update_weight(y_data, x_data, w_set_tt, c_ce, learning_rate, delta):
    grad_set_tt = partial_differentiation(y_data, x_data, w_set_tt, c_ce, delta)
    for i in range(len(w_set_tt)):
        for j in range(len(w_set_tt[0])):
            w_set_tt[i][j] += -grad_set_tt[i][j] * learning_rate
    return w_set_tt
def accuracy(y_data, x_data, w_set_acc):
    acc = 0
    for i in range(len(y_data)):
        y_est = one_hot(softmax(np.dot(w_set_acc, x_data[i])))
        if np.array_equal(y_data[i], y_est):
            acc += 1
    return acc / len(y_data) * 100

def one_hot(x):
    x = list(x)
    x_temp = [0] * (len(x) - 1)
    x_temp.insert(x.index(max(x)), 1)
    return np.array(x_temp)
x_data = list(zip(nQ, study))
x_data = [list(t) for t in x_data]
y_data = [[1, 0] if value == 1 else [0, 1] for value in y_data]

w_set = w_initial(2, 2)
c_ce = cross_entropy(y_data, x_data, w_set)
delta = 0.001
learning_rate = 0.005
tol = 1e-5
i_ter = 0

while True:
    n_w_set = update_weight(y_data, x_data, w_set, c_ce, learning_rate, delta)
    n_ce = cross_entropy(y_data, x_data, n_w_set)
    i_ter += 1
    if abs(c_ce - n_ce) <= tol:
        print('Final w_set', w_set)
        print('Accuracy(%) at the end:', accuracy(y_data, x_data, w_set))
        break
    w_set = n_w_set
    c_ce = n_ce

print('Number of iterations:', i_ter)
