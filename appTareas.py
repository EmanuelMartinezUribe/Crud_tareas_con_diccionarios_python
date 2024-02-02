tareas={
        "01":{
            "descripcion":"levantamiento de requisitos",
            "estado":"pendiente",
            "tiempo":60
    },
        "02":{
                "descripcion":"programacion citas medicas",
                "estado":"pendiente",
                "tiempo":180
    },
        "03":{
                "descripcion":"crud clientes",
                "estado":"pendiente",
                "tiempo":50
    }
}

def creat_crear_tarea(tareas, identificador, tarea_nueva):
    tareas[identificador]=tarea_nueva
    return tareas
    


def read_listar_tareas(tareas):

    for identificador, tarea in tareas.items():
        print(identificador,"-",end="")
        for clave, valor in tarea.items():
            print(valor,",",end="")
        print()

def esta_elemento(idenficador, tareas):
    claves=tareas.keys()
    if idenficador in claves:
        return True
    else:
        return False
        

    
def actualizar_tarea_update(tareas):
    tarea_id = input("Ingrese el ID de la tarea a actualizar: ")
    if tarea_id in tareas:
        tarea = tareas[tarea_id]
        print(f"Tarea encontrada: {tarea['descripcion']} - {tarea['estado']} - {tarea['tiempo']} min.")
        descripcion = input("Ingrese la nueva descripción de la tarea (deje vacío si no quiere cambiarla): ")
        estado = input("Ingrese el nuevo estado de la tarea (deje vacío si no quiere cambiarlo): ")
        if estado not in ["", "pendiente", "completado"]:
            print("Estado inválido.")
            return
        tiempo = input("Ingrese el nuevo tiempo estimado de la tarea en minutos (deje vacío si no quiere cambiarlo): ")
        if tiempo != "":
            tarea["tiempo"] = int(tiempo)
        if descripcion != "":
            tarea["descripcion"] = descripcion
        if estado != "":
            tarea["estado"] = estado
        print("Tarea actualizada con éxito.")
    else:
        print("Tarea no encontrada.")

def eliminar_tarea(tareas):
    tarea_id = input("Ingrese el ID de la tarea a eliminar: ")
    if tarea_id in tareas:
        del tareas[tarea_id]
        print(f"Tarea con ID {tarea_id} eliminada con éxito.")
    else:
        print("Tarea no encontrada.")


while True:
    print(" ")
    print("--- APLICACION CRUD TAREAS ---")
    print("1. adicionar tarea")
    print("2. consultar tarea")
    print("3. actualizar tarea")
    print("4. eliminar tarea")
    print("5. salir")
    
   
    opcion=int(input("ingresa una opcion: "))
    
    #create
    if opcion == 1:
        print()
        print("->adicionar tareas")
        while True:
            identificador=str(input("ingrese identificador de la tarea: "))
            if esta_elemento(identificador, tareas):
                print("este identificador ya existe, utilice otro... ")
            else:
                break
        descripcion=input("ingrese descripcion tarea: ")
        estado=input("ingrese estado de tarea: ")
        tiempo=int(input("ingrese tiempo de tarea: "))

        tarea_nueva={
                "descripcion": descripcion,
                "estado": estado,
                "tiempo": tiempo

            }
            
        tareas=creat_crear_tarea(tareas, identificador, tarea_nueva)
        print(f"tarea {identificador} creada con exito")
          

    
       

    #read
    elif opcion == 2:
        print()
        print("listado de tareas")
        print()
        # llamar funcion de lectura de tareas
        read_listar_tareas(tareas)



    #update
    elif opcion == 3:
        print()
        print("actualizar tarea")
        print()
        # llamar a la funcion de actualizar tarea
        actualizar_tarea_update(tareas)

    #delete
    elif opcion == 4:
        print()
        print("eliminar tarea:")
        print()
        # llamar a la funcion de eliminar tarea
        eliminar_tarea(tareas)

    #exit
    elif opcion == 5:
        print("ha salido exitosamnete") # salir
        break


    else:
        print("ingrese un opcion valida")