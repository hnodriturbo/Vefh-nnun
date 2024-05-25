# Tafla  &lt;Table> 

Bættu töflu inn í vefsíðuna, innhald töflunar á að vera dagskrá af einhverju tagi. Til að byrja með má notast við _dummy_ texta en innihald töflunnar á að vera klárt þegar farið er yfir verkefnið í yfirferð verkefna (_Lykilmatsþáttur - 4. verkefni_). 

Taflan á að birtast í öllum skjástærðum án þess að fara út fyrir skjáinn.  

#### Mynd 1. Viðmið 48em + (760px ~ og stærri skjáir).

![Mynd 1.](Námsefni-3/mynd-1.jpg)

#### Mynd 2. Viðmið 0 – 48 em (0 – 760px) Það á ekki að þurfa að hliðra til skjánum þegar taflan er skoðuð í farsímum.

![Mynd 2.](Námsefni-3/mynd-2.jpg)

Tabular Data &lt;td> er eina tagið sem er hannað til að sækja gögn af miðlara í hvert sinn sem vefsíða er opnuð, jafnvel þegar flett er á milli síðna. Það er mjög gagnlegt þegar um er að ræða upplýsingar sem þurfa að uppfærast daglega eða oftar.

Töflur henta illa í útlithönnun ss til að birta texta og myndir sem breytast ekki. Vafrinn getur geymt slíkar upplýsingar í vinnsluminni sínu og þarf ekki að sækja þessi gögn í sífellu. "Table" tagið er erfitt að eiga við þegar kemur að sveigjanleika vefsíðu og best að nota það ekki nema þegar um gagnvirkar færslur er að ræða.  

---

## Skráningarform 

Setjið skráningarform inn á vefinn ykkar, hafið samræmi í útliti formsins og töflunnar og í rökréttu samhengi við heildarútlit vefsins.  Formið á að vera sýnilegt í öllum helstu skjástærðum. 
  
![Mynd 3.](Námsefni-3/mynd-3.jpg)

#### Form 

Í base.css er búið að tilgreina alla helstu þætti sem hægt er að stíla í formtögunum, aðlagið formið að ykkar útlitshönnun og skipulagi.

#### Réttritun (_validation_)
Þegar smellt er á hnappinn (input submit) í skráningarforminu þá athugar (_validate_) vafrinn hvort texti sé rétt skráður í innsláttarreiti (_input_). Ef textinn uppfyllir ekki þau skilyrði sem eiga við þá á ekki að vera hægt að senda upplýsingar frá vefsíðunni (en ef allt er í lagi þá sendum við innsláttinn út í bláinn). 

` <input type=“x“ name=“x“ value=“X“ required placeholder=“fyllið út þennan reit“> `

* Ekki er hægt að skilja nafnareit auðan 		
* Símanúmer verður að vera tölur (numbers)
* Tölvupóstfang verður að vera með @	      	
* Notið „input date“
* Notið „select option, checkbox og radio“. 	
* Notið aðra leturgerð og stærð í „textarea“

### Námsmat 12%

#### Tafla 

* 2% Taflan inniheldur upplýsingar sem eru skiljanlegar og skilmerkilega settar upp.
* 2% Notaðu thead, tbody og tfooter tögin í töflukóðanum. Í stílsíðu er hægt að nota gerviklasa (Pseudo class - nth-child) til að fá litskiptingu í bakgrunn töflunnar. 
* 2% Taflan er svegjanleg (responsive) og skiptist þannig að hún er öll sýnileg
á litlum skjáum.

#### Form 
* 3%	input -text, -email, -radio, -checkbox, select og textarea er í pöntunarformi 
* 3%	Ekki á að vera hægt að senda (submit) form fyrr en skilyrðum (request)  eru uppfyllt í „text“, „email“, „date“ og „telephone“.

- **[Sýnidæmi](https://vefhonnun.github.io/synidaemi/verkefni-3/)**
- **[Bjargir](https://github.com/vefhonnun/23-Verkefni-s1/wiki#t%C3%B6flur)**

### Verkefnaskil

Öllum vinnugögnum á að skila í verkefnageymsluna þína og tengil á verkefnið í Innu.

#### Einkunn verður birt í Innu.

_Gangi þér vel_

