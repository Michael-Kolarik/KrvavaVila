#!/usr/bin/env python3
import sys
from termcolor import colored
from termcolor import cprint
from Cutscena import Cutscena
from Kostka import Kostka
from Hrdinka import Hrdinka
from Duch import Duch
from Zombie import Zombie
from Zombie import Demon
from Dvere import Nedvere
from Mistnost import Mistnost
from Poklad import Poklad
from Ukryt import Ukryt
from Ukryt import Pokladnice
from Mistnost import Hala
from Mistnost import Kuchyne
from Mistnost import Jidelna
from Dvere import Dvere
from Dvere import Vrata
from Dvere import Zablokovane_dvere


kostka = Kostka(20)
hadanka = "Zlodějka našla učebnici. \n\'Dobrý den, jsem mluvící učebnice,\' promluvil předmět, \'už zbývá jen jedna otázka. Kolik\n rovnostranných trojúhelníků lze vyrobit z šesti celých stejných zápalek?\'"
prevlekani = "Mezzobran potěžkala rapír v ruce. Nebyl o mnoho těžší, než její kordík, ale zato delší. Zkusila si\n tedy pár výpadů s rapírem v pravačce a kordíkem v levačce. Ale kordík byl na levou ruku moc\n těžký, tak jej nahradila dýkou. To už byla opravdu dobrá kombinace."
uvod_zacatek = "Mezzobran vešla do temné sklepní hospody a rozhlédla se jantarovýma očima po ostatních hostech. Většina měla kápě, stejně jako ona sama. \nNepřekvapivé. Pak si všimla, že jeden z hostů má na stole červené jablko. Posadila se naproti němu a položila své vedle jeho.\n \'Vy prý potřebujete udělat nějakou práci,\' řekla. \n \'Vy jste...\' zablekotal její protějšek. \n \'Co? Z Temných říší? Elfí krve? Žena? Ano, to všechno,\' Mezzobran si sčísla bíle vlasy na fialovo-šedou tvář, \'jestli s tím máte problém,\n já nemám problém zase odejít. Vaše problémy řešit nepotřebuju.\' \n Lhala. Dlužila pět set Králů bandě, která ji dostala z Temných říší sem do města. A jestli nezaplatí, tak může buďto utéct někam za moře, \nnebo si to u nich odpracovat. Ani jedno ji příliš nelákalo. Potřebovala peníze. Hodně. Ale to zákazník nesmí vědět. Jinak smlouvá, ne-li o ceně, \n tak o odvedené práci.\n \'Ne, to je vaše věc,\' mávl muž velkoryse rukou. Jako by to snad Mezzobran mohla ovlivnit. \n"
uvod_ukol = "\'Tak o co jde v té práci?\' \n \'No, o jisté dopisy, které jsem poslal jedné lady, a které by mne mohly\n  dostat do společenských problémů,\' vysvětloval klient neurčitě. \n \'Aha,\' Mezzobran tušila svoje\n  a detaily ji nezajímaly, \'a víte, kde ty dopisy jsou.\' \n \'V jejím trezoru. Má ho v ložnici a klíček\n nosí vždy na krku. I do postele.\' \n Aha. No, s tím si bude muset poradit. \n \'Kde najdu tu ložnici?\n Předpokládám, že se tam bude nacházet i dotyčná dáma,\' snažila se temná elfka tvářit sebejistě.\n \'V patře vily na Stříbrném kopci, úplně poslední na hlavní ulici vlevo ve směru od města. Na\n opačném konci, než ústí schodiště, vlevo, když se díváte tím směrem,\' popsal poměrně podrobně\n cestu zákazník. \n \'Dobře. Moje cena je pět set Králů, to snad víte?\' \n \'Jistě, to není nejmenší\n problém.\'\n"
uvod_priprava = "Ve své malé světničce se Mezzobran chystala na loupež. Vsunula do kapsy sadu paklíčů. Ty by\n měly stačit na běžné zámky, ale trezorové nejspíše neodemknou. Proto přidala hadřík a lahvičku\n oleje sladkého vitriolu. Pak zaváhala, ale nakonec oblékla prošívaný kabátec a připásala si kordík.\n Snad to nebude potřeba. Připnula si i láhev s vodou, protože to je potřeba. \n"
uvod_zahrada = "Brána do rozlehlé zahrady elfčiným nástrojům dlouho neodolávaly. Prošla po cestičce k bráně, ale\n její temnotu milující oči jí říkaly, že něco není v pořádku. Zahrady těchto boháčů bývaly\n udržované, takže zkušené oko po pár dnech poznalo, že nikdo není doma. Jako teď, i když věděla,\n že se vloupává do domu, ve kterém se nachází majitel. Podívala se na vilu. V kovových dekoracích\n na oknech v přízemí poznala díky svým zkušenostem bezpečnostní mříže a zdobené hlavní dveře\n byly solidní, pevné a s dobrým zámkem. Velmi ji překvapilo, že byly odemčené.\n"
dialog = "Elfka zkusila vzít za dveře, ale ani se nepohnuly. Než se mohla začít zabývat touto skutečností více\n zabývat, uslyšela z druhé strany zoufalý, prosebný hlas:\n \'Prosím vás, jděte pryč.\' \nO pár okamžiků ho vystřídal jiný. Nebo spíše stejný, ale hovořící panovačným tónem: \n\'Ne, otevřete to nějak, musím se odtud dostat.\' Mezzobran zaváhala a pak poodstoupila ode dveří. Tohle rozhodně nebude zkoušet naslepo."
vypiti_lahve = "Elfka otevřela barovou skříňku a uviděla jedinou, zato zdobenou láhev. Odšpuntovala ji a přičichla. Něco tak příjemného ještě necítila. Zaváhala, ale jestli někdy potřebovala posílit nervy, tak teď. Přiložila lahev ke rtům a pořádně se napila sladkého likéru."
rozbiti_lahve = "Elfka uchopila zbraň a bodla s ní mezi dvířka baru. Ozvalo se tříštění skla a ucítila nasládlou vůni."
bodnuti_zbroje = "Mezzobran bodla mezi dveře skříně, ale čepel zastavila zbroj, která visela vevnitř."
obleceni_zbroje = "Elfka vytáhla zbroj ze skříně a klepla na ni prstem. Ucítila tvrzenou kůži a podle zvuku ji zevnitř\n vyztužovaly kovové pásy. Po krátkém rozmýšlení si ji oblékla přes prošívanici."
vyndani_sosky = "Zlodějka otevřela skříňku se slony a uvnitř se roztočila porcelánová soška slona. Zároveň se ale\n začala ozývat kolotočářská melodie. Elfka zaklela a rychle zatáhla za páčku, čímž strojek utišila."
rozbiti_sosky = "Elfka sekla zbraní a oddělila hlavu tomu vevnitř. Byl to ale jen porcelánový slon."
podivani_do_zrcadla = "Mezzobran otevřela skříňku a uviděla velké zrcadlo. Chtěla skříňku znovu zavřít, ale něco na\n vlastním odrazu ji zarazilo. Podívala se pořádně. A uvědomila si, že vypadá o dvacet let starší.\n Mávla nad tím rukou a zavřela skříňku. Ale pak si uvědomila, že pro člověka, co žije stěží sto let,\n jsou dvě dekády mnohem větší úsek."
rozbiti_zrcadla = "Elfka pootevřela skříňku a švihnutím zbraně rozbila zrcadlo."
obrazky = " obrázky. Je ne nich tříčlenná rodina doma, v lese a ve městě. Tříčlenná rodina sedí\n za stolem a usměvavý muž v zástěře jim nese jídlo. Jezdec na koni před vojáky s nápisem\n TATÍNEK V PPÁCI.  Žena s drdolem čte holčičce s knihy a nápis 2+2=4. Dáma v nádherných\n šatech popsaná MÁMA. Chlapec a dívka drhnou schody a mezi nimi je malé srdíčko. Dáma a rytíř\n a mezi nimi velké srdce."
popis_hlavni_hala = "Hlavní hala zabírá viditelně velkou část přízemí. Její zdi pokrývá mramor a dekorace ve stylu\n starých sloupů. V každé zdi jsou jedny dveře a uprostřed stoupá vyřezávané dřevěné schodiště.\n Dojem elegance kazí jen hnijící ovoce na podlaze.\n"
popis_knihovna = "Podél všech stěn místnosti, vyjma míst s dveřmi a okny, stojí regály s knihami. Starými i novými,\n beletrií i odbornou literaturou, na všechny možná témata. Uprostřed stojí studijní pult."
popis_obyvaci_pokoj = "V místnosti stojí velký zdobený stůl s tuctem židlí. U levé zdi stojí vykládaný bar, u pravé socha\n muže, kterému jiný připíná medaili. Mezzobran v druhém poznala krále dle portrétů na mincích.\n První byl nejspíš pán domu, protože na zdech visely jeho portréty a výjevy z vojenského prostředí,\n kterým vévodil."
popis_jidelna= "V jídelně se nachází především velký stůl obklopený židlemi. Na zdech visí obrazy, zobrazující\n hlavně nádoby a jídlo."
popis_panova_loznice= "Tato místnost je pánský pokoj s dubovou postelí, pracovním stolem pokrytým lejstry, velkou šatní skříní a zdmi\n pokrytými obrazy. Na jednom je svatba, na druhém žena s dítětem, na třetím tříčlenná rodina, pak tu\n visí celá série obrazů, zachycujícím dívenku od narození po šest let."
popis_loznice_pani= "Dámské ložnici vévodí postel z růžového dřeva, na které leží šaty špinavé od krve. Na zdi visí\n společné portréty mladého páru. V rohu je ve zdi zapuštěný kovový trezor, kousek vedle něj stojí \nkosmetická skříňka."
popis_koupelna= "I taková místnost jako koupelna je v této vile dost velká. Vlevo je obložená hliněnými dlaždicemi\n a jsou v ní kovové umyvadlo a dvě kabiny, v jedné je toaleta a v druhé sprcha. Vpravo je obložena\n stříbřitým kamenem, jsou v ní mramorové umyvadlo se skříňkou, dvířka do místnůstky s toaletou a\n vana zakrytá velkým paravánem."
popis_detsky_pokoj= "Pokoj je zdobený namalovanými květinami, po nábytku, od postýlky přes stoleček po skříňky, je\n spousta látkových zvířátek, vyřezávaných panenek, obrázkových knížek a podobně. Nejvíc jich je\n na jemně vyřezávané skříňce s motivy slonů."
popis_ochoz= "Schodiště stoupalo na relativně úzký ochoz v patře, ze kterého vedly čtyři dveře. Jedny ve zdi\n nalevo, druhé ve zdi napravo a dvě ze zdi na druhé straně ochozu."
popis_mistnost_sluzebnictva= "Místnost vypadá spíše jako úzká chodba. Na jednom konci jsou dveře na schodiště, na druhém\n velké okno, kterým proniká světlo měsíce. V jedné stěně jsou dveře zasazené do rámu tak, aby\n nebyly z druhé strany moc vidět, ve druhé stěně jsou dvoje obyčejné dveře. Jinak je místnost\n prázdná a obyčejná."
popis_muzska_loznice= "Tato místnost je na poměry tohoto domu relativně malá. Jsou zde dvě postele a dvě poličky s\n osobními věcmi. Je tu mužské oblečení, holení, kuchařky a knížky s hambatými obrázky. "
popis_zenska_loznice= "Tato místnost je na poměry tohoto domu relativně malá. Jsou zde dvě postele a dvě poličky s\n osobními věcmi. Je tu ženské oblečení, levná kosmetika, učebnice a červená knihovna. "
popis_schodiste= "Prosté točité schodiště spojuje suterén s patrem se zastávkou v přízemí."
dvere_knihovna = "dveře knihovny"
dvere_obyvaci_pokoj = "dveře obývacího pokoje"
dvere_jidelna = "dveře jídelny"
dvere_panova_loznice = "dveře lordovy ložnice"
dvere_loznice_lady = "dveře od ložnice lordovy manželky"
dvere_koupelana = "dveře koupelny"
dvere_detsky_pokoj = "dveře dětského pokoje"
dvere_muzska_loznice = "dveře od ložnice sluhy a kuchaře"
dvere_zenske_loznice = "dveře od ložnice služky a guvernantky"
dvere_kuchyne = "dveře kuchyně"
dvere_haly = "skryté dveře od hlavní haly"
dvere_ochoz = "dveře mezi panskou a služebnickou částí"
dvere_sluzebni_cast = "jeste to musim vymyslet"
popis_kuchyne= "V kuchyni stojí velká kovová kamna se sporákem a pecí, velký pracovní stůl a několik kredenců \ns nádobím. Ve zdi nejdál od pece jsou nízká dvířka ve zdi a poklop v podlaze."
kuchar_utok = "U schodů stál malý tlustý muž v pracovním oblečení s kuchařskou zástěrou a šátkem kolem krku.\n Na jeho čele viděla Mezzobran ránu tak hlubokou, že ji nemohl přežít. Otočil k ní mrtvolně skelný\n pohled a pohybem, který byl jakoby mátožný, ale velmi rychlý, na ni zaútočil.\n"
guvernantka_utok = "Sotva se Mezzobran rozhlédla, uviděla ženu, která k ní mířila podél vyřezávaného zábradlí. Měla\n drdol a strohé šaty guvernantky, do kterých se vpíjela krev z hluboké řezné rány na krku. Sotva se\n dostala na dosah k elfce, přešla do útoku."
lord_utok = "Zpoza dveří náhle vyjde nahý muž s dýkou v zádech a ožene se pěstí."
dcera_utok = "Holčička sahá elfce až do pasu, ale hýbe se rychle, mokré vlasy jí padají na ztuhlý obličej a košilka\n lepí na studené tělo."
sluha_utok = "Za dvířky se ozvala rána a o chvíli později se z nich vykolébal mladík v livreji s železným hákem\n zabodnutým do krku a vrhl se na Mezzobran."
sluzka_utok = "Víko se odklopilo a z díry v podlaze vylezla omrzlá dívka a vyrazila k elfce."
kuchar_popis = "Uprostřed místnosti stojí tlustý duch v zástěře a šátku."
guvernantka_popis = "Vedle pultíku stojí přízrak mladé ženy s drdolem v strohých šatech guvenantky. Na jejím krku se\n táhne hluboká rána."
lord_popis = "U stolu stojí přízračná postava nahého muže s upravenými vlasy i vousy. Na jeho průhledném těle \nse rýsovaly svaly a ze zad mu trčela rukojeť dýky."
dcera_popis = "Uprostřed toho všeho stojí průsvitná postavička. Holčičce se zvedají a vlní vlásky i noční košilka a\n pláče."
sluha_popis = "Mezi postelemi se vznáší duch mladíka v livreji, kterému skrz krk prochází železný hák."
sluzka_popis = "Mezi postelemi stojí duch dívky v černých šatech s bílou zástěrou a čepcem, která má zlomený krk \n a je pokryta jinovatkou."
kuchar_pribeh = "\'Tady ho máte,\' ukázala Mezzobran duchovi sekáček.\n\'Oh, dejte ho prosím támhe,\' ukáže kuchař rukou, \'já si ho vypůjčil, víte, ale opravdu jen vypůjčil.\n Byl bych nerad, kdyby si lord myslel, že jsem ho chtěl okrást.\'\n\'Myslíte, že na tom záleží, po tom co se stalo?\' zavrtěla hlavou temná elfka.\n\'Samozřejmě, na tom záleží, ať se stane cokoli, jeho lordstvo je velmi dobrý zaměstnavatel.\'\n\'A co se vlastně stalo?\'\n\'No, ani nevím, šel jsem do skladu v zahradě pro bednu ovoce a když jsem procházel halou, tak ke \nmně přišla lady Tereza a praštila mne pánví. Co se stalo potom, nevím. Pro mne asi už nic.\'\n\'No, děkuji za pomoc,\' pokrčila temná elfka rameny.\n\'Já děkuji vám. Sbohem.\'"
guvernantka_pribeh = "\'Odpověď je čtyři,\' vybafla na ni elfka, \'prostě tři na desce a z každého rohu jedna nahoru ke \n\'Jmenuji se Sofie, pracuji tu jako guvernantka. Učím mladou slečnu Viktorii, takové kouzelné dítě\n moc hodná holčička. A chytrá. Nikdy jsem nepochybovala, že s ní vyroste správná dáma.\'\n\'A co se vám stalo?\' zeptala se Mezzobran.\n\'No, poslední, co si pamatuji, je, že jsem šla do koupelny a na ochozu v patře potkala lady Terezu.\n Popřála jsem jí dobrý den, ale ona mě chytila za krk, pak vytáhla lordovu holící břitvu a pak už\n nevím. Pomohla jsem vám?\'\n\'No...\'\n\'Vy jste mi totiž pomohla. Mnohokrát děkuji a sbohem.\'"
lord_pribeh = "\'Tady ji máte, rozmlátila jsem ji na kusy,\' ušklíbla se Mezzobran, \'a teď byste mohl být tak laskav\n a říct mi, co se tady vlastně stalo. A kdo vlastně jste?\'\n\'Jsem maršál Vilém z Aurumu. Měl jsem všechno, co si může muž přát. Krásné zdravé dítě.\n Manželku, která mne milovala a já miloval ji. Kariéru, která stoupala ke hvězdám. Slušné jmění,\n krásný dům, věrné služebníky. Ale věci nebyly jen ideální. Jak má kariéra rostla, žádala si o něco\n více mého času. Snažil jsem se rodinu nezanedbávat, a jistě jsem se jí věnoval víc, než mnozí muži\n v mém okolí. Ale má žena začala mít pocit, že má láska vyprchává a začala to přisuzovat svému\n věku. Ano, je to absurdní, vždyť jsem stejně starý a navíc nám nebylo ani čtyřicet. Nicméně ona si\n začala dělat tyto starosti, nejprve kupovala drahá líčidla, a později si chtěla nechat dovést modlu,\n která ji měla pomocí magie omladit. Nesouhlasil jsem, ale já bloud jí vyhověl. Ale během první\n noci, kterou ji měla v ložnici, přišla do mé. Zpočátku to bylo krásné, ale v nečekanou chvíli jsem\n v jejích očích uviděl šílenství, pohled démona. A v tu chvíli popadla dýku a bodla mi ji do zad. Měl\n bych se na ni zlobit, ale nejde mi to. Ona za to nemůže. Ale vám děkuji. Sbohem.\'"
dcera_pribeh = "Mezzobran si klekla a vytáhla knížku. \n\'Jednou ráno se Hopsálek probudil...\' začala číst. \nKdyž skončila, holčička se usmála.\n\'Maminka mi slíbila, že mi tu knížku přečte, když se nechám vykoupat. Ale pak mi jen strčila hlavu\n pod vodu a nechala mě tam.\'\n\'To… od ní nebylo hezké,\' formulovala nejistě Mezzobran.\n\'Že jo,\' řekla dívenka, \'ale ty jsi hodná, že jsi mi ji přečetla. Díky. Ale teď už musím jít. Ahoj.\'"
sluha_pribeh = "Elfka si povzdechla a sundala si zbroj. \n\'Tak víš co? Můžeš.\'\nPřízračné ruce studily, ale jinak to nebylo nijak nepříjemné.\n\'Děkuji. Už jsem byl skoro domluvený s Majdalenou, ale už nám to nevyšlo.\'\n\'Jakto?\'\n\'No, vždycky jsme si rozuměli, a po velké tancovačce jsem to na ni chtěl zkusit. A ona by určitě...\'\n\'Myslím proč vám to nevyšlo,\' přerušila ho Mezzobran, zatímco si znovu oblékala zbroj.\n\'No, večer za mnou přišla lady Tereza a chtěla podat kus uzeného. Tak jsem ve spíži vylezl na\n žebřík, abych to maso sundal a ona mi ten žebřík podkopla a já spadl na hák. Takže se na tu\n tancovačku nedostanu.\'\n\'To mě mrzí.\'\n\'Mě taky. Ale díky za… víte co. Sbohem,\' zamával rukou a zmizel."
sluzka_pribeh = "\'Tak dobře, dej mi minutku,\' řekla Mezzobran. Vrátila se do koupelny a pomocí hromady šminek,\n které předtím našla si vytvořila jemný knírek. Ne že by to platilo na její soukmenovce, ale lidé\n občas elfa od elfky nerozeznali i bez líčení. Pak se vrátila do pokoje.\n\'Mé jméno je Mezzobran, smím prosit, slečno?\'\nNebylo tam místo na víc než pár kroků, ale duchovi to evidentně stačilo.\n\'Děkuji. Těšila jsem se, že si zatančím na velké tancovačce s Martinem, ale vidíte, co se stalo.\'\nA co se stalo?\' zeptala se Mezzobran, \'myslím přesně.\'\n\'No, paní chtěla donést led, tak jsem lezla poklopem v kuchyni do ledárny, ale paní mě skopla dolů\n a já si zlámala vaz.\'\n\'Hrozné.\'\n\'Máte pravdu. Ale už na tom nesejde. Děkuji za tanec a sbohem.\'"
kuchar_pozadavek = "\'Musím vrátit ten sekáček,\' brumlá si, \'kde jen může být?\'"
guvernartka_pozadavek = "\'Musím znát odpověď na tu otázku z té učebnice,\' blekotá guvernantka rozčíleně, \'vás nenapadá, jak to je? Musím\n znát odpověď.\'"
lord_pozadavek = "\'Za všechno určitě může ta modla, musí být zničena,\' řekl muž, jako by to byl rozkaz, \'znič ji a \ndones mi její kusy. Chci vidět, že je zničena!\'"
dcera_pozadavek = "\'Já chci přečíst pohádku o Hopsálkovi,\' fňuká, \'přečteš mi pohádku o Hopsálkovi?\'"
sluha_pozadavek = "\'Já ještě nikdy nesáhl holce pod blůzu,\' zakňoural mládenec a vrhl na Mezzobran smutný pohled."
sluzka_pozadavek = "\'Já si ještě nikdy nezatančila ploužák,\' zakňourala dívka a vrhla na Mezzobran smutný pohled."
trezor = "Temná elfka zkusila otevřít trezor paklíčem, ale došlo jí, že to prostě nepůjde."
modla = "Elfka se rozhlédla a všimla si i dřevěné modly. Cítila, jak se jí neživý pohled zabodává do hlavy.\n Jako by jí uspávala. \n\'Dobrý pokus,\' ušklíbla se, \'ale na elfy tohle neplatí.\'\nA pak vytřeštila oči, protože modla se prudce pohla směrem k ní."
obsah = "Mezzobran vytáhla klíč, otevřela trezor a našla balíček dopisů a uložila si ho do kapsy."
lady_popis = "U stolu seděla zesláblá žena."
lady_pozadavek = "\'Kdo jste?\'\n\'To máte jedno. Co se tady pro všechny bohy stalo?\'\n\'Já… Já nechtěla,\' žena se dala do pláče, \'já… já je zabila. Ale já nechtěla. To ten démon. Donutil\n mne k tomu. Ovládl mne.\'\n\'Ovládl,\' temné elfce sjela ruka k jílci, \'a pořád vás ovládá?\'\n\'Ano. Ne. Já vlastně nevím. Když jsem…\' nedokázala to ani vyslovit, \'…no, potom jsem se\n ovládla. Ale věděla jsem, že tam ve mně pořád je. Utekla jsem sem, zamkla a klíč od jídelny hodila\n z okna, aby mne nemohl… použít znovu. Ale je tam. Drží se mé vůle, skrývá se ve mně, dokud\n mám ještě dost síly a vědomí. Nenechá mne ani spát, jen sedět a vidět vlastní zkázu.\'\n\'Takže se vás drží, dokud máte byť jen trochu vlastní vůle.\'\n\'Bojím se, že se mě drží jako život,\' vzlykla dáma, a pak si uvědomila, že hovoří s temnou elfkou,\n která se jí vloupala do domu, \'ale nezabíjejte mě, pro boha vás prosím, určitě existuje i jiná\n možnost.\'"
omameni = "Mezzobran jí přitiskla na obličej hadr a nepustila, dokud bezvládně neklesla. V duchu se usmála.\n Neudusila ji, jen ji dala mocně dýchnout sladkého oleje vitriolu, ale to démonovi bude možná stačit."
popis_smrti = "Když obdržela tuhle ránu, elfka klesla na zem, paralyzována bolestí. \n\'Takhle přece ne,\' zasípala, ale bylo to tak. Naposledy se pokusila nadechnout a ztratila vědomí,\n kterého už nenabyla."
popis_uteku = "\'Tohle je prostě moc velká špína,\' mumlala si. Rychle se vrátila do svého úkrytu, rozhodnutá už\n neriskovat prácičky od místních lidí. Ty se zdály moc riskantní. A peníze na zaplacení stejně\n neměla. Sbalila si všechny věci a za úsvitu už stála na palubě lodi."
popis_popravy = "Mezzobran vešla do sklepního hostince, ale místo jejího klienta ji tam čekalo několik vojáků.\n\'Zatýkáme tě za sedminásobnou vraždu!\' zahřímal jeden z nich a popadl elfku za rameno. Pokusila\n se tasit zbraň, ale nemělo to smysl. Zkušeně ji přemohli a připoutali v šatlavě. Proces byl veřejný,\n rychlý a trest drakonický. Za hrozný zločin byla temná elfka sťata za úsvitu."
popis_zaplaceni = "Mezzobran druhý den dopisy předala, dostala peníze a zaplatila dluh. Uchytila se ve městě a mohla\n se i dívat, jak popravují ženu, kterou předtím nechala naživu. Cítila hořkou pachuť a výčitky\n svědomí. Ale nejhorší bylo, že cítila, že se jí moc všímají stráže. A věděla, proč. Na přání nového\n maršála."
popis_dluhu = "Mezzobran se chtělo zvracet. Rychle napsala krátký vzkaz: \'Tohle možná vysvětluje, co se stalo ve\n vile za městem.\' Ten přidala k dopisům a svázala je do útlého balíčku. Ten hodila do okna městské\n hlídce a vypařila se. Ráno místo ke svému zákazníkovi navštívila své věřitele. Cokoli po ní můžou\n chtít nebude horší, než žít s tím, že kryje tohle svinstvo."
popis_ocisteni = "Elfka se otočila a poklusem se vrátila do vily. Rychle popadla omámenou ženu a odnesla ji do\n chrámu léčitelů, kde ji rychle dali dohromady.\n\'Děkuji,\' řekla jí pak.\n\'Nepotřebuju díky, potřebuju peníze a vaše svědectví. A vy potřebujete tyhle papíry a moje\n svědectví. Uvidíte, že se z toho navzájem dostaneme.\'\n\nMěla pravdu. Lady Tereza zaplatila za Mezzobran dluh a protože její svědectví bylo velmi zásadní,\n dostala generální amnestii. Mohla tedy na náměstí spokojeně přihlížet popravě bývalého\n vicemaršála."
popis_odmeny = "Během této podívané k ní přistoupila žena v režném rouchu.\n\'Slečno Mezzobran...\'\n\'Lady Terezo. Co to máte na sobě?\'\n\'Rozhodla jsem se odčinit alespoň kousek své viny, žit skromně a svůj majetek používat pro blaho\n potřebných,\' odpověděla žena, \'ale do jednoho majetku už nevkročím nikdy. Svou vilu jsem \npřepsala na vás. Tady máte listinu a klíč.\'\nElfce spadla čelist.\n\'Pomohla jste najít klid všem, kterým jsem ublížila,\' vysvětlovala lady, \'zasloužíte si ji. Prodejte ji\n nebo pronajměte a s těmi penězi můžete vést úspěšný poctivý život. Nebo nepoctivý. Nebo to\n propít. Nebo si ji nechte, bydlete v ní, zřiďte v ní něco. Útulek pro sirotky, hostinec, nevěstinec, to\n je vaše věc. Cokoliv z toho bude pořád lepší, než co jsem v ní udělala já.\'\n\'Já nemám slov. Teda děkuji, ale… no...\'\n\'To nevadí,\' odpověděla žena, nechala elfku s listinou a klíčem a zmizela v davu."
obsah_dopisu = "Temná elfka mávla rukou a objevily se čtyři světélkující koule. Jejich záře byla slabá, ale oči\n přivyklé na absolutní temnotu v ní dokázaly bez problémů číst. A že bylo o čem. Lordův vicemaršál\n si dopisoval s jeho manželkou, lady Terezou, ale vše se zdálo přátelské a nevinné. Ale elfka brzy\n postřehla, že ve vicemaršálových listech se začaly stále častěji objevovat zmínky o dívkách, které\n s jejím manželem potkávají. A pak i uklidnění nervózní adresátky, doplněné zprvu lehkými, později\n vytrvalými narážkami na vzhled. V Mezzobran začalo klíčit podezření. Brzy se dočetla o tom, že jí\n vicemaršál poslal zrcadlo. A i z reakcí začalo být zřejmé, že se dáma, které dopisy chodily, bála\n stárnutí. A vyvrcholilo to tím, že vicemaršál slíbil dodat modlu, která omlazuje. "
Kuchar_duch = Duch(kuchar_popis, kuchar_pozadavek, "chceš li si s kuchařem promluvit", "sekáček.",
                   True, kuchar_pribeh, "Kuchař")
