
import os

#Para DOS/Windows
os.system ("cls") 

try:
    archivo = open( 'prueba.txt' , 'rt', encoding = 'utf-8' )
    print( archivo.read() )
except Exception as e:
    print(e)
finally:
    archivo.close()