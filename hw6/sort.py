import os
import shutil
import argparse
import re
from pathlib import Path

#all extensions our script knows
images=('.jpeg', '.png', '.jpg', '.svg', ".webp",".JPG",".PNG")
video=('.avi', '.mp4', '.mov', '.mkv',".MP4")
docs=('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
music=('.mp3', '.ogg', '.wav', '.amr')
archs=('.zip', '.gz', '.tar')
#all known by script extensions
known_ext=set(images+video+docs+music+archs)

#list of dirs and lists of the extensions
lists=[images,video,docs,music]
dirs_=["another", "archives"]
dirs=["images","videos","docs","music"]
dirs_set=set(dirs+dirs_)

#for translition
CYRILLIC = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
LATIN = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC, LATIN):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

#arguments for the console
parser = argparse.ArgumentParser(description="sort files by type")
parser.add_argument("folder_path")
args = parser.parse_args()

#dictionary of the sorted files
files_dict={
    "images":[],
    "videos":[],
    "docs":[],
    "music":[],
    "archives":[],
    "another":[],
}

#set to remember all extensions we met
extension_set=set()

path = args.folder_path

def normalize(line):
    separate=line.rsplit(".", 1)
    line = separate[0]
    line = line.translate(TRANS)
    line = re.sub(r"[^a-zA-Z0-9]", "_", line)
    try:
        return str(line+"."+separate[1])
    except IndexError:
        return(line)

def cut(ins):
    if len(ins)>20:
        ins=ins[:17] +"..."
    return ins

def move_empty_folders(path):
    with os.scandir(path) as files:
        for file in files:
            if file.name not in dirs_set:
                if os.path.isdir(file.path):
                    if file.name != "bin":
                        target_dir = os.path.join(path, "bin")
                        os.makedirs(target_dir, exist_ok=True)
                        shutil.move(file.path, os.path.join(target_dir, file.name))

    

def rename_all(path):
        with os.scandir(path) as files:
                for file in files:
                    if os.path.isdir(file):
                        rename_all(file.path)
                    else:
                        os.rename(file.path, os.path.dirname(file.path)+"/"+normalize(file.name))

def sort(path,path_=path):
    with os.scandir(path_) as files:
        for file in files:
            extension_set.add((Path(file.path).suffix))

            for list,dir in zip(lists,dirs):

                if file.name.endswith(list):
                    try:
                        files_dict[dir].append(file.name)
                        target_dir = os.path.join(path, dir)
                        os.makedirs(target_dir, exist_ok=True)
                        shutil.move(file.path, os.path.join(target_dir, file.name))
                    except FileNotFoundError:
                        continue
                    # print(f'{file.name} was succesfully moved to dir {dir}')

#scanning for zips and unarchivating them
                elif file.name.endswith(archs):
                    files_dict["archives"].append(file.name)
                    target_dir = os.path.join(path, "archives"+ "/" + normalize((file.name).rsplit(".",1)[0]))
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.unpack_archive(file.path, target_dir, file.name.rsplit(".",1)[1])

#recursivity
                elif os.path.isdir(file.path) and file.name not in dirs and file.name not in dirs_:
                    sort(path,path_+"/"+file.name)
#scanning for another files and extensions
    with os.scandir(path_) as files:
        for file in files:
            try:
                if os.path.isfile(file.path):
                    files_dict["another"].append(file.name)
                    target_dir = os.path.join(path, "another")
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file.path, os.path.join(target_dir, file.name))
            except FileNotFoundError:
                continue
    
                # print(f'{file.name} was succesfully moved to dir another')

    if extension_set != {""}:
        for i, _ in files_dict.items():
            print("|{:^25}|".format(""))
            print("|{:^25}|".format(i))
            for i in _:
                print("|{:^25}|".format(cut(i)))

        unknown_ext=extension_set-known_ext
        print(f"unknown by script extensions: {unknown_ext}")

        print(f"previously known by script extensions: {extension_set-unknown_ext}")
    else:
        print("No movement was performed")

sort(path)
rename_all(path)
move_empty_folders(path)
    