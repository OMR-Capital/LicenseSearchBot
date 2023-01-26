# LicenseSearchBot

This bot was created for waste utilization company. It helps find information about utilization items from db by item code or fuzzy search by name.

## Usage

1. Create bot via BotFather
2. Click on `Deploy to Deta`

    [![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/mamsdeveloper/LicenseSearchBot)
3. Enter env variables
4. Set webhook:

    ```bash
        curl -X POST https://api.telegram.org/bot<TELEGRAM_TOKEN>/setWebhook
    -H "Content-Type: application/json"
    -d '{"url": "https://<example-bot>.deta.sh/webhook", "secret_token": "<WEBHOOK_SECRET>"}'
    ```
   
5. Add items to database (find how yourself :3)
6. Enjoy!
