import subprocess
import sys
from commons import *

def create_key_properties(keyAlias):
    with open('./android/key.properties',"w") as keyfile:
        keyfile.writelines(f"""storePassword=YOUR_STORE_PASSWORD
keyPassword=YOUR_KEY_PASSWORD
keyAlias={keyAlias}
storeFile=../../keys/keystore.jks
""")
    print("written key.properties")

def configure_build_config():
    print("configuring release config")
    readfile=open(appBuildPath,"r").readlines()
    temp = open(appBuildPath,'w')
    for line in readfile:
        if("android {" in line):
            temp.writelines("""
def keystoreProperties = new Properties()
def keystorePropertiesFile = rootProject.file('key.properties')
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
}

android {
            """)
        elif("buildTypes {" in line):
            temp.writelines("""
signingConfigs {
    release {
        keyAlias keystoreProperties['keyAlias']
        keyPassword keystoreProperties['keyPassword']
        storeFile file(keystoreProperties['storeFile'])
        storePassword keystoreProperties['storePassword']
    }
}
buildTypes {
            """)
        elif("signingConfig signingConfigs.debug" in line):
            temp.writelines("            signingConfig signingConfigs.release")
        else:
            temp.writelines(line)
    temp.close()

    print("configured release configs")


if __name__ == "__main__":
    create_key_properties(keyAlias=sys.argv[1])
    configure_build_config()