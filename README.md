# nonlinear_functions_coefficients_prediction

## model summary
<pre>
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 100)               20100     
_________________________________________________________________
dense_1 (Dense)              (None, 100)               10100     
_________________________________________________________________
dense_2 (Dense)              (None, 100)               10100     
_________________________________________________________________
dense_3 (Dense)              (None, 3)                 303       
=================================================================
Total params: 40,603
Trainable params: 40,603
Non-trainable params: 0
_________________________________________________________________
</pre>

## training result
Loss and validation loss.   
![train result](train.png?raw=true "train result")

## evaluation result
Prediction of linear function.
![evaluation result](eval.png?raw=true "evaluation result")