# Schulprotal in gut

## Description

Das schulportal sieht momentan einfach scheisse auss also machen wir es besser.
wenn du selbst eine Version hosten wilst der kramm den du brauchst ist in requirements.txt

## Grund struktur
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
├── README.md           # Redme file
├── run.py              # Startpunkt der Anwendung
└── requirements.txt    # Liste der Python-Abhängigkeiten
```
