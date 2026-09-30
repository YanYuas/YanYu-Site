@echo off
chcp 65001 >nul
title YanYu 数学建模知识库
cd /d "%~dp0"

echo ========================================
echo   YanYu 数学建模知识库 · 一键启动
echo ========================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo [错误] 没有找到 Python，请先安装 Python 3.10 或更高版本
    echo 下载地址：https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [1/2] 正在启动本地预览服务器...
echo [2/2] 浏览器将自动打开 http://127.0.0.1:8000
echo.
echo 提示：关闭这个黑色窗口即可停止服务器。
echo       修改 docs 里的文件后，网页会自动刷新。
echo.

start "" "http://127.0.0.1:8000"
python -m mkdocs serve -a 127.0.0.1:8000

echo.
echo 服务器已停止。
pause
