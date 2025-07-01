![Twilio Auto Call Bot](https://github.com/abu-sinan/twilio-auto-caller-bot/blob/main/banner.png)

# 📞 Twilio Auto Call Bot

This Python automation bot places a scheduled monthly phone call using Twilio's Voice API. It runs continuously and checks every minute for a specific time—**9:02 AM on the last day of each month**—to trigger an outbound voice call with a predefined message. It includes a retry mechanism, detailed logging, and is fully customizable for business use cases like automatic ordering, alerts, or reminders.

---

## 🚀 Features

- ⏰ **Scheduled Execution** — Calls only on the last day of the month at 9:02 AM.
- 🔁 **Retry Logic** — Retries up to 3 times if the line is busy or call fails.
- 🧾 **Logging** — Logs all call attempts and failures to `call_log.txt`.
- 🗣️ **Text-to-Speech** — Uses Twilio’s voice feature (Alice) to read your message aloud.
- ✅ **Fully Customizable** — Easily change message, schedule, or number.

---

## 🛠️ Technologies Used

- **Python 3.7+**
- **Twilio** (for voice calling)
- **schedule** (Python scheduler)
- **logging** (built-in module)

---

## 📂 Project Structure
```
twilio-auto-call-bot/
 |
 ├── auto_call_bot.py       # Main script
 ├── requirements.txt       # Required Python packages
 ├── README.md              # Project documentation
 └── LICENSE
```
---

## ⚙️ Setup Instructions

### 1. Clone or download the repository

If you’re on a PC or Git-supported terminal:

```bash
git clone https://github.com/abu-sinan/twilio-auto-call-bot.git
cd twilio-auto-call-bot
```

On your phone, download or upload the files manually.

---

### 2. Install Dependencie

```bash
pip install -r requirements.txt
```

---

### 3. Update Twilio Credentials

In `auto_call_bot.py`, replace the placeholders:

```python
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_number = '+YOUR_TWILIO_PHONE_NUMBER'
customer_service_number = '+1800×××××××'
account_number = '48761'
```

✅ **Tip:** Never share your credentials publicly. Use `.env` files in production.

---

### 4. Run the Script

```bash
python auto_call_bot.py
```

The script runs in an infinite loop, checking every minute for the trigger time. When the condition is met, it initiates a call using Twilio.

---

## 🛡️ Security Note

- Never commit sensitive data (API keys, auth tokens).

- Add `.env` support using `python-dotenv` for secure local development.

---

## 📌 Customization Ideas

- Change the scheduled time or date logic.

- Use ```client.calls.create(..., url='https://your-server.com/twiml.xml')``` for more complex messages.

- Add Telegram/Email notifications for success/failure.

---

## 🧑‍💻 Author

Abu Sinan  
Cybersecurity & Automation Expert  
🔗 [Upwork Profile](https://www.upwork.com/freelancers/abusinan)

---

## 📄 License

MIT License — see [LICENSE](https://github.com/abu-sinan/twilio-auto-caller-bot/blob/main/LICENSE) file for details.

---

## 🙌 Support & Contributions

Have an idea to improve the bot? Open an issue or submit a PR! Feedback is always welcome.