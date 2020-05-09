import os

searchFile = input("Название файла, который Вы хотите найти (с расширением)")
directory = os.getcwd()
isSearch = False

os.chdir(directory)
for root, dirs, files in os.walk(".", topdown = False):
	for name in files:
		if(name.lower() == searchFile.lower()):
			path = os.path.abspath(name)
			isSearch = True
if isSearch == False:
	print("Файла не суцествует")
else:
	print(path)
input()
