# This script adds firebase auth, google auth and required methods to flutter
import os
from distutils.dir_util import copy_tree
from commons import *

envs = getEnv()
firebaseAuthDependencies=f"  firebase_auth: ^{envs['FIREBASE_AUTH']}\n  google_sign_in: ^{envs['GOOGLE_SIGN_IN']}\n  provider: ^{envs['PROVIDER']}\n\n"
gradlePropertiesPath="./android/gradle.properties"

def add_firebase_auth():
    print("adding firebase auth")
    general_find_add_after(file=pubspecPath,beforeLine="dev_dependencies",linesToAdd=firebaseAuthDependencies)
    print("added firebase auth, google sign in and provider package")

def add_google_services():
    print("adding google services")
    readfile=open(projectBuildPath,"r").readlines()
    temp = open(projectBuildPath,'w')
    for line in readfile:
        temp.writelines(line)
        if("dependencies" in line):
            temp.writelines(f"        classpath 'com.google.gms:google-services:{envs['GOOGLE_SERVICES']}'\n")
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
    with open(gradlePropertiesPath,"r+") as file:
        if("android.useAndroidX=true" in file.read()):
            needs_upgrade = False
            print("Already using androidx")
        else:
            file.write("\nandroid.enableJetifier=true\nandroid.useAndroidX=true\n")
    file.close()
    if(needs_upgrade):
        readfile = open(appBuildPath,"r").readlines()
        temp = open(appBuildPath,"w")
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