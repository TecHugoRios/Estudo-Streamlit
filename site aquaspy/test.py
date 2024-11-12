import smtplib

nome = "hugo"
sender = f"{nome} <user@demomailtrap.com>"
receiver = "aquaspy <hugoba532@gmail.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "c669a11159c33ff4033285e892079063")
    server.sendmail(sender, receiver, message)