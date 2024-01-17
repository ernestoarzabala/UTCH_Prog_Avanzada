texto = "Universidad Tecnologica de Chihuahua"
print("len(texto) ",len(texto))
print("texto[0]=",texto[0],"| texto[1]=",texto[1])
print("texto[-1]=",texto[-1],"| texto[-2]=",texto[-2])
print("texto[0:3]=",texto[0:3],"| texto[12:]=",texto[12:],"| texto[:12]=",texto[:12])
print("texto[:-13]=",texto[:-13],"| texto[12:-13]=",texto[12:-13],"| texto[-24:-13]=",texto[-24:-13])
print("Posicion palabra 'Chihuahua':",texto.find("Chihuahua"))
print("Cambiar palabra 'Chihuahua' por 'Camargo':",texto.replace("Chihuahua","Camargo"))
print("Dividir antes de la palabra 'de':",texto.split('de'))