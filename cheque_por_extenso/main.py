class Cheque_por_extenso:
    tradutor = {
            1 : 'um',
            2 : 'dois',
            3 : 'três',
            4 : 'quatro',
            5 : 'cinco',
            6 : 'seis',
            7 : 'sete',
            8 : 'oito',
            9 : 'nove',
            10: 'dez',
            11: 'onze',
            12: 'doze',
            13: 'treze',
            14: 'quatorze',
            15: 'quinze',
            16: 'dezesseis',
            17: 'dezessete',
            18: 'dezoito',
            19: 'dezenove',
            20: 'vinte',
            30: 'trinta',
            40: 'quarenta',
            50: 'cinquenta',
            60: 'sessenta',
            70: 'setenta',
            80: 'oitenta',
            90: 'noventa',
            100:'cem',
            200:'duzentos',
            300:'trezentos',
            400:'quatrocentos',
            500:'quinhentos',
            600:'seiscentos',
            700:'setecentos',
            800:'oitocentos',
            900:'novecentos'
        }
        
    def __init__(self, valor=None):
        self.valor = valor
           
    def __call__(self, valor):
        self.valor = valor
        return self.escreve_cheques(self.valor)

    def escreve_cheques(self, valor):
        reais = valor // 1
        centavos = round((valor % 1) * 100)
        if reais and centavos:
            return (self.escreve_reais(reais)+' e '+self.escreve_centavos(centavos)+'.').capitalize()
        if reais and not centavos:
            return (self.escreve_reais(reais)+'.').capitalize()
        if centavos and not reais:
            return (self.escreve_centavos(centavos)+'.').capitalize()

    def escreve_reais(self, valor):
        if valor >= 1000:
            return self.escreve_milhares(valor)+' reais'
        elif valor > 99:
            return self.escreve_centena(valor)+' reais'
        elif valor > 1:
            return self.escreve_dezena(valor)+' reais'
        else:
            return 'um real'

    def escreve_centavos(self, valor):
        if valor == 1:
            return 'um centavo'
        else:
            return self.escreve_dezena(valor)+' centavos'
    
    def escreve_milhares(self, valor):
        milhar = valor // 1000
        centena = valor % 1000
        if centena == 0:
            return self.escreve_centena(milhar)+' mil'
        else:
            return self.escreve_centena(milhar)+' mil '+self.escreve_centena(centena)

    def escreve_centena(self, valor):
        centena = (valor//100)*100
        dezena = valor%100
        if centena == 0:
            return self.escreve_dezena(dezena)
        if dezena == 0:
            return self.tradutor[valor]
        elif valor < 200:
            return 'cento e '+self.escreve_dezena(dezena)
        elif valor==0:
            return ''
        else:
            return self.tradutor[centena]+' e '+self.escreve_dezena(dezena)

    def escreve_dezena(self, valor):
        if valor==0:
            return ''
        elif valor <= 20:
            return self.tradutor[valor]
        else:
            if valor % 10 == 0:
                return (self.tradutor[valor])
            else:
                return (self.tradutor[(valor // 10) * 10]+' e '+self.tradutor[valor % 10])

        


