import csv


archivo = open('dataset1.csv')


"""
==PROBLEM==
Informe de clima de la ciudad de salida y la ciudad de llegada para 3,000 tickets
from dataset1.csv file

==INPUT==
Origin format :: 3 Characters (TLC, MTY, MEX)
Destination format :: 3 Characters (TLC, MTY, MEX)
origin_latitude :: 19.0000 ~ 25.9999
origin_longitude :: -99.0000 ~ -100.9999
destination_latitude :: 19.0000 ~ 25.9999
destination_longitude :: -99.0000 ~ -100.9999

==CSV will Look like this==
origin,destination,origin_latitude,origin_longitude,destination_latitude,destination_longitude
TLC,MTY,19.3371,-99.566,25.7785,-100.107
... 2998 lines...
GDL,MEX,20.5218,-103.311,19.4363,-99.0721

"""