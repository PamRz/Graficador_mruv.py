import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Función para calcular la posición en función del tiempo
def calculate_position(X0, V0, a, t):
    return X0 + V0 * t + 0.5 * a * t**2

# Función para graficar la posición en función del tiempo
def plot_position(X0, V0, a, t_max, times):
    # Generar valores de tiempo uniformemente espaciados
    t = np.linspace(0, t_max, 500)
    # Calcular la posición correspondiente a cada tiempo
    X = calculate_position(X0, V0, a, t)
    
    # Crear figura y ejes para el gráfico
    fig, ax = plt.subplots(figsize=(8, 8))  # Hacer el gráfico cuadrado
    ax.plot(t, X, label=f'X(t) = {X0} + {V0}t + 0.5*{a}t²')  # Graficar la posición en función del tiempo
    
    # Marcar los puntos específicos en el gráfico
    for time in times:
        X_time = calculate_position(X0, V0, a, time)
        ax.plot(time, X_time, 'ro')  # 'ro' para puntos rojos
        ax.text(time, X_time, f'({time},{X_time:.2f})', fontsize=9, ha='right')  # Etiquetas de los puntos
    
    # Configuración de los ejes
    ax.set_aspect('equal', adjustable='box')  # Proporción de ejes igual y ajustable
    ax.set_xlim(0, t_max)  # Límites del eje x
    ax.set_xticks(np.arange(0, t_max + 1.0, 1.0))  # Marcas en el eje x cada 1 unidad de tiempo
    ax.set_ylim(0, max(X))  # Límites del eje y
    ax.set_yticks(np.arange(0, max(X) + 1.0, 1.0))  # Marcas en el eje y cada 1 unidad de posición
    
    # Etiquetas y título del gráfico
    ax.set_xlabel('Tiempo (t)')
    ax.set_ylabel('Posición (X)')
    ax.set_title('Posición en función del tiempo')
    ax.legend()  # Leyenda del gráfico
    ax.grid(True)  # Cuadrícula
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Función principal donde se ejecuta todo el programa
def main():
    st.title('Simulación de Movimiento Rectilíneo Uniformemente Variado (MRUV)')

    # Entrada de datos desde el usuario
    X0 = st.number_input('Ingrese la posición inicial (X0):', value=0.0, step=None)
    V0 = st.number_input('Ingrese la velocidad inicial (V0):', value=0.0, step=None)
    a = st.number_input('Ingrese la aceleración (a):', value=0.0, step=None)
    t_max = st.number_input('Ingrese el tiempo máximo (t):', value=10.0, min_value=0.1, step=None)
    t1 = st.number_input('Ingrese el tiempo t1:', value=1.0, min_value=0.0, max_value=t_max, step=None)
    t2 = st.number_input('Ingrese el tiempo t2:', value=2.0, min_value=0.0, max_value=t_max, step=None)
    t3 = st.number_input('Ingrese el tiempo t3:', value=3.0, min_value=0.0, max_value=t_max, step=None)
    t4 = st.number_input('Ingrese el tiempo t4:', value=4.0, min_value=0.0, max_value=t_max, step=None)

    times = [t1, t2, t3, t4]  # Lista de tiempos específicos
    plot_position(X0, V0, a, t_max, times)  # Llamar a la función para graficar la posición

# Verificar si el script se ejecuta directamente
if __name__ == "__main__":
    main()
