import json
from datetime import datetime
import os
import api

def createFile(inData,form,country):
    export = {country:{}}
    if country =='worldwide':
        for case in inData['cases']:
            time = case['update'].strftime('%Y-%m-%d')
            if case['province'] != None:
                province = case['province']
            else:
                province = case['country']
            nation = case['country']  
            if time not in export[country].keys():
                    export[country].update({time:{}})
            if nation not in export[country][time].keys():
                export[country][time].update({nation:{}})
            export[country][time][nation].update({province:{}})
            if form[0]=='1':
                export[country][time][nation][province].update({'Confirmed':case['confirmed']})
            if form[1]=='1':
                export[country][time][nation][province].update({'Active':case['active']})
            if form[2]=='1':
                export[country][time][nation][province].update({'Deaths':case['deaths']})
            if form[3]=='1':
                export[country][time][nation][province].update({'Recovered':case['recovered']})
    else:
        for case in inData['cases']:
            time = case['update'].strftime('%Y-%m-%d')
            province = case['province']
            if case['country']== country:   
                if time not in export[country].keys():
                    export[country].update({time:{}})
                export[country][time].update({province:{}})
                if form[0]=='1':
                    export[country][time][province].update({'Confirmed':case['confirmed']})
                if form[1]=='1':
                    export[country][time][province].update({'Active':case['active']})
                if form[2]=='1':
                    export[country][time][province].update({'Deaths':case['deaths']})
                if form[3]=='1':
                    export[country][time][province].update({'Recovered':case['recovered']})
    with open('export.json', 'w') as outfile: 
        json.dump(export, outfile)
    return os.path.dirname(__file__)