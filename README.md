# Veriryhmäapuri

Sovelluksen tarkoituksena on toimia tukena veriryhmämäärityksen tulkinnassa, jatkotutkimusten tarpeen arvioinnissa ja potilaan verivalmisteiden valinnassa. Käyttäjä syöttää sovellukseen veriryhmämäärityksen raakatulokset ja saa tulkinnan tuloksille. Syötetyt näytteet tallentuvat tiedostoon, josta niitä voi käyttää esimerkiksi opetustarkoituksiin.

[Release](https://github.com/sari-bee/ot-harjoitustyo/releases)

## Python-versio

Sovellus on tarkoitettu käytettäväksi Python-versiolla 3.8 tai korkeampi.

## Dokumentaatio

[Käyttöohje](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausraportti](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/testausraportti.md)

[Työaikakirjanpito](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus ja käynnistys

Asenna riippuvuudet komennolla

```bash
poetry install
```

Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

## Komentorivitoiminnot

Aja testit:

```bash
poetry run invoke test
```

Aja testit ja tuota testikattavuusraportti:

```bash
poetry run invoke coverage-report
```

Suorita Pylint-tarkistukset:

```bash
poetry run invoke lint
```

## Mahdollisia testitapauksia

Testitapausten tulkinta olettaa, ettei konfiguraatiotiedostossa ole tehty muutoksia hyväksyttäviin reaktiovoimakkuuksiin.

Näytetunnisteeksi voit antaa minkä vain uniikin merkkijonon.

Selvä veriryhmä A RhD neg: Anti-A 4, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 4

Ei-hyväksyttävä reaktiovoimakkuus Anti-A:lla: Anti-A 2, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 4

ABO-logiikka ei toteudu: Anti-A 4, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 0
