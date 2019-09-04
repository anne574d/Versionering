import os
import subprocess

class GitOutput:
	def __init__(self, cmd):
		self.output = os.popen("git " + cmd).read()

	def IsInRepository(self):
		index = self.output.find("not a git repository")
		return (index is -1)

	def HasUntrackedFiles(self):
		index = self.output.find("Untracked files:")
		return (index is not -1)

	def HasChangesToBeCommitted(self):
		index = self.output.find("Changes to be committed:")
		return (index is not -1)

	def HasUnstagedChanges(self):
		index = self.output.find("Changes not staged for commit:")
		return (index is not -1)

gitter = GitOutput("status")

if not gitter.IsInRepository():
	print("Dette er ikke et git repository")
else:
	if gitter.HasUntrackedFiles():
		print("Der er untracket filer i dette repository")
	elif gitter.HasChangesToBeCommitted():
		print("Der er ucommittet ændringer i dette repository")
	elif gitter.HasUnstagedChanges():
		print("Der er unstaged ændringer i dette repository")
	else:
		print("Alt er vel her...")