import tkinter as tk
from pytube import YouTube
import moviepy.editor as mpe

# 合併影像音訊方法
def combine_audio(vidname, audname, outname, fps=25):
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname, fps=fps)

class UI(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        # 全域變數
        self.yt=''
        self.video=''
        self.audio=''

        '''介面設計 start''' 
        self.geometry('700x500')
        self.resizable(False, False)

        # 上方區塊(似終端機)
        frame1 = tk.Frame(self, width=500, height=330)
        frame1.place(x=100, y=30)

        self.commandLine = tk.Text(frame1)
        self.commandLine.pack(fill=tk.BOTH)

        # 下方區塊(操作選項)
        frame2 = tk.Frame(self, width=500, height=100)
        frame2.place(x=100, y=370)

        urlLabel = tk.Label(frame2, text="貼上網址→", width=10, height=1)
        urlLabel.place(x=20, y=20)
        self.url = tk.Entry(frame2, width=45)
        self.url.place(x=110, y=20)
        
        searchBtn = tk.Button(frame2, text="搜尋", width=5, height=1, command=self.search)
        searchBtn.place(x=450, y=18)

        videoItagLabel = tk.Label(frame2, text="影像Itag→", width=10, height=1)
        videoItagLabel.place(x=20, y=45)
        self.videoItag = tk.Entry(frame2, width=10)
        self.videoItag.place(x=110, y=45)

        videoDownloadBtn = tk.Button(frame2, text="影像下載", width=7, height=1, command=self.downloadVideo)
        videoDownloadBtn.place(x=200, y=43)

        audioItagLabel = tk.Label(frame2, text="音訊Itag→", width=10, height=1)
        audioItagLabel.place(x=20, y=70)
        self.audioItag = tk.Entry(frame2, width=10)
        self.audioItag.place(x=110, y=70)
        
        audioDownloadBtn = tk.Button(frame2, text="音訊下載", width=7, height=1, command=self.downloadAudio)
        audioDownloadBtn.place(x=200, y=68)
        
        mergeBtn = tk.Button(frame2, text="合併", width=5, height=1, command=self.mergeVideoAudio)
        mergeBtn.place(x=450, y=68)
        '''介面設計 end''' 

    # 進度顯示條
    def progress(self, stream, chunk, bytes_remaining):
        contentSize = self.video.filesize
        size = contentSize - bytes_remaining
        print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
        '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

    # 下載完成後動作
    def complete(self, stream, file_path):
        self.commandLine.insert(tk.END, '下載完成\n')
    
    # 搜尋影片，並列出資訊
    def search(self):
        url = self.url.get()
        self.yt = YouTube(url, on_progress_callback=self.progress, on_complete_callback=self.complete)
        
        self.commandLine.insert(tk.END, self.yt.title + '\n')
        
        ytList = self.yt.streams
        for item in ytList:
            string = str(item).split('"')
            if item.type == 'video':
                string = "itag:" + string[string.index("<Stream: itag=")+1].rjust(3) + "  " + \
                         "type:" + string[string.index(" type=")+1] + "  " + \
                         "resolution:" + string[string.index(" res=")+1].rjust(5) + "  " + \
                         "Video and Audio:" + string[string.index(" progressive=")+1] 
            else:
                string = "itag:" + string[string.index("<Stream: itag=")+1].rjust(3) + "  " + \
                         "type:" + string[string.index(" type=")+1] + "  " + \
                         "bitrate:" + string[string.index(" abr=")+1].rjust(7) + "  " + \
                         "Video and Audio:" + string[string.index(" progressive=")+1] 
            self.commandLine.insert(tk.END, string+'\n')
        print('')
    
    # 下載影像檔
    def downloadVideo(self):
        self.video = self.yt.streams.get_by_itag(self.videoItag.get())
        self.video.download()

    # 下載音訊檔
    def downloadAudio(self):
        self.audio = self.yt.streams.get_by_itag(self.audioItag.get())
        self.audio.download()

    # 合併影像+音訊
    def mergeVideoAudio(self):
        videoName = self.video.default_filename
        audioName = self.audio.default_filename
        outputName = videoName.split('.mp4')[0] + '_new.mp4'
        combine_audio(videoName, audioName, outputName)

UI().mainloop()
