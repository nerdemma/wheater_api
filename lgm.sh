#!//bin/ksh

# Archivo de configuracion personalizado xenodm gestor de interfaz de usuario GNU/Linux, UNIX BSD. 
# Desarrollado por @nerdemma https://github.com/nerdemma/xenodm

#llamando a la api meteorologica

."/wheater.sh"
resultado=${wheater}
echo "$resultado"
	
"./wheatercity.sh"
