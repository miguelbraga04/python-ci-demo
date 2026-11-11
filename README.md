# python-ci-demo
## Asennus ja testaus
#### 1. Kloonaa repository
```bash
git clone https://github.com/miguelbraga04/python-ci-demo.git
cd python-ci-demo
```
#### 2. Luo virtuaaliympäristö
```bash
python3 -m venv .venv
```
#### 3. Aktivoi virtuaaliympäristö
```bash
source .venv/bin/activate
```
#### 4. Päivitä pip
```bash
python -m pip install --upgrade pip
```
#### 5. Asenna riippuvuudet
```bash
pip install -e ".[dev]"
```
#### 6. Suorita testit
```bash
pytest -v
```
#### 7. Suorita linttaus
```bash
ruff check .
```

Jos koodissa ei ole linttausvirheitä, tuloksena on:

```text
All checks passed!
```

# Lisätty error
GitHub Actionsin Lint-vaihe epäonnistui.

Ruffin lokihavainto:
```text
F841 Local variable `unused_variable`
is assigned to but never used.
```

Syy: calculator/operations.py tiedostoon lisätty koodipätkä
```python
def test_error():
    unused_variable = 10
```
Virhe korjattiin poistamalla kyseinen tarpeeton funktio ja käyttämätön muuttuja.


## Projektin sisältö

Projekti sisältää seuraavat laskutoiminnot:

- Yhteenlasku (`add`)
- Vähennyslasku (`subtract`)
- Jakolasku (`divide`)

## Ohjelman käyttö

Laskintoimintoja voi käyttää esimerkiksi Python-tulkissa:

```python
from calculator.operations import add, subtract, divide

print(add(2, 3))
print(subtract(5, 3))
print(divide(10, 2))
```

Tulostus:

```text
5
2
5.0
```

Jakaminen nollalla aiheuttaa `ValueError`-poikkeuksen.

## Testien suorittaminen

Testit kattavat:
- Yhteenlaskun
- Vähennyslaskun
- Jakolaskun
- Nollalla jakamisen virhetilanteen
- Raja-arvotestin, jossa jakajan osoittaja on nolla

Kaikkien testien tulee läpäistä.

## 8. GitHub Actions CI/CD

GitHub Actions käynnistyy automaattisesti seuraavissa tilanteissa:

- `push` main-haaraan
- `pull_request` main-haaraan

CI/CD-putki suorittaa kolme työvaihetta:

1. **Lint:** tarkistaa Python-koodin laadun Ruffilla.
2. **Test:** suorittaa yksikkötestit pytestillä.
3. **Build:** rakentaa Python-paketin ja tallentaa sen GitHub Actions artifactiksi.

Build-vaihe suoritetaan vasta, kun linttaus ja testit ovat onnistuneet.

## Turvallisuusreflektio

Automaattinen testaus ja linttaus parantavat ohjelmiston luotettavuutta ja auttavat havaitsemaan virheitä ennen koodin yhdistämistä päähaaraan.

Branch protection vähentää riskiä, että keskeneräinen tai virheellinen koodi päätyy main-haaraan.

Virtuaaliympäristön käyttö auttaa eristämään projektin riippuvuudet muista Python-projekteista. Salaisuuksia, kuten API-avaimia tai salasanoja, ei pidä tallentaa repositoryyn.

## Kustannusreflektio

Linttaus ja yksikkötestit ovat kevyitä ja niiden suorittaminen vaatii vain vähän laskentaresursseja.

GitHub Actionsin käyttö voi kuitenkin kuluttaa tilin käytettävissä olevia automaatioiden suoritusminuutteja. Lisäksi artifactien tallennus käyttää tallennustilaa.

Tässä projektissa artifactien säilytysajaksi on määritetty seitsemän päivää.
