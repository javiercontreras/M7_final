from django.db import connection

def raw_inmuebles_comuna():
    with connection.cursor() as cursor:
        cursor.execute("SELECT comuna.nombre AS Comuna, nombre_inmueble, descripcion FROM gestion_inmuebles_inmueble AS inmueble INNER JOIN gestion_inmuebles_comuna AS comuna ON inmueble.comuna_id = comuna.id ;")
        results = cursor.fetchall()
        for row in results:
            print(row)

def raw_inmuebles_region_disponible():
    with connection.cursor() as cursor:
        cursor.execute("SELECT region_id, nombre_inmueble, descripcion FROM gestion_inmuebles_region AS region  INNER JOIN gestion_inmuebles_inmueble AS inmueble ON inmueble.region_id = region.id WHERE inmueble.disponible = True;")
        results = cursor.fetchall()
        for row in results:
            print(row)

def raw_inmuebles_region_no_disponible():
    with connection.cursor() as cursor:
        cursor.execute("SELECT region_id, nombre_inmueble, descripcion FROM gestion_inmuebles_region AS region  INNER JOIN gestion_inmuebles_inmueble AS inmueble ON inmueble.region_id = region.id WHERE inmueble.disponible = False;")
        results = cursor.fetchall()
        for row in results:
            print(row)

