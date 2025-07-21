# 🤖 Raspberry Pi 5 LLM Chatbot

Bu proje, **Raspberry Pi 5** üzerinde çalışan, web tabanlı, konteynerize edilmiş bir **LLM (TinyLlama)** tabanlı sohbet uygulamasıdır. Arayüzü modern bir UI kit ile geliştirilmiş, arka planda Python ile yazılmış bir API çalışmaktadır. Proje, düşük güçlü donanımlarda büyük dil modelleriyle sohbet uygulamaları geliştirmek için örnek bir altyapı sunar.

---

## 📌 Teknoloji Yığını

| Bileşen              | Teknoloji                              	     |
|----------------------|-----------------------------------------------|
| 🧠 LLM Modeli       | [TinyLlama](https://huggingface.co/TinyLlama) |
| 💻 Cihaz            | Raspberry Pi 5                                |
| 🐧 İşletim Sistemi  | Raspberry Pi OS (Debian tabanlı)              |
| 🔧 Backend          | Python + Uvicorn (FastAPI ile)                |
| 🧪 API Test         | Postman                                       |
| 📦 Containerization | Docker                                        |
| 💻 Frontend         | React                                         |
| 🎨 UI               | Tailwind CSS + Shadcn                         |
| 🔒 Güvenlik         | Let’s Encrypt + Certbot + Cloudflare          |
| 📜 Logging          | Grafana Loki                                  |
| 🌐 Versiyon Kontrol | Git + GitHub                                  |
| 🗂️ Proje Yönetimi   | Jira                                          |


## 📁 Proje Yapısı
```
raspi-llm-chatbot/
│
├── backend/
│ ├── app/
│ │ ├── main.py 		# FastAPI ile tanımlı endpoint'ler
│ │ ├── llm_handler.py		# TinyLlama modeliyle etkileşim
│ │ └── utils.py 			# Yardımcı fonksiyonlar
│ ├── requirements.txt 		# Python bağımlılıkları
│ └── Dockerfile 			# Backend container'ı
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── App.tsx 		# React ana bileşen
│ │ ├── components/ 		# Chat UI bileşenleri (Shadcn)
│ │ └── services/ 		# API istekleri
│ ├── tailwind.config.js
│ └── Dockerfile 			# Frontend container'ı
│
├── nginx/
│ ├── default.conf 		# Reverse proxy ayarları
│ └── certbot/ 			# SSL dosyaları
│
├── docker-compose.yml 	# Tüm servisi ayağa kaldırır
├── .env 				# Ortam değişkenleri
├── README.md 			# Bu dosya
└── LICENSE
```

## 🚀 Kurulum
> **Not:** Proje Raspberry Pi 5 üzerinde test edilmemiştir.
1. Gerekli yazılımlar:
   - Docker
   - Docker Compose
   - Git
   - Python 3.9+

2. Reponun klonlanması:
```
    git clone https://github.com/kullaniciadi/raspi-llm-chatbot.git
    cd raspi-llm-chatbot
```
3.	Ortam değişkenlerini .env dosyasına yazın:
```
   	API_URL=http://localhost:8000
   	MODEL_NAME=tinyllama/TinyLlama-1.1B-Chat-v1.0
```
4.	Docker container'larını başlatın:
```
	  docker-compose up --build
```
5.	Arayüzü tarayıcıda açın:
```
	  http://<raspberrypi-local-ip>
```
🧠 TinyLlama Modeli
Projede kullanılan model: TinyLlama-1.1B-Chat
Seçim nedenleri:
•	Raspberry Pi gibi sınırlı donanımda çalışabilecek küçük yapıda olması
•	Chat için optimize edilmiş olması
•	Hugging Face Transformers ile kolay entegrasyon
Model, ilk çalıştırmada otomatik olarak indirilecektir. Dilerseniz modeli önceden indirerek llm_handler.py dosyasındaki AutoModelForCausalLM.from_pretrained() fonksiyonunda path olarak gösterebilirsiniz.
________________________________________
🖼️ Chat Arayüzü
UI şu bileşenleri kullanır:
•	React: Modern web uygulama çatısı
•	Tailwind CSS: Stil oluşturma
•	Shadcn UI: Chat arayüz bileşenleri (chat bubble, input, dark mode vs.)
Chat arayüzü kullanıcı mesajını backend’e gönderir ve TinyLlama yanıtını ekrana yansıtır.
________________________________________
🔒 Güvenlik
•	HTTPS kurulumu için Let's Encrypt + Certbot yapılandırılmıştır.
•	Cloudflare üzerinden DNS ve DDoS koruması entegredir.
•	nginx reverse proxy SSL trafiğini yönlendirir.
________________________________________
📈 Gözlem ve Loglama
•	API logları Grafana Loki ile toplanır.
•	Promtail aracıyla container logları alınır.
•	İsteğe bağlı olarak Grafana Dashboard kurulumu yapılabilir.
________________________________________
🔍 API Testi
Tüm endpoint'ler Postman koleksiyonları ile test edilebilir. docs/ dizininde .postman_collection.json dosyası yer almaktadır.

📜 Lisans
Bu proje, [GNU General Public License v3.0 (GPL-3.0)](https://www.gnu.org/licenses/gpl-3.0.html) lisansı ile lisanslanmıştır.
> Bu lisans, projenizin özgür yazılım olmasını sağlar. Kaynak kodu değiştirmek ve paylaşmak serbesttir. Ancak, dağıtılan türev çalışmaların da aynı lisansla lisanslanması gerekir (copyleft).


🤝 Katkıda Bulun
1.	Fork’la
2.	Yeni branch oluştur: git checkout -b feature/yenilik
3.	Commit yap: git commit -m 'Yeni özellik eklendi'
4.	Push et: git push origin feature/yenilik
5.	PR gönder!

