from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import requests
import sys
import pyperclip as pc

from ui import Ui_Form
from ui2 import Ui_Form as Ui_Form2

YOUTUBE_API_KEY = "AIzaSyCdoVRTwGmjcRkai11FtT6onb8G6alUmCA"
# google cloud platform 提供的youtube api v3 的api key

video_num = 0
url_list = []


class yt_playlist_to_URL:
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
        # 返回播放清單影片ID的json

    def get_html_to_json_snippet(self, path):
        api_url = f"{self.base_url}{path}&key={self.api_key}"
        r = requests.get(api_url)
        if r.status_code == requests.codes.ok:
            datas = r.json()
        else:
            datas = None
        return datas

    def append_video_IDs(self, path):  # 把每部影片的video ID抓出來
        video_ids = []
        data = self.get_html_to_json(path)
        for data_item in data["items"]:
            video_ids.append(data_item["contentDetails"]["videoId"])
        video_ids = list(video_ids)
        URL = []
        for i in video_ids:
            http = f"https://www.youtube.com/watch?v={i}"
            URL.append(http)
            # 將每部影片的video ID加上標準網址 使成為可撥放的網址
        return URL

    def append_video_IDs_snippet(self, path):
        video_name = []
        datas = self.get_html_to_json(path)
        for d in datas["items"]:
            video_name.append(d["snippet"]["title"])
        video_name = list(video_name)
        return video_name

    # 結合上面的函式 將playlist ID轉成每部影片的網址
    def playlist_to_URL(self, playlistID, part="contentDetails", max_results=50):
        path = f"playlistItems?part={part}&playlistId={playlistID}&maxResults={max_results}"
        data = self.get_html_to_json(path)
        if not data:
            print("錯誤")
            return []

        totalresult = data["pageInfo"]["totalResults"]
        # 播放清單所包含的影片總數
        if totalresult > 50:
            times = totalresult // 50
        else:
            times = 0
        # 因為youtube api每次最多只能列出50筆資料 所以要確認是否需要多次操作
        URLs = []
        if times > 0:
            url = self.append_video_IDs(path)
            for i in url:
                URLs.append(i)
            for n in range(times):
                nextpagetoken = data["nextPageToken"]
                path = f"playlistItems?part={part}&playlistId={playlistID}&maxResults={max_results}&pageToken={nextpagetoken}"
                url = self.append_video_IDs(path)
                for k in url:
                    URLs.append(k)
                data = self.get_html_to_json(path)
                # 更新api網址
        else:
            URLs = self.append_video_IDs(path)
        return list(URLs)

    def playlist_to_URL_snippet(self, playlistID, part="snippet", max_results=50):
        path = f"playlistItems?part={part}&playlistId={playlistID}&maxResults={max_results}"
        datas = self.get_html_to_json_snippet(path)
        totalresult = datas["pageInfo"]["totalResults"]
        # 播放清單所包含的影片總數
        if totalresult > 50:
            times = totalresult // 50
        else:
            times = 0
        Name = []
        if times > 0:
            name = self.append_video_IDs_snippet(path)
            for i in name:
                Name.append(i)
            for n in range(times):
                nextpagetoken = datas["nextPageToken"]
                path = f"playlistItems?part={part}&playlistId={playlistID}&maxResults={max_results}&pageToken={nextpagetoken}"
                name = self.append_video_IDs_snippet(path)
                for k in name:
                    Name.append(k)
                datas = self.get_html_to_json_snippet(path)
                # 更新api網址
        else:
            Name = self.append_video_IDs_snippet(path)
        return list(Name)


class mainwindow(QtWidgets.QWidget):  # 建立Qt主視窗
    def __init__(self):
        super(mainwindow, self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        sys.stdout = EmittingStr()
        self.ui.output.connect(
            sys.stdout, QtCore.SIGNAL("textWritten(QString)"), self.outputWritten
        )
        sys.stderr = EmittingStr()
        self.ui.output.connect(
            sys.stderr, QtCore.SIGNAL("textWritten(QString)"), self.outputWritten
        )
        # 設定text Edit輸出映射
        self.ui.convert.clicked.connect(self.convert)
        self.ui.copy.clicked.connect(self.copy)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.webopen.clicked.connect(self.web_open)
        self.outputstr = ""

    def convert(self):  # 轉換 按鈕的程式
        self.playlisturl = self.ui.input.toPlainText()
        self.finaloutput, self.name = main(self.playlisturl)
        i = 0
        none_video = []
        for t in self.finaloutput:
            if self.name[i] == "Deleted video" or self.name[i] == "Private video":
                none_video.append(i)
            else:
                print(self.name[i] + "\n" + t + "\n")
            i = i + 1
        num = 0
        for o in none_video:
            self.finaloutput.remove(self.finaloutput[o])
            num = num + 1
        global video_num
        video_num = video_num - num
        print(
            f"""

影片總數為: {video_num}
已移除: {num} 部無法播放的影片
===================================
"""
        )
        self.outputstr = "\n".join(self.finaloutput)
        global url_list
        url_list = self.finaloutput

    def copy(self):  # 複製至剪貼簿 按鈕的程式
        if self.outputstr == "":
            print("請先轉換影片")
        else:
            pc.copy(self.outputstr)

    def clear(self):  # 清除 按鈕的程式
        self.ui.input.clear()
        self.ui.output.clear()
        self.outputstr = ""
        global url_list
        url_list = []

    def web_open(self):
        if url_list == []:
            print("請先轉換影片")
        else:
            self.sub_window = subwindow()
            self.sub_window.show()

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


class subwindow(QtWidgets.QWidget):
    def __init__(self):
        super(subwindow, self).__init__(None)
        self.ui2 = Ui_Form2()
        self.ui2.setupUi(self)
        self.ui2.open.clicked.connect(self.open)
        self.ui2.cancel.clicked.connect(self.cancel)
        self.ui2.label.setText(
            f"<html><head/><body><p>接下來將會用您的預設瀏覽器開啟所有的{video_num}部影片，</p><p>您確定要繼續嗎</p></body></html>"
        )

    def open(self):
        import webbrowser

        for t in url_list:
            webbrowser.open(
                t,
                new=0,
                autoraise=True,
            )
        del webbrowser

    def cancel(self):
        self.close()


def main(playlist):
    start = yt_playlist_to_URL(YOUTUBE_API_KEY)
    playlistid = ""
    if (
        len(str(playlist)) == 34 or len(str(playlist)) == 13
    ):  # 檢查所輸入之字元是否為播放清單或youtube合輯的ID
        playlistid = playlist
    elif (
        "http" not in playlist or "list" not in playlist or str(playlist) == ""
    ):  # 檢查所輸入之字元是否為網址 以及是否為單一影片的網址
        print("錯誤")
    else:
        playlistid = playlist[playlist.find("list=") + 5 :]  # 提取網址中的ID
    outputlist = start.playlist_to_URL(playlistid.strip())
    name = start.playlist_to_URL_snippet(playlistid.strip())
    global video_num
    video_num = len(outputlist)  # 檢查影片數量
    return outputlist, name


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())
