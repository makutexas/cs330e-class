import numpy as np

def rmse(x,y):
    square = 0
    for i in zip(x,y):
        x_num = i[0]
        y_num = i[1]
        square += (x_num - y_num)**2
    error = np.sqrt(square/len(x))
    return error

print(rmse([2,3,4],[4,1,6]))