# Ohjelmistotekniikan harjoitustyö: Veriryhmäapuri

Sovelluksen tarkoituksena on toimia tukena veriryhmämäärityksen tulkinnassa, jatkotutkimusten tarpeen arvioinnissa ja potilaan verivalmisteiden valinnassa. Käyttäjä syöttää sovellukseen veriryhmämäärityksen raakatulokset ja saa tulkinnan tuloksille.

[Release](https://github.com/sari-bee/ot-harjoitustyo/releases)

## Python-versio

Sovellus on tarkoitettu käytettäväksi Python-versiolla 3.8 tai korkeampi.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus ja komentorivikäskyt

Asenna riippuvuudet komennolla

```bash
poetry install
```

Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

Aja testit ja tuota testikattavuusraportti komennolla

```bash
poetry run invoke coverage-report
```

Pelkät testit voit ajaa komennolla

```bash
poetry run invoke test
```

Pylint-tarkistukset voit suorittaa komennolla
```bash
poetry run invoke lint
```

## Mahdollisia testitapauksia

Näytetunnisteeksi voit antaa minkä vain uniikin merkkijonon.

Selvä veriryhmä A RhD neg: Anti-A 4, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 4

Ei-hyväksyttävä reaktiovoimakkuus Anti-A:lla: Anti-A 2, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 4

ABO-logiikka ei toteudu: Anti-A 4, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 0
