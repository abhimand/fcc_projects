import numpy as np

def calculate(list):
    #try except here 'List must contain nine numbers.'

    if len(list) < 9: 
        raise ValueError("List must contain nine numbers.")
    dic = {}
    # mean
    matrix = np.reshape(list, (3,3))
    mean = np.mean(matrix)
    mean0 = np.mean(matrix, axis=0)
    mean1 = np.mean(matrix, axis=1)
    dic['mean'] = [mean0.tolist(), mean1.tolist(), mean]
    # variance
    var = np.var(matrix)
    var0 = np.var(matrix, axis=0)
    var1 = np.var(matrix, axis=1)
    dic['variance'] = [var0.tolist(), var1.tolist(), var]
    # standard deviation 
    std = np.std(matrix)
    std0 = np.std(matrix, axis=0)
    std1 = np.std(matrix, axis=1)
    dic['standard deviation'] = [std0.tolist(), std1.tolist(), std]
    # max
    m = np.max(matrix)
    m0 = np.max(matrix, axis=0)
    m1 = np.max(matrix, axis=1)
    dic['max'] = [m0.tolist(), m1.tolist(), m]
    # min
    mi = np.min(matrix)
    mi0 = np.min(matrix, axis=0)
    mi1 = np.min(matrix, axis=1)
    dic['min'] = [mi0.tolist(), mi1.tolist(), mi]
    # sum
    sm = np.sum(matrix)
    sm0 = np.sum(matrix, axis=0)
    sm1 = np.sum(matrix, axis=1)
    dic['sum'] = [sm0.tolist(), sm1.tolist(), sm]
    return dic