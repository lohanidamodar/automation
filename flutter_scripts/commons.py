import os

pubspecPath ="./pubspec.yaml"
stringsPath="./android/app/src/main/res/values/strings.xml"
manifestPath = "./android/app/src/main/AndroidManifest.xml"
appBuildPath = "./android/app/build.gradle"
projectBuildPath = "./android/build.gradle"

def general_find_add_after(file, beforeLine, linesToAdd):
    readfile=open(file,"r").readlines()
    temp = open(file,'w')
    for line in readfile:
        if(beforeLine in line):
            temp.writelines(linesToAdd)
        temp.writelines(line)

def getEnv():
    file_name = __file__
    sc_dir = os.path.dirname(os.path.abspath(file_name))
    envpath = sc_dir + os.path.sep + ".env"
    envdict={}
    with open(envpath,'r') as file:
        for line in file.readlines():
            line = line.strip("\r\n")
            if line:
                arr = line.split("=")
                envdict[arr[0]]=arr[1]
    file.close()
    return envdict


if __name__ == "__main__":
    envs = getEnv()