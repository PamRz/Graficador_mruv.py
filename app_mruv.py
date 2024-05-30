import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calculate_position(X0, V0, a, t):
    return X0 + V0 * t + 0.5 * a * t**2

def plot_position(X0, V0, a, t_max, times):
    t = np.linspace(0, t_max, 500)
    X = calculate_position(X0, V0, a, t)
    
    fig, ax = plt.subplots(figsize=(14, 7))  # Hacer el gráfico más amplio
    ax.plot(t, X, label=f'X(t) = {X0} + {V0}t + 0.5*{a}t²')
    
    # Marcar los puntos específicos en el gráfico
    for time in times:
        X_time = calculate_position(X0, V0, a, time)
        ax.plot(time, X_time, 'ro')  # 'ro' para puntos rojos
        ax.text(time, X_time, f'({time},{X_time:.2f})', fontsize=9, ha='right')

    # Configuración de los ejes para que sean proporcionales y espaciados de 0.5 en 0.5
    ax.set_aspect('auto', adjustable='box')  # Cambiado de 'equal' a 'auto'
    ax.set_xlim(0, t_max)
    ax.set_xticks(np.arange(0, t_max + 0.5, 0.5))
    ax.set_ylim(min(X), max(X))
    ax.set_yticks(np.arange(min(X), max(X) + 0.5, 0.5))
    
    ax.set_xlabel('Tiempo (t)')
    ax.set_ylabel('Posición (X)')
    ax.set_title('Posición en función del tiempo')
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)

def main():
    st.title('Simulación de Movimiento Rectilíneo Uniformemente Variado (MRUV)')

    X0 = st.number_input('Ingrese la posición inicial (X0):', value=0.0)
    V0 = st.number_input('Ingrese la velocidad inicial (V0):', value=0.0)
    a = st.number_input('Ingrese la aceleración (a):', value=0.0)
    t_max = st.number_input('Ingrese el tiempo máximo (t):', value=10.0, min_value=0.1)
    t1 = st.number_input('Ingrese el tiempo t1:', value=1.0, min_value=0.0, max_value=t_max)
    t2 = st.number_input('Ingrese el tiempo t2:', value=2.0, min_value=0.0, max_value=t_max)
    t3 = st.number_input('Ingrese el tiempo t3:', value=3.0, min_value=0.0, max_value=t_max)
    t4 = st.number_input('Ingrese el tiempo t4:', value=4.0, min_value=0.0, max_value=t_max)

    times = [t1, t2, t3, t4]
    plot_position(X0, V0, a, t_max, times)

if __name__ == "__main__":
    main()

  

