from zipfile import ZipFile
import csv
import os.path
import matplotlib

path = './world_population.csv'
file_is_extracted = os.path.isfile(path)
results_is_created = os.path.isfile('./last_results.txt')
          
if(not file_is_extracted):
    with ZipFile("./archive.zip", 'r') as zObject: zObject.extractall('./')

with open(path, 'r') as csv_file:
    if results_is_created:
        os.remove("./last_results.txt")
        
    new_file = open('./last_results.txt', 'w') 
    reader = csv.reader(csv_file, delimiter=',')
    headers = next(reader)
    results_text = ""
    

        
    for row in reader:
        iterable = zip(headers, row)
        country_dict = {key: value for key, value in iterable}
        results_text = results_text+'\n'+str(country_dict)  
        
    new_file.write(results_text)
        
os.remove("./world_population.csv")



    