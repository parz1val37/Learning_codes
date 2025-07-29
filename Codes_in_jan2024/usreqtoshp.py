import matplotlib.pyplot as plt
import numpy as np
k = input("ENTER EQUATION IN TERMS OF 'X':")

def equation(x):
    try:
        y = eval(k)
        return y
    except:
        print("INVALID EQUATION")
        return None
    
if equation is not None:
    x_values = np.linspace(0 , 900 , 900)
    y_values = equation(x_values)
    
    if y_values is not None:
        plt.plot(x_values,y_values,label="CURVE")
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('GRAPH OF YOUR EQT:')
        plt.legend()
        plt.grid(True)
        plt.show()
        
        