[app]
title = My Login App
package.name = loginapp
package.domain = org.arbab
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
