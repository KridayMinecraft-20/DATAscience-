import pandas as pd

my_data = {
    "Cars" : ["WagonR", "Audi", "Volvo"],
    "Customers" : ["Nathan", "Julie", "Brad"]
}

my_var = pd.DataFrame(my_data)
my_var.index=my_var.index+1
print(my_var)

a=[2, 3, 4]
my_var=pd.Series(a)
print(my_var)

