import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def get_inputs():
    X0 = float(input("Ingrese la posición inicial (X0): "))
    V0 = float(input("Ingrese la velocidad inicial (V0): "))
    a = float(input("Ingrese la aceleración (a): "))
    t_max = float(input("Ingrese el tiempo máximo (t): "))
    t1 = float(input("Ingrese el tiempo t1: "))
    t2 = float(input("Ingrese el tiempo t2: "))
    t3 = float(input("Ingrese el tiempo t3: "))
    t4 = float(input("Ingrese el tiempo t4: "))
    return X0, V0, a, t_max, [t1, t2, t3, t4]

def calculate_position(X0, V0, a, t):
    return X0 + V0 * t + 0.5 * a * t**2

def plot_position(X0, V0, a, t_max, times):
    t = np.linspace(0, t_max, 500)
    X = calculate_position(X0, V0, a, t)
    
    plt.figure(figsize=(14, 7))  # Hacer el gráfico más amplio
    plt.plot(t, X, label=f'X(t) = {X0} + {V0}t + 0.5*{a}t²')
    
    # Marcar los puntos específicos en el gráfico
    for time in times:
        X_time = calculate_position(X0, V0, a, time)
        plt.plot(time, X_time, 'ro')  # 'ro' para puntos rojos
        plt.text(time, X_time, f'({time},{X_time:.2f})', fontsize=9, ha='right')

    # Configuración de los ejes para que sean proporcionales y espaciados de 0.5 en 0.5
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks(np.arange(0, t_max + 0.5, 0.5))
    plt.yticks(np.arange(min(X), max(X) + 0.5, 0.5))
    
    plt.xlabel('Tiempo (t)')
    plt.ylabel('Posición (X)')
    plt.title('Posición en función del tiempo')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    X0, V0, a, t_max, times = get_inputs()
    plot_position(X0, V0, a, t_max, times)

if __name__ == "__main__":
    main()
