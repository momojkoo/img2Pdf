@echo off

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:" %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set "_OLD_CODEPAGE=%%a"
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

set "VIRTUAL_ENV=D:\work\img2pdf"
set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set "_OLD_CODEPAGE="
)

SET pyProgram=%VIRTUAL_ENV%\pdfMerge.py
python %pyProgram%

rem pause