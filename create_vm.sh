#!/bin/bash

RESOURCE_GROUP=Lab3
MACHINE_NAME=${RESOURCE_GROUP}_m1
VM_CREATE_LOG=${MACHINE_NAME}_create.log

# az login
az login

# create resource group

az group create --name $RESOURCE_GROUP --location eastus

# create vm

az vm create --resource-group $RESOURCE_GROUP --name ${MACHINE_NAME} --generate-ssh-keys \
   --output json --image UbuntuLTS --verbose > $VM_CREATE_LOG

IP=$( cat $VM_CREATE_LOG | grep publicIpAddress| cut -d \" -f 4 )
ssh $IP -X "sudo apt-get update"
ssh $IP -X "sudo apt-get install python3"
ssh $IP -X "sudo apt-get install python3-flask"
ssh $IP -X "sudo apt-get install git"
ssh $IP -X "sudo apt-get install bc"
ssh $IP -X "git clone https://github.com/JerzyKochan/cloudlab1.git"
ssh $IP -X "chmod +x cloudlab1/flask1.py"
ssh $IP -X "export FLASK_APP=cloudlab1/flask1.py ; flask run --port=8080 --host=0.0.0.0"


