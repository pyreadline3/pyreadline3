@echo off

:: get the project root directory
set PROJECT_ROOT_DIR=%~dp0\..\

pushd .
cd %PROJECT_ROOT_DIR%
set PROJECT_ROOT_DIR=%CD%
popd

:: start VS Code: assume it is installed
Start "" /D """%PROJECT_ROOT_DIR%""" "Code" .
