# About

[Doki Doki Literature Club!](https://ddlc.moe/)の`*.chr`のデータ解析スクリプトです．

ノベルゲームとしてはかなり斬新的でした．面白いので是非プレイしてみてください．

# Usage

- Python3で動作します．
- `*.chr`と同一ファイルで実行してください．
- 以下のライブラリをインストールしてください．

```
$ pip3 install pillow librosa soundfile
```

## Monika

```
$ ls -1
decode monika.py
monika.chr

$ python3 "decode monika.py" | nkf -w # utf-8
```

## Sayori

```
$ ls -1
decode sayori.py
sayori.chr

$ python3 "decode sayori.py"
```

## Natsuki
GIMP(画像処理ソフト)にて，`Filters > Distorts > Polor Coordinates`を選択する．

## Yuri
`yuri.chr`に関してはただのbase64です．

```
$ ls -1
deocde yuri.py
yuri.chr

$ python3 "decode yuri.py"
```

若しくは

```
$ cat yuri.chr | base64 -d
```

# 仕組み
ネタバレ注意
```



































































































```

<モニカ>

実はmonika.chrはPNG画像である．拡張子をchrからpngに変換して画像ビューアで開くと，中央に砂嵐の様な模様が描かれている．

砂嵐の白いピクセルを0，黒いピクセルを1とするとテキストデータになる．最後にこれをbase64でデコードするとメッセージが出現する．

<サヨリ>

実はsayori.chrはOGG音楽データである．拡張子をchrからoggに変換してビューアで開くと，黒板を引っ掻くような音が流れる．

この音をスペクトログラムで表示すると，QRコードになる．カメラで読み取ると，とあるWebサイトのリンクである．

<ナツキ>
実はnatsuki.chrはPNG画像である．拡張子をchrからpngに変換して画像ビューアで開くと，奇妙な模様が描かれている．

この図を極座標に変換すると，女性のアップショットになる．

<ユリ>

実はyuri.chrはbase64テキストデータである．