Guvernantka_duch = Duch(guvernantka_popis, guvernartka_pozadavek, "chceš li si s guvernantkou promluvit",
                        "odpověď", True, guvernantka_pribeh, "Guvernantka")
Sluha_duch = Duch(sluha_popis, sluha_pozadavek, "chceš li si se sluhou promluvit", "kozy", True,
                  sluha_pribeh, "Sluha")
Sluzka_duch = Duch(sluzka_popis, sluzka_pozadavek, "chceš li si se služkou promluvit", "líčidla.",
                   True, sluzka_pribeh, "Služka")
Majitel_duch = Duch(lord_popis, lord_pozadavek, "chceš li si s lordem promluvit", "kusy modly.", True,
                    lord_pribeh, "Lord")
Dcera_duch = Duch(dcera_popis, dcera_pozadavek, "chceš li si s holčičkou promluvit", "pohádkovou knížku.", True,
                  dcera_pribeh, "Holčička")
Trezor = Duch("Prohledání místnosti a trezor", trezor, "chceš li otevřít trezor", "klíč", True,
              obsah, "Trezor")
Manzelka = Duch(lady_popis, lady_pozadavek, "chceš li si s lady promluvit", "chloroform", True,
                omameni, "Lady")
Zadny_duch = Duch("X", "X", "X", "X", False, "X", "X")
Kuchar_zombie = Zombie("Zombie kuchař", 1, 8, 6, 22, -2, kostka, kuchar_utok)
Guvernantka_zombie = Zombie("Zombie guvernantka", 1, 8, 6, 22, -2, kostka, guvernantka_utok)
Sluha_zombie = Zombie("Zombie sluha", 1, 8, 6, 22, -2, kostka, sluha_utok)
Sluzka_zombie = Zombie("Zombie služka", 1, 8, 6, 22, -2, kostka, sluzka_utok)
Majitel_zombie = Zombie("Zombie lord", 1, 8, 6, 22, -2, kostka, lord_utok)
Dcera_zombie = Zombie("Zombie holčička", 1, 8, 6, 22, -2, kostka, dcera_utok)
Socha_demona = Zombie("Socha démona", 1, 10, 0, 1, 0, kostka, modla)
Zadna_zombie = Zombie("X", 0, 0, 0, 0, 0, kostka, "X")
Zlovony_demon = Demon("Démon", 3, 13, 4, 10, 3, kostka, "démon", True)
Inventar = ["kozy", "chloroform"]
nedvere = Nedvere()
Nepokoj = Mistnost(Zadny_duch, Zadna_zombie, "Nic", "Nic", "Nic", "Nic", Zadna_zombie, nedvere, Zadna_zombie, kostka, "Nic")
Mezzobran = Hrdinka("Mezzobran", 4, 15, 6, 37, Nepokoj, Inventar, 0, True, kostka, hadanka, prevlekani)
Lahev = Poklad(True, False, vypiti_lahve,rozbiti_lahve, "lektvar","vypití flašky", "střepy")
Brigadina = Poklad(True, False, obleceni_zbroje, bodnuti_zbroje, "zbroj", "oblečení brigadiny", "nic")
Zrcadlo = Poklad(True,False,podivani_do_zrcadla, rozbiti_zrcadla, "pohled", "pohled do zrcadla, ", "střepy")
Tancici_figurka = Poklad(True,False,vyndani_sosky, rozbiti_sosky, "hudba", "hudba", "kousky figurky")
Ledarna = Ukryt("Poklop v podlaze", Sluzka_zombie, False, Mezzobran, True, kostka, Zadna_zombie)
Vana = Ukryt("Paraván od vany", Dcera_zombie, False, Mezzobran, True, kostka, Zadna_zombie)
Spiz = Ukryt("Malé jednoduché dveře", Sluha_zombie, False, Mezzobran, True, kostka, Zadna_zombie)
Nic = Ukryt("Nic", Zadna_zombie, True, Mezzobran, False, kostka, Zadna_zombie)
Bar = Pokladnice("bar", Zadna_zombie, False, Mezzobran, True, kostka, Zadna_zombie, Lahev)
Kosmeticka_skrinka = Pokladnice("kosmetickou skříňku", Zadna_zombie, False, Mezzobran, True, kostka, Zadna_zombie, Zrcadlo)
Hraci_skrinka = Pokladnice("hrací skříňku", Zadna_zombie, False, Mezzobran, True, kostka, Zadna_zombie, Tancici_figurka)
Skrin = Pokladnice("skříň", Zadna_zombie, False, Mezzobran, True, kostka, Zadna_zombie, Brigadina)
Hlavni_hala = Hala(Zadny_duch, Kuchar_zombie, "služebnické dveře v přízemí", Nic, popis_hlavni_hala, "Hala", Mezzobran, nedvere,
                   Zadna_zombie, kostka, dvere_haly, nedvere, nedvere, nedvere, nedvere, nedvere)
