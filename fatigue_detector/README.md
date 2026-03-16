<<<<<<< HEAD
# PC Fatigue Detector 1.0

Projekt: Detektor únavy u počítače na základě chování uživatele.

## Rychlý start

1. Nainstaluj závislosti:
```bash
pip install -r requirements.txt
```

2. Spusť GUI:
```bash
python main.py
```

Nebo klikni 2x na `run.bat`

## Struktura projektu

```
fatigue_detector/
├── main.py                  # GUI aplikace (tkinter)
├── data_collector.py        # Sbírač dat (keyboard + CPU monitoring)
├── fatigue_data.csv         # Tvá reálná data (sample)
├── requirements.txt         # Závislosti
├── run.bat                  # Windows launcher
├── README.md
├── data/
│   └── fatigue_model.pkl    # Exportovaný ML model (z Colab)
└── docs/
    ├── colab_fatigue.ipynb  # Colab notebook (training)
    └── data_collection.md   # Dokumentace
```

## Atributy dat

- **typing_speed**: Znaky za minutu (pynput)
- **errors**: Backspace/Delete za minutu
- **pause_duration**: Nejdelší pauza mezi stisky (sekundy)
- **cpu_percent**: Zátěž procesoru
- **hour**: Hodina dne (0-23)
- **fatigue_level**: 0=OK, 1=Střední, 2=Vysoká

## Jak to funguje

1. `data_collector.py` zbírá data na pozadí → `fatigue_data.csv`
2. Colab notebook trénuje RandomForest/XGBoost → `fatigue_model.pkl`
3. GUI (`main.py`) načte model a predikuje únavu každých 5 minut
4. Alert (popup) při předpovědi vysoké únavy (>70%)

## Demo

```powershell
# Sbírač dat (10 sekund test)
python data_collector.py

# GUI
python main.py
```

---

**Vytvořeno jako školní projekt (obhajouba).**
=======
# Projects Portfolio

Vítejte v mém portfoliu projektů! Zde najdete různé aplikace a projekty vytvořené během studia.

## 📁 Projekty

### 🎓 DatabazePortfolio-D1
**Popis:** Webová aplikace pro správu knihovny využívající DAO pattern a MySQL databázi.

**Technologie:** Python Flask, MySQL, HTML/CSS

**Funkce:**
- Správa knih, autorů, studentů a výpůjček
- Transakce při vytváření výpůjček
- Generování reportů s agregovanými daty
- Import dat z CSV souborů
- Ošetření chyb a validace

**Spuštění:** [Přečtěte si instrukce](./DatabazePortfolio-D1/README.md)

---

### 🔧 Jak spustit projekty
Každý projekt má svůj vlastní README s detailními instrukcemi pro instalaci a spuštění.

### 📋 Požadavky
- Python 3.8+
- Příslušné databázové servery (MySQL, atd.)
- Potřebné závislosti (viz requirements.txt v jednotlivých projektech)

---
*Poslední aktualizace: 12. ledna 2026*
>>>>>>> efe3c41a45e37b0463e0c6bb62a6712e3aa88e99
