import sys
import time
import pywinauto
from pywinauto.application import Application
from pywinauto import Desktop

def list_running_windows():
    """遍历并打印当前运行的所有窗口标题"""
    print("正在扫描当前运行的窗口...")
    windows = Desktop(backend="uia").windows()
    for w in windows:
        print(f" - {w.window_text()}")
    return windows

def find_and_connect_game(game_title="Dark and Darker"):
    """
    查找指定游戏窗口并连接
    """
    print(f"\n正在寻找游戏窗口: {game_title} ...")
    
    # 尝试连接已经运行的游戏进程
    # 注意：这里假设游戏窗口标题包含 "Dark and Darker"
    # 如果游戏以全屏独占模式运行，可能需要管理员权限或特定的backend设置
    
    try:
        # 方法1: 通过标题连接
        # 使用 UIA backend 通常对现代 Windows 应用/游戏支持更好
        app = Application(backend="uia").connect(title_re=f".*{game_title}.*", timeout=10)
        print(f"成功连接到进程: {app.process}")
        
        # 获取主窗口
        # window() 查找
        top_window = app.window(title_re=f".*{game_title}.*")
        
        # 等待窗口准备就绪
        top_window.wait('visible', timeout=10)
        print("游戏窗口已就绪。")
        
        return app, top_window
        
    except Exception as e:
        print(f"连接游戏失败: {e}")
        print("提示: 请确保游戏已经启动。如果游戏以管理员权限运行，请尝试以管理员身份运行此脚本。")
        return None, None

def perform_actions(window):
    """
    在游戏窗口执行操作
    """
    if not window:
        return

    print("\n开始执行自动化操作...")
    
    # 获取当前窗口的控件结构，这有助于分析界面
    # 注意：对于某些DirectX游戏，pywinauto可能无法直接获取内部控件，
    # 这种情况下可能需要结合 pyautogui (图像识别) 或直接坐标点击。
    
    # 这里我们尝试打印控件标识符，方便调试
    # window.print_control_identifiers(depth=2) 
    
    try:
        # 示例：尝试点击一个假设的按钮
        # 实际使用时需要用 print_control_identifiers 查看按钮的 title 或 auto_id
        # 例如：window.child_window(title="Play", control_type="Button").click()
        
        print("尝试查找并点击示例按钮 (Start/Play)...")
        # 这是一个占位符逻辑，因为我们不知道具体的UI结构
        # 假设有个 "Enter Lobby" 或 "Play" 按钮
        # 注意: 许多游戏UI不是标准的Windows控件，pywinauto click() 方法不一定有效，
        # 可能需要使用 click_input() 来模拟鼠标点击坐标。
        
        # 模拟点击窗口中心 (通常是"按任意键继续"之类的地方)
        rect = window.rectangle()
        center_x = (rect.left + rect.right) // 2
        center_y = (rect.top + rect.bottom) // 2
        
        print(f"模拟点击窗口中心坐标: ({center_x}, {center_y})")
        # window.click_input(coords=(center_x, center_y)) # 这是一个物理点击模拟，会移动鼠标
        
        print("点击动作演示完毕 (代码中已注释实际点击，以免误操作)")
        
    except Exception as e:
        print(f"操作执行出错: {e}")

def main():
    # 1. 遍历系统运行的软件 (可选，用于调试查看窗口名称)
    list_running_windows()
    
    # 2. 找到 Dark And Darker 游戏窗口并连接
    app, game_window = find_and_connect_game("Dark and Darker") # 根据实际窗口标题调整
    
    if game_window:
        # 3. 尝试点击某个按钮看效果
        perform_actions(game_window)
    else:
        print("未找到游戏窗口，程序结束。")

if __name__ == "__main__":
    main()
