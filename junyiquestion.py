#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:23:32 2020

@author: Chris
"""


"""
#1. (A) 請寫一個程式把裡面的字串反過來。
#程式區
"""
def inversestring(string):
        string=string[::-1]
        return string
#驗證區
string="junyiacademy"
print(inversestring(string))

"""
#(B) 請寫一個程式把裡面的字串,每個單字本身做反轉,但是單字的順序不變。
#程式區
"""
def inversesentence(sentence):
    letter=''
    ans=''
    for i in range(len(sentence)):
        if (sentence[i] != ' ') or (sentence[i]==len(sentence)):
            letter = letter + sentence[i]
        else:
            letter = inversestring(letter)
            ans= ans + letter + ' '
            letter=''
    sentence= ans[0:len(sentence)]
    return sentence

#驗證區
sentence="flipped class room is important"
print(inversesentence(sentence))


"""
2. 請寫一個程式,Input 是一個數字,Output 是從 1 到這個數字,扣除掉所有 3 的倍數以及 5 的倍數,但是需要保留同時是 3 和 5 的倍數的總數字數。
#程式區
"""
def count35(num):
    total=num-int(num/3)-int(num/5)+2*int(num/15)
    return total
#驗證區
num=100
print(count35(15))


"""
3. 房間裡有三個袋子,一個只裝鉛筆,一個只裝原子筆,第三個有鉛筆也有原子筆。
袋子是不透明的,單從袋子的外表上看不出任何差異,你不知道哪個袋子裝什麼。
除了袋子上各貼了一個標示("鉛筆"、"原子筆"、"混和"),且標示都是錯的
(e.g. 標示鉛筆的袋子可能是混和的或是只裝原子筆)。
你只能選一個袋子,拿出裡面一支筆,看是鉛筆還是原子筆,然後你要推論出這三
個袋子分別的情況。請列出你的作法,以及解釋為什麼這樣可以找到答案。

<答>
時間不夠，故無作答。
但認為並無此可能，除非可以搖晃袋子聽聲音，不然老實的照著題型走好像不可能。
原因是這樣的，因為標示是錯的，所以任何一袋都有可能是混合，所以當你今天從一袋中抽出一隻筆，不構成認定此袋子狀態的依據。
"""


"""
4. 有三個人一起到迪士尼遊玩,中午肚子餓了,去餐廳點了一份現在最夯的冰雪奇緣
雙人組,要價 900 元,付錢後,服務生發現今天套餐大特價,只要 750 元,因此
服務生應該退還 150 元給這三個人,但是這位服務生一時鬼迷心竅,決定暗槓 60
元,只退了 90 元給這三個遊客。
那麼:三人各出 300 元 - 服務生還給他們一人 30 元 = 三人各出 270 元。270
元 × 3 人+ 服務生私吞的 60 元 = 810 + 60 = 870 !? 怎麼不是 900 元呢?還
有 30 元去哪了呢?請用敘述的方式,儘量清楚解釋問題出在哪裡。


<答>
首先，服務生私吞的前是由三個人提供的，故60$是涵蓋在810$的部分。
故此算式 810 + 60 = 870 又重複算兩次60$且沒實質意義。
如果想要已算式表示原本價格900的話，應該這樣想：
特價完只要750$，三人原本只要各出250$，但因為服務生暗槓60$，所以每個人要在多出20$，因此每個平均要出(250+20$)
，也因為服務生暗槓的關係（說特價後是750+60=810$），故實際優惠的部分只有90$。
而式子應該這樣列...
(250+20)*3+90=750+60+90=900
"""



#test for test
