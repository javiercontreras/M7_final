from django.db import connection

def Inmuebles_Region(region_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM gestion_inmuebles_comuna WHERE region_id = %s", [region_id])
        resultados = cursor.fetchall()
        for i in resultados:
            print(i[1])

