laplce1:

 This program uses the laplce distribution to give a differentially private average of D1 and D2 differing on at most one data point. We will use the variable mu and b to denote our true average and scale respectively. Our distribution will be centered at the true average, mu, of our dataset. For larger scale size of b, we can expect a more flat distribution, whereas for smaller b, we can expect a more peaked distribution. Also, the number of points in our dataset will determine how close together our distributions are of D1 and D2. For example, running this program with smallpoker1.py and smallpoker2.py will create a larger gap in distribution, because there are only ten hands given. However, for larger datasets pokerhnds.txt and pokerhnds2.txt, we can expect our distributions to be much closer together in probability because there are five hundred hands given. 


laplace2:

This program adds laplace noise to the true average of the dataset, computes the probability of 1000 randomized outputs for each D1 and D2, and plots them to a histogram. We can see that even with added laplace noise we are able to determine that our distribution is maximized while centered near the true average, mu.
