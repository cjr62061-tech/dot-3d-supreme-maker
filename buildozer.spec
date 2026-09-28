[app]
title = Dot3DMaker
package.name = dot3dmaker
package.domain = com.dot3d.maker
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True
p4a.bootstrap = sdl2
p4a.branch = master