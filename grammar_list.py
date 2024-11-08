#=================== S E N T E N C E =============================
grammar = ["-고 싶다",
           "-(으)러 가다/오다",
           "-지요?",
           "-(으)세요",
           "-과/와, 랑/이랑, 하고",
           "-(으)로",
           "-보다 (with 더 and 제일)",
           "A에서 B까지",
           "-(으)세요",
           "-지만",
           "-(으)ㄹ 거예요",
           "-어서/아서 (because)",
           "-고",
           "-(으)ㄹ 수 있다/없다",
           "-어/아 주다",
           "-네요",
           "-(으)ㄹ 줄알다/모르다",
           "-(으)ㄹ 까요?",
           "-어야/아야 되다",
           "-(으)려고 하다",
           "어/아 보세요",
           "ㄴ/은/는 데",
           "-어도/아도 되다",
           "-어/아 봤어요",
           "고 나서",
           "겠어요/겠네요",
           "-(으)ㄹ 때",
           "-겠-",
           "이/그/저",
           "(으)ㄹ 게요",
           "어서/아서 (squence)",
           "(으)ㄴ 다음에",
           "-(으)면",
           "-지 않다",
           "-(으)니까",
           "-(으)ㄴ/는 갓",
           "-(으)면 안 되다",
           "-는 동안",
           "(으)ㄴ 적이 있다/없다",
           "-(으)ㄹ래요",
           "-거든요",
           "-(으)ㄹ 만하다",
           "어/아 놓다",
           "(으)ㄴ/는/(으)ㄹ 것같다",
           "(으)ㄴ/는 편이다",
           "모든, 다, 모두",
           "나",
           "ㄴ가",
           "(이)든지, 아무",
           "마다",
           "-기로 하다",
           "-기 전에, ㄴ/은 후에, 안/내",
           "게 adverbial suffix",
           "어/아 보이다",
           "-(으)ㄹ 까하다",
           "았/었으면 좋겠다",
           "잖아요",
           "-(이)나 and 밖에",
           "(으)면서",
           "-(으)ㄹ 때가 있다",
           "-ㄴ/는 다고",
           "-자마자",
           "-ㄴ/은 지 <time> 되다",
           "-을/를/기 위해(서)",
           "-을/를 통해(서)",
           "(이)라서",
           "에게서 / 한테서 / (으)로부터"
           "-을/를 위해(서)",
           "- (으)면 되다",
           "VERB + -지 말다",
           "-ㄹ/을 줄알다",
           "VERB + -고 오다",
           "VERB + 자",
           "VERB/ADJECTIVE + 네오",
           "개 + ADJECTIVE",
           "VERB + -아/어 드릴까요?",
           "NOUN + 말고 + NOUN",
           "VERB + ㄴ/는다!",
           "-씩",
           "(이)나",
           "거나",
           "-에 대해(서)",
           "고 나니까",
           "고 나면",
           "-는 지",
           "는/ㄴ/은 척하다",
           "-(으)며",
           "-ㄹ/을 만하다",
           "-던, -았/었단",
           "건마는/건만",
           "(으)ㄹ 정도로"
           ]

