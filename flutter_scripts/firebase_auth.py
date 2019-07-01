# This script adds firebase auth, google auth and required methods to flutter
import os
from distutils.dir_util import copy_tree


def add_firebase_auth():
    print("adding firebase auth")
    readfile=open("./pubspec.yaml","r").readlines()
    temp = open("./pubspec.yaml",'w')
    for line in readfile:
        if("dev_dependencies:" in line):
            temp.writelines("  firebase_auth: ^0.11.1+7\n  google_sign_in: ^4.0.2\n  provider: ^3.0.0+1\n\n")
        temp.writelines(line)
    print("added firebase auth, google sign in and provider package")

def add_google_services():
    print("adding google services")
    readfile=open("./android/build.gradle","r").readlines()
    temp = open("./android/build.gradle",'w')
    for line in readfile:
        temp.writelines(line)
        if("dependencies" in line):
            temp.writelines("        classpath 'com.google.gms:google-services:4.2.0'\n")
    temp.close()

    with open("./android/app/build.gradle","a") as file:
        file.write("\napply plugin: 'com.google.gms.google-services'\n")
    file.close()
    print("added google services")

def copying_files():
    print("copying stock files")
    file_name = __file__
    sc_dir = os.path.dirname(os.path.abspath(file_name))
    fromDirectory = sc_dir + os.path.sep + "lib"
    toDirectory = "./lib"
    copy_tree(fromDirectory, toDirectory)
    print("copied stock files")

def upgrade_to_androidx():
    print("upgrading to android x")
    needs_upgrade = True
    with open("./android/gradle.properties","r+") as file:
        content = file.readlines()
        file.seek(0)
        if("android.useAndroidX=true" in line for line in content):
            needs_upgrade = False
            print("Already using androidx")
        else:
            file.write("\nandroid.enableJetifier=true\nandroid.useAndroidX=true\n")
    file.close()
    if(needs_upgrade):
        readfile = open("./android/app/build.gradle","r").readlines()
        temp = open("./android/app/build.gradle","w")
        for line in readfile:
            if("testInstrumentationRunner" in line):
                temp.writelines("        testInstrumentationRunner \"androidx.test.runner.AndroidJUnitRunner\"\n")
            elif("androidTestImplementation 'com.android.support.test:runner" in line):
                temp.writelines("    androidTestImplementation 'androidx.test:runner:1.1.0'\n")
            elif("androidTestImplementation 'com.android.support.test.espresso:espresso-core" in line):
                temp.writelines("    androidTestImplementation 'androidx.test.espresso:espresso-core:3.1.0'\n")
            else:
                temp.writelines(line)

        temp.close()
        print("upgraded to android x")

if __name__ == "__main__":
    add_firebase_auth()
    upgrade_to_androidx()
    add_google_services()
    copying_files()