# import io

textFile = 'Files_and_Exceptions\sample_text.txt'
with open(textFile) as file_object:
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()
    # print(len(lines))
    # print(contents)
# for line in lines:
#     print(line.rstrip())
file_string = ''

for line in lines:
    file_string += line.strip()

# print(file_string)
# print(len(file_string))

secondFile = 'Files_and_Exceptions\copiedText.txt'
with open(secondFile,'w') as file_object:
    for line in lines:
        file_object.write(line.strip())

