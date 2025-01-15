Grund struktur
```
project/
├── app/
│   ├── static/         # Für statische Dateien (CSS, JS, Bilder)
│   ├── templates/      # Für HTML-Vorlagen (Jinja2)
│   ├── __init__.py     # Initialisiert die Flask-App
│   ├── routes.py       # Definiert die Routen (Endpoints)
│   ├── models.py       # (Optional) Datenbankmodelle
│   └── forms.py        # (Optional) Formulare mit WTForms
├── config.py           # Konfigurationsdatei für Flask
├── run.py              # Startpunkt der Anwendung
└── requirements.txt    # Liste der Python-Abhängigkeiten
```
