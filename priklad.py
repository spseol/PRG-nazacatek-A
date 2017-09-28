#!/usr/bin/env python3
# Soubor:  priklad.py
# Datum:   28.09.2017 10:26
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################

n = input('Kolik členů posloupnosti se má tisknout? > ')
n = int(n)

x = 1
i = 1
while i <= n:
    i = i + 1
    if x % 5 == 0:
        print(-x, end=' ')
    else:
        print(x, end=' ')
    x = x + 2
print()    
