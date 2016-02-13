# android-game
python based game/platform for android

### compiling from sources
not an exact science but something like:
- get android studio
 - make sure you have sdk version 19
- clone this repository
 - open in android studio, go File > Project Stucture, click to download ndk
- create android python distribution
 - install python-for-android
   - `pip install git+https://github.com/kivy/python-for-android.git`
 - install virtualenv
   - `pip install virtualenv`
 - create distribution
   - `ANDROIDAPI=19 ANDROID_NDK_HOME="/path/to/ndk" ANDROID_HOME="/path/to/sdk" p4a create --dist_name=android --bootstrap=sdl2 --requirements=python2`
 - copy `python-install` from resulting distribution to `app/src` inside the android studio project directory
   - note: after this you don't require python-for-android or any of its directories it created, so you can get rid of them
- copy `python-install/lib/libpython2.7.so` to `app/src/main/jniLibs/armeabi-v7a`
- zip files in `python-install/lib/python2.7/` (no parent folder) and move to `app/src/main/assets/lib.zip`
