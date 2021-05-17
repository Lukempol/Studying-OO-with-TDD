import unittest
from main import *

class TestChequeExtenso(unittest.TestCase):
    def test_exite_valor(self): 
        cheque = Cheque_por_extenso(27)
        #cheque(27)
        self.assertEqual(cheque.valor, 27)
   
    def test_centavos_uma_palavra(self):
        cheque = Cheque_por_extenso()
        self.assertEqual(cheque(0.01), 'Um centavo.')
        self.assertEqual(cheque(0.05), 'Cinco centavos.')
        self.assertEqual(cheque(0.08), 'Oito centavos.')
        self.assertEqual(cheque(0.11), 'Onze centavos.')
        self.assertEqual(cheque(0.15), 'Quinze centavos.')
        self.assertEqual(cheque(0.18), 'Dezoito centavos.')

    def test_centavos_duas_palavras(self):
        cheque = Cheque_por_extenso()
        self.assertEqual(cheque(0.27), 'Vinte e sete centavos.')
        self.assertEqual(cheque(0.54), 'Cinquenta e quatro centavos.')
        self.assertEqual(cheque(0.89), 'Oitenta e nove centavos.')
    
    def test_reais_uma_palavra_sem_centavos(self):
        cheque = Cheque_por_extenso()
        self.assertEqual(cheque(1), 'Um real.')
        self.assertEqual(cheque(11), 'Onze reais.')
        self.assertEqual(cheque(19), 'Dezenove reais.')
        self.assertEqual(cheque(7), 'Sete reais.')
        self.assertEqual(cheque(12), 'Doze reais.')
        self.assertEqual(cheque(3), 'Três reais.')

    def test_reais_uma_palavra_com_centavos(self):
        cheque = Cheque_por_extenso()
        self.assertEqual(cheque(1.49), 'Um real e quarenta e nove centavos.')
        self.assertEqual(cheque(11.25), 'Onze reais e vinte e cinco centavos.')
        self.assertEqual(cheque(20.33), 'Vinte reais e trinta e três centavos.')
        self.assertEqual(cheque(7.09), 'Sete reais e nove centavos.')
        self.assertEqual(cheque(13.61), 'Treze reais e sessenta e um centavos.')
        self.assertEqual(cheque(3.48), 'Três reais e quarenta e oito centavos.')

    def test_reais_duas_palavras_com_centavos(self):
        cheque = Cheque_por_extenso()
        self.assertEqual(cheque(21.49), 'Vinte e um reais e quarenta e nove centavos.')
        self.assertEqual(cheque(33.25), 'Trinta e três reais e vinte e cinco centavos.')
        self.assertEqual(cheque(67.33), 'Sessenta e sete reais e trinta e três centavos.')
        self.assertEqual(cheque(101.49), 'Cento e um reais e quarenta e nove centavos.')
        self.assertEqual(cheque(313.25), 'Trezentos e treze reais e vinte e cinco centavos.')
        self.assertEqual(cheque(670.33), 'Seiscentos e setenta reais e trinta e três centavos.')

    def test_reais_tres_palavras_com_centavos(self):
        cheque = Cheque_por_extenso()
        self.assertEqual(cheque(421.49), 'Quatrocentos e vinte e um reais e quarenta e nove centavos.')
        self.assertEqual(cheque(933.25), 'Novecentos e trinta e três reais e vinte e cinco centavos.')
        self.assertEqual(cheque(567.33), 'Quinhentos e sessenta e sete reais e trinta e três centavos.')
        self.assertEqual(cheque(181.49), 'Cento e oitenta e um reais e quarenta e nove centavos.')
        self.assertEqual(cheque(323.25), 'Trezentos e vinte e três reais e vinte e cinco centavos.')
        self.assertEqual(cheque(674.33), 'Seiscentos e setenta e quatro reais e trinta e três centavos.')

    def test_milhares_reais__sem_centavos(self):
        cheque = Cheque_por_extenso()
        self.assertEqual(cheque(2145), 'Dois mil cento e quarenta e cinco reais.')
        self.assertEqual(cheque(11000), 'Onze mil reais.')
        self.assertEqual(cheque(14903), 'Quatorze mil novecentos e três reais.')
        self.assertEqual(cheque(7369), 'Sete mil trezentos e sessenta e nove reais.')
        self.assertEqual(cheque(13061), 'Treze mil sessenta e um reais.')
        self.assertEqual(cheque(3480), 'Três mil quatrocentos e oitenta reais.')

    def test_milhares_reais__com_centavos(self):
        cheque = Cheque_por_extenso()
        self.assertEqual(cheque(2000.45), 'Dois mil reais e quarenta e cinco centavos.')
        self.assertEqual(cheque(11500.09), 'Onze mil quinhentos reais e nove centavos.')
        self.assertEqual(cheque(14903.27), 'Quatorze mil novecentos e três reais e vinte e sete centavos.')
        self.assertEqual(cheque(7369.01), 'Sete mil trezentos e sessenta e nove reais e um centavo.')
        self.assertEqual(cheque(113000.45), 'Cento e treze mil reais e quarenta e cinco centavos.')
        self.assertEqual(cheque(3480.30), 'Três mil quatrocentos e oitenta reais e trinta centavos.')

    def test_centenas_milhares_reais__com_centavos(self):
        cheque = Cheque_por_extenso()
        self.assertEqual(cheque(122000.45), 'Cento e vinte e dois mil reais e quarenta e cinco centavos.')
        self.assertEqual(cheque(411500.09), 'Quatrocentos e onze mil quinhentos reais e nove centavos.')
        self.assertEqual(cheque(814903.27), 'Oitocentos e quatorze mil novecentos e três reais e vinte e sete centavos.')
        self.assertEqual(cheque(607369.01), 'Seiscentos e sete mil trezentos e sessenta e nove reais e um centavo.')
        self.assertEqual(cheque(113000.45), 'Cento e treze mil reais e quarenta e cinco centavos.')
        self.assertEqual(cheque(203480.30), 'Duzentos e três mil quatrocentos e oitenta reais e trinta centavos.')