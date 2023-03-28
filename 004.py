#datos=100
#nativa=1007
#if datos==nativa:
#    print("Los Vlan son iguales")
#else:
  #  print("Las Vlan son diferentes")    

acl=int(input("Ingrese el # de ACL: "))
if acl >=1 and acl <=99:
        print("La ACL es estandar")
elif acl >=100 and acl <=199:
    print("La ACL es extendida")
else:
    print("El dato ingresado no es una ACL")
