import os
import subprocess

cmd = "git status"
output = os.popen(cmd).read()

if output.find("Untracked files:"") is not -1:
	print("Du har filer du mangler at tilføje til dit repository!")
	
if output.find("Changes to be committed:") is not -1:
	print("Du har filer hvis ændringer ikke er blevet committet")
	