#!/bin/ksh

#show the selected wheather on the xenodm upper bar


archivo_ciudad="api/garin.json"
archivo_ciudades="api/argentina.json"

function clima
{
estado=$(jq -r --arg ciudad "$ciudad" '.wheater[] | select(.ciudad==$ciudad)| .estado' "$archivo_ciudades")
maxima=$(jq -r --arg ciudad "$ciudad" '.wheater[] | select(.ciudad==$ciudad)|.maxima' "$archivo_ciudades")
minima=$(jq -r --arg ciudad "$ciudad" '.wheater[] | select(.ciudad==$ciudad)|.minima' "$archivo_ciudades")

if [[ ! -z "$estado" ]]; then
echo "$ciudad | Maxima: $maxima | Minima: $minima | $estado"
fi

}

function clima_ciudad
{
ciudad=$(jq -r '.wheater[0].ciudad' $archivo_ciudad)
temperatura=$(jq -r '.wheater[0].temperatura' $archivo_ciudad)
termica=$(jq -r '.wheater[0].termica' $archivo_ciudad)

if [[ ! -z "$temperatura" ]]; then
echo "$ciudad > Temperatura: $temperatura | Sensacion Termica: $termica"
fi
}

	
ciudad="Buenos Aires"

clima

clima_ciudad
