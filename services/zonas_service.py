from utils.db import obtener_conexion

def obtener_zonas():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("CALL obtener_zonas()")
        zonas = cursor.fetchall()
    conexion.close()
    return zonas

def agregar_zona(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("CALL agregar_zona(%s)", (nombre,))
        conexion.commit()
    conexion.close()
    return {'mensaje': 'Zona agregada exitosamente'}

def editar_zona(id, nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("CALL editar_zona(%s, %s)", (id, nombre))
        conexion.commit()
    conexion.close()
    return {'mensaje': 'Zona actualizada exitosamente'}

def eliminar_zona(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("CALL eliminar_zona(%s)", (id,))
        conexion.commit()
    conexion.close()
    return {'mensaje': 'Zona eliminada exitosamente'}
