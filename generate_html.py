import openai
import os

# Klucz API OpenAI (zmień na własny klucz)
openai.api_key = "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"

# Funkcja do wczytania artykułu z pliku
def read_article(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print("[INFO] Plik został poprawnie wczytany.")
        return content
    except FileNotFoundError:
        print(f"[ERROR] Nie znaleziono pliku: {file_path}")
        return None
    except Exception as e:
        print(f"[ERROR] Wystąpił błąd przy wczytywaniu pliku: {e}")
        return None

# Funkcja dzieląca tekst na fragmenty o ograniczonej liczbie znaków
def split_text(text, max_length=2000):
    paragraphs = text.split("\n")
    chunks = []
    current_chunk = ""
    
    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) + 1 > max_length:
            chunks.append(current_chunk.strip())
            current_chunk = ""
        current_chunk += paragraph + "\n"
    
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    
    return chunks

# Funkcja generująca HTML z kontekstowymi promptami w sekcjach alt
def generate_html(article_text):
    prompt = (
        "Convert the following article text into structured HTML content suitable for placing between <body> and </body> tags. "
        "Identify suitable locations for images based on the content and insert <img> tags with src='image_placeholder.jpg'. "
        "Each <img> tag must include an alt attribute containing a detailed and precise prompt that describes the image "
        "based on the context of the surrounding text. These prompts should be clear, specific, and usable to generate AI images. "
        "For example, if the text describes a sunset over the ocean, the alt should say: 'A vivid sunset over a calm ocean with orange and purple hues in the sky.' "
        "Add captions under each image using the <figcaption> tag, if appropriate. Ensure no CSS, JavaScript, or extra tags like <html> or <head> are included.\n\n"
        f"Article Text:\n{article_text}"
    )
    try:
        print("[INFO] Wywołanie API OpenAI...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant generating HTML based on article text."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        html_content = response['choices'][0]['message']['content']
        print("[INFO] Pomyślnie wygenerowano HTML z kontekstowymi promptami w alt.")
        return html_content.strip()
    except Exception as e:
        print(f"[ERROR] Wystąpił błąd podczas wywołania API: {e}")
        return None

# Funkcja zapisu pliku HTML
def save_html(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"[INFO] HTML został zapisany w pliku: {file_path}")
    except Exception as e:
        print(f"[ERROR] Nie udało się zapisać pliku HTML: {e}")

# Ścieżki względne do plików
input_file_path = "artykul.txt"   # Plik z treścią artykułu
output_file_path = "artykul.html" # Wygenerowany plik HTML

# Ścieżka do folderu projektu (bieżący folder)
project_dir = os.getcwd()
input_full_path = os.path.join(project_dir, input_file_path)
output_full_path = os.path.join(project_dir, output_file_path)

if __name__ == "__main__":
    # Wczytaj artykuł
    print("[INFO] Wczytywanie artykułu...")
    article_text = read_article(input_full_path)

    if article_text:
        # Podziel tekst na fragmenty
        chunks = split_text(article_text, max_length=2000)
        full_html_content = ""

        # Przetwarzaj każdy fragment oddzielnie
        for i, chunk in enumerate(chunks):
            print(f"[INFO] Generowanie HTML dla fragmentu {i + 1}/{len(chunks)}")
            chunk_html = generate_html(chunk)
            if chunk_html:
                full_html_content += chunk_html + "\n"
            else:
                print(f"[ERROR] Nie udało się wygenerować HTML dla fragmentu {i + 1}")
                break

        if full_html_content.strip():
            # Zapisz wynikowy HTML
            save_html(output_full_path, full_html_content)
            print("[INFO] Plik artykul.html został pomyślnie wygenerowany.")
        else:
            print("[ERROR] Nie udało się wygenerować pliku HTML.")
    else:
        print("[ERROR] Nie udało się wczytać artykułu.")
