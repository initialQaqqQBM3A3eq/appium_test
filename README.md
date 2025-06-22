# iOS 自動UIテスト環境（Appium + Jenkins + Python）

このプロジェクトは、Mac上で **iOSアプリのUIテストをPython＋Appiumで自動化** し、**JenkinsでCI実行**するためのセットアップ例です。

---

## 📌 構成

- テストコード言語: Python
- テストフレームワーク: Appium Python Client
- CIツール: Jenkins（ローカル起動）
- 対象プラットフォーム: iOS（Xcodeシミュレータ）
- OS: macOS

---

## ⚙️ 前提条件

以下がローカルにインストール済みであること：

- macOS（M1/M2可）
- [Homebrew](https://brew.sh/)
- Xcode（Command Line Tools含む）
- Python 3.x
- Jenkins（Homebrewでインストール）
- Appium CLI（npmでインストール）
- Appium-Python-Client（pipでインストール）

---

## 🛠 セットアップ手順

### 1. Pythonパッケージのインストール

```bash
which python3   # Jenkinsが使う環境を確認
python3 -m pip install Appium-Python-Client
```

### 2. Appium CLI のインストール

```bash
brew install node
npm install -g appium
```

### 3. Jenkinsのインストールと起動

```bash
brew install jenkins-lts
brew services start jenkins-lts
open http://localhost:8080
```

※ 初回パスワード → `/opt/homebrew/var/jenkins_home/secrets/initialAdminPassword`

### 4. Jenkinsジョブ作成

- フリースタイルプロジェクトを作成
- 「ビルド手順を追加」→「シェルの実行」
- 以下を設定：

```bash
#!/bin/bash

# Appium CLI にパスを通す
export PATH="/opt/homebrew/bin:$PATH"

# Appium起動（バックグラウンド）
appium &
sleep 5

# Pythonテスト実行
python3 /Users/yu-endo/Projects/my_project/dev/swift_prj/appium_test/jenkins-tests/login_test.py
```

---

## ✅ テスト実行サンプル（Python）

`login_test.py`

```python
from appium import webdriver
from appium.options.ios import XCUITestOptions

options = XCUITestOptions()
options.platform_name = "iOS"
options.platform_version = "17.0"  # 環境に合わせて
options.device_name = "iPhone 15"
options.app = "/path/to/YourApp.app"  # ビルド済みiOSアプリのパス
options.automation_name = "XCUITest"

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

# ここにUI操作を書く
driver.quit()
```

---

## 🧩 トラブルシューティング

### ❌ `appium: command not found`

→ Jenkinsシェルに `export PATH="/opt/homebrew/bin:$PATH"` を追加

### ❌ `ModuleNotFoundError: No module named 'appium'`

→ Jenkinsが使うPython環境で以下を実行：

```bash
python3 -m pip install Appium-Python-Client
```

### ❌ Jenkinsでシミュレータが起動しない

→ Jenkinsから `xcodebuild` を実行できるように権限と署名設定が必要な場合あり（後述）

---

## 📁 ディレクトリ構成（例）

```
appium_test/
├── jenkins-tests/
│   └── login_test.py
├── README.md
```

---

## 🚧 今後の予定（TODO）

- iOSアプリ側の `accessibilityIdentifier` 設定
- `Appium Inspector` で要素取得確認
- Android対応の拡張（任意）

---

## ✍️ 作者

- Endo Yu（環境：macOS Ventura + M1）
- 初めてのPython・Appium連携実践中！

