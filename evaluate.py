from keras.models import load_model
from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np
import _pickle as pickle
import random

#loads the test input
with open('test_input.pickle', mode='rb') as f:
    test_input = pickle.load(f)
with open('test_output.pickle', mode='rb') as f:
    test_output = pickle.load(f)

#loads the model
model = keras.models.load_model('model.h5')

for i in range(4): #validates 4 times
    test_indices = random.choice(range(100)) #creates random indices to choose from the test dataset
    x = test_input[test_indices][0:100:3] #x is the former half
    y = test_input[test_indices][100:200:3] #y is the latter half
    sample_input = test_input[test_indices][np.newaxis, :]
    output = model.predict(sample_input)

    a, b, c = output[0] #predicts the coefficients
    #maps the coefficients to (x,y) coordinates
    predicted_x = np.arange(-1, 1, 2 / 1000)
    predicted_y = a* predicted_x**2 + b* predicted_x + c

    #creates subplots per each validation
    plt.subplot(220+(i+1))
    plt.plot(x, y, 'x', label="desired output")
    plt.plot(predicted_x, predicted_y,label="prediction")
    plt.legend(loc = 'upper right')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim()
    plt.title('test'+str(i+1))
plt.savefig('eval.png', pad_inches=0.1) #saves the plot in png format. pad_inches is used to prevent the output png from having excess padding
plt.show() #display the plot
