[app]
title = Dot3DMaker
package.name = dot3dmaker
package.domain = com.dot3d.supreme
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd,numpy,opencv

[buildozer]
log_level = 2

[app:android]
orientation = portrait
fullscreen = 0
permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,CAMERA
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.build_tools_version = 33.0.2