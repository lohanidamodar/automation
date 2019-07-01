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