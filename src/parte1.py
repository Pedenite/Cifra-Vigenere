from vigenere.cipher import cifra
from util.args_helper import str2bool
import argparse
import sys

parser = argparse.ArgumentParser(description='Cifra e decifra mensagens usando a cifra de Vigenère.' + 
    '\nSe não passados argumentos, será requisitada a mensagem e a chave durante a execução do programa', 
    formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('mensagem', nargs='?', type=argparse.FileType('r'), help='Arquivo com a mensagem a ser cifrada/decifrada')
parser.add_argument('senha', nargs='?', type=argparse.FileType('r'), help='Arquivo com a chave de criptografia')
parser.add_argument('-o', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='Arquivo de saída (Se não informado, será exibida a saída no terminal)', metavar='output')
parser.add_argument('-d', nargs='?', type=str2bool, const=True, default=False, help='Especifica que a mensagem deve ser decifrada na execução (padrão: cifrar)', metavar='decifrar')

args = parser.parse_args()

msg = pswd = ""

if args.mensagem == None:
    msg = input("Mensagem/Criptograma > ")
else:
    with args.mensagem as file:
        msg = file.read()

if args.senha == None:
    pswd = input("Senha > ")
else:
    with args.senha as file:
        pswd = file.read()

if len(pswd) == 0 or not ascii(pswd).strip("'").isalpha():
    raise Exception(f'Senha Inválida: {pswd}')

res = cifra(msg, pswd, args.d)

with args.o as file:
    if file == sys.stdout:
        print(res)
    else:
        print(res, end='', file=file)
