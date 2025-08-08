# TradingView → Telegram Webhook Bot

## Déploiement Render.com (gratuit)

1. Crée un compte sur https://render.com  
2. Crée un nouveau Web Service connecté à ce repo GitHub  
3. Configure les variables d'environnement :  
   - TELEGRAM_TOKEN = "ton token"  
   - TELEGRAM_CHAT_ID = "ton chat id"  
4. Lancer le service  
5. Copier l’URL fournie (ex: https://xxx.onrender.com/webhook)  
6. Dans TradingView, crée une alerte avec cette URL en Webhook  
7. Mets dans le message JSON de TradingView:  
```json
{"message": "Signal EURUSD Buy détecté"}
