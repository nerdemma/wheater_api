#!/bin/ksh

#show the selected wheather on the xenodm upper bar

function wheater
{
estado=$(jq -r --arg ciudad "$ciudad" '.wheater[] | select(.ciudad==$ciudad)| .estado' "$archivo_json")
maxima=$(jq -r --arg ciudad "$ciudad" '.wheater[] | select(.ciudad==$ciudad)|.maxima' "$archivo_json")
minima=$(jq -r --arg ciudad "$ciudad" '.wheater[] | select(.ciudad==$ciudad)|.minima' "$archivo_json")

if [[ ! -z "$estado" ]]; then
echo "$ciudad | Maxima: $maxima | Minima: $minima | $estado"
fi

}

archivo_json="api/wheater_api.json"
ciudad="Buenos Aires"
wheater
