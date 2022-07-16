from lib2to3.pgen2.token import MINUS
from time import time
import tkinter as tk
import random
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame import mixer
#ランダム番号
many = ["こんにちは","konnitiha","おはようございます","ohayougozaimasu","今日は楽しかったよ","kyouhatanosikattayo","猫の手も借りたい","nekonotemokaritai",
"これは教訓です","korehakyoukundesu","犬も歩けば棒に当たる","inumoarukebabouniataru","四面楚歌","simensoka","排他的経済水域","haitatekikeizaisuiiki",
"明日天気になーれ","asitatenkinina-re","楽しい修学旅行","tanosiisyuugakuryokou","私の名前はたけしです","watasinonamaehatakesidesu","猪突猛進","tyototumousin",
"理解しがたい","rikaisigatai","超高級料理店","tyoukoukyuuryouriten","難聴のおじいちゃん","nantyounoojiityan","草生える","kusahaeru",
"八方美人","happoubijin","天才プログラマー","tensaipurogurama-","明日やろうは馬鹿野郎","asitayarouhabakayarou","しじみのどぶ漬け","sijiminodobuzuke",
"好きこそ物の上手なれ","sukikosomononojyouzunare","忠言は耳に逆らう","tyuugenhamiminisakarau","喉元過ぎれば熱さを忘れる","nodomotosugirebaatusawowasureru","百聞は一見に如かず","hyakubunhaikkennnisikazu",
"へそで茶を沸かす","hesodetyawowakasu","隣の客はよく柿食う客だ","tonarinokyakuhayokukakikuukyakuda","身から出た錆","mikaradetasabi","焼け石にタラバガニ","yakeisinitarabagani",
"そこここと火を動かす","sokokokotohiwougokasu","猿も木から落ちる","sarumokikaraotiru","どうせ俺は足手まといだ","douseorehaasidematoida","石橋を叩いて渡る","isibasiwotataitewataru",
"親しき中にも礼儀あり","sitasikinakanimoreigiari","とらぬ狸の皮算用","toranutanukinokawazanyou","先生に言いつけてやる","senseiniiituketeyaru","東京特許許可局","toukyoutokkyokyokakyokukyokutyou",
"生麦生米生卵","namamuginamagomenamatamago","ここ掘れワンワン","kokohorewanwan","飲みかけのコップ","nomikakenokoppu","コップの円周率を教えてください","koppunoensyuurituwoosietekudasai",
#40
"口は災いのもと","kutihawazawainomoto","ああ言えばこう言う","aaiebakouiu","会うは別れの始め","auhawakarenohajime","青菜に塩","aonanisio",
"圧巻の演技","akkannnoengi","危ない橋を渡る","abunaihasiwowataru","石が流れて木の葉が沈む","isiganagaretekonohagasizumu","一攫千金","ikkakusenkinn",
"一字千金","itijisenkinn","一難去ってまた一難","itinansattemataitinan","一刻千金","ikkokusenkin","一寸先は闇","issunsakihayami",
"一寸法師","issunbousi","赤ずきんちゃん","akazukintyan","負け犬の遠吠え","makeinunotooboe","言わぬが花","iwanugahana",
"嘘つきは泥棒の始まり","usotukihadorobounohajimari","木魚クッキー","mokugyokukki-","馬の耳に念仏","umanomimininenbutu","雲泥の差","undeinosa",
"噂をすれば影が差す","uwasawosurebakagegasasu","縁の下の力持ち","ennnositanotikaramoti","奥歯に物が挟まる","okubanimonogahasamaru","激おこぷんぷん丸","gekiokopunpunmaru",
"同じ釜の飯を食う","onajikamanomesiwokuu","鬼が出るか蛇が出るか","onigaderukajagaderuka","親の心子知らず","oyanokokorokosirazu","飼い犬に手を噛まれる","kaiinunitewokamareru",
"カエルは帰る","kaeruhakaeru","河童の皿","kappanosara","蟹は甲羅に似せて穴を掘る","kanihakouraniniseteanawohoru","金の切れ目が縁の切れ目","kanenokiremegaennnokireme",
"可愛い子には旅をさせよ","kawaiikonihatabiwosaseyo","堪忍袋の緒が切れる","kannninbukuronoogakireru","聞いて極楽見て地獄","kiitegokurakumitejigoku","牛耳を執る","gyuujiwotoru",
"暗がりから牛","kuragarikarausi","苦しい時の神頼み","kurusiitokinokamidanomi","君子は豹変する","kunsihahyouhensuru","月下氷人","gekkahyoujin"
#80
]
#ローマ字
latest_i = []
#日本語
latest_i2 = []
#listの日本語の数をいれる
for i2 in range(80):
    #2の倍数を作る
    next_i2 = int(i2 * 2)#0,2,4,6,8,10,12,14,16,18,20....
    #2の倍数 + 1の文字を取り出す
    last_i2 = many[next_i2]
    #取り出した文字リストに入れる
    latest_i2.append(last_i2)
