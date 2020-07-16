import yagmail
import curiousweb

def send_email(submission):

    """yagmail is a library to manage google smtp in a more simpler manner,
    for more information, visit https://github.com/kootenpv/yagmail"""
    domain = curiousweb.settings.DOMAIN
    yag = yagmail.SMTP('cortexsilicon','jnzbhrbqcsavnlhu') #input the email username and app password

    if submission.image:
        image_part = f"""<tr><td>Attached image</td><td><img src="{domain}{submission.image.url}" style="display:block" width="200"/></td></tr>"""
    else:
        image_part = ''
    contents = f"""
    <html>
    <body>
        <h1>CERTC: Post Submission from {submission.author.last_name}, {submission.author.first_name}</h1>
        <table>
            <tr><td>Name </td> <td>{submission.author.last_name}, {submission.author.first_name}</td></tr>
            <tr><td>Content </td> <td>{submission.text}</td></tr>
            {image_part}
        </table>
      </body>
    </html>"""

    #edit the course accordingly
    #remove the middle portion for tutorial
    yag.send(to =['lesliecaminade@gmail.com',], subject = f"""CERTC: Post Submission from {submission.author.first_name}""", contents = contents) #send the email