Ochoz = Hala(Zadny_duch, Guvernantka_zombie, "skryté dveře v patře", Nic, popis_ochoz, "Ochoz", Mezzobran, nedvere,
             Zadna_zombie, kostka, dvere_ochoz, nedvere, nedvere, nedvere, nedvere, nedvere)
Oblast_sluzebnictva = Hala(Zadny_duch, Zadna_zombie, "Nic", Nic, popis_mistnost_sluzebnictva, "Oblast služebnictva", Mezzobran, nedvere,
                           Zadna_zombie, kostka, dvere_sluzebni_cast, nedvere, nedvere, nedvere, nedvere, nedvere)
Schody_pro_sluzebnictvo = Hala(Zadny_duch, Zadna_zombie, "Nic", Nic, popis_schodiste, "Schody pro služebnictvo",
                               Mezzobran, nedvere, Zadna_zombie, kostka, "Nic", nedvere, nedvere, nedvere, nedvere, nedvere)
Obyvaci_pokoj = Mistnost(Majitel_duch, Zadna_zombie, "vojenskou medaili.", Bar, popis_obyvaci_pokoj, "Obývák", Mezzobran, nedvere,
                         Zadna_zombie, kostka, dvere_obyvaci_pokoj)
Knihovna = Mistnost(Guvernantka_duch, Zadna_zombie, "pohádkovou knížku.", Nic, popis_knihovna, "Knihovna", Mezzobran, nedvere,
                    Zadna_zombie, kostka, dvere_knihovna)
