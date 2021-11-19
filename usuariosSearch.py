import unittest

class testUsuariosBusqueda(unittest.TestCase):

    def test_busqueda_correcta(self):

        dato = True
        self.assertTrue(dato)

    def test_busqueda_incorrecta(self):

        dato = False
        self.assertFalse(dato)

    #no es necesario el main
    #if __name__ == '__main__':
    #    unittest.main()

