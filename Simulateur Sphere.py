#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def surface_sphere(rayon):
    return 4 * np.pi * rayon**2

def volume_sphere(rayon):
    return (4/3) * np.pi * rayon**3

def plot_sphere(rayon):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = rayon * np.outer(np.cos(u), np.sin(v))
    y = rayon * np.outer(np.sin(u), np.sin(v))
    z = rayon * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color='b', alpha=0.6)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.title("Sphère")
    plt.show()

def main():
    print("Bienvenue dans le calculateur de surface et volume !")

    rayon = float(input("Entrez le rayon de la sphère : "))
    surface = surface_sphere(rayon)
    volume = volume_sphere(rayon)

    print(f"Pour une sphère de rayon {rayon}:")
    print(f"Surface : {surface}")
    print(f"Volume : {volume}")

    plot_sphere(rayon)

if __name__ == "__main__":
    main()



# In[ ]:




