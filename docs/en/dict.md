# 23. Dictionary

[TOP](../../readme.md)
/
[JP](../jp/dict.md)

See [dict.csv](https://github.com/Eruhitsuji/SFGPL/blob/main/dict.csv) for details.

|ID|word|func|How to use|Japanese|English|
|:--:|:--:|:--:|:--:|:--:|:--:|
|0|pa|LangObj. NOT|pa A|Aでない|not A|
|1|pe|LangObj. Because|pe A B|AなぜならばB|A because B|
|2|pi|LangObj. IF|pi A B|もしAならばBである|if A, B|
|3|pu|LangObj. So|pu A B|AだからB|A so B|
|4|po|LangObj. But|po A B|AしかしB|A but B|
|5|ba|LangObj. AND|ba A B|AかつB|A and B|
|6|be|LangObj. OR|be A B|AまたはB|A or B|
|7|bi|LangObj. IFELSE|bi A B C|もしAならばBである，そうでなければCである|If A, B, otherwise C|
|8|bu|LangObj. NAND|bu A B|AかつBでない|A nand B|
|9|bo|LangObj. NOR|bo A B|AまたはBでない|A nor B|
|10|ja|LangObj. logicIFELSE|ja A B C|もしAならばBを出力，そうでなければCを出力する|If A, output B, otherwise output C|
|11|fa|Noun|fa A|Aは存在する|There be A /  A exist|
|12|fi|Noun. V2N|fi A|動詞から名詞に変換する|Converting verbs to nouns.|
|13|fu|Noun. M2N|fu A|修飾語から名詞に変換する|Converting modifiers to nouns.|
|14|fo|Noun. none|fo|品詞が名詞の無意味の語を作る|The part of speech makes the noun nonsensical|
|15|ma|Noun. eq|ma A F B|AはBで(F)ある|A F(Verbs such that A means equal to B) B|
|16|me|Noun. haveP|me A F B|AがBという性質が(F)ある|A F(Verbs such that A means equal to B) B|
|17|mi|Noun. have|mi A F B|AはBを所有している/AはBを含んでいる|A have B/ A include B|
|18|mu|Noun. belong|mu A F B|AはBに所属している/AはBに含まれている|A belongs to B/ A is included in B|
|19|mo|Noun. gt|mo A F B C|AはCより（Bという比較基準で）大きい|A is more B than C|
|20|moa|Noun. hearSay|moa A F B C|Bという内容をCという情報源から，AはFする|A(Subject) F(Verb) that B(Content) according to C(Source)|
|21|ta|Noun. do|ta A F|AはF（～する）|A F(do)|
|22|te|Noun. doT|te A F B|AはBをF（～する）|A F(do) B|
|23|ti|Noun. give|ti A F B C|AはBにCをF（～与える）|A F(give) B C|
|24|tu|Noun. makeN|tu A F B C|AはBをCの状態にF（～する）|A F(make) B C[Noun]|
|25|to|Noun. makeM|to A F B C|AはBをCの状態にF（～する）|A F(make) B C[Modifier]|
|26|da|Phrase. interrogative|da A|A（～ですか）[疑問]|A(interrogative form)|
|27|de|Phrase. imperative|de A|A（～しろ）[命令]|A(imperative form)|
|28|di|Phrase. past|di A|A（～した）[過去]|A(did)|
|29|du|Phrase. future|du A|A（～するだろう/する予定である）[未来]|A(will do /  be going to do)|
|30|sa|Verb|sa A|A（～する）行為が存在する|There is an act of A|
|31|si|Verb. M2V|si A|修飾語から動詞に変換する|Converting from modifiers to verbs.|
|32|su|Verb. N2V|su A|名詞から動詞に変換する|Converting from nouns to verbs.|
|33|so|Verb. none|so|品詞が動詞の無意味の語を作る|The part of speech makes the verb nonsensical|
|34|na|Verb. add|na A B|A（～する）にB（～く/～に）[副詞]という意味を付加する|Adding the meaning of B to A [verb]|
|35|ne|Verb. passive|ne A|A（～される）[受動]|A(be done)|
|36|ni|Verb. progressive|ni A|A（～している）[継続]|A(be doing)|
|37|nu|Verb. perfective|nu A|A（～したことのある）[経験/完了/結果/継続]|A(have done)|
|38|la|Modifier|la A|A（～な/～の/～に/～く）[形容詞/副詞]という修飾語が存在する|There is a modifier [adjective/ adverb] called A|
|39|li|Modifier. N2M|li A|A（～の/～に/～で）|(of/ in/ at/ on/ by/ with etc.) A|
|40|lu|Modifier. V2M|lu A|動詞から修飾語に変換する|Converting verbs to modifiers.|
|41|lo|Modifier. none|lo|品詞が修飾語の無意味の語を作る|The part of speech makes the modifier nonsensical|
|42|ka|Modifier. add|ka A B|AにB[副詞]という意味を付加する|Adding the meaning of B to A [modifier]|
|43|ke|Modifier. Neg|ke A|Aでなく|not A|
|44|ki|Modifier. Very|ki A|とてもAである|very A|
|45|pan|DeterminerN. biology|pan A|名詞を「Aが何らかの人や生物」と限定する|Limit nouns to 'A is some kind of person or creature'|
|46|pen|DeterminerN. thing|pen A|名詞を「Aが何らかの物や概念」と限定する|Limit nouns to 'A is some object or concept'|
|47|pin|DeterminerN. time|pin A|名詞を「Aが何らかの時間」と限定する|Limit a noun to 'A is some time'|
|48|pun|DeterminerN. place|pun A|名詞を「Aが何らかの場所」と限定する|Limit a noun to 'A is some place'|
|49|pon|DeterminerN. reason|pon A|名詞を「Aが何らかの理由」と限定する|Limit a noun to 'A is some reason'|
|50|ban|DeterminerN. method|ban A|名詞を「Aが何らかの方法や道具や手段」と限定する|Limit nouns to 'A is some way or tool or means'|
|51|ben|DeterminerN. human|ben A|名詞を「Aが何らかの人間」と限定する|Limit nouns to 'A is some kind of human being'|
|52|bin|DeterminerN. animal|bin A|名詞を「Aが何らかの動物」と限定する|Limit nouns to 'A is some kind of animal'|
|53|bun|DeterminerN. plant|bun A|名詞を「Aが何らかの植物」と限定する|Limit the noun to 'A is some kind of plant'|
|54|bon|DeterminerN. material|bon A|名詞を「Aが何らかの材料」と限定する|Limit the noun to 'A is some kind of material'|
|55|fan|DeterminerN. start|fan A|名詞を「Aが何らかの始点」と限定する|Limit a noun to 'A is some starting point'|
|56|fen|DeterminerN. end|fen A|名詞を「Aが何らかの終点」と限定する|Limit a noun to 'A is some end point'|
|57|fin|DeterminerN. section|fin A|名詞を「Aが何らかの区間」と限定する|Limit a noun to 'A is some interval'|
|58|fun|DeterminerN. In|fun A|名詞を「Aが何らかの中」と限定する|Limit nouns to 'A is in some'|
|59|fon|DeterminerN. Out|fon A|名詞を「Aが何らかの外」と限定する|Limit nouns to 'A is out some'|
|60|man|DeterminerN. above|man A|名詞を「Aが何らかの上」と限定する|Limit nouns to 'A above some'|
|61|men|DeterminerN. below|men A|名詞を「Aが何らかの下」と限定する|Limit nouns to 'A is below some'|
|62|min|DeterminerN. on|min A|名詞を「Aが何らかに接地している」と限定する|Limit nouns to 'A is grounded to something'|
|63|mun|DeterminerN. right|mun A|名詞を「Aが何らかの右」と限定する|Limit nouns to 'A is some right'|
|64|mon|DeterminerN. left|mon A|名詞を「Aが何らかの左」と限定する|Limit nouns to 'A is some left'|
|65|tan|DeterminerN. affect|tan A|名詞を「Aが何らかの影響を与えるものや関連していること」と限定する|Limit the noun to 'something that A affects or is related to in some way'|
|66|ten|DeterminerN. affected|ten A|名詞を「Aが何らかの影響が与えられるもの」と限定する|Limit noun to 'something that A is affected by in some way'|
|67|tin|DeterminerN. near|tin A|名詞を「Aが近くにあるものや関連しているもの」と限定する|Limit the noun to 'something that A is near or related to'.|
|68|tun|DeterminerN. move|tun A|名詞を「Aが横切る」や「Aが通る」「Aが向かう」と動きのあるものに限定する|Limit nouns to those with motion, such as 'A crosses', 'A passes' or 'A heads'.|
|69|ton|DeterminerN. stop|ton A|名詞を静止のあるものに限定する|Limit nouns to those with static|
|70|dan|DeterminerN. all|dan A|名詞を「すべてのA」と限定する|Limit the noun to 'all A'|
|71|den|DeterminerN. many|den A|名詞を「多くのA」と限定する|Limit the noun to 'many A', 'much A' or 'a lot of A'|
|72|din|DeterminerN. some|din A|名詞を「いくつかのA」と限定する|Limit the noun to 'some A', 'a few A' or 'several A'|
|73|dun|DeterminerN. one|dun A|名詞を「ある（一つの）A」と限定する|Limit the noun to 'a certain A', 'one certain A'.|
|74|don|DeterminerN. plural|don A|名詞を複数形にする|Making nouns plural|
|75|san|DeterminerN. stressed|san A|名詞を強調形する|Stressed form of nouns.|
|76|sen|DeterminerN. possessive|sen A|所有代名詞を作成する|Creating possessive pronouns|
|77|sin|DeterminerN. reflexive|sin A|再帰代名詞を作成する|Creating recursive pronouns|
|78|sun|DeterminerN. etc|sun A|名詞を「Aなど」と限定する|Limit nouns to 'A etc.'|
|79|son|DeterminerN. abstract|son A|～的/～のようなもの/名詞を抽象化する|something like A/ Abstracting nouns|
|80|nan|DeterminerN. front|nan A|名詞を「Aが何らかの空間的に前」と限定する|Limit nouns to 'A is in front of some space'|
|81|nen|DeterminerN. behind|nen A|名詞を「Aが何らかの空間的に後ろ」と限定する|Limit nouns to 'A is behind in some space'|
|82|nun|DeterminerN. future|nun A|名詞を「Aが何らかの時間的に未来」と限定する|Limit nouns to 'A is some time in the future'|
|83|non|DeterminerN. past|non A|名詞を「Aが何らかの時間的に過去」と限定する|Limit nouns to 'A is some time in the past'|
|84|lan|DeterminerN. male|lan A|名詞を「Aが何らかの男性や雄」と限定する|Limit noun to 'A is some male'|
|85|len|DeterminerN. female|len A|名詞を「Aが何らかの女性や雌」と限定する|Limit the noun to 'A is some female'|
|86|pak|DeterminerV. Estimation100|pak A|100%の確率でAする|100% probability A|
|87|pek|DeterminerV. Estimation75|pek A|75%の確率でAする|75% probability A|
|88|pik|DeterminerV. Estimation50|pik A|50%の確率でAする|50% probability A|
|89|puk|DeterminerV. Estimation25|puk A|25%の確率でAする|25% probability A|
|90|pok|DeterminerV. Estimation0|pok A|0%の確率でAする|0% probability A|
|91|fak|DeterminerV. Frequency100|fak A|100%ぐらいの頻度でAする|100% frequently A|
|92|fek|DeterminerV. Frequency75|fek A|75%ぐらいの頻度でAする|75% frequently A|
|93|fik|DeterminerV. Frequency50|fik A|50%ぐらいの頻度でAする|50% frequently A|
|94|fuk|DeterminerV. Frequency25|fuk A|25%ぐらいの頻度でAする|25% frequently A|
|95|fok|DeterminerV. Frequency0|fok A|0%ぐらいの頻度でAする|0% frequently A|
|96|tak|DeterminerV. Start|tak A|Aし始める|Someone starts doing something|
|97|tek|DeterminerV. Condition|tek A|Aしている途中である|Someone is in the middle of doing something|
|98|tik|DeterminerV. Complete|tik A|Aしている途中だったが完了した|Someone was in the middle of doing something but has completed|
|99|tuk|DeterminerV. Continue|tuk A|Aしている状態が続いている|Someone is still doing something|
|100|tok|DeterminerV. End|tok A|Aし終える|Someone finishes doing something|
|101|bak|DeterminerV. past|bak A|過去にはAであった|In the past it was A|
|102|bik|DeterminerV. present|bik A|現在Aである|In the present it is A|
|103|bok|DeterminerV. future|bok A|未来にはAだろう|In the future it will be A|
|104|nak|DeterminerV. Possible|nak A|Aできる/Aすることが可能である|can|
|105|nek|DeterminerV. Ability|nek A|Aする能力がある|can|
|106|nik|DeterminerV. Will|nik A|Aしよう|will/ shall|
|107|nuk|DeterminerV. Obligation|nuk A|Aすべきだ|should/ ought to|
|108|nok|DeterminerV. Necessary|nok A|Aする必要がある|need to|
|109|lak|DeterminerV. Duty|lak A|Aしなければならない|must/ have to|
|110|lek|DeterminerV. forced|lek A|外部からの強い力で強制的にAさせられる|be forced to A by a strong external force|
|111|lik|DeterminerV. want|lik A|Aしたい/Aすることを願望する|want to A|
|112|luk|DeterminerV. dare|luk A|あえてAする/思い切ってAする/Aする勇気がある|dare A|
|113|lok|DeterminerV. allow|lok A|Aすることを許す|allow to A|
|114|kak|DeterminerV. easy|kak A|Aしやすい|be easy to A|
|115|kek|DeterminerV. hard|kek A|Aしにくい|be hard to A|
|116|kik|DeterminerV. habit|kik A|習慣的にAする|Habitually A|
|117|kuk|DeterminerV. Polite|kuk A|Aします（丁寧表現）|Make the verb a polite expression|
|118|kok|DeterminerV. Respect|kok A|Aされる（尊敬表現）|Make the verb a respectful expression|
|119|gak|DeterminerV. volitional|gak A|意識的にAする|Consciously A|
|120|gek|DeterminerV. nonVolitional|gek A|無意識的にAする|Unconsciously A|
|121|gik|DeterminerV. Requests|gik A|Aしてください|will/ would/ can/ could|
|122|guk|DeterminerV. Permission|guk A|Aしてもよいですか|can/ may|
|123|gok|DeterminerV. Suggestion|gok A|Aしましょうか|shall|
|124|ga|Pronoun. I|ga|私|I|
|125|ge|Pronoun. you|ge|あなた|you|
|126|gi|Pronoun. he|gi|彼/彼女/それ|he/ she/ it|
|127|gu|Pronoun. proximal|gu|これ|this|
|128|go|Pronoun. distal|go|それ/あれ|that|
|129|wa|Pronoun. interrogative|wa|どれ|what|
|130|we|Pronoun. indefinite|we|どれか|something|
|131|kan|WordV. create|kan|生み出す/作る/産む|create/ make/ bear|
|132|ken|WordV. destroy|ken|破壊する/壊す/死ぬ|destroy/ break/ die|
|133|kin|WordV. act|kin|行動する/動く/実行する/歩く/働く|act/ move/ do/ walk/ work|
|134|kun|WordV. turn|kun|回る/回転する/急ぐ/走る|turn/ rotate/ hurry/ run|
|135|kon|WordV. receive|kon|感じ取る/受信する/受け取る/入れる/摂取する/取得する/得る/習う/聞く/見る/食べる/飲む|receive/ accept/ acquire/ get/ learn/ hear/ see/ listen/ look at/ watch/ eat/ drink|
|136|gan|WordV. stimulate|gan|発する/発信する/発射する/出す/送信する/送る/教える/刺激する/言う/話す/攻撃する|emit/ transmit/ put out/ send/ give/ teach/ stimulate/ say/ speak/ attack|
|137|gen|WordV. exist|gen|ある/いる/存在する/生きている/住んでいる/留まる/止まっている/休む|be/ exist/ live/ stay/ be stopping/ get rest|
|138|gin|WordV. use|gin|使う/使用する|use|
|139|gun|WordV. change|gun|変わる/なる/成長する/移行する/移動する|change/ become/ grow/ transfer|
|140|wan|WordM. big|wan|大きい/長い/広い/高い/多い/重い|big/ long/ wide/ tall/ many/ heavy/ large|
|141|wen|WordM. near|wen|近い/親しい/似ている/好きである|near/ familiar/ close to/ similar/ like|
|142|win|WordM. good|win|良い/新しい/若い/美しい|good/ new/ young/ beautiful|
|143|won|WordM. bright|won|明るい/白い/色鮮やかな|bright/ white/ colourful|
|144|pas|Bool. false|pas|偽|False (Boolean)|
|145|pos|Bool. true|pos|真|True (Boolean)|
|146|pis|Bool. B2N|pis A B|AはBである（Bは真偽）|A is B (B is true or false)|
|147|fas|BoolList|fas|真偽のリスト（BoolList）を作成する|Create a list of true/ false (BoolList)|
|148|fes|BoolList. get|fes A B|BoolList(A)のB番目の値を取得する|Gets the B-th value of BoolList(A)|
|149|fis|BoolList. append|fis A B|BoolListに1つのBoolを末尾に加える|Add one Bool to the end of the BoolList|
|150|fus|BoolList. slice|fus A B C|AというBoolListに対して，B番目からC番目までのリストを取得する|Get the B-th through C-th lists for a BoolList (A).|
|151|fos|BoolList. add|fos A B|2つのBoolListを結合する|Combine two BoolLists|
|152|mas|BoolList. twoBit|mas A B|2つBoolの値からなるBoolListを作成する|Create a BoolList consisting of 2 Bool values|
|153|mis|BoolList. fourBit|mis A B C D|4つBoolの値からなるBoolListを作成する|Create a BoolList consisting of 4 Bool values|
|154|mos|BoolList. byte|mos X1 X2 X3 X4 X5 X6 X7 X8|8つBoolの値からなるBoolListを作成する|Create a BoolList consisting of 8 Bool values|
|155|tas|BoolList. NaturalNum|tas A|BoolListを2進数の自然数とみなす|BoolList is considered a binary natural number|
|156|tes|BoolList. Int|tes A|BoolListを2進数の整数とみなす|BoolList is considered a binary integer|
|157|tis|BoolList. Float|tis A|BoolListを2進数の浮動小数とみなす|BoolList is considered a binary floating number|
|158|tus|BoolList. ASCII|tus A|BoolListをASCII文字とみなす|BoolList is considered an ASCII character|
|159|tos|BoolList. IntBL2NL|tos A|整数のBoolListをNumberListに変換する|Convert an integer BoolList to a NumberList|
|160|pat|LangFunc. setFunc|pat A B|あるLangListを引数とするAという名前のBを返す関数を設定する|Set up a function that returns B named A with a certain LangList as an argument.|
|161|pit|LangFunc. arg|pit|LangFunc.setFunc()の引数用に使用する|Used for LangFunc.setFunc() arguments|
|162|pot|LangFunc. runFunc|pot A B|設定したAという名前のLangFuncを引数Bとして実行する|Execute the configured LangFunc named A with argument B|
|163|fat|LangList|fat|LangObjのリストLangListを作成する|Create a list of LangObj (LangList)|
|164|fet|LangList. get|fet A B|LangList(A)のB番目の値を取得する|Gets the B-th value of LangList(A)|
|165|fit|LangList. append|fit A B|LangListに1つのLangObjを末尾に加える|Add one LangObj to the end of the LangList|
|166|fut|LangList. slice|fut A B C|AというLangListに対して，B番目からC番目までのリストを取得する|Get the B-th through C-th lists for a LangList (A).|
|167|fot|LangList. add|fot A B|2つのLangListを結合する|Combine two LangLists|
|168|tat|LangList. While|tat A B C|繰り返し処理を行う|Repeat processing|
|169|pal|Number. zero|pal|0|0|
|170|pel|Number. one|pel|1|1|
|171|pil|Number. two|pil|2|2|
|172|pul|Number. three|pul|3|3|
|173|pol|Number. four|pol|4|4|
|174|bal|Number. five|bal|5|5|
|175|bel|Number. six|bel|6|6|
|176|bil|Number. seven|bil|7|7|
|177|bul|Number. eight|bul|8|8|
|178|bol|Number. nine|bol|9|9|
|179|fal|NumberList|fal|NumberのリストNumberListを作成する|Create a list of Number(NumberList)|
|180|fel|NumberList. get|fel A B|NumberList(A)のB番目の値を取得する|Gets the B-th value of NumberList(A)|
|181|fil|NumberList. append|fil A B|NumberListに1つのNumberを末尾に加える|Add one Number to the end of the NumberList|
|182|ful|NumberList. slice|ful A B C|AというNumberListに対して，B番目からC番目までのリストを取得する|Get the B-th through C-th lists for a NumberList (A).|
|183|fol|NumberList. add|fol A B|2つのNumberListを結合する|Combine two NumberLists|
|184|mal|NumberList. digit1|mal A|10進数1桁からなるNumberListを作成する|Create a NumberList consisting of one decimal digit|
|185|mel|NumberList. digit2|mel A B|10進数2桁からなるNumberListを作成する|Create a NumberList consisting of two decimal digit|
|186|mil|NumberList. digit3|mil A B C|10進数3桁からなるNumberListを作成する|Create a NumberList consisting of three decimal digit|
|187|mul|NumberList. digit4|mul A B C D|10進数4桁からなるNumberListを作成する|Create a NumberList consisting of four decimal digit|
|188|mol|NumberList. digit5|mol A B C D E|10進数5桁からなるNumberListを作成する|Create a NumberList consisting of five decimal digit|
|189|tal|NumberList. calcAdd|tal A B|2つのNumberListに対して加算をする|Perform addition on two NumberLists|
|190|tel|NumberList. calcSub|tel A B|2つのNumberListに対して減算をする|Perform subtraction on two NumberLists|
|191|til|NumberList. calcMul|til A B|2つのNumberListに対して乗算をする|Perform multiplication on two NumberLists|
|192|tul|NumberList. calcDiv|tul A B|2つのNumberListに対して除算をする|Perform division on two NumberLists|
|193|tol|NumberList. IntNL2BL|tol A|整数のNumberListをBoolListに変換する|Convert an integer NumberList to a BoolList|
|194|sal|NumberList. isPN|sal A|正の数かを判定する|Determine if it is a positive number|

