SABORES=[]
COBERTURAS=[]
TOTALGD=0
VAL=1
def IMPRIMIRSABORES():
  A=1
  for i in SABORES: 
    print(A,') ',i[0],(' '*(20-len(i[0]))),i[1],(' '*(5)),i[2],(' '*(5)))
    A+=1
def IMPRIMIRCOBERTURAS():
  A=1
  for i in COBERTURAS: 
    print(A,') ',i[0]+(' '*(20-len(i[0]))),i[1],(' '*(5)),i[2],(' '*(5)))
    A+=1
def MENU():
  print('MENU PRINCIPAL\n1. COMPRAR\n2. AGREGAR UN NUEVO PRODUCTO\n3. VER INVENTARIO\n4. AGREGAR AL INVENTARIO\n5. TOTAL DE VENTAS DEL DIA\nq: SALIR')
  OPC=input()
  return OPC
def VENTA():
  INV=0
  INVC=0
  for i in SABORES:
    INV=0
    if i[2]!=0 or SABORES==[]:
      INV=1
      break
  for j in COBERTURAS:
    INVC=0
    if j[2]!=0 or COBERTURAS==[]:
      INVC=1
      break
  if INV==0:
    print('NO HAY DISPONIBILIDAD EN EL INVENTARIO')
    return
  if INVC==0:
    print('NO HAY DISPONIBILIDAD DE COBERTURAS')
    return
  print('NUEVA VENTA:\nESCOJA UN SABOR:')
  IMPRIMIRSABORES()
  A=int(input())
  if A>len(SABORES):
    print('ENTRADA INVALIDA,POR FAVOR INTENTE NUEVAMENTE')
    return
  SAB=SABORES[A-1]
  print('USTED SELECCIONO:\n',SAB[0]+(' '*(20-len(SAB[0]))),SAB[1],(' '*(5)),SAB[2],(' '*(5)),('\nCUANTAS PORCIONES?'))
  PORC=int(input())
  print('DESEA COBERTURA?(s/n):')
  DESCOB=input()
  COBERTURA=0
  if DESCOB == ('s'):
    print('ESCOJA UNA COBERTURA:')
    IMPRIMIRCOBERTURAS()
    COB=COBERTURAS[int(input())-1]
    COBERTURA=COB[1]
    print('USTED SELECCIONO:\n',COB[0]+(' '*(20-len(COB[0]))),COB[1],(' '*(5)),COB[2],(' '*(5)))
  if DESCOB !=('s') and DESCOB !=('n'):
    print('\nPORFAVOR SELECCIONE UNA DE LAS OPCIONES VALIDAS')
    return  
  TOTAL=(SAB[1]*PORC+COBERTURA)
  print('\nTOTAL A PAGAR:   ',TOTAL)
  global TOTALGD 
  TOTALGD+=TOTAL
  SAB[2]-=PORC
  COB[2]-=1

def AGREGAR():
  NUEVOPRODCUTO=[]
  print('TIPO DE PRODUCTO (1 o 2)\n1. HELADO\n2. COBERTURA\nq. SALIR')
  OPC=input()
  if OPC==('1'):
    print('INGRESE EL NOMBRE DEL PRODUCTO')
    NOMBRE=input()
    print('INGRESE EL VALOR DE PORCION')
    VALORPORC=int(input())
    print('INGRESE EL NUMERO DE PORCIONES DISPONIBLES')
    PORCIONES=int(input())
    NUEVOPRODCUTO.append(NOMBRE)
    NUEVOPRODCUTO.append(VALORPORC)
    NUEVOPRODCUTO.append(PORCIONES)
    global SABORES
    SABORES.append(NUEVOPRODCUTO)
  elif OPC==('2'):
    print('INGESE EL NOMBRE DEL PRODUCTO')
    NOMBRE=input()
    print('INGRESE EL VALOR DE PORCION')
    VALORPORC=int(input())
    print('INGRESE EL NUMERO DE PORCIONES DISPONIBLES')
    PORCIONES=int(input())
    NUEVOPRODCUTO.append(NOMBRE)
    NUEVOPRODCUTO.append(VALORPORC)
    NUEVOPRODCUTO.append(PORCIONES)
    global COBERTURAS
    COBERTURAS.append(NUEVOPRODCUTO)
  elif  OPC==('q'):
    return
  else:
     print('\nENTRADA INVALIDA,POR FAVOR INTENTE NUEVAMENTE')
     return
def INVENTARIO():
  print('INVENTARIO\n\n')
  print('HELADOS')
  if SABORES==[]:
    print('NADA :(')
  IMPRIMIRSABORES()
  print('\nCOBERTURAS')
  if COBERTURAS==[]:
    print('NADA :(')
  IMPRIMIRCOBERTURAS()
  print('\n\n')
def AGREGARINVENTARIO(): 
  print('TIPO DE PRODUCTO (1 o 2)\n1. HELADO\n2. COBERTURA\nq. SALIR')
  OPC=input()
  if OPC==('1'):
    if SABORES==[]:
        print('NO HAY SABORES A LOS QUE AGREGAR PORCIONES')
        return
    print('SELECCIONE UN PRODUCTO')
    IMPRIMIRSABORES()
    SABOR=int(input())
    SELECCION=SABORES[SABOR-1]
    print('USTED SELECCIONÓ:\n',SELECCION[0]+(' '*(20-len(SELECCION[0]))),SELECCION[1],(' '*(5)),SELECCION[2],(' '*(5)),'\n\nINGRESE LA CANTIDAD DE PORCIONES A AÑADIR')
    SELECCION[2]+=int(input())
  elif OPC==('2'):
    if COBERTURAS==[]:
        print('NO HAY COBERTURAS A LAS QUE AGREGAR PORCIONES')
        return
    print('SELECCIONE UN PRODUCTO')
    IMPRIMIRCOBERTURAS()
    COB=int(input())
    SELECCION=COBERTURAS[COB-1]
    print('USTED SELECCIONÓ:\n',SELECCION[0]+(' '*(20-len(SELECCION[0]))),SELECCION[1],(' '*(5)),SELECCION[2],(' '*(5)),'\n\nINGRESE LA CANTIDAD DE PORCIONES A AÑADIR')
    SELECCION[2]+=int(input())
  elif  OPC==('q'):
    return
  else:
     print('\nENTRADA INVALIDA,POR FAVOR INTENTE NUEVAMENTE')
  return
def TOTALVD():
  print(TOTALGD)
print('******ADMIN HELADERIA********')
while VAL==1:
  X=MENU()
  if X==('1'):
    VENTA()
  elif X==('2'):
    AGREGAR()
  elif X==('3'):
    INVENTARIO()
  elif X==('4'):
    AGREGARINVENTARIO()
  elif X==('5'):
    TOTALVD()
  elif X==('q'):
    VAL=0  
  else:
    print('ENTRADA INVALIDA,POR FAVOR INTENTE NUEVAMENTE')


