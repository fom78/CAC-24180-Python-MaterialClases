# Son funciones que añaden funcionalidades a otras, lo estan decorando
# Esta formada por 3 funciones A,B y C,donde A recibe
# como parametro a B para devolver C. Siempre devuelve una funcion
#  Devolviendo esta funcion le da nuevas funcionalidades
# a la funcion que queremos decorar

#1- definir funciones suma - resta
#2- crear funcion decorador
#3- agregar decorador
#funcion A recibe parametro B
def funcion_decoradora(funcion_parametro):
    
    #funcion C
    def funcion_interior(a,b):

        #acciones adicionales que decoran
        print('Se inicia el calculo')
        funcion_parametro(a,b)
        #acciones adicionales que decoran
        print('Se ha terminado con el calculo')
    
    #retorno de la funcion C desde el decorador
    return funcion_interior




@funcion_decoradora
def suma(a,b):    
    print(a+b)

@funcion_decoradora
def resta(a,b):
    print(a-b)


suma(4,5)

resta(10,45)