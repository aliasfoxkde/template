@echo off
:: Be careful, this script WILL override existing files. It grabs
:: files from other maintained repos, so that they don't need to 
:: be manually updated and two versions maintained.

:: Best Practices: Also, do not edit directly the files that will
:: be overwrote, instead update the repo where they reside or use
:: a custom module (in case of a fork or limited access).

:: Alternatively, you may want to delete this file if you created 
:: a fork.

:: Public Snippet Library
..\bin\tools\curl.exe "https://raw.githubusercontent.com/aliasfoxkde/snippets/master/snippets.py" --output snippets.py

TIMEOUT 5