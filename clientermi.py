import Pyro4

ns = Pyro4.locateNS()  # Localizamos el servidor de nombres

uri = ns.lookup('obj') # Y obtenemos la uri con el nombre simple

o = Pyro4.Proxy(uri)  # Ya que hemos subido el objeto al servidor para que
                      # los demás lo obtengan y con el Proxy lo obtenemos
                      # mediante la uri que seria el identificador


print(o.recolector()) # Nos retornara el numero de objetos que ha
                      # recolectado la función





                      