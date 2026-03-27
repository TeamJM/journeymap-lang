@echo off
setlocal
set SCRIPT_DIR=%~dp0

py -3 "%SCRIPT_DIR%tool\update_lang_files.py" %*
if %errorlevel%==0 exit /b 0

python "%SCRIPT_DIR%tool\update_lang_files.py" %*
if %errorlevel%==0 exit /b 0

python3 "%SCRIPT_DIR%tool\update_lang_files.py" %*
exit /b %errorlevel%
