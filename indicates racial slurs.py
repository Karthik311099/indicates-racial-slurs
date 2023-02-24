#!/usr/bin/env python
# coding: utf-8

# In[6]:


# import module for scrap the twitter tweet

import snscrape.modules.twitter as sntwitter


# In[11]:


limit = 1000 #set limit for how many tweet we want

# create empyt list for store tweets
tweets = []

# Getting tweets from any persons by using username
for tweet in sntwitter.TwitterSearchScraper("elonmusk").get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append(tweet.user.description) #Append tweets in a list


# In[8]:


# Racial Slurs words that I got from google 
racial_slurs=''' 
abo
Africoon
Africoon-Americoon
Africoonian
Africunt
Afrocoon
Ah Tiong
albo
Ali Baba
Americoon
apefirmative action
Apefrica
Apefrican
Apelanta
aperest
apesault
apple
Aunt Jane
Aunt Jemima
Aunt Thomasina
bagel
baguette
banana
Bangla
bean-eater
beanbreath
beaner
Black Dutch
black Irish
black trash
blacky
Boche
bohunk
bong
boogie
boong
boonga
boot
bootlip
bootlipped
booty scratcher
brillo pad
brown
brownie
Citations:bucksow
buckwheat
burn coal
burrhead
bushy
CAC
Cajun
camel jockey
camelfucker
Cape Dutch
Casper
cheesehead
Chen
chickenlips
chimp
Chimpcago
chimpout
China bug
Chinese farmer
ching chong
Chink
chocolate face
chopstick
Christ-killer
chug
chuhra
clog wog
coal burner
cockroach
coconut
Conch
congresscoon
coon
coonass
coonery
coonfuse
coonmunity
Coontown
coonvicted
coonviction
cotton picker
cracka
cracker
cracker-ass
crackerass
cracklet
crapaud
criminigger
crow
crunchie
cullud pusson
cumskin
cumskinned
curry nigger
curry-muncher
currycel
Curryland
currywhore
dago
dago bomb
dago dazzler
darkey
Deutschbag
diaperhead
diego
dindu nuffin
dogeater
dothead
dune coon
durka durka
Dutch
Dutchman
Dutchwoman
egg
eight-ball
Englishman
Eyetie
farm nigger
featherwood
fishhead
Flip
Fritz
frog
frogese
froggy
froglet
Frogspeak
fuzzy-headed
fuzzy-minded
ginzo
gippo
goatfucker
goffel
golly
goo-goo
goodification
goodify
googoo
gook
gook wagon
gookland
gooky
goombah
grasseater
greaseball
greaser
gringo
groid
Guat
gugu
guidette
guido
Guinea
guinea
gussuk
gutter ape
gweilo
gweipo
gyppo
gyppy
gypsyism
hairyback
hajji
half-breed
heeb
heebish
hick
hillbilly
homo negronus
homo negronus Americanus
honklet
honky
honorable
hoogie
hoojah
house nigger
hout
Hun
hunky
Hymie
ice monkey
injun
Jacky
Jap
jap
japie
Japland
Jerry
jerry
Jewfucker
Jewish nose
Jewtard
jig
jigaboo
Jim Crow
Johnny Crapaud
jook-sing
Judeo-Bolshevik
Judeo-Bolshevist
jungle bunny
jungle fever
kaffir
kangaroo fucker
katsap
kebab
Keling
khokhol
kike
kikey
kimchi
Knackerville
kneegrow
koala fucker
Kraut
Latrino
Leb
Lebo
limey
little brown fucking machine
Citations:macaca
malaun
mangia-cake
Mangkali
Mat
mayo
mayonnaise face
mean white
Mexcrement
Mexicoon
Mexicunt
Mexishit
mick
moke
monkey
mooley
moolie
moolinyan
moon cricket
mud
mud shark
mud sharking
munt
nappyhead
Nazi
negress
negrette
Nep
nicker
nig
nig-nog
nigaboo
nigcel
nigfant
nigga
niggacide
Niggatown
nigger
nigger chaser
nigger killer
nigger knocker
nigger lottery
nigger lover
nigger moment
nigger nose
nigger rich
nigger shooter
nigger stick
nigger university
nigger-brown
niggeration
niggerbabble
niggerball
niggerbitch
niggerboy
niggercide
Citations:niggerdick
niggerese
niggeresque
niggerette
niggerfaggot
niggerfied
niggerfuck
niggerfucker
niggerfuxate
niggerfuxated
niggerfuxation
niggergirl
niggergram
niggerhood
Niggerian
niggerish
niggerishly
niggerishness
niggerism
niggerization
niggerize
Niggerland
niggerless
niggerlike
niggerling
niggerlips
niggerly
niggerman
niggerology
niggerous
niggerphile
niggership
niggerskin
niggerspeak
Niggertown
Citations:Niggertown
niggertry
Niggerville
niggerwhine
niggery
niggress
niggy
niglet
niglette
nigra
nigro
nigtard
nilla
Nip
nog
nogger
noggie
noodlewhore
Nork
Norte
Norteño
ofay
oil trash
oiler
ook
Oreo
pajeet
Paki
paleass
Palesimian
Palestinkian
pasty
pavement ape
Citations:pavement ape
pea soup
peckerwood
pekkie
Pepsi
pepsi
petrol sniffer
pickaninny
pigger
pinky
pizza nigger
pizzahead
plantation nigger
Plastic Paddy
pollywog
pommy
poopskin
poor white trash
porch monkey
Porki
Portagee
potato chaser
potato nigger
prairie nigger
promdi
Pukistani
pumpkin head
puncturewala
raghead
rape ape
red man
red nigger
redneck
redneckitis
redskin
reffo
reptilian
rice
rice bag
rice burner
rice chaser
rice nigger
rice rocket
rice-eater
ricecel
ricer
rockfish
rooinek
roundeye
rug
rug pilot
rug rider
rughead
Rusky
Russki
sakai
Sambo
sand monkey
sand nigger
sandnigga
sauerkraut
schvartze
schwartza
scrap
Seppo
Serbo-Bolshevik
Serbo-Communist
sheboon
sheeny
shegetz
shitnigger
shitskin
shitskinned
shoneen
shonicker
shonk
shvartze
shvartzer
shylock
Skinnie
skinnie
slant
slanteye
slope
smoked Irish
smoked Irishman
snakehead
snow bunny
snow-white
snuff-and-butter
spade
spaghetti bender
spearchucker
spic
Spicanese
spicish
spiclet
spicspeak
spigger
spook
squaw
-stan
street ape
sulla
suspook
Synagogue of Satan
taco nigger
taco-bender
tar baby
teenaper
teenigger
timber nigger
TNB
Tojo
tootsoon
towelhead
towelheaded
trailer park trash
trailer trash
tree nigger
turdler
Turkroach
Twinkie
Uncle Tom
Uncle Tomahawk
vanilla wafer
wapanese
wetback
white boy
white bread
white devil
white negro
white nigger
white trash
whiteass
whiteboy
whiteskin
whitey
wigger
wise guy
wog
wogball
woggish
woggy
Wogland
wogspeak
wood
woolly-head
woolly-headed
wop
woppish
wopspeak
yard ape
yarpie
yellow
yellow cab
yellow man
yellow nigger
zebra
ziggaboo
ZioJew
zipperhead
zot'''


# In[4]:


# Make racial slur words into list
list=racial_slurs.split()


# In[10]:


count = 0 
for i in tweets:
    count = 0
    for j in list:
        if j in i:
            count = count + 1
    if count >= 5: # Count of racial slur words greater than 5 is SEVERE
        print(i, 'is :' ,"SEVERE")
        print()
    elif count >= 3: # Count of racial slur words greater than 3 is MODERATE
        print(i, 'is : ', "MODERATE")
        print()
    elif count > 2: # Count of racial slur words greater than 2 is MILD
        print(i, 'is : ', 'MILD')
        print()

