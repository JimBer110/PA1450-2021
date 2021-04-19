import os
from application import case
from datetime import datetime

def importData():
    cases = []
    countries = {}
    for fileName in os.listdir(os.path.dirname(__file__)+"/covid_case_data/"):
        with open(os.path.dirname(__file__)+"/covid_case_data/"+fileName, encoding='utf-8-sig') as f:
            text = f.readlines()
            form = getFormat(text[0])
            for line in text[1:]:
                covid_case=splitLine(line)
                country = covid_case[form['CountryRegion']].replace(" ", "")
                province = covid_case[form['ProvinceState']].replace(" ", "")
                if (country not in countries.keys()):
                    countries.update({country:{province:[len(cases)]}})
                elif province not in countries[country].keys():
                    countries[country].update({province:[len(cases)]})
                else:
                    countries[country][province].append(len(cases))
                createCase(cases,covid_case,form)
    data = {}
    data['cases'] = cases
    data['countries'] = countries
    return data

def createCase(listOfCases,caseToAdd,form):
    index = len(listOfCases)
    listOfCases.append(case.Case())
    content=[]
    if 'FIPS' in form.keys() and caseToAdd[form['FIPS']] !='':
        listOfCases[index].setFips(int(caseToAdd[form['FIPS']]))
        content.append('FIPS')
    if 'Admin2' in form.keys()and caseToAdd[form['Admin2']] !='':
        listOfCases[index].setAdmin2(caseToAdd[form['Admin2']])
        content.append('Admin2')
    if 'ProvinceState' in form.keys()and caseToAdd[form['ProvinceState']] !='':
        listOfCases[index].setProvinceState(caseToAdd[form['ProvinceState']])
        content.append('ProvinceState')
    if 'CountryRegion' in form.keys()and caseToAdd[form['CountryRegion']] !='':
        listOfCases[index].setCountryRegion(caseToAdd[form['CountryRegion']])
        content.append('CountryRegion')
    if 'LastUpdate' in form.keys()and caseToAdd[form['LastUpdate']] !='':
        try:
            datetime_object = datetime.fromisoformat(caseToAdd[form['LastUpdate']])
        except:
            try:
                caseToAdd[form['LastUpdate']] = '0'+caseToAdd[form['LastUpdate']]
                datetime_object = datetime.strptime(caseToAdd[form['LastUpdate']], '%m/%d/%y %H:%M')
            except:
                datetime_object = datetime.strptime(caseToAdd[form['LastUpdate']], '%m/%d/%Y %H:%M')
        listOfCases[index].setLastUpdate(datetime_object)   
        content.append('LastUpdate')                
    if 'Lat' in form.keys()and caseToAdd[form['Lat']] !='':
        listOfCases[index].setLat(float(caseToAdd[form['Lat']]))
        content.append('Lat')
    if 'Long' in form.keys()and caseToAdd[form['Long']] !='':
        listOfCases[index].setLong(float(caseToAdd[form['Long']]))
        content.append('Long')
    if 'Confirmed' in form.keys()and caseToAdd[form['Confirmed']] !='':
        listOfCases[index].setConfirmed(int(caseToAdd[form['Confirmed']]))
        content.append('Confirmed')
    if 'Deaths' in form.keys()and caseToAdd[form['Deaths']] !='':
        listOfCases[index].setDeaths(int(caseToAdd[form['Deaths']]))
        content.append('Deaths')
    if 'Recovered' in form.keys()and caseToAdd[form['Recovered']] !='':
        listOfCases[index].setRecovered(int(float(caseToAdd[form['Recovered']])))
        content.append('Recovered')
    if 'Active' in form.keys()and caseToAdd[form['Active']] !='':
        listOfCases[index].setActive(int(caseToAdd[form['Active']]))
        content.append('Active')
    if 'CombinedKey' in form.keys()and caseToAdd[form['CombinedKey']] !='':
        listOfCases[index].setCombinedKey(caseToAdd[form['CombinedKey']])
        content.append('CombinedKey')
    if 'IncidentRate' in form.keys()and caseToAdd[form['IncidentRate']] !='':
        listOfCases[index].setIncidentRate(float(caseToAdd[form['IncidentRate']]))
        content.append('IncidentRate')
    if 'CaseFatalityRatio' in form.keys()and caseToAdd[form['CaseFatalityRatio']] !='' and caseToAdd[form['CaseFatalityRatio']] !='#DIV/0!':
        listOfCases[index].setCaseFatalityRatio(float(caseToAdd[form['CaseFatalityRatio']]))
        content.append('CaseFatalityRatio')
    if 'IncidenceRate' in form.keys()and caseToAdd[form['IncidenceRate']] !='':
        listOfCases[index].setIncidenceRate(float(caseToAdd[form['IncidenceRate']]))
        content.append('IncidenceRate')
    listOfCases[index].setForm(content)
        

def getFormat(line):
    form = {}
    line = splitLine(line)
    for l in range(len(line)):
        s1="".join(c for c in line[l] if c.isalpha())
        if (s1=='Latitude'):
            s1='Lat'
        elif (s1=='Longitude'):
            s1='Long'
        form.update({s1:l})
    return form

def splitLine(lines):
    if(lines.find('"')!=-1):
        newlist = lines.split(",")
        newlist[len(newlist)-1]=newlist[len(newlist)-1].rstrip("\n")
        index= []

        for word in range(len(newlist)):
            if(newlist[word].find('"')!=-1):
                index.append(word)
                newlist[word]=newlist[word].replace('"',"")
                
        while (len(index)>0):
            newlist[index[-2]:index[-1]+1]=[''.join(newlist[index[-2]:index[-1]+1])]
            index.pop(-1)
            index.pop(-1)

    else:
        newlist = lines.split(",")
        newlist[len(newlist)-1]=newlist[len(newlist)-1].rstrip("\n")
    
    return newlist
