readme v1 2020/2/21
介紹:
這個程式可以依照時間還有關鍵字去搜尋torrent(你也可以選擇不要使用篩選器，那程式就會以最多人下載的torrent去載)。因為這網站是以category去分種類(有真人影片,動畫,漫畫,寫真,同人誌這幾個)，如果你不太懂，程式問你要哪種category時你就回答all category的那個選項(回答1)。對了，我爬的這網站應該是我所知最多人在用、分類最整齊、廣告最少的網站(piratebay除外)，所以不用擔心速度太慢。

注意事項:
1.exe只有windows 64位元的電腦才能執行，我日後會處理(mac我不確定，因為我是用win10)
2.chrome要更新到最新版本，開這個網站會自動更新chrome://settings/help
3.chrome driver要更新到最新版本，去https://chromedriver.chromium.org/，找到符合你作業系統的下載下來，解壓縮，直到剩下一個叫chromedriver.exe的檔案，複製貼上到這份txt的資料夾，如果電腦問說要不要覆蓋掉舊的檔案，請按是。
4.家裡有色情守門員的人有兩種選擇，一個是電腦直接掛vpn，另外一個是用cus_main.exe ，這裡面會自動幫你連vpn，但問題是那vpn的速度很不穩定，有很高機率會失敗或斷線，所以建議用第一個方法
5.防毒軟體會亂刪東西，解決方法就是把防毒軟體暫時關掉，並把被他刪掉的檔案還原或重新下載，如果他沒辦法還原你就重新解壓所吧。
6.下載好torrent的位置如同你chrome下載預設的位置
7.github:https://github.com/Freddy930727/sukebei-crawler，有興趣的可以參考
8.有問題的話可以email我(930727fre@gmail.com)，如果你跟我在同個群組，也可以直接私訊我

pip list 打包
desc&有誤
comment_check()可能有更好、更嚴謹的寫法
headless模式
You've exceeded the maximum number of pages. Please make your search query less broad.
用txt比對下載過的檔案，避免重複下載
torrent 也有可能bad gate，好像趕緊手動案返回就可以補救
等待動畫應該完成了吧 但要確認exe時執行的狀況
exe結束時好像會閃退
參考國外文章的google extension 作法 他們選的vpn應該比較穩定
pyinstaller 還有一些好東西，有空研究一下
exe icon
animation_stop 搞不好可以省略，但要看在python shell,exe介面時的狀況
from import 可以參考cus_main 簡化
cus_main需要大幅度更新

未來更新目標:
32位元exe
更穩定的vpn
readme打好懂一點
gui
magnet 支援
提升效能 簡化