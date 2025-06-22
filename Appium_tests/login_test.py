from appium.options.ios import XCUITestOptions
from appium import webdriver
from time import sleep

# Appiumサーバーの接続情報（desired capabilities）
# xcrun simctl list devices でシミュレータのバージョンを確認できるよ

options = XCUITestOptions()
options.platform_name = "iOS"
options.platform_version = "18.5"
options.device_name = "iPhone 16 Pro"
options.automation_name = "XCUITest"
options.bundle_id = "com.example.LoginSample"
options.no_reset = True

# desired_caps = {
#     "platformName": "iOS",
#     "platformVersion": "18.5",  # シミュレータのiOSバージョンに合わせて変更
#     "deviceName": "iPhone 16",  # シミュレータ名に合わせて変更
#     "automationName": "XCUITest",
#     "bundleId": "com.example.LoginSample",  # ← Xcodeで確認
#     "noReset": True
# }

# Appiumサーバーに接続
driver = webdriver.Remote("http://localhost:4723", options=options)

# UI要素の操作
username_field = driver.find_element(by="accessibility id", value="usernameField")
password_field = driver.find_element(by="accessibility id", value="passwordField")
login_button = driver.find_element(by="accessibility id", value="loginButton")

# 入力＋ボタンタップ
username_field.send_keys("testuser")
password_field.send_keys("testpass")
login_button.click()

# 簡易確認のため数秒待機
sleep(3)

# テスト終了
driver.quit()
