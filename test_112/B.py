dit = {
    "Tetrahedron":4,
    "Cube":6,
    "Octahedron":8,
    "Dodecahedron":12,
    "Icosahedron":20
}

m = 0
for i in range(int(input())):       
    m += dit[input()]
print(m)

"""
4
Icosahedron
Cube
Tetrahedron
Dodecahedron
"""