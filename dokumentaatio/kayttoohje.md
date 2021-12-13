# Veriryhmäapurin käyttöohje

## Sovelluksen käynnistäminen

Asenna riippuvuudet komennolla
´´´bash
poetry install
´´´

Ja käynnistä sovellus komennolla
´´´bash
poetry run invoke start
´´´

## Kirjautuminen

Sovellus avautuu kirjautumisikkunaan.

![Login](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/login.png)

Voit kirjautua sisään olemassaolevalla käyttäjätunnuksella antamalla tunnuksen "Syötä käyttäjätunnus"-kenttään ja painamalla Kirjaudu sisään. Huomioi, että tunnuksessa isot ja pienet kirjaimet ovat merkitseviä.

Tarvittaessa tee uusi käyttäjätunnus syöttämällä se "Lisää uusi käyttäjätunnus"-kenttään ja painamalla Lisää!. Kirjaudu sitten sisään.

## Näytteen tietojen syöttäminen

Sisäänkirjautumisen jälkeen olet näytteen tietojen syöttöikkunassa.

![Sample](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sample.png)

Syötä sen näytteen näytetunniste, jota haluat käsitellä. Näytetunniste on pakollinen tieto. Syötä reaktiovoimakkuudet numeroilla 0-4 tai kaksoispopulaatio kirjoittamalla DP. Halutessasi lisää kommentti. Paina sen jälkeen Tarkista. Näet näytön alalaidassa antamasi näytetunnisteen, tulosten tulkinnan sekä mahdollisesti syöttämäsi kommentin. Näytteen tiedot tallentuvat automaattisesti tietokantaan. Halutessasi voit tyhjentää kentät tarkistamatta ja tallentamatta tietoja painamalla Tyhjennä kentät.

### Testitapauksia

Mahdollisia testitapauksia ovat mm.
- Selvä veriryhmä A RhD neg: Anti-A 4, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 4
- Ei-hyväksyttävä reaktiovoimakkuus Anti-A:lla: Anti-A 2, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 4
- ABO-logiikka ei toteudu: Anti-A 4, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 0

## Näytehistoria

Näytehistoria-painikkeesta pääset ikkunaan, jossa voit hakea tallennettuja näytteitä eri hakuehdoilla.

![History](https://github.com/sari-bee/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/history.png)

Antamalla haluamasi näytteen näytetunnisteen ja painamalla Etsi näytetunnisteella näet yksittäisen näytteen tiedot ja tulkinnan. Tallentamasi näytteet -painikkeella näet itse syöttämäsi näytteet ja Selaa kaikkia näytteitä -painikkeella kaikki tälle koneelle tallennetut näytteet aikajärjestyksessä tuoreimmasta vanhimpaan. Voit siirtyä aiempiin tai myöhempiin näytteisiin näytön alalaidan painikkeista Aiemmat näytteet ja Myöhemmät näytteet.

## Uloskirjautuminen

Kirjaudu ulos sulkemalla sovellus. Jos haluat kirjautua toisena käyttäjänä, käynnistä sovellus uudestaan.