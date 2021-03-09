readme v1 2021/3/8
重點:
點main.exe就可以執行了
如果防毒軟體自動刪除部分檔案，請關閉防火牆並直接重新解壓縮
記得更新chrome,chrome driver(詳見注意事項)

介紹:
這個程式是用selenium,python寫成的，並依照幾種filter去搜尋torrent(也可以選擇不要使用，那程式就會爬seeder最大的torrent)。
This program is based on selenium and python.It will simulate what you want to do and execute it automatically.On top of that,it provides several filters for you to choose from and you can download torrent directly or it will open the magnet link(a torrent program is required).

功能:
filter:time,keyword,category
同時支援torrent下載或點擊magnet link
按照關鍵字建表、存檔，避免載到重複的torrent

注意事項:
1.exe只有windows 64位元的電腦才能執行，我日後會重新編譯(這份exe只支援windows，linux和osx都不能執行)
2.chrome要更新到最新版本，用chrome開啟這個網站會自動更新chrome://settings/help
3.chrome driver要更新到最新版本，去https://chromedriver.chromium.org/ ，找到符合你作業系統的下載下來(注意是穩定版本，不要下載到beta版)，解壓縮，直到剩下一個叫chromedriver.exe的檔案，複製貼上到這份資料夾，如果電腦問說要不要覆蓋掉舊的檔案，請按是。
4.如果要用magnet link,請先把bt軟體詢問是否要下載的這種功能關掉，不然這軟體點擊magnet link會快到讓你電腦當掉，你也會按確認按到手痠。
4.家裡有色情守門員的人有兩種選擇，一個是電腦直接掛vpn，另外一個是用cus_main.exe ，這裡面會自動幫你連vpn，但問題是那vpn的速度很不穩定，有很高機率會失敗或斷線，所以建議用第一個方法
5.防毒軟體會亂刪東西，建議把防毒軟體暫時關掉，並直接重新解壓縮。
6.下載好的位置在這份資料夾的download中。
7.github:https://github.com/Freddy930727/sukebei-crawler ，有興趣的可以參考
8.有問題的話可以email我(930727fre@gmail.com)，如果你跟我在同個群組，也可以直接私訊我

.md
有些沒有torrent 可以下載
pyinstaller console window window based
測試的check()
	page maximum 可能用按下下一頁的方法解決
comment_check()可能有更好、更嚴謹的寫法
	torrent 也有可能bad gate，好像趕緊手動案返回就可以補救
等待動畫應該完成了吧 但要確認exe時執行的狀況
exe結束時好像會閃退
參考國外文章的google extension 作法 他們選的vpn應該比較穩定
exe icon
animation_stop 搞不好可以省略，但要看在python shell,exe介面時的狀況
cus_main需要大幅度更新

未來更新目標:
32位元exe
更穩定的vpn
readme打好懂一點
gui
magnet 支援
提升效能 簡化