import unittest

import usuarios
import usuariosSearch
#import cuentas


#loader es donde cargamos las pruebas
loader = unittest.TestLoader()

#el loader va a terminar cargando nuestras pruebas en la suit
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(usuarios))
suite.addTests(loader.loadTestsFromModule(usuariosSearch))
#para correr un determinado test de una clase y no ejecutar todos de una (no se porque no funciona)
#suite.addTest(cuentas.Test_cuentas("test_cuentas_creadas"))

#verbosity es como el nivel de detalle
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)