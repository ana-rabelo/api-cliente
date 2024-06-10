def cpf_valido(num_cpf):
    return len(num_cpf) == 11

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(num_rg):
    return len(num_rg) == 9

def celular_valido(num_celular):
    return len(num_celular) >= 11