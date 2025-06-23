# Calculate number of exercise done on each topic of Python
import os

path = "C:\\Users\\Lenovo\\OneDrive\\Documents\\python lab"
x = os.listdir(path)
for path_1 in x:
    path_2 = f"C:\\Users\\Lenovo\\OneDrive\\Documents\\python lab\\{path_1}"
    print(f"topic={path_1} ,{len(os.listdir(path_2))}")
