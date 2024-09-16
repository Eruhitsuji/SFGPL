# 24. Dictionary

[TOP](../../readme.md)
/
[JP](../jp/dict.md)

See [dict.csv](https://github.com/Eruhitsuji/SFGPL/blob/main/dict.csv) for details.

|ID|word|func|How to use|Japanese|English|
|:--:|:--:|:--:|:--:|:--:|:--:|
|0|pa|```LangObj.NOT```|pa A|Aでない|not A|
|1|pe|```LangObj.Because```|pe A B|AなぜならばB|A because B|
|2|pi|```LangObj.IF```|pi A B|もしAならばBである|if A, B|
|3|pu|```LangObj.So```|pu A B|AだからB|A so B|
|4|po|```LangObj.But```|po A B|AしかしB|A but B|
|5|ba|```LangObj.AND```|ba A B|AかつB|A and B|
|6|be|```LangObj.OR```|be A B|AまたはB|A or B|
|7|bi|```LangObj.IFELSE```|bi A B C|もしAならばBである，そうでなければCである|If A, B, otherwise C|
|8|bu|```LangObj.NAND```|bu A B|AかつBでない|A nand B|
|9|bo|```LangObj.NOR```|bo A B|AまたはBでない|A nor B|
|10|ja|```LangObj.logicIFELSE```|ja A B C|もしAならばBを出力，そうでなければCを出力する|If A, output B, otherwise output C|
|11|fa|```Noun```|fa A|Aは存在する|There be A /  A exist|
|12|foa|```Noun.borrowed```|foa A B|Aという名詞の単語をBという言語から借用する|Borrowing noun words called A from the language B|
|13|fi|```Noun.V2N```|fi A|動詞から名詞に変換する|Converting verbs to nouns.|
|14|fu|```Noun.M2N```|fu A|修飾語から名詞に変換する|Converting modifiers to nouns.|
|15|fo|```Noun.none```|fo|品詞が名詞の無意味の語を作る|The part of speech makes the noun nonsensical|
|16|ma|```Noun.eq```|ma A F B|AはBで(F)ある|A F(Verbs such that A means equal to B) B|
|17|me|```Noun.haveP```|me A F B|AがBという性質が(F)ある|A F(Verbs such that A means equal to B) B|
|18|mi|```Noun.have```|mi A F B|AはBを所有している/AはBを含んでいる|A have B/ A include B|
|19|mu|```Noun.belong```|mu A F B|AはBに所属している/AはBに含まれている|A belongs to B/ A is included in B|
|20|mo|```Noun.gt```|mo A F B C|AはCより（Bという比較基準で）大きい|A is more B than C|
|21|moa|```Noun.hearSay```|moa A F B C|Bという内容をCという情報源から，AはFする|A(Subject) F(Verb) that B(Content) according to C(Source)|
|22|ta|```Noun.do```|ta A F|AはF（～する）|A F(do)|
|23|te|```Noun.doT```|te A F B|AはBをF（～する）|A F(do) B|
|24|ti|```Noun.give```|ti A F B C|AはBにCをF（～与える）|A F(give) B C|
|25|tu|```Noun.makeN```|tu A F B C|AはBをCの状態にF（～する）|A F(make) B C[Noun]|
|26|to|```Noun.makeM```|to A F B C|AはBをCの状態にF（～する）|A F(make) B C[Modifier]|
|27|da|```Phrase.interrogative```|da A|A（～ですか）[疑問]|A(interrogative form)|
|28|de|```Phrase.imperative```|de A|A（～しろ）[命令]|A(imperative form)|
|29|di|```Phrase.past```|di A|A（～した）[過去]|A(did)|
|30|du|```Phrase.future```|du A|A（～するだろう/する予定である）[未来]|A(will do /  be going to do)|
|31|sa|```Verb```|sa A|A（～する）行為が存在する|There is an act of A|
|32|soa|```Verb.borrowed```|soa A B|Aという動詞の単語をBという言語から借用する|Borrowing verb words called A from the language B|
|33|si|```Verb.M2V```|si A|修飾語から動詞に変換する|Converting from modifiers to verbs.|
|34|su|```Verb.N2V```|su A|名詞から動詞に変換する|Converting from nouns to verbs.|
|35|so|```Verb.none```|so|品詞が動詞の無意味の語を作る|The part of speech makes the verb nonsensical|
|36|na|```Verb.add```|na A B|A（～する）にB（～く/～に）[副詞]という意味を付加する|Adding the meaning of B to A [verb]|
|37|ne|```Verb.passive```|ne A|A（～される）[受動]|A(be done)|
|38|ni|```Verb.progressive```|ni A|A（～している）[継続]|A(be doing)|
|39|nu|```Verb.perfective```|nu A|A（～したことのある）[経験/完了/結果/継続]|A(have done)|
|40|la|```Modifier```|la A|A（～な/～の/～に/～く）[形容詞/副詞]という修飾語が存在する|There is a modifier [adjective/ adverb] called A|
|41|loa|```Modifier.borrowed```|loa A B|Aという修飾詞の単語をBという言語から借用する|Borrowing modifier words called A from the language B|
|42|li|```Modifier.N2M```|li A|A（～の/～に/～で）|(of/ in/ at/ on/ by/ with etc.) A|
|43|lu|```Modifier.V2M```|lu A|動詞から修飾語に変換する|Converting verbs to modifiers.|
|44|lo|```Modifier.none```|lo|品詞が修飾語の無意味の語を作る|The part of speech makes the modifier nonsensical|
|45|ka|```Modifier.add```|ka A B|AにB[副詞]という意味を付加する|Adding the meaning of B to A [modifier]|
|46|ke|```Modifier.Neg```|ke A|Aでなく|not A|
|47|ki|```Modifier.Very```|ki A|とてもAである|very A|
|48|pan|```DeterminerN.biology```|pan A|名詞を「Aが何らかの人や生物」と限定する|Limit nouns to 'A is some kind of person or creature'|
|49|pen|```DeterminerN.thing```|pen A|名詞を「Aが何らかの物や概念」と限定する|Limit nouns to 'A is some object or concept'|
|50|pin|```DeterminerN.time```|pin A|名詞を「Aが何らかの時間」と限定する|Limit a noun to 'A is some time'|
|51|pun|```DeterminerN.place```|pun A|名詞を「Aが何らかの場所」と限定する|Limit a noun to 'A is some place'|
|52|pon|```DeterminerN.reason```|pon A|名詞を「Aが何らかの理由」と限定する|Limit a noun to 'A is some reason'|
|53|ban|```DeterminerN.method```|ban A|名詞を「Aが何らかの方法や道具や手段」と限定する|Limit nouns to 'A is some way or tool or means'|
|54|ben|```DeterminerN.human```|ben A|名詞を「Aが何らかの人間」と限定する|Limit nouns to 'A is some kind of human being'|
|55|bin|```DeterminerN.animal```|bin A|名詞を「Aが何らかの動物」と限定する|Limit nouns to 'A is some kind of animal'|
|56|bun|```DeterminerN.plant```|bun A|名詞を「Aが何らかの植物」と限定する|Limit the noun to 'A is some kind of plant'|
|57|bon|```DeterminerN.material```|bon A|名詞を「Aが何らかの材料」と限定する|Limit the noun to 'A is some kind of material'|
|58|fan|```DeterminerN.start```|fan A|名詞を「Aが何らかの始点」と限定する|Limit a noun to 'A is some starting point'|
|59|fen|```DeterminerN.end```|fen A|名詞を「Aが何らかの終点」と限定する|Limit a noun to 'A is some end point'|
|60|fin|```DeterminerN.section```|fin A|名詞を「Aが何らかの区間」と限定する|Limit a noun to 'A is some interval'|
|61|fun|```DeterminerN.In```|fun A|名詞を「Aが何らかの中」と限定する|Limit nouns to 'A is in some'|
|62|fon|```DeterminerN.Out```|fon A|名詞を「Aが何らかの外」と限定する|Limit nouns to 'A is out some'|
|63|man|```DeterminerN.above```|man A|名詞を「Aが何らかの上」と限定する|Limit nouns to 'A above some'|
|64|men|```DeterminerN.below```|men A|名詞を「Aが何らかの下」と限定する|Limit nouns to 'A is below some'|
|65|min|```DeterminerN.on```|min A|名詞を「Aが何らかに接地している」と限定する|Limit nouns to 'A is grounded to something'|
|66|mun|```DeterminerN.right```|mun A|名詞を「Aが何らかの右」と限定する|Limit nouns to 'A is some right'|
|67|mon|```DeterminerN.left```|mon A|名詞を「Aが何らかの左」と限定する|Limit nouns to 'A is some left'|
|68|tan|```DeterminerN.affect```|tan A|名詞を「Aが何らかの影響を与えるものや関連していること」と限定する|Limit the noun to 'something that A affects or is related to in some way'|
|69|ten|```DeterminerN.affected```|ten A|名詞を「Aが何らかの影響が与えられるもの」と限定する|Limit noun to 'something that A is affected by in some way'|
|70|tin|```DeterminerN.near```|tin A|名詞を「Aが近くにあるものや関連しているもの」と限定する|Limit the noun to 'something that A is near or related to'.|
|71|tun|```DeterminerN.move```|tun A|名詞を「Aが横切る」や「Aが通る」「Aが向かう」と動きのあるものに限定する|Limit nouns to those with motion, such as 'A crosses', 'A passes' or 'A heads'.|
|72|ton|```DeterminerN.stop```|ton A|名詞を静止のあるものに限定する|Limit nouns to those with static|
|73|dan|```DeterminerN.all```|dan A|名詞を「すべてのA」と限定する|Limit the noun to 'all A'|
|74|den|```DeterminerN.many```|den A|名詞を「多くのA」と限定する|Limit the noun to 'many A', 'much A' or 'a lot of A'|
|75|din|```DeterminerN.some```|din A|名詞を「いくつかのA」と限定する|Limit the noun to 'some A', 'a few A' or 'several A'|
|76|dun|```DeterminerN.one```|dun A|名詞を「ある（一つの）A」と限定する|Limit the noun to 'a certain A', 'one certain A'.|
|77|don|```DeterminerN.plural```|don A|名詞を複数形にする|Making nouns plural|
|78|san|```DeterminerN.stressed```|san A|名詞を強調形する|Stressed form of nouns.|
|79|sen|```DeterminerN.possessive```|sen A|所有代名詞を作成する|Creating possessive pronouns|
|80|sin|```DeterminerN.reflexive```|sin A|再帰代名詞を作成する|Creating recursive pronouns|
|81|sun|```DeterminerN.etc```|sun A|名詞を「Aなど」と限定する|Limit nouns to 'A etc.'|
|82|son|```DeterminerN.abstract```|son A|～的/～のようなもの/大体の～/おおよそ～ぐらい/名詞を抽象化する|something like A/ Abstracting nouns|
|83|nan|```DeterminerN.front```|nan A|名詞を「Aが何らかの空間的に前」と限定する|Limit nouns to 'A is in front of some space'|
|84|nen|```DeterminerN.behind```|nen A|名詞を「Aが何らかの空間的に後ろ」と限定する|Limit nouns to 'A is behind in some space'|
|85|nun|```DeterminerN.future```|nun A|名詞を「Aが何らかの時間的に未来」と限定する|Limit nouns to 'A is some time in the future'|
|86|non|```DeterminerN.past```|non A|名詞を「Aが何らかの時間的に過去」と限定する|Limit nouns to 'A is some time in the past'|
|87|lan|```DeterminerN.male```|lan A|名詞を「Aが何らかの男性や雄」と限定する|Limit noun to 'A is some male'|
|88|len|```DeterminerN.female```|len A|名詞を「Aが何らかの女性や雌」と限定する|Limit the noun to 'A is some female'|
|89|lin|```DeterminerN.every```|lin A|名詞を「Aがあらゆる何らかのもの」と限定する|Limit the noun to 'A is every something'|
|90|lun|```DeterminerN.each```|lun A|名詞を「Aがそれぞれの何らかのもの」と限定する|Limit the noun to 'A is each something'|
|91|lon|```DeterminerN.other```|lon A|名詞を「Aが他の何らかのもの」と限定する|Limit the noun to 'A is other something'|
|92|pak|```DeterminerV.Estimation100```|pak A|100%の確率でAする|100% probability A|
|93|pek|```DeterminerV.Estimation75```|pek A|75%の確率でAする|75% probability A|
|94|pik|```DeterminerV.Estimation50```|pik A|50%の確率でAする|50% probability A|
|95|puk|```DeterminerV.Estimation25```|puk A|25%の確率でAする|25% probability A|
|96|pok|```DeterminerV.Estimation0```|pok A|0%の確率でAする|0% probability A|
|97|fak|```DeterminerV.Frequency100```|fak A|100%ぐらいの頻度でAする|100% frequently A|
|98|fek|```DeterminerV.Frequency75```|fek A|75%ぐらいの頻度でAする|75% frequently A|
|99|fik|```DeterminerV.Frequency50```|fik A|50%ぐらいの頻度でAする|50% frequently A|
|100|fuk|```DeterminerV.Frequency25```|fuk A|25%ぐらいの頻度でAする|25% frequently A|
|101|fok|```DeterminerV.Frequency0```|fok A|0%ぐらいの頻度でAする|0% frequently A|
|102|tak|```DeterminerV.Start```|tak A|Aし始める|Someone starts doing something|
|103|tek|```DeterminerV.Condition```|tek A|Aしている途中である|Someone is in the middle of doing something|
|104|tik|```DeterminerV.Complete```|tik A|Aしている途中だったが完了した|Someone was in the middle of doing something but has completed|
|105|tuk|```DeterminerV.Continue```|tuk A|Aしている状態が続いている|Someone is still doing something|
|106|tok|```DeterminerV.End```|tok A|Aし終える|Someone finishes doing something|
|107|bak|```DeterminerV.past```|bak A|過去にはAであった|In the past it was A|
|108|bik|```DeterminerV.present```|bik A|現在Aである|In the present it is A|
|109|bok|```DeterminerV.future```|bok A|未来にはAだろう|In the future it will be A|
|110|nak|```DeterminerV.Possible```|nak A|Aできる/Aすることが可能である|can|
|111|nek|```DeterminerV.Ability```|nek A|Aする能力がある|can|
|112|nik|```DeterminerV.Will```|nik A|Aしよう|will/ shall|
|113|nuk|```DeterminerV.Obligation```|nuk A|Aすべきだ|should/ ought to|
|114|nok|```DeterminerV.Necessary```|nok A|Aする必要がある|need to|
|115|lak|```DeterminerV.Duty```|lak A|Aしなければならない|must/ have to|
|116|lek|```DeterminerV.forced```|lek A|外部からの強い力で強制的にAさせられる|be forced to A by a strong external force|
|117|lik|```DeterminerV.want```|lik A|Aしたい/Aすることを願望する|want to A|
|118|luk|```DeterminerV.dare```|luk A|あえてAする/思い切ってAする/Aする勇気がある|dare A|
|119|lok|```DeterminerV.allow```|lok A|Aすることを許す|allow to A|
|120|kak|```DeterminerV.easy```|kak A|Aしやすい|be easy to A|
|121|kek|```DeterminerV.hard```|kek A|Aしにくい|be hard to A|
|122|kik|```DeterminerV.habit```|kik A|習慣的にAする|Habitually A|
|123|kuk|```DeterminerV.Polite```|kuk A|Aします（丁寧表現）|Make the verb a polite expression|
|124|kok|```DeterminerV.Respect```|kok A|Aされる（尊敬表現）|Make the verb a respectful expression|
|125|gak|```DeterminerV.volitional```|gak A|意識的にAする|Consciously A|
|126|gek|```DeterminerV.nonVolitional```|gek A|無意識的にAする|Unconsciously A|
|127|gik|```DeterminerV.Requests```|gik A|Aしてください|will/ would/ can/ could|
|128|guk|```DeterminerV.Permission```|guk A|Aしてもよいですか|can/ may|
|129|gok|```DeterminerV.Suggestion```|gok A|Aしましょうか|shall|
|130|ga|```Pronoun.I```|ga|私|I|
|131|ge|```Pronoun.you```|ge|あなた|you|
|132|gi|```Pronoun.he```|gi|彼/彼女/それ|he/ she/ it|
|133|gu|```Pronoun.proximal```|gu|これ|this|
|134|go|```Pronoun.distal```|go|それ/あれ|that|
|135|wa|```Pronoun.interrogative```|wa|どれ|what|
|136|we|```Pronoun.indefinite```|we|どれか|something|
|137|kan|```WordV.create```|kan|生み出す/作る/産む|create/ make/ bear|
|138|ken|```WordV.destroy```|ken|破壊する/壊す/死ぬ|destroy/ break/ die|
|139|kin|```WordV.act```|kin|行動する/動く/実行する/歩く/働く|act/ move/ do/ walk/ work|
|140|kun|```WordV.turn```|kun|回る/回転する/急ぐ/走る|turn/ rotate/ hurry/ run|
|141|kon|```WordV.receive```|kon|感じ取る/受信する/受け取る/入れる/摂取する/取得する/得る/習う/聞く/見る/食べる/飲む|receive/ accept/ acquire/ get/ learn/ hear/ see/ listen/ look at/ watch/ eat/ drink|
|142|gan|```WordV.stimulate```|gan|発する/発信する/発射する/出す/送信する/送る/教える/刺激する/言う/話す/攻撃する|emit/ transmit/ put out/ send/ give/ teach/ stimulate/ say/ speak/ attack|
|143|gen|```WordV.exist```|gen|ある/いる/存在する/生きている/住んでいる/留まる/止まっている/休む|be/ exist/ live/ stay/ be stopping/ get rest|
|144|gin|```WordV.use```|gin|使う/使用する|use|
|145|gun|```WordV.change```|gun|変わる/なる/成長する/移行する/移動する|change/ become/ grow/ transfer|
|146|wan|```WordM.big```|wan|大きい/長い/広い/高い/多い/重い|big/ long/ wide/ tall/ many/ heavy/ large|
|147|wen|```WordM.near```|wen|近い/親しい/似ている/好きである|near/ familiar/ close to/ similar/ like|
|148|win|```WordM.good```|win|良い/新しい/若い/美しい|good/ new/ young/ beautiful|
|149|won|```WordM.bright```|won|明るい/白い/色鮮やかな|bright/ white/ colourful|
|150|pas|```Bool.false```|pas|偽|False (Boolean)|
|151|pos|```Bool.true```|pos|真|True (Boolean)|
|152|pis|```Bool.B2N```|pis A B|AはBである（Bは真偽）|A is B (B is true or false)|
|153|fas|```BoolList```|fas|真偽のリスト（BoolList）を作成する|Create a list of true/ false (BoolList)|
|154|fes|```BoolList.get```|fes A B|```BoolList(A)```のB番目の値を取得する|Gets the B-th value of ```BoolList(A)```|
|155|fis|```BoolList.append```|fis A B|BoolListに1つのBoolを末尾に加える|Add one Bool to the end of the BoolList|
|156|fus|```BoolList.slice```|fus A B C|AというBoolListに対して，B番目からC番目までのリストを取得する|Get the B-th through C-th lists for a BoolList (A).|
|157|fos|```BoolList.add```|fos A B|2つのBoolListを結合する|Combine two BoolLists|
|158|foas|```BoolList.len```|foas A|BoolListの長さを取得する|Get the length of the BoolList|
|158|mas|```BoolList.twoBit```|mas A B|2つBoolの値からなるBoolListを作成する|Create a BoolList consisting of 2 Bool values|
|159|mis|```BoolList.fourBit```|mis A B C D|4つBoolの値からなるBoolListを作成する|Create a BoolList consisting of 4 Bool values|
|160|mos|```BoolList.byte```|mos X1 X2 X3 X4 X5 X6 X7 X8|8つBoolの値からなるBoolListを作成する|Create a BoolList consisting of 8 Bool values|
|161|tas|```BoolList.NaturalNum```|tas A|BoolListを2進数の自然数とみなす|BoolList is considered a binary natural number|
|162|tes|```BoolList.Int```|tes A|BoolListを2進数の整数とみなす|BoolList is considered a binary integer|
|163|tis|```BoolList.Float```|tis A|BoolListを2進数の浮動小数とみなす|BoolList is considered a binary floating number|
|164|tus|```BoolList.ASCII```|tus A|BoolListをASCII文字とみなす|BoolList is considered an ASCII character|
|165|tos|```BoolList.IntBL2NL```|tos A|整数のBoolListをNumberListに変換する|Convert an integer BoolList to a NumberList|
|166|pat|```LangFunc.setFunc```|pat A B|あるLangListを引数とするAという名前のBを返す関数を設定する|Set up a function that returns B named A with a certain LangList as an argument.|
|167|pit|```LangFunc.arg```|pit|```LangFunc.setFunc()```の引数用に使用する|Used for ```LangFunc.setFunc()``` arguments|
|168|pot|```LangFunc.runFunc```|pot A B|設定したAという名前のLangFuncを引数Bとして実行する|Execute the configured LangFunc named A with argument B|
|169|bat|```LangVar.set```|bat A B|グローバル変数としてAという名前の変数を定義し，LangList Bを代入する|Define a variable named A as a global variable and assign LangList B to it.|
|170|bot|```LangVar.get```|bot A|定義されたAという名前のグローバル変数を取得する|Obtain the defined global variable named A|
|171|fat|```LangList```|fat|LangObjのリストLangListを作成する|Create a list of LangObj (LangList)|
|172|fet|```LangList.get```|fet A B|```LangList(A)```のB番目の値を取得する|Gets the B-th value of ```LangList(A)```|
|173|fit|```LangList.append```|fit A B|LangListに1つのLangObjを末尾に加える|Add one LangObj to the end of the LangList|
|174|fut|```LangList.slice```|fut A B C|AというLangListに対して，B番目からC番目までのリストを取得する|Get the B-th through C-th lists for a LangList (A).|
|175|fot|```LangList.add```|fot A B|2つのLangListを結合する|Combine two LangLists|
|176|foat|```LangList.len```|foat A|LangListの長さを取得する|Get the length of the LangList|
|177|tat|```LangList.While```|tat A B C|繰り返し処理を行う|Repeat processing|
|178|pal|```Number.zero```|pal|0|0|
|179|pel|```Number.one```|pel|1|1|
|180|pil|```Number.two```|pil|2|2|
|181|pul|```Number.three```|pul|3|3|
|182|pol|```Number.four```|pol|4|4|
|183|bal|```Number.five```|bal|5|5|
|184|bel|```Number.six```|bel|6|6|
|185|bil|```Number.seven```|bil|7|7|
|186|bul|```Number.eight```|bul|8|8|
|187|bol|```Number.nine```|bol|9|9|
|188|fal|```NumberList```|fal|NumberのリストNumberListを作成する|Create a list of Number (NumberList)|
|189|fel|```NumberList.get```|fel A B|```NumberList(A)```のB番目の値を取得する|Gets the B-th value of ```NumberList(A)```|
|190|fil|```NumberList.append```|fil A B|NumberListに1つのNumberを末尾に加える|Add one Number to the end of the NumberList|
|191|ful|```NumberList.slice```|ful A B C|AというNumberListに対して，B番目からC番目までのリストを取得する|Get the B-th through C-th lists for a NumberList (A).|
|192|fol|```NumberList.add```|fol A B|2つのNumberListを結合する|Combine two NumberLists|
|193|foal|```NumberList.len```|foal A|NumberListの長さを取得する|Get the length of the NumberList|
|194|mal|```NumberList.digit1```|mal A|10進数1桁からなるNumberListを作成する|Create a NumberList consisting of one decimal digit|
|195|mel|```NumberList.digit2```|mel A B|10進数2桁からなるNumberListを作成する|Create a NumberList consisting of two decimal digit|
|196|mil|```NumberList.digit3```|mil A B C|10進数3桁からなるNumberListを作成する|Create a NumberList consisting of three decimal digit|
|197|mul|```NumberList.digit4```|mul A B C D|10進数4桁からなるNumberListを作成する|Create a NumberList consisting of four decimal digit|
|198|mol|```NumberList.digit5```|mol A B C D E|10進数5桁からなるNumberListを作成する|Create a NumberList consisting of five decimal digit|
|199|tal|```NumberList.calcAdd```|tal A B|2つのNumberListに対して加算をする|Perform addition on two NumberLists|
|200|tel|```NumberList.calcSub```|tel A B|2つのNumberListに対して減算をする|Perform subtraction on two NumberLists|
|201|til|```NumberList.calcMul```|til A B|2つのNumberListに対して乗算をする|Perform multiplication on two NumberLists|
|202|tul|```NumberList.calcDiv```|tul A B|2つのNumberListに対して除算をする|Perform division on two NumberLists|
|203|tol|```NumberList.IntNL2BL```|tol A|整数のNumberListをBoolListに変換する|Convert an integer NumberList to a BoolList|
|204|sal|```NumberList.isPN```|sal A|正の数かを判定する|Determine if it is a positive number|
|205|sel|```NumberList.minus```|sel A|符号を反転させる|Reversing the sign|
|206|sil|```NumberList.abs```|sil A|整数の絶対値を取得する|Obtaining the absolute value of an integer|

