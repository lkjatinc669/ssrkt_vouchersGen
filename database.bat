@echo off
cd receipt-app/database
python ss.py
cd ..
cd ..
del install.bat 
del requirements.txt
del database.txt 