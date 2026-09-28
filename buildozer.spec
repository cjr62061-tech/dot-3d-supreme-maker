[app]
title = Dot 3D Maker
package.name = dot3dmaker
package.domain = com.dot3d.supreme

source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd,opencv,numpy,pillow

[buildozer]
log_level = 2

# Android settings
[app:android]
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,CAMERA
android.api = 33
icon.filename = %(source.dir)s/IMG-20260929-WA4255.jpg
