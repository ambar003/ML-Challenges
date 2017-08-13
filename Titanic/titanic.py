import numpy as np 
import csv as csv

csv_file_object = csv.reader(open('train.csv'))
header = next(csv_file_object)
data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)
# print(np.shape(data))
# print(data)

number_passengers = np.size(data[1:,1].astype(np.float))
# print(number_passengers)
number_survived = np.sum(data[1:,1].astype(np.float))
# print(number_survived)

no_of_women = data[0:,4] == "female"
# print(np.size(no_of_women))
no_of_men = data[0:,4] != "female"
# print(np.size(no_of_men))

women_onboard = data[no_of_women,1].astype(np.float)
men_onboard = data[no_of_men,1].astype(np.float)
# print(np.size(women_onboard))
# print(np.size(men_onboard))    

women_survived = np.sum(women_onboard)/np.size(women_onboard)
men_survived = np.sum(men_onboard) / np.size(men_onboard)

# print(women_survived)
# print(men_survived)

test_file = open('test.csv')
test_file_object = csv.reader(test_file)
header = next(test_file_object)

prediction_file = open('genderbasemodel.csv','w', newline='')
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:       
    if row[3] == 'female' or (len(row[4])!=0 and len(row[1])!=0 and float(row[4])<18 and float(row[1])<=2):                                          
        prediction_file_object.writerow([row[0],'1'])   
    else:                                
        prediction_file_object.writerow([row[0],'0'])
test_file.close()
prediction_file.close()
