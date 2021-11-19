import unittest

class Test_cuentas(unittest.case):

    def test_cuentas_creadas(self):
        cuenta = 12345
        self.assertEqual(cuenta, 121345)
