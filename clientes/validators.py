import re
from validate_docbr import CPF

def cpf_valido(num_cpf):
    cpf = CPF()
    return cpf.validate(num_cpf)

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(num_rg):
    return len(num_rg) == 9

def celular_valido(num_celular):
    """Verifica se o número de celular é válido. 
    O número deve seguir o padrão: 11 91234-1234"""
    
    regex_celular = r'^[0-9]{2} 9[0-9]{4}-[0-9]{4}$'
    return re.match(regex_celular, num_celular) is not None