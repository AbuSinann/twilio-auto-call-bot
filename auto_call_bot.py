import time
import schedule
from datetime import datetime, date
from twilio.rest import Client
import logging
import calendar

# ---------------- Twilio credentials ----------------
# Replace these with your actual Twilio Account SID, Auth Token, and Twilio phone number
account_sid = 'YOUR_ACCOUNT_SID'              # Your Twilio Account SID
auth_token = 'YOUR_AUTH_TOKEN'                # Your Twilio Auth Token
twilio_number = '+YOUR_TWILIO_PHONE_NUMBER'  # Your Twilio phone number (e.g., +1978xxxxxxx)

# Create Twilio client instance
client = Client(account_sid, auth_token)

# ---------------- Call details ----------------
customer_service_number = '+1800×××××××'  # Customer service number to call
account_number = '48761'                  # Your liquor store account number
max_retries = 3                          # Number of retries if call fails or is busy
retry_delay_sec = 120                    # Delay between retries in seconds (2 minutes)

# ---------------- Logging setup ----------------
# Logs call attempts and errors into call_log.txt file
logging.basicConfig(
    filename='call_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------- Helper function ----------------
def is_last_day_of_month():
    """
    Check if today is the last day of the month.
    Returns True if last day, else False.
    """
    today = date.today()
    last_day = calendar.monthrange(today.year, today.month)[1]
    return today.day == last_day

# ---------------- Main call function ----------------
def make_call():
    """
    Attempts to call the customer service number and play the order message.
    Retries up to max_retries times if the call fails or is busy.
    """
    if not is_last_day_of_month():
        logging.info("Today is not the last day of the month. No call made.")
        return

    # Message to be read by the Twilio voice (using Alice voice)
    message = (
        f"Good morning. This is a scheduled monthly liquor order for account number {account_number}. "
        "Please process the usual order for this store. Thank you, and have a great day."
    )

    # Retry loop for call attempts
    for attempt in range(1, max_retries + 1):
        try:
            logging.info(f"Attempt {attempt}: Calling {customer_service_number} ...")

            # Initiate the call with Twilio
            call = client.calls.create(
                twiml=f'<Response><Say voice="alice">{message}</Say></Response>',  # TwiML for text-to-speech message
                to=customer_service_number,
                from_=twilio_number,
                timeout=20  # Seconds to wait for the call to be answered
            )

            logging.info(f"Call initiated, SID: {call.sid}")

            # Wait to allow call to complete (adjust timing if needed)
            time.sleep(60)

            logging.info("Call completed successfully.")
            break  # Exit retry loop on success

        except Exception as e:
            logging.error(f"Call attempt {attempt} failed: {e}")

            # If more retries left, wait before retrying
            if attempt < max_retries:
                logging.info(f"Waiting {retry_delay_sec} seconds before retrying...")
                time.sleep(retry_delay_sec)
            else:
                logging.error("Max retries reached. Giving up.")

# ---------------- Scheduled job ----------------
def job():
    """
    This function runs every minute.
    It checks if the current time is 9:02 AM, and if so, triggers the call.
    """
    now = datetime.now()
    if now.hour == 9 and now.minute == 2:
        make_call()
    else:
        logging.debug(f"Checked time {now}, waiting for 09:02.")

# ---------------- Schedule setup ----------------
# Run 'job' function every minute to check the time
schedule.every(1).minutes.do(job)

logging.info("Auto call bot started and running...")

# ---------------- Main loop ----------------
# Keep script running indefinitely to allow schedule to work
while True:
    schedule.run_pending()
    time.sleep(1)