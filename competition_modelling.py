import numpy as np
import matplotlib.pyplot as plt

# Constants
a = 10
b = 1
c_a = 2
c_b = 1

# Demand curve
def demand_price(p):
    return a - b * p**2

# Marginal cost curves
def mc_a(q):              
    return c_a

def mc_b(q):
    return c_b

# Reaction functions
def reaction_a(p_b):
    return (a - p_b) / (2 * b)

def reaction_b(p_a):
    return (a - p_a) / (2 * b)

# Generate price range
prices = np.linspace(0, 5, 100)

# Plot demand curve
plt.figure(figsize=(10, 6))
plt.plot(prices, demand_price(prices), label='Demand Curve')

# Plot marginal cost curves
plt.axhline(y=c_a, color='r', linestyle='--', label='MC_A')
plt.axhline(y=c_b, color='g', linestyle='--', label='MC_B')

# Plot reaction functions
plt.plot(prices, reaction_a(prices), label='Reaction Function A', linestyle='-.')
plt.plot(prices, reaction_b(prices), label='Reaction Function B', linestyle='-.')

# Plot equilibrium point
eq_price = (c_a + c_b) / 2
plt.plot(eq_price, demand_price(eq_price), 'ro', label='Equilibrium Price')

plt.title('Bertrand Competition Model')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)
plt.show()
