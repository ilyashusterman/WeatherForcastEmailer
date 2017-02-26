from gunicorn._compat import FileNotFoundError

import mailer
import weather


# def get_weather_forecast():
#     url = 'http://api.openweathermap.org/data/2.5/weather?' \
#           'q=telaviv,il&units=metric&APPID=25441a00f9654bd8ecf437efdf73b5a1'
#     weather_request = requests.get(url)
#     weather_json = weather_request.json()
#
#     description = weather_json['weather'][0]['description']
#     temp_min = weather_json['main']['temp_min']
#     temp_max = weather_json['main']['temp_max']
#     forecast = 'The service forecast for today is '
#     forecast += description + ' with a high of ' + str(int(temp_max))
#     forecast += ' and a low of ' + str(int(temp_min))
#     return forecast


# def send_emails(emails, schedule, forecast):
#     # Connect to the smpt server
#     server = smtplib.SMTP('smtp.gmail.com', '587')
#
#     # Start TLS encryption
#     server.starttls()
#
#     # Login
#     password = raw_input('Whats your password?')
#     from_email = 'ilyailya2666@gmail.com'
#     server.login(from_email, password)
#     print('logged in successfully!')
#
#     # Send email to email list
#     for to_email, name in emails.items():
#         message = 'Subject : Welcome to Ilya shusterman forecast-weather service '
#         message += ' Hi ' + name + '!\n\n'
#         message += forecast + '\n\n'
#         message += schedule
#         message += 'Have a wonderful day from Ilya shusterman!'
#         server.sendmail(from_email, to_email, message)
#
#     # End of sending emails
#     server.quit()


def get_emails():
    # Reading emails from a file
    emails = {}

    try:
        email_file = open('email2.txt', 'r')

        for line in email_file:
            # emails.append(line.strip())
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print (err)

    return emails


def get_schedule():
    # Reading text from a file
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print (err)

    return schedule


def main():
    emails_list = get_emails()
    print(emails_list)
    schedules = get_schedule()
    print (schedules)
    forecast = weather.get_weather_forecast()
    print (forecast)
    mailer.send_emails(emails_list, schedules, forecast)

main()
