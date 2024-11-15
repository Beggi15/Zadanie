# Projekt HTML Artykułu

## Opis projektu

Projekt umożliwia:
- **Automatyczne generowanie HTML na podstawie artykułu**: Skrypt przetwarza tekst dostarczony w pliku `artykul.txt` i generuje HTML z odpowiednią strukturą oraz obrazami z kontekstowymi opisami.
- **Szablon HTML**: Plik `szablon.html` to pusty szablon HTML gotowy do ręcznego wstawiania treści artykułów.
- **Podgląd artykułu**: Plik `podglad.html` zawiera pełną wizualizację artykułu z odpowiednią stylizacją i obrazami.

## Struktura projektu

- **`generate_html.py`**: Główny skrypt do przetwarzania artykułu i generowania HTML.
- **`artykul.txt`**: Plik wejściowy z treścią artykułu do przetworzenia.
- **`szablon.html`**: Pusty szablon HTML gotowy do wstawienia treści.
- **`podglad.html`**: Plik z wygenerowanym artykułem w HTML.

---

## Wymagania

1. **Python 3.7 lub nowszy**.
2. Biblioteki Python:
   - `openai`
   - `python-dotenv`
3. Konto OpenAI z aktywnym kluczem API.

---

## Jak działa aplikacja?

### Generowanie HTML
Skrypt `generate_html.py` wykonuje następujące kroki:
1. Wczytuje tekst z pliku `artykul.txt`.
2. Dzieli długi tekst na fragmenty, aby zmieścić się w limitach API OpenAI.
3. Wysyła fragmenty tekstu do OpenAI API, które generuje odpowiednią strukturę HTML:
   - Wstawia tagi `<h1>`, `<p>`, `<img>` i `<figcaption>`.
   - Generuje atrybuty `alt` w `<img>`, zawierające kontekstowe opisy nawiązujące do tekstu.
4. Łączy wygenerowane fragmenty i zapisuje wynik w pliku `artykul.html`.

---

## Instrukcja uruchomienia

### 1. Pobierz i zainstaluj Python

1. Sprawdź, czy Python jest zainstalowany:

2. Otwórz terminal (Linux/macOS) lub Wiersz Poleceń (Windows).
Wpisz:

 python --version

3. Jeśli Python jest zainstalowany, zobaczysz jego wersję (wymagana 3.7 lub nowsza).
4. Jeśli Python nie jest zainstalowany:

5. Pobierz Pythona z https://www.python.org/downloads/.
6. Podczas instalacji upewnij się, że zaznaczyłeś opcję „Add Python to PATH”.

### 2. Pobierz projekt

1. Otwórz przeglądarkę i przejdź do repozytorium projektu na GitHubie.
2. Kliknij przycisk Code i wybierz Download ZIP.
3. Wypakuj pobrany plik ZIP do folderu na komputerze.

### 3. Zainstaluj wymagane biblioteki
1. Otwórz terminal w folderze projektu:

2. Przejdź do folderu, gdzie wypakowałeś pliki projektu.

np. cd C:\ścieżka\do\projektu

3. W terminalu wpisz:

pip install openai python-dotenv

### 4. Uruchomienie aplikacji
1. Uruchom skrypt, w terminalu wpisz:

python generate_html.py


