import Pyro4
import gc
i = 0
@Pyro4.expose

class ServidorRMI:

    def recolector(self):

        # Las listas se borran cada vez que se ejecuta una colección completa
        # o una colección de la generación más alta (2)

        recolectado = gc.collect() # o también gc.collect(2)
        print ("Recolector de Basura: %d objetos recolectados." % (recolectado))
 
        print ("Creando ciclos...")
        for i in range(10):

            # Se crea un ciclo y en cada iteracion x como un diccionario se le 
            # asigna 1

             x = { }
             x[i+1] = x
             print (x)
 
        recolectado = gc.collect()
 
        print ("Recolector de Basura: %d objetos recolectados." % (recolectado))

        return recolectado

daemon = Pyro4.Daemon()  #Iniciamos y llamamos a ese Daemon de Pyro4

uri = daemon.register(ServidorRMI) # registramos nuestro objeto en el Daemon y al 
                                   # registrarlo esto nos retorna lo que es la 
                                   # identificación al cual vamos a llamar: uri

ns = Pyro4.locateNS()  # Localizamos un servidor de nombres para no tener que 
                       # copiar la uri en el Proxy de cliente

ns.register('obj', uri) # Registramos el objeto, le pasamos el nombre simple 'obj'
                        # y la uri

print(uri) # imprimimos la uri para poder ver cual es

daemon.requestLoop() # Le decimos al Daemon que inicie, es decir, que inicie su Loop



