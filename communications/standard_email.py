import yagmail

def send_email(to, subject, contents):

    """yagmail is a library to manage google smtp in a more simpler manner,
    for more information, visit https://github.com/kootenpv/yagmail"""

    USERNAME = 'cortexsilicon'
    APP_PASSWORD = 'jnzbhrbqcsavnlhu'

    yag = yagmail.SMTP(USERNAME, APP_PASSWORD) #input the email username and app password

    yag.send(to = to, subject = subject, contents = contents) #send the email

if __name__ == '__main__':
    send_email()
