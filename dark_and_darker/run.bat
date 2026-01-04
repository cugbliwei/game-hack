@echo off
chcp 65001
echo ==========================================
echo      Dark And Darker Automation Setup
echo ==========================================

REM 检查 Python 是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Python，请先安装 Python 并添加到环境变量。
    pause
    exit /b
)

echo [INFO] 正在检查并安装依赖...
pip install pywinauto

echo.
echo [INFO] 依赖安装完成。
echo [INFO] 正在启动脚本...
echo.

python main.py

echo.
echo ==========================================
echo      脚本执行完毕
echo ==========================================
pause
