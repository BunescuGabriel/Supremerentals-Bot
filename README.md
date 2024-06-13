# Telegram Bot - Supreme Rentals

## Descriere
Acest bot Telegram, numit "Supreme Rentals", furnizează informații despre serviciile și flota de mașini disponibile la agenția de Închirieri Auto Supreme Rentals din Republica Moldova.

## Funcționalități
- **Meniu Principal**: Utilizatorii pot accesa meniul principal al botului prin comanda `/start` sau `/menu`, unde pot alege între opțiunile disponibile.
- **Despre Noi**: Oferă informații despre agenția Supreme Rentals și viziunea, valorile și serviciile sale.
- **Termeni și Condiții**: Utilizatorii pot accesa termenii și condițiile agenției Supreme Rentals.
- **Servicii Prestate**: Afișează serviciile prestate de agenție și detaliile acestora.
- **Flota de Mașini**: Utilizatorii pot explora flota de mașini disponibile pentru închiriere, cu opțiunea de a naviga prin pagini.

## Cum să Folosești
1. Porniți botul folosind comanda `/start` sau `/menu`.
2. Alegeți una dintre opțiunile disponibile pentru a obține informații specifice.

## Tehnologii Folosite
- [Python](https://www.python.org/): Limbajul de programare utilizat pentru dezvoltarea botului.
- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI): Bibliotecă Python pentru dezvoltarea de boturi Telegram.

## Cum să Rulezi Botul
1. Clonați acest repository.
2. Instalați dependențele folosind 
```bash
pip install -r requirements.txt`
```
3. Obțineți token-ul botului de la [BotFather](https://t.me/BotFather) și înlocuiți `token_bot` cu token-ul primit.
4. Rulați fișierul `main.py`.


# Utilizarea SQLite cu Python - Telegram Bot

Verificarea Existentei Tabelului în baza de date SQLite.
```python
import sqlite3
conn = sqlite3.connect('exemplu.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='about_servici';")
table_exists = cursor.fetchone()
```
## Funcționalități

### Adăugarea unui Serviciu
Pentru a adăuga un serviciu nou în baza de date, folosește comanda `/add` în chat-ul cu botul și urmează instrucțiunile pentru a introduce numele noului serviciu.

```bash
/add serviciu_nou
```
Sau a doua varianta, este introducerea `/add`, și deja în mesaj nou vom introduce `serviciu_nou`.
### Obținerea Listei de Servicii
Pentru a afișa lista completă a serviciilor prestate de Supreme 
Rentals, poți accesa comanda "Servicii Prestate" din meniul principal
al botului. Aceasta va afișa o listă detaliată a tuturor serviciilor disponibile.