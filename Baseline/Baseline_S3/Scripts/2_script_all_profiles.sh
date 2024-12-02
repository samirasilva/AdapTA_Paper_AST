#!/bin/bash


#Example of call: 

if [[ "$#" -gt 4 ]]; then
    echo "Too many arguments were passed!"
    exit 1
fi

if [[ "$#" -eq 0 ]]; then
    execution_time=15
    number_of_executions=1
else
    execution_time=1
    number_of_executions=$2
fi

directory_ros="${HOME}/.ros/"
bsn_patient_folder="${HOME}/sa-bsn/src/sa-bsn/configurations/environment/"
bsn_sensors_folder="${HOME}/sa-bsn/src/sa-bsn/configurations/target_system/"

arquivos="$(find "../DTMCs/" -name "patient.launch")"


for ((j=0;j<"$number_of_executions";j++));do

   
   origin=$(pwd)

   for patient in ${arquivos}; do
    #echo "$(dirname ${patient})"

      if [ -z "$(ls -A ${bsn_patient_folder})" ]; then
         echo "Empty"
      else
      rm "${bsn_patient_folder}"*".launch"
      fi
      echo "${patient}"
      cp -a "${patient}" "${bsn_patient_folder}"
            
      p_folder="$(dirname ${patient})"
      #Create the output folder
      directory_Output="${p_folder}/output_${j}/"
      if [ ! -d "$directory_Output" ]; then
         mkdir -p "$directory_Output"
      fi
   
      
      cd "${HOME}/sa-bsn"
      source devel/setup.bash
      start=`date +%s`
      bash run.sh $execution_time
      end=`date +%s`
      temp="${directory_Output}time.txt"
      cd "$origin"
      echo `expr $end - $start` seconds. >> "$temp" 
      destiny="${directory_Output}g4t1_${i}-1-stdout.log"
      cp "${directory_ros}log/latest/g4t1-1-stdout.log" "$destiny"

      #exit
      
   done
done
