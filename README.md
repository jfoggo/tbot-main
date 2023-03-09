# tbot-main
This repository contains a *minimal template* for a __telegram-bot__ hosted on `deta.space` platform. The bot is written in `Python3` and makes use of `FastAPI` web-framework. The bot initially greets the user at the `/start`, otherwise it only repeats the initial message. Feel free to use this code as an entry point for your very first telegram bot.

---

## How to install?
1) Create Telegram Bot via Bot-Father:
    - Open Telegram (webiste or app)
    - Send `/newbot` to the `BotFather` account
    - Save `TELEGRAM_BOT_TOKEN` provided by `BotFather`
2) Initialize deta.space project:
    - Create empty directory: `mkdir tbot-main`
    - Navigate to directory: `cd tbot-main`
    - Create new space project: `space new`
    - Download and copy code from this repository into directory
    - Enter your `TELEGRAM_BOT_TOKEN` into `Spacefile`
3) Deploy project to Space:
    - Deploy code: `space push`
    - Login to `deta.space` platform
    - Visit your App's Home-Wesite (click on app)
    - You should see a similar message: "Webhook was set", otherwise something went wrong!
4) Test your bot:
    - Open Telegram again
    - Send `/start` to your new created bot
    - If you receive a respone everything is good, otherwise check the logs

---

## HTTP-Endpoints:
- Set webhook-url for telegram-bot: (private route)  
`GET https://<HOSTNAME>/`
- Handle update-messages from telegram-api: (public route)  
`POST https://<HOSTNAME>/open`

---

## Usefull Links:
- [Deta-Space Documentation](https://deta.space/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Telegram BOT-API Documenation](https://core.telegram.org/bots/api)