#ここにも
for i in range(80):
    #2の倍数を作る
    next_i = int(i * 2)
    #2の倍数 + 1の文字を取り出す
    last_i = many[next_i + 1]#1,3,5,7...
    #取り出した文字リストに入れる
    latest_i.append(last_i)
y = 0
z = 0
#クラスナンバー
class Number:
    def random_number(self):
        global x
        #ここにも日本語の数の範囲いれる
        x = str(random.randint(0,79))
        return x
    #ミスタイプ数計算
    def miss(self):
        global y 
        y = int(y) + 1
        return y
    def miss_no_global(self):
        global y 
        y = int(y)
        return y
    def success(self):
        global z
        z = int(z) + 1
        return z
    def success_no_global(self):
        global z
        z = int(z)
        return z
class Sentance:
    #番号作る
    def sentance_info(self):
        global random_num
        random_num = Number().random_number()
        rand = int(random_num)
        global perfect_i
        perfect_i = latest_i[rand]
        #文字列バラバラ
        global bara_i
        bara_i = list(perfect_i)
        #文字列数える
        global len_i
        len_i = int(len(bara_i))
        
        global perfect_i2
        perfect_i2 = latest_i2[rand]
        #文字列バラバラ
        global bara_i2
        bara_i2 = list(perfect_i2)
        #文字列数える
        global len_i2
        len_i2 = int(len(bara_i2))
        return   perfect_i,bara_i,len_i, perfect_i2 ,bara_i2 ,len_i2

Sentance().sentance_info()
miss_key = []
miss_count = ["","","","","","","","","","","","","","","","","","","","","","","","","",""]
miss_roma = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
sort_count = miss_count
def key_handler(e):
    key = e.keysym
    def def_miss(receive_key):
        miss_key.append(receive_key)
        miss_key.sort()
        miss_count[0] = str(miss_key.count("a"))
        miss_count[1] = str(miss_key.count("b"))
        miss_count[2] = str(miss_key.count("c"))
        miss_count[3] = str(miss_key.count("d"))
        miss_count[4] = str(miss_key.count("e"))
        miss_count[5] = str(miss_key.count("f"))
        miss_count[6] = str(miss_key.count("g"))
        miss_count[7] = str(miss_key.count("h"))
        miss_count[8] = str(miss_key.count("i"))
        miss_count[9] = str(miss_key.count("j"))
        miss_count[10] = str(miss_key.count("k"))
        miss_count[11] = str(miss_key.count("l"))
        miss_count[12] = str(miss_key.count("m"))
        miss_count[13] = str(miss_key.count("n"))
        miss_count[14] = str(miss_key.count("o"))
        miss_count[15] = str(miss_key.count("p"))
        miss_count[16] = str(miss_key.count("q"))
        miss_count[17] = str(miss_key.count("r"))
        miss_count[18] = str(miss_key.count("s"))
        miss_count[19] = str(miss_key.count("t"))
        miss_count[20] = str(miss_key.count("u"))
        miss_count[21] = str(miss_key.count("v"))
        miss_count[22] = str(miss_key.count("w"))
        miss_count[23] = str(miss_key.count("x"))
        miss_count[24] = str(miss_key.count("y"))
        miss_count[25] = str(miss_key.count("z"))
        label8["text"]=miss_roma[miss_count.index(max(miss_count))]
        miss_count[miss_count.index(max(miss_count))]="0"
        label9["text"]=miss_roma[miss_count.index(max(miss_count))]
        miss_count[miss_count.index(max(miss_count))]="0"
        label10["text"]=miss_roma[miss_count.index(max(miss_count))]
        miss_count[miss_count.index(max(miss_count))]="0"
        label11["text"]=miss_roma[miss_count.index(max(miss_count))]
    if key == 'minus':
        key = '-'
    if key == bara_i[0]:
        del bara_i[0]
        label4["text"]=bara_i
        sound3.play()
        label5["text"] = str(Number().success())
        #成功率
        label7["text"] = str(format(Number().success_no_global() / (Number().miss_no_global() + Number().success_no_global())*100,'.1f'))
        if int(len(bara_i)) == 0:
            #print("success")
            Sentance().sentance_info()
            label1["text"]=perfect_i2
            label4["text"]=bara_i
            box.delete(0,tk.END)
            sound3.stop()
            sound4.play()
            
    else:
        global sound2
        sound2=pygame.mixer.Sound("bad.mp3")
        sound2.play()
        sound2.set_volume(0.2) 

        label3["text"] = str(Number().miss())
        #成功率計算
        label7["text"] = str(format(Number().success_no_global() / (Number().miss_no_global() + Number().success_no_global())*100,'.1f')) 
        def_miss(key)
        #print(miss_key)
        #print(miss_count.index(max(miss_count)))
         
