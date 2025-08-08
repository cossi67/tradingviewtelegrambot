# Bot Telegram pour alertes TradingView

Ce projet déploie un serveur Flask qui reçoit des alertes webhook depuis TradingView  
et les transmet automatiquement dans un groupe ou chat Telegram.

---

## Usage

- Configurer les variables d'environnement `TELEGRAM_TOKEN` et `TELEGRAM_CHAT_ID` sur Render.  
- Déployer le service sur Render (ou autre hébergeur).  
- Configurer les alertes TradingView avec l'URL webhook pointant vers ce service.

---

## Auteur

Projet réalisé avec l'aide d’Usman (ChatGPT).

