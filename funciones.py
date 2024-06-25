import json

with open("biblioteca.json" , mode="r" ) as archivoJson:
    leerjson= json.load(archivoJson)
    Usuarios={
        "Miembros id":len(leerjson{"Miembros"}) +1
        "Nombre": "Benjamin "
        "email" : "bp4055100@gmail.com"
        "FechaRegistro" : "26/06/2024"
    }

    leerjson["Nombre"].append(Usuarios)







