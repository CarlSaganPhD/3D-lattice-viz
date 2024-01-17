import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def main():
    st.title('3D Lattice Vector Visualization')

    # Use st.sidebar.slider to put the sliders in the sidebar
    # Sliders for n values
    n1 = st.sidebar.slider('n1', -5, 5, 1)
    n2 = st.sidebar.slider('n2', -5, 5, 1)
    n3 = st.sidebar.slider('n3', -5, 5, 1)

    # Sliders for a1 vector components
    a1x = st.sidebar.slider('a1x', -5.0, 5.0, 1.0)
    a1y = st.sidebar.slider('a1y', -5.0, 5.0, 0.0)
    a1z = st.sidebar.slider('a1z', -5.0, 5.0, 0.0)

    # Sliders for a2 vector components
    a2x = st.sidebar.slider('a2x', -5.0, 5.0, 0.0)
    a2y = st.sidebar.slider('a2y', -5.0, 5.0, 1.0)
    a2z = st.sidebar.slider('a2z', -5.0, 5.0, 0.0)

    # Sliders for a3 vector components
    a3x = st.sidebar.slider('a3x', -5.0, 5.0, 0.0)
    a3y = st.sidebar.slider('a3y', -5.0, 5.0, 0.0)
    a3z = st.sidebar.slider('a3z', -5.0, 5.0, 1.0)


    # Calculate the R vector
    R = np.array([n1 * np.array([a1x, a1y, a1z]) +
                  n2 * np.array([a2x, a2y, a2z]) +
                  n3 * np.array([a3x, a3y, a3z])])

    fig = plot_lattice_vectors(R)
    st.pyplot(fig)

def plot_lattice_vectors(R):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Origin point
    origin = np.array([[0, 0, 0]])

    # Plotting the vector
    ax.quiver(*origin.T, *R.T, color='b', arrow_length_ratio=0.1)

    # Setting plot limits
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    return fig

if __name__ == "__main__":
    main()
