#!/bin/bash

#Exécuter la configuration waf
cd /home/pal/robot_dart/
./waf configure
./waf examples
cd /home/pal/Lampe-Robotique

#Copie du fichier lampe.cpp
file_lampe_cpp="lampe.cpp"
destination_dir="../robot_dart/src/examples/"

if [ -e "$file_lampe_cpp" ] 
then
	cp "$file_lampe_cpp" "$destination_dir"
	echo "Le fichié a été copié avec succès"
else
	echo "Le fichier n'existe pas dans le répertoire source"
fi

#Copie du fichier lampe.hpp
file_lampe_hpp="lampe.hpp"
destination_dir="../robot_dart/src/robot_dart/robots/"

if [ -e "$file_lampe_hpp" ] 
then
	cp "$file_lampe_hpp" "$destination_dir"
	echo "Le fichié a été copié avec succès"
else
	echo "Le fichier n'existe pas dans le répertoire source"
fi

#Copie du fichier lampe.urdf
file_lampe_urdf="lampe.urdf"
destination_dir="../robot_dart/utheque/"

if [ -e "$file_lampe_urdf" ] 
then
	cp "$file_lampe_urdf" "$destination_dir"
	echo "Le fichié a été copié avec succès"
else
	echo "Le fichier n'existe pas dans le répertoire source"
fi

cd ../robot_dart/
./waf examples --targets=lampe