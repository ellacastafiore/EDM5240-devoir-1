#coding: utf-8

for year in range(1930,2018) :
    for number in range(0,1000) :
        print(str(year)[2:] + format(number, "03d"));

# Excellent! Ce second script, plus simple, corrige les problèmes du premier.