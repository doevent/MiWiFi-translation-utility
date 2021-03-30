# Xiaomi MiWiFi XML translation utility (English, Russian, others)

### Functions
Fills strings in a new file from an old file XML

### Instructions
1. Download Xiaomi MiWiFi APP [Android APP](http://www1.miwifi.com/miwifi_download.html) 
2. Unpack APK file [for example](https://github.com/kefir500/apk-editor-studio)
3. Сopy 4 files from unpack miwifi.APK: strings.xml, plurals.xml

```
\res\values\strings.xml and plurals.xml
in
values\strings.xml and plurals.xml
```
```
\res\values-zh-rCN\strings.xml and plurals.xml
in
values-zh-rCN\strings.xml and plurals.xml
```
4. Run python translator.py
5. New strings are copied to file: new_string.txt
6. Translate new strings in new_string.txt
7. Run python translator.py
8. Repack APK file

### Compatibility
* Python 3.4+
