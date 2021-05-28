import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as pl2

x1_value=[]
x2_value=[]

def gibbs_sampler(mus, sigmas):
    n_iter=10000
    
    y = mus[1]
    for _ in range(n_iter):
        x = p_x1_given_x2(y, mus, sigmas)
        y = p_x2_given_x1(x, mus, sigmas)
        x1_value.append(x)
        x2_value.append(y)
       
        
    

def p_x1_given_x2(y, mus, sigmas):
    mu = mus[0] + sigmas[1, 0] / sigmas[0, 0] * (y - mus[1])
    sigma = sigmas[0, 0] - sigmas[1, 0] / sigmas[1, 1] * sigmas[1, 0]
    return np.random.normal(mu, sigma)

def p_x2_given_x1(x, mus, sigmas):
    mu = mus[1] + sigmas[0, 1] / sigmas[1, 1] * (x - mus[0])
    sigma = sigmas[1, 1] - sigmas[0, 1] / sigmas[0, 0] * sigmas[0, 1]
    return np.random.normal(mu, sigma)


if __name__ == "__main__":
    mus = np.asarray([1, 2])
    a=.99
    sigmas = np.asarray([[1, a], [.0, a]])

    gibbs_sampler(mus, sigmas)
    
    mean_for_x1=np.mean(x1_value)
    mean_for_x2=np.mean(x2_value)
    print("mean of x1 ",mean_for_x1)
    print("mean for x2 ",mean_for_x2)
    sigma11=np.cov(x1_value,x2_value)
    print("Sigma values are  ",sigma11)
    new_x1_value=[]
    new_x2_value=[]

    for i in range(2000,10000):
        new_x1_value.append(x1_value[i])
        new_x2_value.append(x2_value[i])
    print("after burning")
    pl2.plot(new_x1_value)
    pl2.plot(new_x2_value)
    pl2.show()
    
    
    
    
    