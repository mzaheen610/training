
file = 'Files_and_Exceptions\image.jpg'

with open(file,"rb", buffering=0) as image_obj:
    contents = image_obj.readlines()

print(contents)