import time
import xml.etree.ElementTree as ET
from os import listdir, path
import requests
import json


mypath = './hosts'
files = [path.join(mypath, f) for f in listdir(mypath) if f.endswith('.xml')]

for file in files:
    tree = ET.parse(file)
    root = tree.getroot()

    for name in root.findall('./hosts/host/name'):
        name = name.text
        print("name = " + name)
    for name in root.findall('./hosts/host/groups/group/name'):
        group = name.text
        print("group = " + group)

    for type_full in root.iter('type_full'):
        type_full = type_full.text
        print("modele = " + type_full)

    for os in root.iter('os'):
        os = os.text
        print("version de l'os = " + os)

    for vendor in root.iter('vendor'):
        vendor = vendor.text
        print("vendeur = " + vendor)

    for ip in root.iter('ip'):
       ip = ip.text
       print("IP = " + ip)
    print('\n')
