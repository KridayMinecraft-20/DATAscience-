import matplotlib.pyplot as plt
import numpy as np

# Data
months = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

facecream  = np.array([2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900])
facewash   = np.array([1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760])
toothpaste = np.array([5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400])
bathingsoap= np.array([9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400])
shampoo    = np.array([1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800])
moisturizer= np.array([1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760])

profit = np.array([211000,183300,224700,222700,209600,201400,
                   295500,361400,234000,266700,412800,300200])

# ------------------ GRAPH 1: Profit per Month ------------------
plt.plot(months, profit, marker='o', color='green', label='Profit')
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly Profit Comparison")
plt.legend()
plt.show()

# ------------------ GRAPH 2: All Products Sales ------------------
plt.plot(months, facecream,  marker='o', color='blue',   label='Face Cream')
plt.plot(months, facewash,   marker='o', color='orange', label='Face Wash')
plt.plot(months, toothpaste, marker='o', color='red',    label='Toothpaste')
plt.plot(months, bathingsoap,marker='o', color='purple', label='Bathing Soap')
plt.plot(months, shampoo,    marker='o', color='brown',  label='Shampoo')
plt.plot(months, moisturizer,marker='o', color='pink',   label='Moisturizer')

plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.title("Monthly Sales of All Products")
plt.legend()
plt.show()

# ------------------ GRAPH 3: Face Cream vs Face Wash ------------------
plt.plot(months, facecream, marker='o', color='blue',   label='Face Cream')
plt.plot(months, facewash,  marker='o', color='orange', label='Face Wash')

plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.title("Face Cream vs Face Wash Sales Comparison")
plt.legend()
plt.show()

