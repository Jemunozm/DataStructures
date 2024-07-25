from ColeccionUsuarios import ColeccionUsuarios
from Usuario import Usuario

# Create a ColeccionUsuarios object
colecion = ColeccionUsuarios()

# Add some Usuario objects to the collection
colecion._UsuariosList.addFirst(Usuario("Jesus", 1000, "10/10/1999", "Montería", 3209467789, "jemunozm@unal.edu.co", "68, 51b-31, Sevilla, Medellín, piso 2, """))
colecion._UsuariosList.addFirst(Usuario("Daniel", 1001, "5,9,2000", "Cali", 3113825465,  "jemunozm@unal.edu.co", "68, 51b-31, Sevilla, Medellín, piso 2, """))
colecion._UsuariosList.addFirst(Usuario("Diego", 1005, "15,2,1999", "Medellín", 3105309854,  "jemunozm@unal.edu.co", "68, 51b-31, Sevilla, Medellín, piso 2, """))
colecion._UsuariosList.addFirst(Usuario("Emir", 2001, "1,6,2000", "Sincelejo", 3023271941,   "jemunozm@unal.edu.co", "68, 51b-31, Sevilla, Medellín, piso 2, """))
colecion._UsuariosList.addFirst(Usuario("Juan", 1002, "27,8,2000", "Boyacá", 3029461941,   "jemunozm@unal.edu.co", "68, 51b-31, Sevilla, Medellín, piso 2, """))

# Print the collection before sorting
print("Before sorting:")
print(colecion._UsuariosList)

# Sort the collection
colecion.sort()



# Print the collection after sorting
print("After sorting:")
print(colecion._UsuariosList)
