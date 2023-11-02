import csv

inputfile = 'Files_and_Exceptions\\business-operations-survey-2022-information-and-communications-technology.csv'
outputfile = 'business-operations-survey-2022-information-and-communications-technology-modified.csv'

def getStandard(value):
    if value > 1000:
        return "High"
    else:
        return "Low"

    
with open(inputfile) as input_object, open(outputfile,'w') as output_object:
    reader = csv.reader(input_object)
    writer = csv.writer(output_object)

    header = next(reader)
    header.append("standard")
    writer.writerow(header)

    for row in reader:
        value = row[5]
        # print(type(value))
        try:
            standard = getStandard(int(value))
        except ValueError:
            print(row)
            writer.writerow(row)
            print("Skipped a null value")
            continue
            
        row.append(standard)
        writer.writerow(row)


    
