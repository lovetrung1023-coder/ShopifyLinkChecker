
# Telegram Notification Setup Guide

## Step 1: Create a Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Start a chat and send `/newbot`
3. Follow the instructions to choose a name and username for your bot
4. Save the **bot token** you receive (looks like: `123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ`)

## Step 2: Get Your Chat ID

1. Search for `@userinfobot` in Telegram
2. Start a chat and it will send you your **chat ID** (a number)
3. Save this number

## Step 3: Configure Replit Secrets

1. In Replit, open the **Secrets** tool (lock icon in left sidebar)
2. Add these two secrets:
   - Key: `TELEGRAM_BOT_TOKEN`, Value: (your bot token from step 1)
   - Key: `TELEGRAM_CHAT_ID`, Value: (your chat ID from step 2)

## Step 4: Test the Connection

1. Restart your Replit app
2. In the sidebar, you should see "✅ Telegram connected"
3. Click "🧪 Test Telegram" to send a test message
4. Check your Telegram to confirm you received the message

## Features

Once configured, you'll receive Telegram notifications for:
- **Newly DEAD stores** - Immediate alerts when stores go down
- **Status changes** - When stores recover or change status
- **Scheduled check summaries** - Regular updates from automatic checks

## Automatic Notifications

The system will automatically send notifications when:
- A store changes from LIVE/UNPAID to DEAD
- A store recovers from DEAD to LIVE
- Any status change occurs during scheduled checks

## Environment Variables

You can also set these via environment variables instead of Secrets:
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
export TELEGRAM_CHAT_ID="your_chat_id_here"
```

## Scheduler Configuration

Control automatic checking frequency:
- Default: 60 minutes
- Set via environment variable: `CHECK_INTERVAL_MINUTES=30`
- Or adjust in the UI sidebar
