### Youtube Download Tool 只是一個簡單(簡陋)的下載工具

空閒的時候做的一個小工具

由於網路上有些免費下載軟體

只提供低解析度的影片下載

所以才想自己做一個


> 使用語言：Python

> 使用套件：pytube3 && moviepy

------

Before you use it,
you may need to install these two packages `pytube3` and `moviepy`.

or you can try this below：

```
pip install -r requirement.txt
```


功能:
- [x] 下載影像
- [x] 下載音訊
- [x] 影像、音訊合併
- [x] 建議的訊息提示框
- [ ] 有些影片無法下載(不確定是不是官方帳號的關係)
- [ ] 無提供檔名修改功能
- [ ] 未進行防呆措施


簡易介面如下：

![image](https://github.com/CYT823/YoutubeDownloadTool/blob/master/image/screenshot.png)


### 橘色框框：

僅是簡易的command line，顯示一些資訊供參考用。

### 紅色框框：

將想下載的youtube網址貼到紅色框框中，

按下「搜尋」按鈕，即會在「橘色框框」中顯示`歌曲名稱`及`該影片提供的串流檔案格式`。

### 綠色框框：

依據「橘色框框」顯示的資訊，找到你想下載的串流格式。

並在影像|音訊的Itag中樹入對應編號(如圖所示)。

輸入完畢後，按下「下載」按鈕，即會下再到你所在目錄(current dir)。

### 藍色框框：

由於有些串流格式，僅提供影像或音訊格式 → 並無完整影音合併的檔案。

因此，可以下載【影像格式檔案】+【音訊格式檔案】。

而後，按下「合併」按鈕，將影像及音訊合併。

