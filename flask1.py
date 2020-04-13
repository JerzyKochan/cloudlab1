#!/bin/python3

from flask import Flask
import os
import subprocess


app = Flask(__name__)

@app.route('/status')
def hello():
    output = ""
    os.environ["PATH"] += os.pathsep +"/bin/"
    os.environ["PATH"] += os.pathsep + "/sbin/"
    host = subprocess.check_output('hostname',shell=True).decode('utf-8')
    ip = subprocess.check_output('ifconfig eth0 | grep inet | grep -v inet6 | cut -d \  -f 10',shell=True).decode('utf-8')
    cpus = subprocess.check_output(' cat /proc/cpuinfo | grep processor | wc -l',shell=True).decode('utf-8')
    memGb = subprocess.check_output('echo  $(cat /proc/meminfo | grep MemTotal | sed -e "s/MemTotal:[ ]*//g" | sed -e "s/[^0-9]*$//g" ) / 1024 / 1024 | bc ',shell=True).decode('utf-8')
    output += "{\n"
    output +=' "hostname": "' + host.strip() + '",\n'
    output +=' "ip_address": "' + ip.strip() + '",\n'
    output +=' "cpus": "' + cpus.strip() + '",\n'
    output +=' "memory": "' + memGb.strip() + '",\n'
    output +="}\n"
    return output


