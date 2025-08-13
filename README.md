# TradingView → Telegram Bot

Ce bot reçoit des alertes TradingView via webhook et les envoie sur Telegram.

## 🚀 Déploiement sur Render

1. Pousser ce projet sur GitHub  
2. Sur Render : New → Web Service  
3. Branch : main  
4. Build Command :  
5. Start Command :  
6. Variables d'environnement :  

## 📡 Test webhook

Tester avec curl :  
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"message":"Signal EUR/USD - Vente 🔻"}' \
https://ton-app.onrender.com/alert
