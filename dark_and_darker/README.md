# Dark And Darker 自动化脚本

这是一个基于 `pywinauto` 的自动化辅助脚本，用于连接 "Dark And Darker" 游戏窗口并执行简单的模拟操作。

## 功能描述

1. **自动搜寻窗口**: 遍历系统当前运行的进程/窗口，查找标题包含 "Dark and Darker" 的窗口。
2. **进程连接**: 使用 UIA (User Interface Automation) 后端连接到游戏进程。
3. **模拟操作**: 
   - 目前实现了连接后的基础框架。
   - 包含了一个模拟点击窗口中心坐标的示例代码（默认为安全起见已注释实际点击动作）。
   - 在代码中提供了如何打印控件标识符 (`print_control_identifiers`) 的方法，方便后续开发识别游戏内UI元素。

## 如何运行

### 前置要求
- Windows 操作系统
- Python 3.x 已安装并添加到系统环境变量
- 游戏 "Dark And Darker" 正在运行

### 运行步骤
1. 双击运行目录下的 `run.bat` 脚本。
2. 脚本会自动安装所需的 Python 依赖 (`pywinauto`)。
3. 脚本会自动寻找游戏窗口并尝试连接。

## 注意事项
- 如果脚本无法找到窗口，请确认游戏是否以管理员权限运行。如果是，请尝试以管理员身份运行 `run.bat`。
- 部分全屏游戏可能无法被 standard Windows controls 识别，可能需要配合图像识别（如 `pyautogui`）或坐标点击 (`click_input`)。
