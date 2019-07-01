from commons import *

googleMapPlugin = "  google_maps_flutter: ^0.5.19\n\n"
mapApiKey="        <meta-data android:name=\"com.google.android.geo.API_KEY\" android:value=\"@string/map_api_key\"/>"

def add_google_map():
    print("adding google map")
    general_find_add_after(file=pubspecPath,beforeLine="dev_dependencies",linesToAdd=googleMapPlugin)
    print("added google maps plugin 0.5.19")

def add_key_to_manifest():
    print("adding key to manifest")
    general_find_add_after(file=manifestPath,beforeLine="<activity",linesToAdd=mapApiKey)
    print("added key to manifest")

def setup_api_key():
    print("setting up api key metadata")
    with open(stringsPath,'w') as file:
        file.writelines("""
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="map_api_key">YOUR_API_KEY</string>
</resources>        
""")
    file.close()



if __name__ == "__main__":
    add_google_map()
    setup_api_key()
    add_key_to_manifest()