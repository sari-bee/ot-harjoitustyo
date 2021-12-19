# Testausraportti

## Yksikkö- ja integraatiotestaus

Automaattisilla testeillä testataan Entities-, Repositories- ja Services-kansioiden luokat. Käyttöliittymä jää automaattisten testien ulkopuolelle. Testiluokan nimi vastaa varsinaisen luokan nimeä etuliitteellä Test. Testejä varten tietojen pysyväistallennukseen tarkoitetuista tiedostoista tehdään omat test-etuliitteellä alkavat versiot, joiden nimet on määritelty .env.test-tiedostossa. Tiedostot tyhjennetään aina uuden testin alkaessa.

### Testauskattavuus

Automaattisia testejä on 52 kappaletta. Testien haarautumakattavuus yllämainittujen luokkien osalta on 99%.

![Coverage-report](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coverage_report.png)

Olennaisin automaattitesteillä testaamatta jäänyt asia oli tilanne, jossa pysyväistalletukseen tarkoitetuissa tiedostoissa oli virheellisen muotoista tietoa. Tämä testattiin manuaalisesti.

## Järjestelmätestaus

Järjestelmätestaus suoritettiin manuaalisesti. Sovellus on asennettu ja testattu macOS- ja Linux-ympäristöissä. Testauksen pohjana toimivat vaatimusmäärittelydokumentissa mainitut toiminnallisuudet; lisäksi testattiin virheellisten syötteiden vaikutusta ohjelman toimintaan. Testausta suoritettiin myös muuttaen konfiguraatiotiedostossa olevia asioita.

### Kirjautumisikkuna

Uuden käyttäjätunnuksen luominen ja luodulla käyttäjätunnuksella kirjautuminen onnistuvat. Ohjelma huomauttaa graafisessa käyttöliittymässä, jos yritetään kirjautua käyttäjätunnuksella jota ei ole olemassa, jos yritetään lisätä käyttäjätunnus joka on jo varattu tai jos lisättävä käyttäjätunnus on liian lyhyt. Kirjautumisen jälkeen kirjautumisikkuna lukkiutuu, joten eri käyttäjätunnuksilla toimiminen ei voi mennä sekaisin.

Ensimmäisen käyttäjän ensimmäinen kirjautuminen luo Data-kansioon tiedoston, johon käyttäjät talletetaan.

### Näyteikkuna

Ohjelma huomauttaa graafisessa käyttöliittymässä, jos näytetunniste puuttuu tai on jo käytössä. Samoin ohjelma huomauttaa, jos jokin reaktiovoimakkuus puuttuu tai on virheellinen. Näytetunnisteen voi antaa myös pienillä kirjaimilla ja se muutetaan automaattisesti uppercase-muotoon. Kenttien täyttämisen jälkeen käyttäjä saa Tarkista-painiketta painamalla näytteen tulkinnan vaatimusmäärittelyn mukaisesti. Tyhjennä-painike tyhjentää kaikki syöttökentät. Uuden näytteen tiedot voi lisätä sekä painamatta Tyhjennä-painiketta että tyhjentämällä kentät näytteiden välissä.

Ensimmäisen käyttäjän ensimmäisen näytteen tietojen tarkastus luo Data-kansioon tiedoston, johon näytteet talletetaan.

### Historiaikkuna

Näyteikkunan Näytehistoria-painikkeesta avautuu Näytehistoria-ikkuna. Yksittäisen näytetunnisteen antamalla voi hakea yhden näytteen tiedot. Näytetunnisteen voi antaa myös pienillä kirjaimilla ja se muutetaan automaattisesti uppercase-muotoon. Ohjelma huomauttaa graafisessa käyttöliittymässä, jos haettua näytetunnistetta ei löydy. Lisäksi käyttäjä voi selata itse tallettamiaan näytteitä tai kaikkia näytteitä vaatimusmäärittelyn mukaisesti. Ohjelma huomauttaa, jos listattavia näytteitä ei ole. Hakutuloksia näytetään yksittäisessä ikkunassa 5 kpl. Tarvittaessa käyttäjä voi siirtyä aiempiin tai myöhempiin näytteisiin näytön alalaidan painikkeiden kautta; painikkeet ovat disabloituja, jos aiempia/myöhempiä tuloksia ei ole. Jos käyttäjä painaa ko. painikkeita etsittyään yksittäisellä näytetunnisteella, ohjelma pyytää valitsemaan ensin haun. Historiaikkunoita voi halutessaan avata useita eikä ohjelma kaadu tästä.

## Sovelluksen laatuongelmat

Käyttäjätunnuksessa kirjainkoko on merkitsevä. Tämä voisi periaatteessa johtaa tilanteeseen, jossa käyttäjä virheellisesti käyttää kahta erillistä käyttäjätunnusta, jotka eroavat toisistaan esimerkiksi ensimmäisen ison kirjaimen suhteen. Toisaalta on tietoinen valinta, että käyttäjätunnuksen kirjainkoko on merkitsevä, ja tämä on lähinnä ohjeistuskysymys.

Joissakin harvinaisissa tilanteissa sovellus voisi kaatua, jos käyttäjä lisäisi suoraan pysyväistallennustiedostoihin dataa, joka on virheellistä mutta oikean muotoista.

Sovellusta ei päästy testamaan tilanteessa, jossa näytetunniste luettaisiin sovellukseen viivakoodinlukijalla.