grammar_reference = {"-고 싶다": '''ngk chap 4
expresses ones desires
고 싶어 하다 is used to express desire of the 3rd person
https://www.reddit.com/r/Korean/comments/3jya17/%EC%9B%90%ED%95%98%EB%8B%A4_%EC%8B%B6%EB%8B%A4_korean_words_vs_words_6/''',
                     "-(으)러 가다/오다": "ngk chap 4",
                     "-지요?": "ngk chap 4",
                     "-(으)세요": "ngk chap 4",
                     "-과/와, 랑/이랑, 하고": '''ngk chap 6
also from https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/lesson-13/#kp4
means 'with' or 'and' between different nouns
in terms of formality 과/와 > 하고 > 랑/이랑''',
                     "-(으)로": "ngk chap 6",
                     "-보다 (with 더 and 제일)": "ngk chap 6",
                     "A에서 B까지": "ngk chap 6",
                     "-(으)세요": "ngk chap 7",
                     "-지만": "ngk chap 7",
                     "-(으)ㄹ 거예요": "ngk chap 7",
                     "-어서/아서 (because)": "ngk chap 7",
                     "-고": "ngk chap 7",
                     "-(으)ㄹ 수 있다/없다": "ngk chap 8",
                     "-어/아 주다": "ngk chap 8",
                     "-네요": '''ngk chap 8
express the speakers spontanous reaction
expresses surprise or admeration''',
                     "-(으)ㄹ 줄알다/모르다": '''ngk chap 8
to know/not know how to do
different from 수 있/없다 in that 줄 알다/모르다 only expression to KNOW
and does not imply capability whereas 수 있/없다 can also imply capability''',
                     "-(으)ㄹ 까요?": '''ngk chap 8
howtostudykorean.com lesson 63
Used for:
\tAsking question to ones self
\tshall we
\tshall i
\t(if subject is 3rd person or object) do you think..?
\t Used while asking for someones opinion, suggesting to do something, or questions/thoughts/guesses
''',
                     "-어야.아야 되다": '''ngk chap 8
note: using -어야.아야 하다 means the same thing and soudns a bit more formal''',
                     "-(으)려고 하다": '''ngk chap 9
used to express intention of future plan
only difference between this and (으)러 is
this can be used with any verb while (으)러
can only be used with 가다 and 오다
''',
                     "-(으)ㄴ: noun-modifying form (adjective)": "ngk chap 9",
                     "어/아 보세요": "ngk chap 9",
                     "ㄴ/은/는 데": '''ngk chap 9
provides background information
ㄴ/은 for adjectives
는 for verbs OR past tense marker ㅆ/었/았
이다/아니다 + 데 = 인 데 / 아닌 데''',
                     "-어도/아도 되다": "ngk chap 9",
                     "-어/아 봤어요": "ngk chap 10",
                     "고 나서": '''
ngk chap 10
from https://funkorean4u.com/2016/06/18/grammar-%EA%B3%A0-%EB%82%98%EB%8B%A4-after-i-did/
means after i do V then ->
eg. 먹고 나서 숙제할 거예요. -> after i eat i will do my homework
''',
                     "겠어요/겠네요": '''ngk chap 10
express speakers conjure about other people or things
eg. you must be so tired
eg. you must be so happy''',
                     "-(으)ㄹ 때": "ngk chap 10",
                     "-겠-": "ngk chap 11",
                     "이/그/저": "ngk chap 11",
                     "(으)ㄹ 게요": '''ngk chap 11
expressing willingness or intention "i will do something"
often used when speaker makes a promise for a future action
interchangable with -겠어요 ONLY in a statement''',
                     "어서/아서 (squence)": "ngk chap 12",
                     "(으)ㄴ 다음에": '''ngk chap 12
tells a chronological squence of events that are not
nessearily related unlike 어/아 서 which implies the first
event leads to the second''',
                     "-(으)면": "ngk chap 12",
                     "-지 않다": "ngk chap 12",
                     "-(으)니까": '''ngk chap 13
similar to 어/아 서 but more ephasis on the cause directly effecting the effect
eg. i have no money so i can buy this
usually has a sort of annoying connotation to it as if the speaker is annoyed at the cause''',
                     "-(으)ㄴ/는 갓": "ngk chap 13",
                     "-(으)면 안 되다": '''ngk chap 13
attached to verb stem to express prohibition or refusal of permission
"(someone) should not do (something)
''',
                     "-는 동안": '''
ngk chapter 13
means while -ing
는 동안 is interchangable with (으)ㄹ 때
tense is marked in the following clause not in the 동안 clause
집에서 쉬는 동안 첵을 많이 읽었어요. -> while resting at home I read of books
한국에 있는동안 여행을 많이 했습니다. -> while i was in korea i travelled a lot
                     ''',
                     "(으)ㄴ 적이 있다/없다": "ngk chap 13",
                     "-(으)ㄹ래요": "ngk chap 14",
                     "-거든요": '''ngk chap 14
"thats because"
is used to respond to a question or statement with a reason and explanation
form is used between people who have a close relationship''',
                     "-(으)ㄹ 만하다": "ngk chap 14",
                     "어/아 놓다": '''
from ngk chap 14
also from https://www.topikguide.com/%EC%95%84-%EC%96%B4-%EC%97%AC-%EB%86%93%EB%8B%A4-%EB%91%90%EB%8B%A4-korean-grammar/
it expresses when the speaker does something and leaves it in that state for future use

eg. 저는 칭문을 열어 놓았어요 -> i opened the window (and its still open)
this is different from just 열었어요 because in that case i dont know if it is for sure still open
but with this grammar point i am sure it is still in that state
''',
                     "(으)ㄴ/는/(으)ㄹ 것같다": '''ngk chap 14
best translated as "it seems"
also used to express politeness even when the speaker has clear evidence''',
                     "(으)ㄴ/는 편이다": '''ngk chap 15
means to tend to
refers to the belonging to a side or group among possiblities express a characteristic of a 
person or object in a non-conclusive mannar by grouping the person or object into a general category
요즘 온라인 쇼핑이 백화점보다 싼 편이에요. -> recently online shopping tends to be cheaper than department stores
토론토 겨울 날씨는 괘 추운 편이에요. -> toronto winter weather tends to be quite cold
''',
                     "모든, 다, 모두": '''
from howtostudykorean lesson 25
모든: is the most common way to say every__
is a prefix
eg 모든 것 -> everything, 모든 과일 -> every fruit, etc
다: means 'all' and is put after a noun
eg. 라면을 다 -> all ramen
모든 and 다 are different in
다 means to do one action to completion and leaving nothing behind
모든 is more like an action performed on all possible nouns
eg. 라면을 다 먹었어 vs 모든라면을 먹었어
sentence one says you ate all of the ramen, the bowl is empty whereas
sentence 2 means you have tried every kind of ramen available
note: this second sentence sounds kind of weird but still its there
모두: when used as an adverb similar to 다
eg. 선생님들은 모두 똑똑해요. -> All teachers are smart
also be used as a noun and when used as a noun will mean either everybody or everything
eg. 모두가 이해했어요. -> Everybody understood
eg. 모두 얼마예요?. -> How much is everything?
''',
                     "나" : '''
howtostudykorean lesson 25
add as suffix to 어디, 언제, 누구 to mean everywhere, everytime, everyone repsectively
eg. 밥은 어디나 맛이 똑같아요. -> Rice taste the same everywhere
eg. 그녀 언제나 늦 와요. -> she comes late every time
eg. 누구나 한국을 좋아해요. -> everyone likes kore
''',
                     "ㄴ가": '''
from howtostudykorean lesson 25
add as suffix to 뭐, 어디, 언제, 누구, to mean something, somewhere, sometime, and somebody respectively
eg. 난 방금 원가 봤어. -> I just saw something a minute ago
eg. 열쇠를 어딘가에 뒀어 -> I left my keys somewhere
eg. 나는 언젠가 중국어도 베우고 싶어요, -> I also want to learn chinese at sometime
eg. 누군가 너를 찾고 있어. -> Someone is looking for you
''',
                     "(이)든지, 아무": '''
from ngk chapter 15
from howtostudykorean lesson 25
누구든지 == 아무나 == anyone
뭐든지 == 아무거나 == anything
어니든지 == 아무데나 == anyplace
언제든지 == 아무때나 == anytime
when using 하고 or 와/과 for nouns or 에서 for places u put it between the
thing and 나
eg. 나는 아무와나 사귀고 싶어요. -> I want to go out with anybody
For 아무_나, 나 can be replaced by 도 to negate eg. 아무도 == nobody
above rule does not apply to 아무때나 because 'no time' makes no sense
so instead use 전혀
Also in english we try to avoid double negatives but actually 도 is always
used in a negative sentence
eg. 저는 아무도 못 봤어요 -> I couldnt see anybody
eg. 아무 때나 좋아요 -> anytime is good
eg  저는 아무 데나 가고 싶어요. -> I want to go anywhere
''',
                     "마다": '''
from howtostudykorean lesson 25
is a suffix that means "each"
eg. 날마다 -> each day
eg. 그 버스는 10분마다 와요.
''',
                     "-기로 하다": "ngk chap 15",
                     "-기 전에, ㄴ/은 후에, 안/내": '''
from ngk chap 15
also from howtostudykorean.com chapter 24
A기 전에 B means before A, B
eg. 나는 오기 전에 빕을 먹었어 -> before I came I ate
A은 후에 B means after A, B
eg. 밥을 벅은 후에 찬구를 만났어 -> after eating I met with my friend
안에/이내 means within a time period
eg. 우리는 1년 이내 결혼할 거예요 -> I will get married within one year
eg. 우리는 1년 안에 결혼할 거예요 -> I will get married within one year
''',
                     "게 adverbial suffix": "ngk chap 15",
                     "어/아 보이다": "ngk chap 16",
                     "-(으)ㄹ 까하다": "ngk chap 16",
                     "았/었으면 좋겠다": "ngk chap 16",
                     "잖아요": "ngk chap 16",
                     "-(이)나 and 밖에": "ngk chap 16",
                     "(으)면서": "ngk chap 16",
                     "-(으)ㄹ 때가 있다": '''
used to express the moment you feel or experience something
can also be translated as "Sometimes I... "
like eg. 술플 때가 있어 -> I am sad sometimes
''',
                     "-ㄴ/는 다고": '''
used to express quoting something someone may have said

note that this form is just the plain form conjurgation of a verb

which means that for adjectives it would just be the
dictionary form (in present tense)

https://www.howtostudykorean.com/unit-3-intermediate-korean-grammar/unit-3-lessons-51-58/lesson-52/
''',
                     "-자마자": ''' to mean "as soon as" a verb occurs
eg. 제가 가르치기 시작하자마자 학생들이 조용해졌어요 -- As soon as i started teaching
the students became quiet
https://www.howtostudykorean.com/upper-intermediate-korean-grammar/unit-4-lessons-84-91/lesson-84/
''',
                     "-ㄴ/은 지 <time> 되다": '''
https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/lesson-30/#303
means "since" some time
eg. 밥을 먹은 지 5분 됐다 -> its been 5 minutes since i have been eating
eg. 한국에서 산 지 25 년 됐어요 ->it has been 25 years since ive been living in korea .
the 지 is very technically a noun representing the time period denoted from <time> to now
for verbs that are continuous like eating, showering, exercising, studying it can
denote both how long has it been since you did it or how long you have been doing it for
for verbs that are one time they always mean how long since that exact moment happen
in context, it is usually very easy to understand
can also use 얼마나 and 오래 to ask questions about how long its been since whatever
한국어를 공부한 지 얼마니 되었어요? -> how long have you been studying korean for?
운동한 지 오래 됐어? -> have you been exercising for a long time?
''',
                     "-을/를/기 위해(서)": '''
https://www.topikguide.com/noun-%EC%9D%84-%EB%A5%BC-%EC%9C%84%ED%95%B4%EC%84%9C-%EC%9C%84%ED%95%B4-and-verb-%EA%B8%B0-%EC%9C%84%ED%95%B4%EC%84%9C-%EC%9C%84%ED%95%B4-korean-grammar/
for objects means to do something for <object>
for verbs it means in order to <verb>
remember that "for" is not a good direct translation and
this form specifically means for the benefit of
''',
                     "-을/를 통해(서)": '''
means through
expresses "by means of / through a passage / through an experience
combines with nouns
eg. 인터넷을 통해서
''',
                     "-(이)라서": '''
from ttmik real life korean conversations for beginners 2020 dialogue 4
means because it is NOUN
add 이 if last letter is consonant, dont if is vowel
attach to a noun to mean because it is NOUN
eg. 생일이라서 -> because its ones brithday
eg. 숙제라서 -> because it is homework
''',
                     "에게서 / 한테서 / (으)로부터": '''
https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/lesson-13/#kp4
means from someone or something
combines 'to' and 서 to mean the opposite of what 'to' usually means
eg. 저는 그것을 친구한테서 들었어요 -> I heard about that from my friend
''',
                     "- (으)면 되다": '''
from ttmik real life conversations for beginners 2020 dialogue 5
asking about the requirements or instructions when given a task
from ttmik real life korean conversations for beginners 2020
also from https://www.howtostudykorean.com/upper-intermediate-korean-grammar/unit-4-lessons-76-83/lesson-80/#803
similar to 아/어야 되다 but less harsh, this is more of a suggestion tone
this is why its used a lot when asking for advice or about requirements and instructions
''',
                     "VERB + -지 말다": '''
from ttmik real life conversation for beginners 2020 dialogu 6
means dont verb
말다 is super irregular and it conjurgation always drops the ㄹ so 지 마 or 지 마요 or 지 마세요, etc
except when using 고 its just 마고
the difference between this and 면 안 되다 is that this is telling someone to not doing the verb
where as 안 되다 is saying you are not permitted to do the verb 
''',
                     "-ㄹ/을 줄알다": '''
https://www.howtostudykorean.com/upper-intermediate-korean-grammar/unit-4-lessons-84-91/lesson-85/#851
means to know how to do
put after a verb
eg. do you know how to make kimchi fried rice? -> 김치볶음밥을 만들 줄 알아요?
''',
                     "VERB + -고 오다": '''
from ttmik real life conversations for beginners 2020
to come after VERB-ing
eg. to come after eating -> 먹고 오다
''',
                     "VERB + 자": '''
ttmik real life korean conversations for beginners 2020 dialogue 3
means lets VERB (casual)
eg. 보자 -> lets see
결혼하자 -> lets get married
''',
                     "VERB/ADJECTIVE + 네오": '''
from ttmik real life korean conversation for beginners 2020 dialogue 13
expressing your impression
eg. 작네요 -> (oh i see) it is small
''',
                     "개/존나 + ADJECTIVE": '''
from kal
adds emphasis to the adjective similar to the meaning very/really/fucking
eg. 개맛있어 -> fucking delicious
eg. 존나재밌어 -> fucking fun
존나 is far more sever in its use where as 개 is just a typical slang used
among friends
''',
                     "VERB + -아/어 드릴까요?": '''
from ttmik real life korean conversations for beginners 2020 dialogue 14
shall i VERB (for you)?
add onto the verb to ask if you shall do something for someone
eg. 추천해 드릴까요? -> should i recommend you (it)?
eg. 사 드릴까요? -> shall i buy you (it)?
''',
                     "NOUN + 말고 + NOUN": '''
from ttmik real life conversations for beginners 2020 dialogue 19
not NOUN but NOUN
to means not 1 thing but other thing
eg. 친구 말고 남자찬구 -> not a friend but boyfriend
eg. 그것 말고 저것 -> not that one but that one over there
''',
                     "VERB + ㄴ/는다!": '''
from ttmik real life korean conversations for beginners 2020 dialogue 22
ending is used to show surprise or discovery of a certain fact
if verb stemp is vowel (or ㄹ) add ㄴ (if ㄹ, remove ㄹ)
if verb stem is consonant add 는
eg. they are coming! -> 온다!
eg. but the section cheif is going to the meeting room right now! 과장님 지금 회의실 간다
''',
                     #####
                     "-씩": '''
from howtostudykorean.com lesson 127
typically add to a counter word to mean "each"
eg. I will give one cookie to each kid -> 저는 아이들에게 과자를 한 개씩 줄 거에요
can also translate to "at a time"
eg. Two people at a time can go up -> 두 명씩 올라가면 됩니다
can also be attached to a time word to mean that duration of time (at regular intervals)
eg. The bell rings for one minute every hour -> 종이 한 시간에 1분씩 울려요

''',
                     "(이)나": '''
from howtostudykorean.com unit 3 lesson 58
used as a typical translation for OR.
indicates that it hasnt been decided which noun/object will be acted on
eg. 딸이나 아들을 낳고 싶어요? -> do you want to have a daughter or a son?
can also be attached to subject of the sentence to indicate that it hasnt been
decided which subject will perform the action
eg. 우리 엄마나 우리 아빠가 저를 차로 거기까지 데러다 줄 거계요. ->
either mom or dad will take me there by car
can also be attached to one word in a sentence to convay the feeling of
would rather do something else but is choosing the thing specified as a last resort
eg. 밥이나 먹을래? -> i guess we could eat rice?
when used in a negative sentence it means you dont have either object
eg. 무기나 칼이 없어요. -> I dont have a weapon or a knife
''',
                     "거나 / 또는": '''
from howtostudykorean.com unit 3 lesson 58
used in a typical translation for OR BUT for verbs
거나 is more common, 또는 is more formal
eg. 여자 찬구를 위해 편지를 쓰거나 선물을 사 졸 거예요. ->
For my girlfriend, I will write a letter or buy a present
when used twice in a sentence the speaker is focused more on
describing the choice its self, and they might react/feel/act as a result
eg. 비가 오거나 안 오거나 중요하지 않아요 -> whether it rains or not its not important
can also be used in the form -거나 말거나 to indiciate that the outcome of
doing an action or other action is irrelevant (or doesnt matter)
eg. 대학고에 가거나 말거나 공부해야돼요. -> you need to study if you go to university or not
when used in a negative sentence it means you cant do either
eg. 저는 눕거나 앉을 수 없어요. -> I cant lay down or sit
eg. 저는 그 여자를 보거나 말하지 않을 거예요. -> I am not going to look or talk with that girl
''',
                     "-에 대해(서)": '''
from howtostudykorean.com unit 1 lesson 13
attached to nouns to mean "about"
eg. 난 너에 대해 생각앴어 -> I was thinking about you
''',
                     "고 나니까": '''
from https://funkorean4u.com/2016/06/18/grammar-%EA%B3%A0-%EB%82%98%EB%8B%A4-after-i-did/
means after i do V, I found out a fact
eg. 먹고 나니까 이제 졸려요. -> After I had i (found out) am sleepy
sometimes can see 고 보니까 which means the same thing but for fixed verbs 알다 and 듣다
''',
                     "고 나면": '''
from https://funkorean4u.com/2016/06/18/grammar-%EA%B3%A0-%EB%82%98%EB%8B%A4-after-i-did/
if i do V, it will~ (second part should be present/future and be the effect of first part)
eg. 약을 먹고 나면 좋아질 거예요. -> if you take medicine, you will be fine
sometimes can see 고 보면 which is the same thing but for fixdd verbs like 알다 and 듣다
''',
                     "-는 지": '''
from https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/lesson-30/#301
can be used in place of -는 거 to show uncertainty
similar to 거, for verbs its -는 거 and adjectives is -/ㄴ/은 거
eg. 저는 친구가 어디 가는지 모르겠어요 -> I dont know where my friend is going.
note: on 모르다 -겠- is typically used to make it sound less rude
more examples without question word:
eg. 엄마가 지금 먹고 있는지 모르겠어요 -> i dont know if mom is eating now.
can be used for uncertain past tense sentences
eg. 열쇠를 어디 두었는지 잊어버렸어요. -> i (totally) ended up forgetting where i put my keys
future too
eg. 택배가 언제 올지 모르겠어요. -> i dont know (if) when the delivery will come
can also mean if.. or not...
eg. 수술을 받을지 안받을지 확실하지 않아요. -> im not sure if i will get surgery or not
also clauses dont nessearily have to be the same thing repeated
eg. 내일 공원에 갈지 영화를 볼지 모르겠어요. -> im not sure if i will go to the park or watch a movie tomorrow
form can also be used to ask a question which would usually end in 알다
eg. 서울에 어떻게 가는지 알아요? -> do you know how to get to seoul?
and can be responded with: 서울에 어떻게 가는지 알아요. as in they know how to get to seoul
''',
                     "는/ㄴ/은 척(체)하다": '''
from https://www.howtostudykorean.com/upper-intermediate-korean-grammar/unit-4-lessons-92-100/lesson-98/#981
means to pretned or act like
add 는/ㄴ/은 depending on if its action verb or descriptive verb
(also if its present tense or past tense)
저는 공부하는 척하고 있어요. -> I am pretending to study
농구에 대해 잘아는 척했어요. -> I pretended to know a lot about basketball

''',
                     "-(으)며": '''
from howtostudykorean lesson 62
first meaning is similar to (으)면서
can be meant to mean two actions are occurring continuously at the same time
but (으)면서 is more common in this situation and (으)며 would be more for
formal situations
the second meaning is to list to connect two clauses that have a similar idea
eg. 그 사람이 한국에서 살면서 한국어를 할수 없어요. -> That person lives in korea, but cant speak korean
VS. 그 사람이 한국에서 살며 한국어를 할수 없어요.-> that person lives in korea, and cant speak korean.
the first one describes how the person lives and korean while concurrently not being
able to speak korean where the second sentence just implies that there is
some connected meaning between them living in korea and them not speaking korean
''',
                     "-ㄹ/을 만하다": '''
from howtostudykorean.com lesson 124
means for something to be worth doing
note: 만하다 is an adjective which means if you are conjurgating it you
will as an adjective
eg. 한국은 살 만해요? -> Is it wroth living in korea?
these sentences dont typical have objects in them but its possible when
받다 is the verb
eg. 그 선생님은 상을 받을 만해요. -> that teacher deserves an award
or in sentences where the verb is __하다 because all 하다 verbs can be split into
object and verb
can also be used as a noun descriptor
eg. 먹을 만한 식당을 알라요? -> Do you know a worthwile restaurant to eat?
note: how it is conjurgated like an adjective
can also be used to express something that is possible desipte maybe not being the best option
eg. 한국요리는 할 만해요?. -> Is it worth cooking korean food?
but in a given context the above sentence could be like "is it still possible to?"
this can also be expressed similarly by sentences with 가치 있어요.
eg. 그 영화를 세 시간 동안 볼 가치가 있었어요. -> it was worth watching that movie for 3 hours
''',
                     "-던, -았/었단": '''
from howtostudykorean lesson 27
means to describe a noun from the past but different from ending the verb
in ㄴ/은
it is different because you are basically conjuring up the fact that you remember
and experienced and the experience and memoory is a recurring one
eg. 내가 입던 옷 -> the clothse i wore
in this example i am saying its clothse i used to wear repeatedly
over time and i still wear from time to time these days
for 내가 입었던 옷, it is the clothse i that i have worn but this implies
that I no longer wear the clothes for some reason, maybe i got rid of it or it doesnt fit
these are different from just plain 내가 입은 옷 in that this sentence doesnt really say
anything about the state of the worn clothes like maybe u just wore it once or you are
wearing it right now (you put it on this morning), etc. This form doesnt inform much without
context
note: since it must be a recurring thing you cant say like 내가 태어나던 도시 -> the city i was born
because you dont keep being born it only happens once. in this case you can only use ㄴ/은
for adjectives you rarely ever hear 던 being used because most adjectives cant be recurring
but 았/었던 can be and it would have the same meaning as they use to be _ but now they are not
eg. 예벘던 여자 -> The girl who i recall being pretty but is not pretty anymore
more examples
eg. 이 빵은 슬기가 자주 먹던 빵이야 -> this bread is brea dthat seulgi ate (and still eats) often
eg. 그컴퓨터는 작년에 썼던 거예요. -> this is the computer i used last year
eg. 맑던 하늘이 갑자기 어두 워졌어요
''',
                     "건마는/건만": '''
from go billy korean abridged https://www.youtube.com/watch?v=07g3mU3liBg
similar meaning to 지만 like BUT or HOWEVER
the difference is this form is used purely in a literary sense, gives a similar feeling of posh british lol
like fancy and old fasion
another difference is the statement that follows an unexpected one
also it is not a requirement but the second statement usually has a feeling of disappointment or regret
this means there is no feeling of disapointment directly coming from the grammar but when categorizing
the sentences its used it is typical used in these types of sensetences
eg. every day I clean this place but since its old it can never look clean ->
여간 매일 총소하건만 낡아서 깨끗해 보이지 않아요
''',
                     "(으)ㄹ 정도로": '''
from https://www.koreantopik.com/2017/05/l2g42-av-grammar-to-extent-thatexpress.html
means to express the degree or extent of the action or state
has 2 forms: (으)ㄹ 정도로 (used in the middle of sentence) and (으)ㄹ 정도이다 (used at end of sentence)
저는 몇 번째 다시 볼 정도로 이 드라마를 좋아애요 -> i like this drama to the extent i watched it again several times
너무 많이 비를 와서 앞이 잘 안보일 정도예요. -> it is raining so much i can hardly see infront of me
''',
                     "는/ㄴ/은 척하다": '''
from https://www.howtostudykorean.com/upper-intermediate-korean-grammar/unit-4-lessons-92-100/lesson-98/
means to pretend to
for verbs 는 for present tense, (으)ㄴ for past tense
for adjectives and 이다 is 은
엄마가 오자 저는 설거지하는 쳑했어요. -> as soon as my mom came i pretended to do the dishes
여자는 자기 남자 친구한테 귀여운 척했어요. -> the girl pretended to be cute to her boyfriend
also there is an alterantive grammar that uses 체하다 which has similar, if not identical meaning
'''
                     }