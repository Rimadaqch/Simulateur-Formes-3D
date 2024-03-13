#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def surface_cube(cote):
    return 6 * cote**2

def volume_cube(cote):
    return cote**3

def plot_cube(cote):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Les sommets du cube
    verts = [
        [0, 0, 0],
        [0, cote, 0],
        [cote, cote, 0],
        [cote, 0, 0],
        [0, 0, cote],
        [0, cote, cote],
        [cote, cote, cote],
        [cote, 0, cote]
    ]

    # Les faces du cube
    faces = [
        [verts[0], verts[1], verts[2], verts[3]],
        [verts[4], verts[5], verts[6], verts[7]],
        [verts[0], verts[1], verts[5], verts[4]],
        [verts[2], verts[3], verts[7], verts[6]],
        [verts[1], verts[2], verts[6], verts[5]],
        [verts[0], verts[3], verts[7], verts[4]]
    ]

    # Création de la collection Poly3DCollection
    poly3d = Poly3DCollection(faces, linewidths=1, edgecolors='r', alpha=.25)
    ax.add_collection3d(poly3d)

    # Configuration des limites des axes
    ax.set_xlim([0, cote])
    ax.set_ylim([0, cote])
    ax.set_zlim([0, cote])

    # Étiquetage des axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.title("Cube")
    plt.show()

def main():
    print("Bienvenue dans le calculateur de surface et volume !")

    cote = float(input("Entrez la longueur du côté du cube : "))
    surface = surface_cube(cote)
    volume = volume_cube(cote)

    print(f"Pour un cube de côté {cote}:")
    print(f"Surface : {surface}")
    print(f"Volume : {volume}")

    plot_cube(cote)

if __name__ == "__main__":
    main()

