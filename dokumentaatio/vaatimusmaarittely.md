# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus auttaa verikeskuksen laboratoriohoitajaa potilaan veriryhmämäärityksen tulkinnassa ja mahdollisten jatkotutkimusten valinnassa. Käsitellyt tapaukset voidaan tallentaa esimerkiksi opetustarkoituksiin.

## Käyttäjäroolit

Sovelluksella on vain yksi käyttäjätyyppi, kirjautuminen tapahtuu nimen perusteella.

## Käyttöliittymäluonnos

Sovellus koostuu neljästä eri näkymästä:
- Alkunäyttö, jossa käyttäjä valitsee nimensä
- Päänäyttö, johon käyttäjä syöttää veriryhmämäärityksen reaktiovoimakkuudet, saa tulkinnan ja voi syöttää kommenteja sekä tallentaa tapauksen tiedot
- Jatkotutkimusnäyttö, johon käyttäjä voi syöttää suositeltujen jatkotutkimusten tuloksia
- Historianäyttö, jossa historiatietoja voi hakea ja selata

![Käyttöliittymäluonnos](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/UI.jpg)

Esitetty käyttöliittymäluonnos sisältää myös jatkokehitysideoissa mainittuja toiminnallisuuksia.

## Perusversion toiminnallisuudet

### Alkunäyttö

- Käyttäjä voi luoda itselleen käyttäjäroolin nimen perusteella
- Käyttäjäroolin nimen tulee olla uniikki
- Ohjelman avautuessa käyttäjä valitsee käyttäjäroolinsa nimellä valikosta

### Päänäyttö

- Käyttäjä syöttää veriryhmämäärityksen reaktiovoimakkuudet kenttiin
- Sovellus antaa käyttäjälle tiedon, onko veriryhmämääritys selvä
- Jos veriryhmämääritys on selvä, sovellus antaa veriryhmän tulkinnan
- Jos veriryhmämääritys on epäselvä, sovellus ohjaa käyttäjää tekemään jatkotutkimuksia
- Käyttäjä voi syöttää näytenumeron, joka yksilöi näytteen
- Käyttäjä voi syöttää tuloksen yhteyteen kommentteja
- Käyttäjän nimi tallentuu hänen syöttämiensä tapausten yhteyteen
- Tallennusaika tallentuu tapauksen tallennuksen yhteydessä
- Tallenna-painikkeella kaikki syötetyt tulokset tallentuvat tiedostoon, joka on paikallisen koneen levyllä
- Tallennus ei onnistu jos näytenumero-kenttä on tyhjä
- Tyhjennä-painikkeella päänäytön voi tyhjentää tallentamatta

### Yleiset vaatimukset

- Sovelluksen tulee toimia Linux- ja OSX-käyttöjärjestelmissä
- Käyttäjä kirjautuu ulos sulkemalla sovelluksen

## Jatkokehitysideat

### Päänäyttö

- Epäselville veriryhmille kuvataan, missä reaktiossa/reaktioissa epäselvyys on
- Epäselville veriryhmille annetaan tarkempia jatkotutkimusehdotuksia epäselvyyden tyypin mukaan

### Historianäyttö

- Historianäytössä käyttäjä voi selata kaikkia talletettuja tapauksia
- Käyttäjä voi hakea aiempia tapauksia käyttäjänimen tai näytenumeron perusteella

### Jatkotutkimusnäyttö

- Jatkotutkimusnäytössä näytetään täytettäviä kenttiä suositeltujen jatkotutkimusten perusteella
- Jatkotutkimusnäyttöön syötetyt tulokset tallentuvat näytteen muiden tietojen yhteyteen
