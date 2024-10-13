# SPF parser

Python skript skontroluje SPF politiku v DNS danej domény a vypisuje zoznam všetkých IP adries, ktoré môžu odosielať e-maily v mene tejto domény.

## Funkcie

- Vyhľadanie SPF záznamu pre danú doménu
- Vyberanie IP adries zo záznamu SPF
- Rekurzívne spracovanie domén, ktoré sú vypísané v zázname SPF
- Zabraňuje opätovnému spracovaniu už navštívených domén

## Prerekvizity

- Python 3.x
- `dnspython` knižnica

Knižnica `dnspython` sa nainštaluje pomocou pip:

```sh
pip install dnspython
