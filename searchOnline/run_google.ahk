#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

^G:: ;keybinding ctrl+g
Run, python3 .\main.py,, Hide
return