<<<<<<< HEAD
# Projects Portfolio

Welcome to the Projects Portfolio! This README serves as a directory to navigate through the various projects included in this repository. Click on the links below to explore each project.

## Projects

- [Bankomat Threads](./fatigue_detector/BankomatThreads1/README.md): A simulation of ATM operations using threads.
- [Database Portfolio](./fatigue_detector/DatabazePortfolio-D1/README.md): A database management system with various features.
- [P2P Project](./fatigue_detector/P2P_Project/README.md): A peer-to-peer communication system.

Feel free to explore the projects and their documentation for more details.
=======
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
>>>>>>> origin/main
