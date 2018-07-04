import os, shutil

if os.path.exists('dist'):
	shutil.rmtree("dist")
if os.path.exists('build'):
	shutil.rmtree("build")
if os.path.exists('__pycache__'):
	shutil.rmtree("__pycache__")

os.system("pyinstaller -F -i images/s2m.ico generate-iru2dot-message.py")
shutil.copyfile("dist/generate-iru2dot-message.exe", "./generate-iru2dot-message.exe")
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")