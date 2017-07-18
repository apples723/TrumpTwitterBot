@echo off
git add * 
git commit -m "some changes auto added by update script.bat at %date% %time%" 
git push origin master 