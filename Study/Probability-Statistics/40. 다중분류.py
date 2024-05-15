import numpy as np
import matplotlib.pyplot as plt
import random
import csv

data_set = open('C:/Users/ABC/Desktop/data/iris.csv', 'r')
data = csv.reader(data_set)
data = list(data)
x_data = []
for i in range(len(data)):
    x_temp = []
    for j in data[i][0:4]:
        x_temp.append(float(j))
    x_data.append(x_temp)
x_data=np.array(x_data)
print(x_data)
y_dict={'Iris-setosa':[1,0,0], 'Iris-versicolor':[0,1,0], 'Iris-virginica':[0,0,1]}
y_data = []
for line in data:
    y_data.append(y_dict[line[4]])
y_data = np.array(y_data)
print(y_data)
def w_initial(x,y):
    w = np.random.rand(x,y)
    return w
def cross_entropy(y_data, x_data, w_set_cros):
    y_error = 0
    for i in range(len(y_data)):
        y_error += -sum(y_data[i]*np.log(softmax(np.dot(w_set_cros, x_data[i]))))
    return y_error/len(y_data)
def softmax(x):
    e_x = np.exp(x)
    return e_x/e_x.sum()
def partial_differentiation(y_data, x_data, w_set_t, c_ce, delta):
    grad_set = [[0 for col in range(len(w_set_t[0]))] for row in range(len(w_set_t))]
    for i in range(len(w_set_t)):
        for j in range(len(w_set_t[0])):
            w_set_t[i][j] += delta
            grad_set[i][j] = (cross_entropy(y_data, x_data, w_set_t)-c_ce)/delta
    return grad_set

def update_weight(y_data, x_data, w_set_tt, c_ce, learning_rate, delta):
    grad_set_tt = [[0 for col in range(len(w_set_tt[0]))] for row in range(len(w_set_tt))]
    grad_set_tt = partial_differentiation(y_data, x_data, w_set_tt, c_ce, delta)
    for i in range(len(w_set_tt)):
        for j in range(len(w_set_tt[0])):
            w_set_tt[i][j] += -grad_set_tt[i][j]*learning_rate
    return w_set_tt
def accuracy(y_data, x_data, w_set_acc):
    acc=0
    for i in range(len(y_data)):
        y_est=one_hot(softmax(np.dot(w_set_acc, x_data[i])))
        if (np.dot(y_data[i], y_est) == 1):
            acc += 1
    print('accuracy(%)=', acc/len(y_data)*100)
def one_hot(x):
    x = list(x)
    x_temp = [0]*(len(x)-1)
    x_temp.insert(x.index(max(x)),1)
    return np.array(x_temp)

w_set = w_initial(3, 4)
c_ce = cross_entropy(y_data, x_data, w_set)
delta = 0.001
learning_rate = 0.005
tol = 10 ** (-5)
i_ter = 0

while(True):
    n_w_set = []
    n_w_set = update_weight(y_data, x_data, w_set, c_ce, learning_rate, delta)
    n_ce = cross_entropy(y_data, x_data, n_w_set)
    i_ter += 1
    if(abs(c_ce - n_ce) <= tol):
        print('final w_set', w_set)
        accuracy(y_data, x_data, w_set)
        break
    w_set = []
    w_set = n_w_set
    c_ce = n_ce
    if (i_ter % 1000)==0:
        print('i_ter:', i_ter, 'w_set=', w_set)
        accuracy(y_data, x_data, w_set)

