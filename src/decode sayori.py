#!/usr/bin/env python3
import sys, os
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import scipy.io.wavfile
import librosa, librosa.display

def main():

    fname = "sayori.chr"

    if not os.path.exists(fname):
        print("Error: " + fname + " not found.", file=sys.stderr)
        sys.exit(1)

    # sayori.chrの実態はOGGファイルである．
    # scipyでOGGが読み込む処理を見つけていないため，WAVに変換する．
    data, rate = sf.read(fname)
    fname += ".wav"
    sf.write(fname, data, rate)

    # WAV形式で読み込む．
    rate, data = scipy.io.wavfile.read(fname)

    # 16bitの音楽データを-1~1で正規化する．
    data = data / 2**(16-1)
    # フレーム長，フレームシフト長
    n_fft = 1024
    hop_length = int(n_fft / 4)

    # 短時間フーリエ変換(Short-Time Fourier Transform)でスペクトログラム用データを抽出する．
    amplitude = np.abs((librosa.core.stft(data, n_fft=n_fft, hop_length=hop_length))) ** 2.0
    db = librosa.core.amplitude_to_db(amplitude)

    # 対数グラフにしないとカメラで読み取れない．
    ax = plt.gca()
    ax.set_yscale("log")

    # スペクトログラムを表示する．
    librosa.display.specshow(db, sr=rate, hop_length=hop_length, x_axis="time", y_axis="hz", cmap="binary")

    # 表を設定する．
    plt.colorbar(format="%+2.0f dB")
    plt.title("Sayori")
    plt.show()


if __name__ == "__main__":
    main()
