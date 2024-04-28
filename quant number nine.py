#coding: utf-8
#Program quant number nine
#DATE: 27/04/2024 DD/MM/YEAR
#Autor: Sonecav2

quantNumber = 0
for index in range(100):
    for jindex in range(len(str(index))):
        if str(index)[jindex] == "9":
            quantNumber = quantNumber + 1

print(f"The amount of number nine is {quantNumber}.")