# escribir y probar una función que toma un argumento (un año) 
#y devuelve Verdadero si el año es bisiesto o Falso de lo contrario.



testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
def YearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
for i in range(len(testData)):
    year = testData[i]
    result = YearLeap(year)
    if result == testResults[i]:
        if result == True:
            print(f'{year} --> OK.')
        elif result == False:
            print(f'{year} --> Failed.')
