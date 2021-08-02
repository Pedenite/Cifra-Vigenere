def cifra(mensagem, senha_raw, opt):
    senha = processa_senha(senha_raw)
    res = ''
    i = 0
    for c in mensagem:
        if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
            res += cifra_letra(c, senha[i], 'a' if c >= 'a' else 'A', opt)
            i = (i+1) % len(senha)
        else:
            res += c

    return res

def processa_senha(senha):
    res = []
    for c in senha.lower():
        res.append(ord(c) - ord('a'))

    return res

def cifra_letra(letra, k, case, opt):
    n = ord(letra) - ord(case)
    if opt:
        n -= k
    else:
        n += k

    return chr((n%26) + ord(case))
