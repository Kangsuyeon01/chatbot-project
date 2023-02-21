import json
import xmltodict
import argparse
import os
from tqdm import tqdm
def read_file(args):
    dir_path = args.datapath
    file_list = []
    for (root, directories, files) in os.walk(dir_path):
        for file in files:
            if '.xml' in file:
                file_path = os.path.join(root, file)
                file_list.append(file_path)
    return file_list

def xmlparser(args,files):
    save_path = args.savepath

    for i in tqdm(range(len(files))):
        with open(files[i],'r') as f:
            xmlString = f.read()
        
        print("xml input (xml_to_json.xml):")
        print(xmlString)

        jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)

        with open(save_path + files[i][len(args.datapath):-3] + "json", 'w') as f:
            f.write(jsonString)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--datapath", type=str, default="./xml_dataset")
    parser.add_argument("--savepath", type=str, default="./json_dataset")
    args = parser.parse_args()

    files = read_file(args)
    print("start!")
    xmlparser(args,files)
    print("END!")

