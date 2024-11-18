import tabulate as tab
import numpy_financial as npf
import tabulate as tab


capital = 30000
tasa_1 = 8.5
calculo_tasa = (tasa_1/100)/12
tasa =  calculo_tasa
plazo = 24
cuota = round(npf.pmt(tasa, plazo, -capital, 0), 0)
saldo = capital
saldo_inicial =capital
datos = []

for i in range(1,plazo+1):
	pago_capital = npf.ppmt(tasa,i,plazo, -capital, 0)
	pago_int = cuota - pago_capital
	saldo -= pago_capital 
	saldo_inicial -= pago_capital
	linea = [i,  format(saldo_inicial, '0,.2f'),format(cuota, '0,.2f'),format(pago_capital, '0,.2f'),format(pago_int, '0,.2f'),format(saldo, '0,.2f')]
	datos.append(linea)
	#print(datos)
print(tab.tabulate(datos, headers=['Saldo Inicial','Cuota Mensual','Abono a Capital','Pago de Intereses','Saldo Final'], tablefmt='psql'))




