import os
import xmltodict
import json
import codecs
path = './files'
converted='./converted'
for filename in os.listdir(path):
    # path to the file to convert
    path_file=path+"/{}".format(filename)
    with open(path_file, 'r') as content_file:
        # content file in the json format
        content=json.dumps(xmltodict.parse(content_file.read()))
        # decode the \\ to \
        # content=codecs.decode(content, 'unicode_escape')
        # new path file for the file in the json format
        new_path_file=converted+"/{}.json".format(os.path.splitext(filename)[0])
        with open(new_path_file, "w") as f:
           f.write(content)
print("The process has finished.")
