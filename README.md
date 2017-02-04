# raspberrypi

## 環境構築手順

### pyenvのインストール
```sh
git clone https://github.com/yyuu/pyenv.git ~/.pyenv

# bash使ってる人は ~/zshrc -> ~/.bash_profile に変更！
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# シェルの再起動
exec $SHELL -l

# 下記が実行できればインストール完了
pyenv
```

### python2系の最新版をインストール
```sh
pyenv install 3.5.3
```

### vertualenvのインストール
```sh
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

# bash使ってる人は ~/zshrc -> ~/.bash_profile に変更！
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# シェルの再起動
exec $SHELL -l

# インストールできたか確認
pyenv virtualenv
```

### 今回の開発環境のセットアップ
```sh
# 予めひつようなものを入れる
brew install portaudio

git clone git@github.com:hot-coffee-hd17/raspberrypi.git
cd raspberrypi

# 仮想環境を作成
pyenv virtualenv 3.5.3 raspi_3.5.3
pyenv local raspi_3.5.3

# 必要モジュールのインストール（一部エラー出るが気にしない）
pip install -r requirements.txt
# ラズパイのセンサ用モジュールのエミュレータをインストール
pip install git+https://github.com/nosix/raspberry-gpio-emulator/
```

## モジュールを追加する場合
作業ディレクトリ（仮想環境）上で普通にpipで入れる。
```sh
pip install MODULE_NAME
```
その後、requirements.txtを更新する。
```sh
pip freeze > requirements.txt
```

## モジュールが追加された場合
最新のリポジトリをpullした後で下記を実行する。
```sh
# 一部エラー出るが気にしない
pip install -r requirements.txt
```

## ディレクトリ構成
```
- src
  - raspi          ... ラズパイでしか動作しないコード群
  - no_raspi       ... ラズパイでなくても動作するコード群
- requirements.txt ... Pythonのモジュール管理
```

## 上位ディレクトリのimportについて
例えば、`src/raspi/`上のスクリプトから、`src/no_raspi/`上のスクリプトをimportしたい場合は、下記をスクリプトの先頭に記述する。
```python
# この2行を記述（pathを追加している）
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# importできるようになる
from no_raspi import sample
```

## 参考にしたページ
pyenvとvirtualenvで環境構築 - Qiita  
http://qiita.com/Kodaira_/items/feadfef9add468e3a85b

GPIO 操作するプログラムを macOS で開発する  
http://nosix.hatenablog.com/entry/2016/12/22/163640

## TODO
- ディレクトリ構成決める
- ラズパイ上の環境にできるだけ合わせる
  - ラズパイ上で`pip freeze`を実行して確認
