import unittest

class test_usuarios(unittest.TestCase):

    def test_usuarios_creados(self):

        usuario = 'Pepe'
        self.assertEqual(usuario, 'Pepe')


    def test_usuario_no_creado(self):

        respuesta = 'El usuario no ha creado'
        self.assertEqual(respuesta, 'El usuario no ha creado')


    #no es necesario el main

    #if __name__ == '__main__':
    #    unittest.main()

