from .models import Usuario, Inmueble, Region, Comuna

def nuevo_usario(first_name:str, second_name:str, rut:str,telefono,direccion,tipo_usuario):
    usuario = Usuario(user_name = first_name, 
                      second_name = second_name, rut = rut, telefono = telefono, direccion = direccion, tipo_usuario = tipo_usuario)
    usuario.save()    
