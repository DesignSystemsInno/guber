import os
try:
    for i in os.listdir(r'C:\Users\Jairo\OneDrive - Universidad EAFIT\Documentos\Semillero Maria Helena\puntico'):
      
        for j in os.listdir(r'C:/Users/Jairo/OneDrive - Universidad EAFIT/Documentos/Semillero Maria Helena/puntico'+'/'+i):
            os.chdir(r'C:/Users/Jairo/OneDrive - Universidad EAFIT/Documentos/Semillero Maria Helena/puntico'+'/'+i)
            file = open(j,'r',encoding=enc)
            try:
                for f in file:
                    if (f.find(r"Decreto 2067")!= -1):
                        print(i,f)
                        file.close()
                        print("Se cambio de directorio",j)
                        os.replace(r'C:/Users/Jairo/OneDrive - Universidad EAFIT/Documentos/Semillero Maria Helena/filtrado'+'/'+i+'/'+j, r'C:/Users/Jairo/OneDrive - Universidad EAFIT/Documentos/Semillero Maria Helena/filtrado_decreto'+'/'+i+'/'+j)
                        break
                    else:
                        pass
            except UnicodeDecodeError:
                print("No se pudo")
                #file.close()
                #os.replace(r'C:/Users/Jairo/OneDrive - Universidad EAFIT/Documentos/Semillero Maria Helena/prueba_busqueda_todos'+'/'+i+'/'+j, r'C:/Users/Jairo/OneDrive - Universidad EAFIT/Documentos/Semillero Maria Helena/puntico'+'/'+i+'/'+j)
                pass
except NotADirectoryError:
    print("No se pudo")
    pass    
print(auxiliar)
#     file = open((i))
#     s = s + 1
#     try: 
#         for j in file:
            
#             if (j.find(r"con participaci\'f3n")!= -1):
#                 print(j)
#                 break
#     except UnicodeDecodeError:
#         print(i)
#         p = p + 1 

# print("el total de puntos es: ", p)
# print("el total son: ",s+p)
