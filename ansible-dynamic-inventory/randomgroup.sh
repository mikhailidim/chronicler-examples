#!/bin/sh
set +x
if [ "$1" == "--list" ]; then
 echo -e '{ "static_group": {\n\t"hosts": [ "localhost"]},'
 echo -e ' "dynamic_group": {\n\t"hosts": ['
 # Calcualte second group member
 coin=$(( $RANDOM % 2 )) 
 if [ $coin -ge 1 ]; then
  echo -e '"localhost"]},'
 else  
  echo -e ']},'
 fi
 echo -e '"_meta": {"hostvars": {}}\n}'

elif [ "$1" == "--host" ]; then   
  echo '{"_meta": {"hostvars": { }}}'
else
 echo "{ }"
fi 
