# Matikkapeli

Sovelluksen tarkoituksena on luoda kokonaisuuksia, jotka sisältävät matemaattisia haasteita eli niin sanottuja pieniä matikkapelejä. Peli sisältää useamman matemaattisen kysymyksen, joihin käyttäjän tulee vastata oikealla vastauksella. Oikeasta vastauksesta saa aina yhden pisteen. Alkuun luodaan ainakin kaksi valmista peliä, toinen helpoille ja toinen vaikeille laskutoimituksille. Kun käyttäjä on pelannut pelin, näkee hän tämän jälkeen saamansa tuloksen. Käyttäjä voi myös missä tahansa kohtaa keskeyttää pelin pelaamisen, mutta pisteet määräytyvät ainoastaan saatujen oikeiden vastausten mukaan. Tuloksista pidetään tulostaulua, johon pääsee noin 10 parhaiten suoriutunutta käyttäjää. Tulokset peleistä näkyvät jokaisella pelisivulla erikseen. Käyttäjä voi myös halutessaan lisätä peleistä arvioita muiden nähtäväksi. 


## Käyttäjän luonti ja sisäänkirjautuminen
Ensin tulee luoda tunnus ja tälle salasana sekä valita missä roolissa ohjelmaa käytetään, käyttäjänä vai ylläpitäjänä. Esimerkiksi oppilas on käyttäjä ja opettaja taas ylläpitäjä.
Onnistuneen käyttäjätunnuksen luomisen jälkeen henkilö voi kirjautua sisään (tai automaattinen sisäänkirjaus).
Mikäli käyttäjätunnus on varattu, tästä nousee käyttäjälle ilmoitus.

## Käyttäjäroolit
### Käyttäjä
- Sisäänkirjautumisen jälkeen oikeus pelata pelejä sekä lisätä näistä arvioita.
- Näkee jokaisen kokonaisuuden sivulta omat pelikerrat ja oman parhaimman tuloksen. Näkee jokaisen pelin omalta sivulta myös top 10 -tulostaulun ja käyttäjien antamat arviot.
- Pystyy kirjautumaan ulos.

### Ylläpitäjä
- Sisäänkirjautumisen jälkeen ylläpitäjä voi pelata pelejä, mutta näiden tulokset eivät lisäänny tulostauluun. Omat tilastot toimivat samalla tavalla kuin käyttäjän roolissakin. Näkee myös jokaiselta pelisivulta top 10 -tulostaulun ja arviot. Ylläpitäjällä on oikeus lisätä arvioita.  
- Oikeus tehdä uusia pelejä. Ko. pelin luonut ylläpitäjä voi myös halutessaan poistaa tämän itse tekemänsä pelin.
- Näkee tilastotaulun tekemistään peleistä. Tässä tilastotaulussa on listattuna kaikki kyseistä peliä pelanneet käyttäjät ja heidän pisteet.
- Pystyy kirjautumaan ulos.

## Pelin toiminnot
- Yhteen peliin saa luotua niin monta kysymystä kuin ylläpitäjä haluaa, mutta tietokannasta arvotaan aina peliä pelatessa tietty määrä kysymyksiä esimerkiksi 10-15 kysymystä peliä kohden, jotta kysymykset eivät välttämättä olisi jokaisella kerralla samat.

## Projektin nykystatus
Pelissä onnistuu vasta käyttäjän luonti ja sisäänkirjautuminen. Käyttäjätietokanta luotu. HUOM. Virheiden annot puuttuvat! 

Sovellus on todella pahasti keskeneräinen. Alun haasteiden ja koko sovelluksen toimivuudessa hieman kesti.

Matikkapelin Heroku-sivulle pääsee [tästä](https://tsoha-kavijat.herokuapp.com/).

Web-sovelluksen teko on osa Helsingin yliopiston Tietojenkäsittelytieteen Tietokantasovellus-harjoitustyö -kurssia.
