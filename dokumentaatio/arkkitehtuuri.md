# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa pääsääntöisesti kolmitasoista kerrosarkkitehtuuria seuraavin yhteyksin:

![Kansiorakenne](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/packages.png)

Kansio *ui* sisältää käyttöliittymästä, *services* sovelluslogiikasta ja *repositories* tietojen pysyväistallennuksesta vastaavat luokat. Kansio *entities* sisältää sovelluksen tieto-oliot rakentavat luokat.

## Käyttöliittymä

Käyttöliittymä sisältää kolme näkymää:

- Kirjautumisikkuna (LoginView)
- Näytteen tietojen syöttöikkuna (SampleView)
- Näytehistorianäkymä (HistoryView)

Jokaisesta näkymästä vastaa oma luokkansa ja näkymät avautuvat aina uuteen ikkunaan. Kun näytteen tietojen syöttöikkuna avautuu, kirjautumisikkunan napit disabloituvat. Näkymien näyttämisestä vastaa UI-luokka. Käyttöliittymä kutsuu ainoastaan SampleHandler- ja UserHandler-luokkien metodeja.

## Sovelluslogiikka

Sovelluksen tieto-olioiden rakenteena toimivat luokat Sample ja User, jotka kuvaavat näytettä ja käyttäjää. Tieto-olioita manipuloivat luokat SampleHandler ja UserHandler, joiden metodeja käyttöliittymä kutsuu. Tieto-olioiden hallinnasta ja tietojen pysyväistalletuksesta vastaavat SampleRepository- ja UserRepository-luokat. Lisäksi sovelluksessa on neljä ainoastaan luokkametodeja sisältävää services-tyyppistä luokkaa, jotka toteuttavat sovelluslogiikkaa (ListingService, ABOLogic, ReactionLogic ja TransfusionDirections). Sovelluksen eri luokkien keskinäiset yhteydet ovat seuraavanlaiset:

![Arkkitehtuuri](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/architecture.png)

## Tietojen pysyväistallennus

Tiedot näytteistä ja käyttäjistä pysyväistalletetaan yksittäisen tietokoneen levylle kahteen erilliseen CSV-tiedostoon, joita *repositories*-kerroksen luokat SampleRepository ja UserRepository lukevat ja kirjoittavat. Tiedostojen polut määritellään SampleHandler- ja UserHandler-luokkien konstruktoreissa. Tarvittaessa tiedostojen nimiä voi muuttaa konfiguraatiotiedoston .env kautta. Mikäli tietojen tallennustapaa haluttaisiin muuttaa, voitaisiin uusi menetelmä määritellä SampleRepositoryn ja UserRepositoryn metodeissa *read* ja *write*, joita muut metodit kutsuvat.

Tiedot tallennetaan CSV-tiedostoon seuraavasti:

Näytteet:
```
ABCDE;tämä on näyte;4;0;0;0;0;4;2021-12-13 20:00:00.00000
```
Näytetunniste, näytekommentti, anti-A, anti-B, anti-D, kontrolli, A1-solu, B-solu, aikaleima (vvvv-kk-pp hh:mm:ss.sssss).

Käyttäjät:
```
Testi-Tiina;ABCDE;12345;qwerty;789
```
Käyttäjätunnus, näytetunnisteet puolipisteellä erotettuna

## Päätoiminnallisuudet

Toiminnallisuudet kuvataan tyypillisten käyttötapausten kautta.

### Käyttäjätunnuksen luominen ja sisäänkirjautuminen

![Kirjautuminen](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/login_sequence.png)

Käyttäjä syöttää kirjautumisikkunan alempaan kenttään käyttäjätunnuksen, jonka hän haluaa rekisteröidä ja painaa Lisää!. Käyttöliittymä kutsuu UserHandlerin metodia add_new_user, joka luo uuden käyttäjän ja lisää sen UserRepositoryyn. Tämän jälkeen käyttäjälle näytetään tieto, että rekisteröityminen onnistui. Jos käyttäjätunnus on jo käytössä, add_new_user palauttaa None.

Seuraavaksi käyttäjä syöttää kirjautumisikkunan ylempään kenttään käyttäjätunnuksensa ja painaa Kirjaudu sisään. Käyttöliittymä kutsuu UserHandlerin metodia find_user_by_username, joka hakee käyttäjän UserRepositorystä ja palauttaa sen käyttöliittymälle. Käyttöliittymän LoginView-luokka kutsuu seuraavaksi UI-luokan metodia to_sample_view, jolle se antaa parametriksi juuri noudetun käyttäjän. Jos käyttäjän syöttämää käyttäjätunnusta ei löydy, find_user_by_username palauttaa None.

### Näytteen tietojen syöttäminen ja tulkinta

![Näytetulkinta](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sample_sequence.png)

Käyttäjä syöttää näyteikkunassa näytteen tiedot ja painaa Tarkista. Käyttöliittymä kutsuu SampleHandler-luokan metodia check_input. Check_input palauttaa True, jos annetut syötteet ovat valideja. Jos annetut syötteet eivät ole valideja, check_input palauttaa listan kenttiä, joissa syöte on virheellinen. 

Tämän jälkeen käyttöliittymä kutsuu SampleHandler-luokan metodia add_sample_data, joka luo näyteolion annetuilla syötteillä ja lisää näytteen SampleRepositoryyn kutsumalla metodia add_sample. Jos näytetunniste on jo käytössä, add_sample palauttaa False. Lisäksi käyttöliittymä kutsuu UserHandler-luokan metodia add_sample_to_user, joka huolehtii näytetunnisteen lisäämisestä sisäänkirjautuneen käyttäjän tietoihin UserRepository-luokan avulla.

