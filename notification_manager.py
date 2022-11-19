import smtplib

EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "cbqsmtp@gmail.com"
MY_PASSWORD = "osxpvbvolrcsicsi"
email = "crisbustaq@gmail.com"


class NotificationManager:
    def send_emails(self, message, product_link):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:El producto que buscas está en oferta!\n\n{message}\n{product_link}".encode('utf-8')
            )
