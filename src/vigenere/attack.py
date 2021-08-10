from util.args_helper import letter_freq
import re

DEBUG_LOGGING = False
MAXIMUM_KEYSIZE = 30

def breaker(mensagem, lang_freq_list):
    regex = re.compile('[^a-zA-Z]')

    msg = regex.sub('', mensagem).lower()
    keysize = find_keysize(msg)
    if (keysize == 0):
        return "FALHA: Não foi possível encontrar a chave!"

    print("key size:", keysize)
    
    msg_freq = msg_letter_frequency(msg, keysize)
    result_key = ""
    for i in range(keysize):
        menor_diff = ('a', 999999999)
        for j in range(26):
            diff = 0
            for k in range(26):
                loop_chr = chr(ord('a') + k)
                shifted_chr = chr((ord(loop_chr)-ord('a') + j)%26 + ord('a'))
                if shifted_chr in msg_freq[i]:
                    diff += abs(msg_freq[i][shifted_chr] - lang_freq_list[loop_chr])

            if diff < menor_diff[1]:
                menor_diff = (chr(ord('a') + j), diff)

        result_key += menor_diff[0]

    return result_key

def find_keysize(msg):
    crivo = [0] * (MAXIMUM_KEYSIZE+1)
    for i in range(0, len(msg), 3):
        if i+3 >= len(msg):
            break

        c = msg[i:(i+3)]
        for j in range(i+3, len(msg)-2):
            if msg[j] != c[0] or msg[j+1] != c[1] or msg[j+2] != c[2]:
                continue

            dist = j-i
            if DEBUG_LOGGING:
                print(dist, '\t', msg[j], msg[j+1], msg[j+2], sep='', end='\t')

            for k in range(3, len(crivo)):
                if k > dist:
                    break

                if dist%k == 0:
                    crivo[k] += 1
                    if DEBUG_LOGGING:
                        print(k, end=' ')
            
            if DEBUG_LOGGING:
                print()

    return crivo.index(max(crivo))

def msg_letter_frequency(msg, keysize):
    i = 0
    res = [{} for i in range(keysize)]
    for i in range(len(msg)):
        if msg[i] in res[i%keysize]:
            res[i%keysize][msg[i]] += 1
        else:
            res[i%keysize][msg[i]] = 1
            
    return res
