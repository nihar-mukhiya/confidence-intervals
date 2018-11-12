import scipy.stats as st
from math import sqrt
import matplotlib.pyplot as plt
n = int(input("enter number of observations n: "))
x = float(input("enter sample mean x: "))
s = float(input("enter sample standard deviation s: "))
cf = float(input("enter confidence interval: "))
z = st.norm.ppf(1 - (1 - cf) / 2)
e = z * (s / sqrt(n))
left = x - e
right = x + e
print("The confidence interval for mean "+str(x)+" is: "+str(left)+" to "+str(right))