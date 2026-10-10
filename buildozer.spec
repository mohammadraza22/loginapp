[app]
title = My Login App
package.name = loginapp
package.domain = org.arbab
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.1.0
requirements = python3,kivy,pillow
orientation = portrait
fullscreen = 0
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
android.ndk = 25b
android.ndk_api = 21
p4a.branch = master
