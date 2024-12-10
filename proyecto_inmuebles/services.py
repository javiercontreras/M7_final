from django.db import connection

def raw_inmuebles():
    with connection.cursor() as cursor:
        cursor.execute("SELECT comuna.nombre AS Comuna, nombre_inmueble, descripcion FROM gestion_inmuebles_inmueble AS inmueble INNER JOIN gestion_inmuebles_comuna AS comuna ON inmueble.comuna_id = comuna.id ;")
        results = cursor.fetchall()
        for row in results:
            print(row)

raw_inmuebles()