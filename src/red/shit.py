'''
Created on 08/07/2017

@author: 
'''
import logging
import sys
import math

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def red_shit_es_primo(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def red_shit_precaca(mierda, putadas):
    mierda.extend([sys.maxsize, 1, 1, 1, 2])
    for ass in range(5, 41):
        mierda.append(mierda[ass - 1] + mierda[ass - 4])
    
    conta_caca = 0
    for ass in range(217287):
        if red_shit_es_primo(ass):
            conta_caca += 1
        putadas.append(conta_caca)
        
def red_shit_core(caca, mierda):
    vale_verga = 0
    vale_verga = mierda[caca]
    return vale_verga
    
def red_shit_main():
    mierda = []
    putadas = []
    lineas = list(sys.stdin)
    
    red_shit_precaca(mierda, putadas)
#    logger_cagada.debug("aora la mierda es %s y las putadas %s" % (mierda, putadas))
    
    for linea in lineas[1:]:
        if(not linea.strip()):
            break
        caca = int(linea)
        
        fuck = red_shit_core(caca, mierda)
        logger_cagada.debug("mierda %s" % fuck)
        fuck = putadas[fuck]
        print(fuck)
    
    



if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        red_shit_main()
