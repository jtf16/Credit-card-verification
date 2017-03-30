''' Projeto realizado pelo grupo 45: Miguel Carreiro, n82012, Jose Gomes n82015 e Joao Freitas n81950'''


import random
'''import random permite utilizar a funcao random, que esta localizada na biblioteca random '''

categoria1 = ('Companhias aereas','Companhias aereas e outras tarefas futuras da industria','Viagens e entretenimento e bancario / financeiro','Servicos bancarios e financeiros','Servicos bancarios e financeiros','Merchandising e bancario / financeiro','Petroleo e outras atribuicoes futuras da industria','Saude, telecomunicacoes e outras atribuicoes futuras da industria','Atribuicao nacional')
emissora = ('American Express','Diners Club International','Discover Card','Maestro','Master Card','Visa Electron','Visa')
abreviatura = ('AE','DCI','DC','M','MC','VE','V')
digitos_iniciais = (('34','37'),('309','36','38','39'),('65', ),('5018','5020','5038'),('50','51','52','53','54','19'),('4026','426','4405','4508'),('4024','4532','4556'))
num_digitos = (('15', ),('14', ),('16', ),('13','19'),('16', ),('16', ),('13','16'))
'''Estes tuplos permitem mais facilmente identificar emissoras baseado no tipo de dados que e tratado pela funcao. O indice dos elementos dos tuplos corresponde a uma emissora, p. ex., o indice 0 corresponde a American Express, o indice 1 corresponde ao Diners Club International, etc em todos os tuplos exceto o da categoria'''


def calc_soma(x):
    '''calc_soma : string -> int
       calc_soma faz o algoritmo de Luhn a partir do numero do cc'''
    x = x[::-1]
    x = list(map(int, x))
    

    cnt = 0
    
    while cnt < len(x):
        x[cnt] = x[cnt]*2
        cnt = cnt + 2
        
    cnt = 0
    
    while cnt < len(x):
        if x[cnt] > 9:
            x[cnt] = x[cnt]-9
            cnt = cnt + 1
        else:
            cnt = cnt + 1
    cnt = 0
    res = 0
    while cnt < len(x):
        res = x[cnt] + res
        cnt = cnt + 1
    return res


def luhn_verifica(y):
    '''luhn_verifica : str -> bool
       luhn_verifica se o numero inserido corresponde a alguma rede emissora'''
    x = eval(y) // 10 
    x = str(x)
    res = eval(y) % 10
    num = calc_soma(x) + res
    
    if num % 10 == 0:
        return True
    else:
        return False
    
def comeca_por(cad1, cad2):
    '''comeca_por : str1 x str2 -> bool
       comeca_por verifica se str1 comeca por str2'''
    if cad1[:len(cad2)] == cad2:
        return True
    else:
        return False
    
def comeca_por_um(cad, t_cads):
    '''comeca_por_um : str x tuple -> bool
       comeca_por_um verifica se cad comeca por um dos elementos do tuplo'''
    n=0
    while n < len(t_cads):
        if comeca_por(cad, t_cads[n]):
            return True
        n = n + 1
            
    return False

def valida_iin(x):
    '''valida_iin : str -> str
       valida_iin verifica a que emissora pertence o numero de cartao de credito inserido, se pertencer a uma'''
    m=0
    n=0
    while m < len(digitos_iniciais):
        while n < len(digitos_iniciais[m]):
            if x[:len(digitos_iniciais[m][n])] == digitos_iniciais[m][n]:
                emi = emissora[m]
                j = 0
                while j < len(num_digitos[m]):
                    if str(len(x)) == num_digitos[m][j]:
                        return emi
                    j = j + 1
            n = n + 1
        n = 0
        m = m +1
    return ''
    
def categoria(x):
    '''categoria : str -> str
       categoria verifica a categoria da entidade emissora do cartao de credito'''
    a = int(x[0])
    if a == 0:
        return ''
    else:
        return categoria1[a-1]
    
def verifica_cc(x):
    '''verifica_cc : int -> tuple
       verifica_cc devolve a categoria e a emissora do cartao de credito'''
    x = str(x)
    if luhn_verifica(x) == True:
        if valida_iin(x) != '':
            return (categoria(x), valida_iin(x))
        return 'cartao invalido'
    return 'cartao invalido'

def digito_verificacao(x):
    '''digito_verificacao : str -> str
       digito_verificacao verifica qual e o digito de verificacao que o numero deve do cartao de credito deve ter'''
    if calc_soma(x) % 10 == 0:
        return '0'
        
    return str(10 - (calc_soma(x) % 10))
    
def gera_num_cc(x):
    '''gera_num_cc : str -> int
       gera_num_cc gera um numero de cartao de credito aleatoriamente baseado a abreviatura da entidade emissora'''
    n = 0
    while n < len(abreviatura):
        if x == abreviatura[n]:
            break
        n = n + 1
    m = random.randint(0, len(digitos_iniciais[n])-1)
    a1 = digitos_iniciais[n][m]
    n1 = random.randint(0, len(num_digitos[n])-1)
    c = num_digitos[n][n1]
    
    b = 0
    res = eval(a1)
    while b < eval(c)-1-len(a1):
        n2 = random.randint(0, 9)
        res = res * 10 + n2
        b = b + 1
    return str(res) + digito_verificacao(str(res))