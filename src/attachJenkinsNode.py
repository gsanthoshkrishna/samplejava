'''
Created on 21-Nov-2017

@author: Santhosh.Gade
'''
import json

jsonFile = open('outputfile.json')
jsonCont = json.load(jsonFile)
print jsonCont.public_dns