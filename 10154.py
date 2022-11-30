import numpy as mp
import matplotlib as mpl

W=np.random.randint(0,1)
b=np.random.randint(0,1)

step_size = 0.5

for epoch in range(100):
    y_pred = W *\ +b

    objective = np.abs(y_pred-y).mean()

    w_grad=step_size*((y-pred-y)*x).mean()
    b_grad=step_size*(y_pred-y).mean()

    W -= w_grad
    b -= b_grad