import matplotlib.pyplot as plt
import numpy as np

def rand_laplace(mu, b, k):
    sample = np.random.laplace(mu, b, k)
    return sample
    
def dp_avg(A, xmax, xmin, epsilon):
    for x in A:
        if(x>xmax or x<xmin):
            error = 'Value error: vaules can not be greater than',xmax,'or less than ',xmin
            sys.exit(error)
    mu = np.mean(A)
    print mu
    b = np.std(A)*epsilon #find b with respect to epsilon
    n = 1000
    return rand_laplace(mu,b,n) 
    
def hist(sample, mu, b):
    mu, b = np.mean(sample), np.std(sample)
    x = np.arange(-b, b, .01)
    pdf1 = np.exp(-abs(x-mu)/b)/(2.*b)
    plt.hist(sample, bins=100)
    
    plt.xlabel('x')
    plt.ylabel('pdf')
    plt.title('Title')
    plt.show()
    
def main():
    
    f = file('smallpoker1.txt', 'r')
    f = open('smallpoker1.txt', 'r')
    
    D1 = []
    count=0
    ace= []
    
    for line in f:
        line = line.split(",")
        count += line.count('1')
        line = map(int, line)
        ace.append(count)
        count=0
        del line[-1]
        D1.append(line)
    f.close()

    sample = dp_avg(ace,5,0,.01)
    mu, b = np.mean(ace), np.std(ace)
    hist(sample, mu, b) 
    plt.figure(1)

    g = file('smallpoker2.txt', 'r')
    g = open('smallpoker2.txt', 'r')
    
    D2 = []
    count=0
    ace2= []

    for line in g:
        line = line.split(",")
        count += line.count('1')
        line = map(int, line)
        ace2.append(count)
        count=0
        del line[-1]
        D1.append(line)
    g.close()
    
    sample2 = dp_avg(ace2,5,0,.01)
    mu, b = np.mean(ace2), np.std(ace2)
    plt.clf()
    hist(sample2, mu, b) 
    plt.figure(2)


if __name__ == "__main__":
    main()
    
                                    
