import json

with open ('vaccin.json') as f:
    data = json.load(f)

for vaccinationer in data['vaccinationer_tidsserie']:
    del (vaccinationer['slug'], vaccinationer['region'],vaccinationer['f_15l'],vaccinationer['f_70p'],vaccinationer['key'],vaccinationer['pop_15l'],vaccinationer['pop_70p'], vaccinationer['region_cat'])

for vaccinationer in data['vaccinerade_alder']:
    del (vaccinationer['slug'], vaccinationer['region'],vaccinationer['f_15l'],vaccinationer['f_70p'],vaccinationer['key'],vaccinationer['pop_15l'], vaccinationer['pop_70p'], vaccinationer['region_cat'])
   
for vaccinationer in data['vaccinerade_kommun']:
    del (vaccinationer['slug'], vaccinationer['f_15l'],vaccinationer['f_70p'],vaccinationer['key'],vaccinationer['knkod'],vaccinationer['knnamn'], vaccinationer['pop_70p'], vaccinationer['pop_15l'], vaccinationer['region_cat'])


for vaccinationer in data['vaccinerade_kommun_och_alder']:
    del (vaccinationer['kommun'], vaccinationer['lan'])

for vaccinationer in data['vaccinerade_tidsserie']:
    del (vaccinationer['slug'], vaccinationer['f_15l'],vaccinationer['f_70p'],vaccinationer['key'],vaccinationer['mapregion'], vaccinationer['pop_70p'], vaccinationer['pop_15l'], vaccinationer['region_cat'])



with open('ny_vaccin.json', 'w') as f:
    json.dump(data, f, indent=2)

