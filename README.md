# Xiaomi MiWiFi XML translation utility (English, Russian, others)

### Functions
Fills strings in a new file from an old file XML

### Instructions
1. Download Xiaomi MiWiFi APP [Android APP](http://www1.miwifi.com/miwifi_download.html) 
2. Unpack APK file [for example](https://github.com/kefir500/apk-editor-studio)
3. Rename and copy old translation files from this repository: strings.xml
```
lang_old\values\strings-en.xml
in 
values-strings.xml
```
```
lang_old\values-zh-rCN\strings-en.xml
in 
values-zh-rCN-strings.xml
```

4. Сopy two files from unpack miwifi.APK: strings.xml

```
\res\values\strings.xml
in
values\strings.xml
```
```
\res\values-zh-rCN\strings.xml
in
values-zh-rCN\strings.xml
```
5. Run python translator.py
6. New strings are copied to file: string.txt
7. Translate new strings and copy files back \res\values-zh-rCN and \res\values\strings.xml unpack APK
8. Repack APK file

### Compatibility
* Python 3.4+
