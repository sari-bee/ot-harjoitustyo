# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus auttaa verikeskuksen laboratoriohoitajaa potilaan veriryhmämäärityksen tulkinnassa ja verivalmisteiden veriryhmän valinnassa. Käsitellyt tapaukset tallennetaan esimerkiksi opetustarkoituksiin.

## Käyttäjäroolit

Sovelluksella on vain yksi käyttäjärooli, kirjautuminen tapahtuu käyttäjätunnuksen perusteella.

## Käyttöliittymäluonnos

Sovellus koostuu kolmesta eri näkymästä:

- Kirjautumisnäyttö, jossa käyttäjä syöttää käyttäjätunnuksensa ja voi lisätä uuden käyttäjätunnuksen
![Login](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/login.png)

- Päänäyttö, johon käyttäjä syöttää veriryhmämäärityksen reaktiovoimakkuudet, saa tulkinnan ja voi syöttää kommenteja sekä tallentaa tapauksen tiedot
![Sample](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sample.png)

- Historianäyttö, jossa historiatietoja voi hakea ja selata
![History](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/history.png)

## Toiminnallisuudet

### Kirjautumisnäyttö

- Käyttäjä tunnistautuu syöttämällä käyttäjätunnuksensa
- Jos käyttäjää ei ole olemassa, käyttäjätunnuksen voi lisätä painikkeesta
- Käyttäjätunnuksen tulee olla uniikki
- Käyttäjätunnuksen minimipituus on 3 merkkiä ja kirjainkoko on merkitsevä

### Näytenäyttö

- Käyttäjä syöttää näytetunnisteen, joka yksilöi näytteen
- Kirjainkoko ei ole merkitsevä näytetunnisteessa
- Käyttäjä syöttää veriryhmämäärityksen reaktiovoimakkuudet kenttiin
- Sovellus antaa käyttäjälle tiedon, onko veriryhmämääritys selvä
- Jos veriryhmämääritys on selvä, sovellus antaa veriryhmän tulkinnan
- Jos veriryhmämääritys on epäselvä, sovellus ohjaa käyttäjää tekemään jatkotutkimuksia
- Epäselville veriryhmille kuvataan, missä reaktiossa/reaktioissa epäselvyys on
- Käyttäjälle annetaan ohje verivalmisteiden veriryhmän valinnasta
- Käyttäjä voi syöttää tuloksen yhteyteen kommentteja
- Tallennusaika tallentuu tapauksen tallennuksen yhteydessä
- Tallenna-painikkeella kaikki syötetyt tulokset tallentuvat tiedostoon, joka on paikallisen koneen levyllä
- Tallenna-painikkeella näyte tallentuu kyseisen käyttäjän listalle tiedostoon, joka on paikallisen koneen levyllä
- Tallennus ei onnistu jos näytetunnistetta ei ole annettu
- Tyhjennä-painikkeella päänäytön voi tyhjentää tallentamatta

### Historianäyttö

- Käyttäjä voi selata kaikkia talletettuja tapauksia uusimmasta vanhimpaan
- Käyttäjä voi hakea itse tallettamansa tapaukset uusimmasta vanhimpaan
- Käyttäjä voi hakea yksittäistä tapausta näytetunnisteen perusteella
- Haettavan näytetunnisteen tulee olla täsmällinen (mutta kirjainkoko ei ole merkitsevä)

### Yleiset vaatimukset

- Sovellus toimii Linux- ja OSX-käyttöjärjestelmissä
- Käyttäjän kirjautuessa sisään kirjautumisnäyttö lukkiutuu
- Käyttäjä kirjautuu ulos sulkemalla sovelluksen
- Tallennustiedostojen polkuja, hyväksyttäviä reaktiovoimakkuuksia sekä verensiirto-ohjeita voidaan konfiguroida

## Poikkeamat alkuperäisestä vaatimusmäärittelystä

Sovellukseen ei tässä vaiheessa tullut suosituksia jatkotutkimuksista eikä jatkotutkimusnäyttöä, johon olisi voinut syöttää jatkotutkimusten tuloksia. Tämä jää jatkokehitysehdotukseksi, jollaisena se olikin vaatimusmäärittelyssä mainittu.

Alkuperäisessä vaatimusmäärittelyssä mainittiin, että käyttäjätunnuksen voisi valita listalta kirjautumisnäytössä. Totesin tämän vaihtoehdon kuitenkin epäkäytännölliseksi tilanteessa, jossa käyttäjiä on monia. Lisäksi tässä olisi suurempi riski, että käyttäjä valitsee virheellisen käyttäjätunnuksen. Tästä syystä toteutin käyttäjätunnuksen syöttämisen tavallisena tekstinsyöttönä.

Lisäksi alkuperäisessä vaatimusmäärittelyssä mainittiin, että tapauksia voisi hakea käyttäjätunnuksen perusteella. Totesin kuitenkin, että käyttäjätunnus ei ole relevantti missään muussa yhteydessä kuin silloin, kun käyttäjä hakee itse tallettamiaan näytteitä. Tästä syystä en toteuttanut tätä hakua vaan suoraan käyttäjän omien tapausten haun.
