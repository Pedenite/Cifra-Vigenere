from vigenere.attack import breaker
import util.args_helper as a_h
import argparse
import sys

parser = argparse.ArgumentParser(description='Tenta quebrar uma mensagem cifrada pela cifra de Vigenère.' + 
    '\nSe não passados argumentos, será requisitado o criptograma durante a execução do programa', 
    formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('mensagem', nargs='?', type=argparse.FileType('r'), help='Arquivo com o criptograma')
parser.add_argument('-o', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='Arquivo de saída (Se não informado, será exibida a saída no terminal)', metavar='output')
parser.add_argument('-p', nargs='?', type=a_h.str2bool, const=True, default=False, help='Define a língua da mensagem do criptograma para português (padrão: Inglês)', metavar='ptbr')

args = parser.parse_args()

msg = ""

if args.mensagem == None:
    msg = input("Criptograma > ")
else:
    with args.mensagem as file:
        msg = file.read()

res = breaker(msg, a_h.letter_freq(args.p))

with args.o as file:
    if file == sys.stdout:
        print(res)
    else:
        print(res, end='', file=file)