Lordova_loznice = Mistnost(Zadny_duch, Majitel_zombie, "rapír a dýku.", Skrin, popis_panova_loznice, "Lordova ložnice",
                           Mezzobran, nedvere, Zadna_zombie, kostka, dvere_panova_loznice)
Loznice_lady = Mistnost(Trezor, Socha_demona, "kusy modly.", Kosmeticka_skrinka, popis_loznice_pani, "Ložnice lady", Mezzobran,
                        nedvere, Zadna_zombie, kostka, dvere_loznice_lady)
Detsky_pokoj = Mistnost(Dcera_duch, Zadna_zombie, obrazky, Hraci_skrinka, popis_detsky_pokoj, "Dětský pokoj", Mezzobran,
                        nedvere, Zadna_zombie, kostka, dvere_detsky_pokoj)
Koupelna = Mistnost(Zadny_duch, Zadna_zombie, "líčidla.", Vana, popis_koupelna, "Koupelna", Mezzobran, nedvere,
                    Zadna_zombie, kostka, dvere_koupelana)
Muzska_loznice = Mistnost(Sluha_duch, Zadna_zombie, "sekáček.", Nic, popis_muzska_loznice, "Mužská ložnice", Mezzobran,
                          nedvere, Zadna_zombie, kostka, dvere_muzska_loznice)
