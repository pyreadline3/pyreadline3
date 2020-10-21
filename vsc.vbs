
Option Explicit

Dim fsObj
Dim wshShell
Dim scriptDir
Dim strCommand1
Dim strCommand2

Set fsObj = CreateObject("Scripting.FileSystemObject")
Set wshShell = WScript.CreateObject("WScript.Shell")

scriptDir = fsObj.GetParentFolderName(WScript.ScriptFullName)

strCommand1 = Chr(34) & scriptDir & "\.vscode\pyenv.bat" & Chr(34)
strCommand2 = Chr(34) & scriptDir & "\.vscode\vsc.bat" & Chr(34)

' x = msgbox(strCommand1,0, "Launch Command")
' x = msgbox(strCommand2,0, "Launch Command")

Call wshShell.Run(strCommand1, 1, True)
Call wshShell.Run(strCommand2, 0, True)
