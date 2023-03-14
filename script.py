# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
BLC Communication and Security Systems
AYPOS Project PDU Data Recording

author: @Burak Gumus
"""

import subprocess
import datetime
import time

def split_string (data):
    seperator="\""
    parts = data.split(seperator,1)
    return tuple(parts)

def spl (data):
    test = split_string(data)[1]
    test2 = split_string(test)[0]
    return test2

now = datetime.datetime.now()
data_format = "time,voltaje,current,energy"
record = open("/home/virbox/Desktop/12_Socket.txt", "w")
record2 = open("/home/virbox/Desktop/13_Socket.txt", "w")  
record.write(data_format)
record2.write(data_format)

start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(hours=6)
count= 0

while datetime.datetime.now() < end_time:
    
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    energy_12   =  subprocess.Popen([r"snmpget","-v1","-c","public","10.150.1.89","iso.3.6.1.4.1.30966.7.1.10.12.0"], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
    current_12  =  subprocess.Popen([r"snmpget","-v1","-c","public","10.150.1.89","iso.3.6.1.4.1.30966.7.1.8.1.12.0"], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
    voltaj_c1  =  subprocess.Popen([r"snmpget","-v1","-c","public","10.150.1.89","iso.3.6.1.4.1.30966.7.1.3.1.4.0"], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
    v1=spl(voltaj_c1)
    c1=spl(current_12)
    e1=spl(energy_12)
    formatted= now_str,v1,c1,e1
    formatted2= str(",".join(formatted))
    record.write("\n"+formatted2)
    
    energy_13  =  subprocess.Popen([r"snmpget","-v1","-c","public","10.150.1.89","iso.3.6.1.4.1.30966.7.1.10.13.0"], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
    current_13 =  subprocess.Popen([r"snmpget","-v1","-c","public","10.150.1.89","iso.3.6.1.4.1.30966.7.1.8.1.13.0"], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
    voltaj_c2  =  subprocess.Popen([r"snmpget","-v1","-c","public","10.150.1.89","iso.3.6.1.4.1.30966.7.1.3.2.4.0"], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
    v2=spl(voltaj_c2)
    c2=spl(current_13)
    e2=spl(energy_13)
    formatted3= now_str,v2,c2,e2
    formatted4= str(",".join(formatted3))
    record2.write("\n"+formatted4)
    time.sleep(2)
    print("flag",count)
    count= count+2
    
record.close()
record2.close()
