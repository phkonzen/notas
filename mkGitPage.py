import os

os.chdir("./AnaliseMatematica")
os.system("make html")
os.system("rm -rf ../docs/AnaliseMatematica")
os.system("mv html ../docs/AnaliseMatematica")
