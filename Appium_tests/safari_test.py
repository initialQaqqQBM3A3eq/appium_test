from appium import webdriver
from appium.options.ios import XCUITestOptions
import time

# オプション設定
options = XCUITestOptions()
options.platform_name = "iOS"
options.platform_version = "18.5"  # 環境に合わせて変更
options.device_name = "iPhone 16 Pro"  # シミュレータ名
options.browser_name = "Safari"   # Safariを使う
options.automation_name = "XCUITest"

# Appiumサーバーに接続
driver = webdriver.Remote("http://localhost:4723", options=options)

# Webサイトにアクセス
driver.get("https://www.google.com")
time.sleep(5)

# Safari終了
driver.quit()
