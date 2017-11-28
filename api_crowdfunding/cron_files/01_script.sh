#! /bin/bash
PATH_RAW="/home/mvilchis/Desktop/csv"
FILE_OUTPUT="cf_grupos.json"

FILE_HEADER='{"results": ['
FILE_FOOTER=']}'

echo $FILE_HEADER > $FILE_OUTPUT
ls $PATH_RAW/| grep "CodigosGrupos"|while read indicador_acumulado
do

  tail -n +2 $PATH_RAW"/"$indicador_acumulado|sed "s/\"//g"|
  jq --slurp --raw-input --raw-output \
      'split("\n") | .[0:-1] | map(split(",")) |
          map({"id": .[0],
               "id3": .[1],
               "id2": .[2],
             })' >> $FILE_OUTPUT
done

echo $FILE_FOOTER >> $FILE_OUTPUT
