import timeit
import json
import yaml
from yaml import SafeLoader
def prog():
    with open("EntrFile.yaml", encoding = "utf-8") as f:
        yaml_string = f.read()
    #print(yaml_string)
    python_dict=yaml.load(yaml_string, Loader=SafeLoader)
    file=open("dop1.json","w")
    json.dump(python_dict, file, indent = 2)
    file.close()
print(timeit.timeit(prog, number = 100))

# В выходном файле нет [], и русские буквы не переводятся из ascii
