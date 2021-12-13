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

Jokaisesta näkymästä vastaa oma luokkansa ja näkymät avautuvat aina uuteen ikkunaan. Kun näytteen tietojen syöttöikkuna avautuu, kirjautumisikkunan napit disabloituvat. Näkymien näyttämisestä vastaa UI-luokka. Käyttöliittymä kutsuu ainoastaan SampleHandler- ja UserHandler-luokkien metodeja (lisäksi se käyttää User-luokkaa aktiivisen käyttäjän tietojen hakemiseen).

## Sovelluslogiikka

Sovelluksen tieto-olioiden rakenteena toimivat luokat Sample ja User, jotka kuvaavat näytettä ja käyttäjää. Tieto-olioita manipuloivat luokat SampleHandler ja UserHandler, joiden metodeja käyttöliittymä kutsuu. Tieto-olioiden hallinnasta ja tietojen pysyväistalletuksesta vastaavat SampleRepository- ja UserRepository-luokat. Lisäksi sovelluksessa on kolme ainoastaan luokkametodeja sisältävää services-tyyppistä luokkaa, jotka toteuttavat sovelluslogiikkaa (ListingService, ABOLogic ja ReactionLogic). Sovelluksen eri luokkien keskinäiset yhteydet ovat seuraavanlaiset:

![Arkkitehtuuri](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/architecture.jpg)

## Tietojen pysyväistallennus

Tiedot näytteistä ja käyttäjistä pysyväistalletetaan yksittäisen tietokoneen levylle kahteen erilliseen CSV-tiedostoon, joita *repositories*-kerroksen luokat SampleRepository ja UserRepository lukevat ja kirjoittavat. Tiedostojen polut määritellään SampleHandler- ja UserHandler-luokkien konstruktoreissa. Mikäli tietojen tallennustapaa haluttaisiin muuttaa, voitaisiin uusi menetelmä määritellä SampleRepositoryn ja UserRepositoryn metodeissa *read* ja *write*, joita muut metodit kutsuvat.

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

Käyttäjä syöttää kirjautumisikkunan alempaan kenttään käyttäjätunnuksen, jonka hän haluaa rekisteröidä ja painaa Lisää!. Käyttöliittymä kutsuu UserHandlerin metodia add_new_user, joka luo uuden käyttäjän ja lisää sen UserRepositoryyn. Tämän jälkeen käyttäjälle näytetään tieto, että rekisteröityminen onnistui. Seuraavaksi käyttäjä syöttää kirjautumisikkunan ylempään kenttään käyttäjätunnuksensa ja painaa Kirjaudu sisään. Käyttöliittymä kutsuu UserHandlerin metodia find_user_by_username, joka hakee käyttäjän UserRepositorystä ja palauttaa sen käyttöliittymälle. Käyttöliittymän LoginView-luokka kutsuu seuraavaksi UI-luokan metodia to_sample_view, jolle se antaa parametriksi juuri noudetun käyttäjän.

### Näytteen tietojen syöttäminen ja tulkinta

Selvän veriryhmän tulkinta käyttäjän syöttämistä reaktioista käyttäjälle annettavaan tulkintaan:
![Näytetulkinta](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sample_sequence.png)

Käyttäjä syöttää näyteikkunassa näytteen tiedot ja painaa Tarkista. Käyttöliittymä kutsuu SampleHandler-luokan metodia check_input, joka tarkistaa, ovatko annetut syötteet valideja. Tämän jälkeen käyttöliittymä kutsuu SampleHandler-luokan metodia add_sample_data, joka luo näyteolion annetuilla syötteillä ja lisää näytteen SampleRepositoryyn. Käyttöliittymä kutsuu UserHandler-luokan metodia add_sample_to_user, joka huolehtii näytetunnisteen lisäämisestä sisäänkirjautuneen käyttäjän tietoihin. Tämän jälkeen käyttöliittymä kutsuu SampleHandlerin metodia get_results, joka noutaa ensin näytteen tiedot SampleRepositorystä ja pyytää sitten näyteoliota ajamaan tulkintatarkistukset metodilla run_checks, joka hyödyntää ReactionLogic- ja ABOLogic-servicejä. Metodi palauttaa näytteen tulkinnan lopulta käyttöliittymälle, joka näyttää tulkinnan käyttäjälle.

### Yksittäisen näytteen tietojen tarkastelu

Näytteen haku näytetunnisteella ja näyttäminen käyttäjälle:
![Historia](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/history_sequence.png)

Käyttäjä syöttää historianäkymässä näytetunnisteen ja painaa Etsi näytetunnisteella. Käyttöliittymä kursuu SampleHandler-luokan metodia get_sample_by_id, joka noutaa näytteen tiedot SampleRepositorystä. Tämän jälkeen SampleHandler kutsuu ListingServicen metodia get_one_sample, joka noutaa näytteen tulosten tulkinnan Sample-luokan metodin run_checks-avulla; tässä hyödynnetään ReactionLogic- ja ABOLogic-servicejä. ListingService koostaa näytteen tulkinnan ja palauttaa sen SampleHandlerin kautta käyttöliittymälle, joka näyttää tiedot käyttäjälle.

Näytteen tulkintaa ei ole tallennettu CSV-tiedostoon vaan se haetaan aina erikseen näytehistoriaa tarkastellessa. Tämä johtuu siitä että näytteitä talletetaan opetustarkoituksiin, jolloin on tärkeä varmistaa, ettei listauksiin jää mahdollisesti vanhentuneita tulkintoja, mikäli reaktioiden tulkintaohjeet muuttuvat.