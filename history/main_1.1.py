from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import requests
import sys
import pyperclip as pc

from ui import Ui_Form

YOUTUBE_API_KEY = "AIzaSyCdoVRTwGmjcRkai11FtT6onb8G6alUmCA"
# google cloud platform 提供的youtube api v3 的api key

video_num = 0


class yt_playlist_to_URL():
    def __init__(self, api_key):
        self.base_url = "https://www.googleapis.com/youtube/v3/"
        self.api_key = api_key

    def get_html_to_json(self, path):  # 從google的youtube api 抓取撥放清單的資料
        api_url = f"{self.base_url}{path}&key={self.api_key}"
        r = requests.get(api_url)
        if r.status_code == requests.codes.ok:
            data = r.json()
        else:
            data = None
        return data
        # 返回播放清單資訊的json

    def append_video_IDs(self, path):  # 把每部影片的video ID抓出來
        video_ids = []
        data = self.get_html_to_json(path)
        for data_item in data['items']:
            video_ids.append(data_item['contentDetails']['videoId'])
        video_ids = list(video_ids)
        URL = []
        for i in video_ids:
            URL.append(f"https://www.youtube.com/watch?v={i}")
            # 將每部影片的video ID加上標準網址 使成為可撥放的網址
        return URL

    # 結合上面的函式 將playlist ID轉成每部影片的網址
    def playlist_to_URL(self, playlistID, part='contentDetails', max_results=50):
        path = f'playlistItems?part={part}&playlistId={playlistID}&maxResults={max_results}'
        data = self.get_html_to_json(path)
        if not data:
            print('錯誤')
            return []

        totalresult = data['pageInfo']['totalResults']
        # 播放清單所包含的影片總數
        if totalresult > 50:
            times = (totalresult // 50)
        else:
            times = 0
        # 因為youtube api每次最多只能列出50筆資料 所以要確認是否需要多次操作
        URLs = []
        if times > 0:
            url = self.append_video_IDs(path)
            for i in url:
                URLs.append(i)
            for n in range(times):
                nextpagetoken = data['nextPageToken']
                path = f'playlistItems?part={part}&playlistId={playlistID}&maxResults={max_results}&pageToken={nextpagetoken}'
                url = self.append_video_IDs(path)
                for k in url:
                    URLs.append(k)
                data = self.get_html_to_json(path)
                # 更新api網址
        else:
            URLs = self.append_video_IDs(path)
        return list(URLs)


class mainwindow(QtWidgets.QWidget):  # 建立Qt主視窗
    def __init__(self):
        super(mainwindow, self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        sys.stdout = EmittingStr()
        self.ui.output.connect(sys.stdout, QtCore.SIGNAL(
            "textWritten(QString)"), self.outputWritten)
        sys.stderr = EmittingStr()
        self.ui.output.connect(sys.stderr, QtCore.SIGNAL(
            "textWritten(QString)"), self.outputWritten)
        # 設定text Edit輸出映射
        self.ui.convert.clicked.connect(self.convert)
        self.ui.copy.clicked.connect(self.copy)
        self.ui.clear.clicked.connect(self.clear)

    def convert(self):  # 轉換 按鈕的程式
        self.playlisturl = self.ui.input.toPlainText()
        self.finaloutput = main(self.playlisturl)
        print(f'''{self.finaloutput}


影片總數為: {video_num}.
===========================================================================
        ''')

    def copy(self):  # 複製至剪貼簿 按鈕的程式
        pc.copy(self.finaloutput)

    def clear(self):  # 清除 按鈕的程式
        self.ui.input.clear()
        self.ui.output.clear()

    def outputWritten(self, text):  # 設定text Edit輸出映射
        cursor = self.ui.output.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.output.setTextCursor(cursor)
        self.ui.output.ensureCursorVisible()

    def keyPressEvent(self, event):  # 設定鍵盤按鍵映射
        super(mainwindow, self)
        if event.key() == Qt.Key_Delete:
            self.clear()


class EmittingStr(QtCore.QObject):  # 設定text Edit輸出信號
    textWritten = QtCore.Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


def main(playlist):
    start = yt_playlist_to_URL(YOUTUBE_API_KEY)
    playlistid = ''
    if len(str(playlist)) == 34 or len(str(playlist)) == 13:    #檢查所輸入之字元是否為播放清單或youtube合輯的ID
        playlistid = playlist
    elif 'http' not in playlist or 'list' not in playlist:    #檢查所輸入之字元是否為網址 以及是否為單一影片的網址
        print('錯誤')
    else:
        playlistid = playlist[playlist.find('list=')+5:]    #提取網址中的ID
    outputlist = start.playlist_to_URL(playlistid.strip())
    global video_num
    video_num = len(outputlist)    #檢查影片數量
    outputstr = '\n'.join(outputlist)    #將網址換行並轉換成str
    return outputstr


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())
