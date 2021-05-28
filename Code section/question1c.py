import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def gibbs_sampler(mus, sigmasX):
    samples = []
    n_iter=10000
    y = mus[1]
    for _ in range(n_iter):
        x = p_x1_given_x2(y, mus, sigmas)
        y = p_x2_given_x1(x, mus, sigmas)
        samples.append([x, y])
    return samples


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
    sigmas = np.asarray([[1, a], [a, 1]])

    samples = gibbs_sampler(mus, sigmas); samples[:5]
    burn = 2000
    x, y = zip(*samples[burn:])
    sns.jointplot(x, y, kind='hex')
    plt.show()
   
    
    
