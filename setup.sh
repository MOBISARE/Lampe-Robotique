#!/bin/bash



#Exécuter la configuration waf

cd robot_dart/

./waf configure

./waf examples

cd ..



#Setup du projet

source_dir="./Lampe-Robotique/"





#Copie du fichier lampe.cpp

file_lampe_cpp="lampe.cpp"

destination_dir="./robot_dart/src/examples/"





if [ -e "$sourcce_dir$file_lampe_cpp" ] 

then

	cp "$source_dir$file_lampe_cpp" "$destination_dir"

	echo "Le fichié a été copié avec succès"

	

else

	echo "Le fichier n'existe pas dans le répertoire source"

fi



#Copie du fichier lampe.hpp

file_lampe_hpp="lampe.hpp"

destination_dir="./robot_dart/src/robot_dart/robots/"



if [ -e "$sourcce_dir$file_lampe_hpp" ] 

then

	cp "$source_dir$file_lampe_hpp" "$destination_dir"

	echo "Le fichié a été copié avec succès"

	

else

	echo "Le fichier n'existe pas dans le répertoire source"

fi



cd robot_dart/

./waf examples --targets=lampe

build/lampe
