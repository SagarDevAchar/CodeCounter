import os
from datetime import datetime as dt


def printMultilineFormat(multiline_text, width, alignment):
    single_lines = multiline_text.split("\n")
    for single_line in single_lines:
        if len(single_line) > width:
            print(single_line)
        else:
            print(("{:%c%ds}" % (alignment, width)).format(single_line))


def scanCodeFiles(root_path):
    path_contents = os.listdir(root_path)

    for content in path_contents:
        current_path = root_path + "\\" + content

        if os.path.isdir(current_path):
            scanCodeFiles(current_path)
        else:
            try:
                if current_path[-3:] == '.py' or current_path[-4:] == '.pyw':
                    print("\r{:95s}".format(("\rScanning PY \"%s\"" % current_path.replace(PATH, ""))[:95]), end="")
                    with open(current_path, 'r', encoding='utf-8') as py_file:
                        PY_COUNT.append(len(py_file.readlines()))
                    SCAN_LIST.append(current_path)
                elif current_path[-2:] == '.c':# or current_path[-2:] == '.h':
                    print("\r{:95s}".format(("\rScanning C \"%s\"" % current_path.replace(PATH, ""))[:95]), end="")
                    with open(current_path, 'r', encoding='utf-8') as c_file:
                        C_COUNT.append(len(c_file.readlines()))
                    SCAN_LIST.append(current_path)
                elif current_path[-4:] == '.cpp':# or current_path[-4:] == '.hpp':
                    print("\r{:95s}".format(("\rScanning C++ \"%s\"" % current_path.replace(PATH, ""))[:95]), end="")
                    with open(current_path, 'r', encoding='utf-8') as cpp_file:
                        CPP_COUNT.append(len(cpp_file.readlines()))
                    SCAN_LIST.append(current_path)
                elif current_path[-5:] == '.java':
                    print("\r{:95s}".format(("\rScanning JAVA \"%s\"" % current_path.replace(PATH, ""))[:95]), end="")
                    with open(current_path, 'r', encoding='utf-8') as java_file:
                        JAVA_COUNT.append(len(java_file.readlines()))
                    SCAN_LIST.append(current_path)
                elif current_path[-4:] == '.ino':
                    print("\r{:95s}".format(("\rScanning INO \"%s\"" % current_path.replace(PATH, ""))[:95]), end="")
                    with open(current_path, 'r', encoding='utf-8') as ino_file:
                        INO_COUNT.append(len(ino_file.readlines()))
                    SCAN_LIST.append(current_path)
            except Exception as e:
                print("\rScanning of %s failed due to error : %s" % (content, str(e)))


def getTableHeader():
    table_header = ""

    for _ in FILE_TYPES:
        table_header += "+" + "-" * 12
    table_header += "+\n"
    for FILE_TYPE in FILE_TYPES:
        table_header += "| {:^10s} ".format(FILE_TYPE)
    table_header += "|\n"
    for _ in FILE_TYPES:
        table_header += "+" + "-" * 12
    table_header += "+"

    return table_header


def getTableData(func):
    table_data = ""

    for COUNT in TOTAL_COUNT:
        if func == "max":
            table_data += "| {:10d} ".format(max(COUNT))
        elif func == "min":
            table_data += "| {:10d} ".format(min(COUNT[1:]))
        elif func == "sum":
            table_data += "| {:10d} ".format(sum(COUNT))
        elif func == "len":
            table_data += "| {:10d} ".format(len(COUNT) - 1)
    table_data += "|\n"
    for _ in FILE_TYPES:
        table_data += "+" + "-" * 12
    table_data += "+\n"

    return table_data


program_name_artwork = r"""
   _____          _       _____                  _            
  / ____|        | |     / ____|                | |           
 | |     ___   __| | ___| |     ___  _   _ _ __ | |_ ___ _ __ 
 | |    / _ \ / _` |/ _ \ |    / _ \| | | | '_ \| __/ _ \ '__|
 | |___| (_) | (_| |  __/ |___| (_) | |_| | | | | ||  __/ |   
  \_____\___/ \__,_|\___|\_____\___/ \__,_|_| |_|\__\___|_|   
                                                              """

results_artwork = r"""
  _____                 _ _       
 |  __ \               | | |      
 | |__) |___  ___ _   _| | |_ ___ 
 |  _  // _ \/ __| | | | | __/ __|
 | | \ \  __/\__ \ |_| | | |_\__ \
 |_|  \_\___||___/\__,_|_|\__|___/
                                  """

printMultilineFormat(program_name_artwork, 100, "^")
print("{:^100s}".format("By Sagar Dev Achar (https://github.com/SagarDevAchar)"))
print("\n" + "=" * 100)

PATHS = input("Enter the Directory Paths : ").strip().replace("\"", "").split("|")

print("\nStarting Scan...")

FILE_TYPES = [".py .pyw",
              ".c",
              ".cpp",
              ".java",
              ".ino"]

PY_COUNT = [0]
C_COUNT = [0]
CPP_COUNT = [0]
JAVA_COUNT = [0]
INO_COUNT = [0]

SCAN_LIST = []

for PATH in PATHS:
    PATH = PATH.strip()
    print("\nScanning for files in \"%s\"" % PATH)
    scanCodeFiles(PATH)

print("\r{:100s}".format("Scanning Complete!"))
print("=" * 100)
TOTAL_COUNT = [PY_COUNT, C_COUNT, CPP_COUNT, JAVA_COUNT, INO_COUNT]

printMultilineFormat(results_artwork, 100, "^")
print("\n{:^100s}".format(dt.now().strftime("%d %B %Y")))

print("\n Total number of Code Files Found : %d" % (len(PY_COUNT) - 1 +
                                                    len(C_COUNT) - 1 +
                                                    len(CPP_COUNT) - 1 +
                                                    len(JAVA_COUNT) - 1 +
                                                    len(INO_COUNT) - 1))

print(getTableHeader())
print(getTableData("len"))

print("\n Total number of Lines Coded : %d lines" % (sum(PY_COUNT) +
                                                     sum(C_COUNT) +
                                                     sum(CPP_COUNT) +
                                                     sum(JAVA_COUNT) +
                                                     sum(INO_COUNT)))

print(getTableHeader())
print(getTableData("sum"))

print("\n Longest Code Written : %d lines" % (max(max(PY_COUNT),
                                                  max(C_COUNT),
                                                  max(CPP_COUNT),
                                                  max(JAVA_COUNT),
                                                  max(INO_COUNT))))

print(getTableHeader())
print(getTableData("max"))

with open("scan_list.txt", "w") as txt:
    for ITEM in SCAN_LIST:
        txt.write(ITEM + "\n")

print("\nscan-list.txt generated!")

print("\n" + "=" * 100)

input("\nPress ENTER to exit...")
