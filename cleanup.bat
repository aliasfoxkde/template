@echo off
:: Run this script before commmiting so that python runtimes, 
:: HTML outputs, Kubix Generated Output files, and games are 
:: not included in the Repo. If you want to keep any files,
:: back them up outside of the git root directory without
:: cleanup.bat deleting them. Currenty, *.html, .kb* and 
:: *.pyc files are excluded with ".git/info/exclude".

:: Delete Python Bytecodes Files
del /S *.pyc

:: Deletes Generated HTML Files
del .\out\html\*.html

:: Deletes Generated Kb* files
del .\out\*.kb*

:: Deletes Generated "Games" (TBD)

:: Deletes python specific files and folders
rmdir "libs/__pycache__" /q
rmdir "docs/__pycache__" /q

TIMEOUT 3