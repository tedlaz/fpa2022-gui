python create_version.py
python create_nsi_installer.py
pyinstaller -F -w -i iso2fpa.ico iso2fpa.py
copy .\dist\iso2fpa.exe .
rd /S /Q dist
rd /S /Q build
del iso2fpa.spec
"C:\Program Files (x86)\NSIS\makensis.exe" installer.nsi
