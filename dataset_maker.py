import numpy as np
from numpy.random import randn, choice
import _pickle as pickle

dataset_len = 100 #number if sets per batch
train_len = 10000 #number of training batches
test_len = 1000 #number of test batches

train_input = np.zeros((train_len, 2*dataset_len)) #stores the (x,y) for each batch
train_output = np.zeros((train_len, 3)) #stores the coefficients
test_input = np.zeros((test_len, 2*dataset_len))
test_output = np.zeros((test_len, 3))

for i in range(train_len): #y=ax^2+bx+c. Creates random (x,y) coordinates
    a = 100*randn(1)
    b = 100*randn(1)
    c = randn(1)
    x = np.arange(-1,1,2/dataset_len)
    y = a*x**2 + b*x + c + (randn(dataset_len)-0.5)/10 #adds random noises to y
    train_input[i] = np.array([x, y]).flatten() #flattens all the (x,y) coordinates
    train_output[i] = np.array([a, b, c]).flatten() #flattens all the coefficients 

for i in range(test_len): #y=ax^2+bx+c. Creates random (x,y) coordinates
    a = 100*randn(1)
    b = 100*randn(1)
    c = randn(1)
    x = np.arange(-1,1,2/dataset_len)
    y = a*x**2 + b*x + c + (randn(dataset_len)-0.5)/10 #adds random noises to y
    test_input[i] = np.array([x, y]).flatten() #flattens all the (x,y) coordinates
    test_output[i] = np.array([a, b, c]).flatten() #flattens all the coefficients 

#input shapes are [train(test)_len, 2*dataset_len]. Output shapes are [train(test)_len, 3].
with open('train_input.pickle', mode='wb') as f:
    pickle.dump(np.array(train_input), f)
with open('train_output.pickle', mode='wb') as f:
    pickle.dump(np.array(train_output), f)
with open('test_input.pickle', mode='wb') as f:
    pickle.dump(np.array(test_input), f)
with open('test_output.pickle', mode='wb') as f:
    pickle.dump(np.array(test_output), f)