Zenska_loznice = Mistnost(Sluzka_duch, Zadna_zombie, "učebnici.", Nic, popis_zenska_loznice, "Žeská ložnice",
                          Mezzobran, nedvere, Zadna_zombie, kostka,dvere_zenske_loznice)
Kuchyne_vily = Kuchyne(Kuchar_duch, Zadna_zombie, "výtah.", Ledarna, popis_kuchyne, "Kuchyně", Mezzobran, nedvere,
                       Zadna_zombie, kostka, dvere_kuchyne, Spiz, nedvere)
Jidelna_vily = Jidelna(Manzelka, Zlovony_demon, "klíč", Ledarna, popis_jidelna, "Jídelna", Mezzobran, nedvere,
                       Zadna_zombie, kostka, dvere_jidelna, nedvere)
hlavni_vchod = Vrata(Hlavni_hala, Nepokoj, "Vstup do vily", Mezzobran)
hala_jidelna = Zablokovane_dvere(Hlavni_hala, Jidelna_vily, "dveře v levé zdi haly", Mezzobran, dialog)
hala_obyvak = Dvere(Hlavni_hala, Obyvaci_pokoj, "dveře v zadní stěně haly", Mezzobran)
hala_knihovna = Dvere(Hlavni_hala, Knihovna, "dveře v pravé stěně haly", Mezzobran)
hala_schodiste = Dvere(Hlavni_hala, Schody_pro_sluzebnictvo, "služebnické dveře v přízemí", Mezzobran)
hala_ochoz = Dvere(Hlavni_hala, Ochoz, "velké schodiště", Mezzobran)
ochoz_lordova_loznice = Dvere(Ochoz, Lordova_loznice, "dveře v protější zdi vpravo", Mezzobran)
ochoz_loznice_lady = Dvere(Ochoz, Loznice_lady, "dveře v protější zdi vpravo", Mezzobran)
ochoz_detsky_pokoj = Dvere(Ochoz, Detsky_pokoj, "dveře v pravé zdi", Mezzobran)
ochoz_koupelna = Dvere(Ochoz, Koupelna, "dveře v levé zdi", Mezzobran)
ochoz_oblast_sluzebnictva = Dvere(Oblast_sluzebnictva, Ochoz, "skryté dveře v patře", Mezzobran)
oblast_sluzebnivtva_muzska_loznice = Dvere(Oblast_sluzebnictva, Muzska_loznice, "dveře vlevo", Mezzobran)
oblast_sluzebnictva_zenska_loznice = Dvere(Oblast_sluzebnictva, Zenska_loznice, "dveře vpravo", Mezzobran)
oblast_sluzebnictva_schodiste = Dvere(Oblast_sluzebnictva, Schody_pro_sluzebnictvo, "služební dveře v patře", Mezzobran)
schodiste_kuchyne = Dvere(Schody_pro_sluzebnictvo, Kuchyne_vily, "služební dveře v suterénu", Mezzobran)
kuchynsky_vytah = Dvere(Kuchyne_vily, Jidelna_vily, "výtah", Mezzobran)
Neexistijici_dvere = Dvere(Nepokoj, Nepokoj, "Neexistuje", Mezzobran)
Hlavni_hala.predefinovani_dveri(hlavni_vchod)
Hlavni_hala.predefinovani_dalsich_dveri(hala_ochoz, hala_jidelna, hala_knihovna, hala_obyvak, hala_schodiste)
Ochoz.predefinovani_dveri(hala_ochoz)
Ochoz.predefinovani_dalsich_dveri(ochoz_detsky_pokoj, ochoz_koupelna, ochoz_loznice_lady,
             ochoz_lordova_loznice, ochoz_oblast_sluzebnictva)