root = tk.Tk()
root.geometry("350x200")
root.title("まんぼうタイピング")
# 画像の取得
img = tk.PhotoImage(file='background3.png')
label = tk.Label(root, image=img)
label.grid(row=1, column=1)
label.place(x=-60,y=0)

#文字列取り出し
box = tk.Entry(root,justify=tk.CENTER,bg="mediumturquoise",state=tk.NORMAL)
box.place(x=60, y=20, width=150, height=30)
box.bind("<KeyPress>", key_handler)

#日本語
label1 = tk.Label(root,text ="",font = ("",15),bg="mediumturquoise")
label1.place(x = 40, y = 60)
label1["text"]=perfect_i2
#miss
label2 = tk.Label(root,text ="ミス",font = ("",15),bg = "Royalblue")
label2.place(x = 42, y = 110)
#成功
label2 = tk.Label(root,text ="成功", font = ("",15),bg = "orangered")
label2.place(x = 90, y = 110)
#missカウント
label3 = tk.Label(root,text ="0", font = ("",15),bg = "Royalblue")
label3.place(x = 47, y = 130)
#成功カウント
label5 = tk.Label(root,text ="0", font = ("",15),bg = "orangered")
label5.place(x = 97, y = 130)
#ローマ字
label4 = tk.Label(root,text ="s", font = ("",15),bg="salmon")
label4.place(x=10,y=82)
label4["text"]=bara_i
#苦手キー
back = tk.Label(root,text ="           ", font = ("",15),bg="tomato")
back.place(x = 114, y = 165)
label11 = tk.Label(root,text ="", font = ("",15),bg="tomato")
label11.place(x = 184, y = 165)
label10 = tk.Label(root,text ="", font = ("",15),bg="tomato")
label10.place(x = 164, y = 165)
label9 = tk.Label(root,text ="", font = ("",15),bg="tomato")
label9.place(x = 144, y = 165)
label8 = tk.Label(root,text ="", font = ("",15),bg="tomato")
label8.place(x = 124, y = 165)
nigate = tk.Label(root,text ="苦手キー:", font = ("",15),bg="tomato")
nigate.place(x = 35, y = 165)
#%
persent_bg = tk.Label(root,text ="          ", font = ("",15),bg="tomato")
persent_bg.place(x = 157, y = 130)
persent = tk.Label(root,text ="%", font = ("",15),bg="tomato")
persent.place(x = 212, y = 130)
label7 = tk.Label(root,text ="0", font = ("",15),bg="tomato")
label7.place(x = 162, y = 130)
label6 = tk.Label(root,text ="成功率", font = ("",15),bg="tomato")
label6.place(x = 151, y = 110)
#効果音
mixer.init()        #初期化
sound2=pygame.mixer.Sound("bad.mp3")
sound3=pygame.mixer.Sound("success.mp3")
sound4=pygame.mixer.Sound("pa.mp3")
#bgm
mu = pygame.mixer.Sound("muon.mp3")
sound=pygame.mixer.Sound("yukai.mp3")
sound5=pygame.mixer.Sound("simple.mp3")	
sound6=pygame.mixer.Sound("sound.mp3")
sound7=pygame.mixer.Sound("sound_two.mp3")
sound8=pygame.mixer.Sound("sound_three.mp3")	
mu.play(-1)
# メインループ
click = -1
def show_text():
    global click
    click = click + 1
    if click == 0:
        mu.stop()
        sound.play(-1)
        button["bg"]="green"
    elif click == 1:
        sound.stop()
        sound5.play(-1)
        button["bg"]="red"
    elif click == 2:
        sound5.stop()
        sound6.play(-1)
        button["bg"]="blue"
    elif click == 3:
        sound6.stop()
        sound7.play(-1)
        button["bg"]="purple"
    elif click == 4:
        sound7.stop()
        sound8.play(-1)
        button["bg"]="orange"
    elif click == 5:
        sound8.stop()
        mu.play(-1)
        button["bg"]="gray"
        click = -1
'''
def reset():
    global now 
    now = 0
    timer.destroy()
now = 0
class Clock():
    def __init__(self):
        self.timer = tk.Label(text="", font=('Helvetica', 12))
        self.timer.place(x=270,y=22)
        self.update_clock()
        

    def update_clock(self):        
        global now
        now += 0.5
        self.timer.configure(text=str(int(now)))
        self.timer.after(1000, self.update_clock)
Clock().__init__
timer = tk.Button(root, text="タイマー", bg="gray", fg="white", command=reset)
timer.place(x=260,y=22)
'''
button = tk.Button(root, text="BGM", bg="gray", fg="white", command=show_text)
button.pack()
button.place(x=260,y=130)

#kaisi = tk.Button(root, text="開始", bg="gray", fg="white", command=start)
#kaisi.pack()
#kaisi.place(x=260,y=160)
root.mainloop()
