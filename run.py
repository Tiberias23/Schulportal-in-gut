from app import create_app

app = create_app()

# Starten der Anwendung
if __name__ == '__main__':
    app.run(debug=True)  # Debug-Modus aktivieren
