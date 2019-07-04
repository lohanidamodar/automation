# Let's code the code
This repository contains my automation scripts, that I wrote to automate the tasks I find myself repeating.

## 1. create.py
This script along with the following bash function automates the process of creating a flutter project, initializing git, creating a private github repository and pushing the first commit to the master branch. (to run this you need change the username to your github username and instead of running this script directly, you should run from following bash function)

```
function fcreate() {
	echo -n Github Password: 
	read -s password
	echo
	flutter create "$1"
	cd "$1"
	git init
	git add .
	git commit -m "first commit"
	python <path_to>/create.py "$1" "$password"
	git remote add origin git@github.com:lohanidamodar/"$1".git
	git push -u origin master
}
```

### running this script
You need to add the above bash function to your `.bashrc` then you can run the following command from terminal in your flutter project folder and follow the instructions

```
fcreate <name_of_flutter_project>
```

***

## 2. web_blocker.py
This is a very simple script, that modifies the system's hosts file to block certain websites during specified period. Here I block facebook, gmail and netflix from 8 am to 4 pm of my work hours.

To make this work, you need to add path to your hosts file (works by default in linux), and you can change time and list of websites to your preference.

### running the script
This script is better run as a cron job.
[Use this Stackoverflow answer to setup cron job](https://askubuntu.com/questions/799023/how-to-set-up-a-cron-job-to-run-every-10-minutes)

***

## 3. firebase_auth.py
[Youtube video]() describing how to use this script and customize boilerplate code
This script setups firebase authentication with google and email based login automatically in a flutter project. Also copies boilerplate login ui flow using `provider` package for state management

In order for this script to work, you need 3 files and a folder together, the `firebase_auth.py`, `commons.py` and `.env` (sample env is provided) and the `lib` folder with boilerplate code.

Sample .env file
```
FIREBASE_AUTH=0.11.1+7
GOOGLE_SIGN_IN=4.0.2
PROVIDER=3.0.0+1
GOOGLE_SERVICES=4.2.0
```

### running this script
First, from terminal cd into the flutter project directory where you want to setup firebase authentication then run the following command

```
python3 <path_to_flutter_scripts>/firebase_auth.py
```

After running this script, you just need to do two things, import `ui/pages/home.dart` to main file and in MaterialApp home property replace existing with `HomePage()` widget from `ui/pages/home.dart`

***

## 4. google_maps.py
This script automatically sets up google maps flutter plugin on android platform in a flutter project. For this to work again you need the `google_maps.py`, `commons.py` and `.env` as above.

After you run the script in your flutter project you need to modify `android/app/src/main/res/values/strings.xml` file changing the text `YOUR_API_KEY` to your actual google maps Api key.

### running this script
First, from terminal cd into the flutter project directory where you want to setup google maps then run the following command

```
python3 <path_to_flutter_scripts>/google_maps.py
```

***

## 5. android_signing.py
This script along with the following bash function automates the process preparing android platform app of flutter for release. It helps you to create keystore, keys and performs all the config setup.

```
function fandsign() {
	echo -n keystore "alias"
	read keyAlias
	mkdir keys
	keytool -genkey -v -keystore ./keys/keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias "$keyAlias"
	python3 /home/dlohani/Documents/projects/automation/flutter_scripts/android_signing.py "$keyAlias"
}
```

### running this script
You need to add the above bash function to your `.bashrc` then you can run the following command from terminal in your flutter project folder and follow the instructions

```
fandsign
```

After running this command, you need to find `android/key.properties` file and need to add your keystore password and key alias password. After that you can just run `flutter build apk` to build release apk for your flutter application

***