Tämän jälkeen käyttöliittymä kutsuu SampleHandlerin metodia get_results, joka noutaa ensin näytteen tiedot SampleRepositorystä ja pyytää sitten näyteoliota ajamaan tulkintatarkistukset metodilla run_checks. run_checks kutsuu ensin ReactionLogic-serviceä, joka tarkistaa yksittäisten reaktioiden reaktiovoimakkuudet. Mikäli näissä on poikkeavaa, palautetaan lista poikkeamista ja TransfusionDirections-servicen antama verensiirto-ohje. Mikäli poikkeavaa ei ole, ReactionLogic palauttaa True ja run_checks kutsuu ABOLogic-serviceä. ABOLogic-service tarkistaa reaktioiden kokonaisuuden ja palauttaa veriryhmän tulkinnan sekä TransfusionDirections-servicen antaman verensiirto-ohjeen. Lopulta näytteen tulkinta palautetaan käyttöliittymälle, joka näyttää tulkinnan käyttäjälle.

### Näytehistoria

![Historia](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/history_sequence.png)

Käyttäjä syöttää historianäkymässä näytetunnisteen ja painaa Etsi näytetunnisteella. Käyttöliittymä kutsuu SampleHandler-luokan metodia get_sample_by_id, joka noutaa näytteen tiedot SampleRepositorystä. Tämän jälkeen SampleHandler kutsuu ListingServicen metodia get_one_sample, joka noutaa näytteen tulosten tulkinnan Sample-luokan metodin run_checks-avulla; tässä hyödynnetään ReactionLogic-, ABOLogic- ja TransfusionLogic-servicejä samaan tapaan kuin yllä on kuvattu. ListingService koostaa näytteen tulkinnan ja palauttaa sen SampleHandlerin kautta käyttöliittymälle, joka näyttää tiedot käyttäjälle.

Vaihtoehtoisesti käyttäjä voi hakea kaikki konekohtaisesti talletetut näytteet. Käyttäjä painaa painiketta Selaa kaikkia näytteitä, joka kutsuu SampleHandlerin kahta metodia. Ensin haetaan talletettujen näytteiden kokonaismäärä listauksen ryhmittelyä varten metodilla get_number_of_samples ja sitten haetaan varsinaiset näytteet metodilla get_all_samples. SampleHandler hakee näytteet SampleRepositorysta ja pyytää sitten ListingServicen metodia list_samples noutamaan näytteiden tulosten tulkinnan. Tämän jälkeen oleellisesti sekvenssi menee kuten yhden näytteen hakemisessa.

Kolmantena vaihtoehtona käyttäjä voi hakea kaikki itse tallentamansa näytteet painamalla painiketta Tallettamasi näytteet. Tällöin kutsutaan UserHandlerin kahta metodia: get_number_of_samples, jolla haetaan käyttäjän tallettamien näytteiden määrä listauksen ryhmittelyä varten ja get_samples_by_user, joka hakee listan näytetunnisteita. Tämä lista annetaan parametriksi SampleHandlerin metodille get_samples_by_several_ids. SampleHandler hakee listan perusteella SampleRepositorysta vastaavat näytteet, minkä jälkeen sekvenssi menee kuten kaikkien näytteiden hakemisessa.

Näytteen tulkintaa ei ole tallennettu CSV-tiedostoon vaan se haetaan aina erikseen näytehistoriaa tarkastellessa. Tämä johtuu siitä että näytteitä talletetaan opetustarkoituksiin, jolloin on tärkeä varmistaa, ettei listauksiin jää mahdollisesti vanhentuneita tulkintoja, mikäli reaktioiden tulkintaohjeet muuttuvat.

## Sovelluksen heikkoudet

Päädyin käyttämään sovelluksessani CSV-tiedostoja tietojen pysyväistalletukseen lähinnä helppouden vuoksi ja siksi, että se tuntui talletusmuotona sopivan tiedolle, jota talletin. Jälkikäteen ajateltuna ainakin käyttäjien tiedot olisi voinut hyvin tallentaa myös tietokantaan.
Olisin myös voinut tehdä ratkaisun, joka lukee tiedostojen sisällön aina ohjelman aukaisun yhteydessä ja tallettaa sen uudestaan ohjelman sulkemisen yhteydessä; nykyratkaisu, jossa tiedostoja luetaan ja kirjoitetaan toistuvasti lienee tehoton.

SampleRepository- ja UserRepository-luokissa on omat tiedoston luku- ja kirjoitusmetodinsa. Nämä olisi ehkä voinut toteuttaa myös yleisluonteisina metodeina.

Näytteen tulkinta haetaan nyt Sample-olion metodin kautta. Tämän olisi ehkä voinut toteuttaa myös suoraan SampleHandlerin kautta. Myös näytteiden listauksissa olisi ehkä ollut mahdollisuuksia vielä toteuttaa enemmän yhteisiä metodeja SampleView:n ja HistoryView:n välille.

Jatkokehitysideana voisi olla järkevää tallettaa suurempi osa tuloksen tulkinnasta jonkinlaisiin konfiguraatiotiedostoihin kovakoodauksen sijaan. Lisäksi olisi hyvä tehdä ratkaisu, jossa käyttäjä voi kirjautua ulos ja uusi käyttäjä kirjautua sisään ilman, että sovellus täytyy sulkea välissä.