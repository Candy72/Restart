#!/bin/bash
#The purpose of this program is to automate the installation of our packages!

#install cowsay
#sudo yum install -y cowsay
#echo cowsay installed | cowsay

#install jq
#sudo yum install -y | jq
#echo jq installed | cowsay


for package in cowsay jq tmux
do
        sudo yum install -y $package
        echo $package was installed | cowsay
done
