# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus auttaa verikeskuksen laboratoriohoitajaa potilaan veriryhmämäärityksen tulkinnassa ja mahdollisten jatkotutkimusten valinnassa. Käsitellyt tapaukset voidaan tallentaa esimerkiksi opetustarkoituksiin.

## Käyttäjäroolit

Sovelluksella on vain yksi käyttäjärooli, kirjautuminen tapahtuu nimen perusteella.

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

- Käyttäjä voi tunnistautua valikosta löytyvän käyttäjänimen perusteella (tehty vko 6, tosin toteutettu hieman eri tavalla)
- Jos käyttäjää ei löydy valikosta, käyttäjänimen voi lisätä painikkeesta (tehty vko 6)
- Käyttäjänimen tulee olla uniikki (tehty vko 6)

### Päänäyttö

- Käyttäjä syöttää veriryhmämäärityksen reaktiovoimakkuudet kenttiin (tehty)
- Sovellus antaa käyttäjälle tiedon, onko veriryhmämääritys selvä (tehty)
- Jos veriryhmämääritys on selvä, sovellus antaa veriryhmän tulkinnan (tehty)
- Jos veriryhmämääritys on epäselvä, sovellus ohjaa käyttäjää tekemään jatkotutkimuksia (tehty)
- Käyttäjä voi syöttää näytenumeron, joka yksilöi näytteen (tehty)
- Käyttäjä voi syöttää tuloksen yhteyteen kommentteja (tehty)
- Käyttäjän nimi tallentuu hänen syöttämiensä tapausten yhteyteen
- Tallennusaika tallentuu tapauksen tallennuksen yhteydessä (tehty)
- Tallenna-painikkeella kaikki syötetyt tulokset tallentuvat tiedostoon, joka on paikallisen koneen levyllä (tehty)
- Tallennus ei onnistu jos näytenumeroa ei ole annettu (tehty)
- Tyhjennä-painikkeella päänäytön voi tyhjentää tallentamatta (tehty)

### Yleiset vaatimukset

- Sovelluksen tulee toimia Linux- ja OSX-käyttöjärjestelmissä (tehty)
- Käyttäjä kirjautuu ulos sulkemalla sovelluksen (tehty vko 6)

## Jatkokehitysideat

### Päänäyttö

- Epäselville veriryhmille kuvataan, missä reaktiossa/reaktioissa epäselvyys on (tehty)
- Epäselville veriryhmille annetaan tarkempia jatkotutkimusehdotuksia epäselvyyden tyypin mukaan

### Historianäyttö

- Historianäytössä käyttäjä voi selata kaikkia talletettuja tapauksia (tehty)
- Käyttäjä voi hakea aiempia tapauksia käyttäjänimen tai näytenumeron perusteella (tehty vko 6)

### Jatkotutkimusnäyttö

- Jatkotutkimusnäytössä näytetään täytettäviä kenttiä suositeltujen jatkotutkimusten perusteella
- Jatkotutkimusnäyttöön syötetyt tulokset tallentuvat näytteen muiden tietojen yhteyteen
