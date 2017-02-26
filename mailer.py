import smtplib


def send_emails(emails, schedule, forecast):
    # Connect to the smpt server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = raw_input('Whats your password?')
    from_email = 'ilyailya2666@gmail.com'
    server.login(from_email, password)
    print('logged in successfully!')

    # Send email to email list
    for to_email, name in emails.items():
        message = 'Subject : Welcome to Ilya shusterman forecast-weather service '
        message += ' Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule
        message += 'Have a wonderful day from Ilya shusterman!'
        server.sendmail(from_email, to_email, message)

    # End of sending emails
    server.quit()