Oblast_sluzebnictva.predefinovani_dveri(oblast_sluzebnictva_schodiste)
Oblast_sluzebnictva.predefinovani_dalsich_dveri(oblast_sluzebnictva_zenska_loznice,
                           oblast_sluzebnivtva_muzska_loznice, ochoz_oblast_sluzebnictva, Neexistijici_dvere, Neexistijici_dvere
                           )
Schody_pro_sluzebnictvo.predefinovani_dveri(schodiste_kuchyne)
Schody_pro_sluzebnictvo.predefinovani_dalsich_dveri(oblast_sluzebnictva_schodiste,
                               hala_schodiste, Neexistijici_dvere, Neexistijici_dvere, Neexistijici_dvere)
Obyvaci_pokoj.predefinovani_dveri(hala_obyvak)
Knihovna.predefinovani_dveri(hala_knihovna)
Lordova_loznice.predefinovani_dveri(ochoz_lordova_loznice)
Loznice_lady.predefinovani_dveri(ochoz_loznice_lady)
Detsky_pokoj.predefinovani_dveri(ochoz_detsky_pokoj)
Koupelna.predefinovani_dveri(ochoz_koupelna)
Muzska_loznice.predefinovani_dveri(oblast_sluzebnivtva_muzska_loznice)
Zenska_loznice.predefinovani_dveri(oblast_sluzebnictva_zenska_loznice)
Kuchyne_vily.predefinovani_dveri(schodiste_kuchyne)
Jidelna_vily.predefinovani_dveri(hala_jidelna)
Kuchyne_vily.predefinovani_vytahu(kuchynsky_vytah)
Jidelna_vily.predefinovani_vytahu(kuchynsky_vytah)
Mezzobran.poloha(Hlavni_hala.nazev())
Hra = Cutscena(uvod_zacatek, uvod_ukol, uvod_priprava,  uvod_zahrada, Hlavni_hala, Mezzobran, popis_smrti, popis_uteku, popis_popravy, popis_zaplaceni, popis_dluhu, popis_ocisteni, popis_odmeny, obsah_dopisu)

Hra.hra()
