# Küçük boyutlu Python imajı kullanılır
FROM python:3.10-slim

# Çalışma dizini
WORKDIR /app

# Kodları kopyala
COPY . .

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı başlat
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
