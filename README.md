# 🐍 Python Oefeningen – Student Handleiding

Welkom bij de Python-oefeningen! 🎉  
In deze repository vind je oefeningen en een **student-friendly test-systeem** waarmee je direct kan zien of jouw code correct is.

---

## 📦 1. Installatie

### Stap 1.1 – Clone of fork de repository

#### **Aanbevolen: Fork workflow**
1. Ga naar de GitHub pagina van deze repository.
2. Klik op **Fork** (rechtsboven) om een kopie naar je eigen account te maken.
3. Clone jouw fork naar je computer:

bash
git clone https://github.com/DhrLeroy/Python---oefeningen.git
cd Python---oefeningen

### Stap 1.2 – Maak een virtuele omgeving (aanbevolen)

bash
python -m venv venv

venv\Scripts\activate


### Stap 1.3 – Installeer vereisten
bash
pip install -r requirements.txt



## Stap 2 - Maak oefeningen
Oefeningen staat in de map 'oefeningen'


## Stap 3 - Test jouw oplossing
bash
python tests/run_tests.py


## Stap 4 - Nieuwe oefeningen en oplossingen binnenhalen

### Stap 4.1 - Voeg upstream toe
bash
git remote add upstream https://github.com/DhrLeroy/Python---oefeningen.git
git fetch upstream
git merge upstream/main

### Stap 4.2 - Update project
bash
git pull upstream main

