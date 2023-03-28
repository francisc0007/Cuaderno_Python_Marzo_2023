# escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) 
#y devuelve los días correspondiente del año, o devuelve None si alguno de los argumentos es inválido.


def isYearLeap(year):
    if year>1900:
        if (year%4)==0 and (year%100)==0 and (year%400)==0:
            return True
        else:
            return False
    else:
        return None
 
def daysInMonth(year, month):
    meses=[1,2,3,4,5,6,7,8,9,10,11,12]
    mesestre=[4,6,9,11]
    #mesestreuno=[1,3,5,7,8,10,12]
    x=isYearLeap(year)
    if month in meses:
        if month==2:
            if x:
                return 29
            else:
                return 28
        elif month in mesestre:
            return 30
        else:
            return 31
    else:
        return None
 
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 13]
testResults = [29, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
       # print(dayOfYear(2000, 12, 31))