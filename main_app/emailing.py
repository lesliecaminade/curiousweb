import yagmail

def send_email_student(student):

    """yagmail is a library to manage google smtp in a more simpler manner,
    for more information, visit https://github.com/kootenpv/yagmail"""

    yag = yagmail.SMTP('cortexsilicon','jnzbhrbqcsavnlhu') #input the email username and app password

    if student.student.course == 'ece':
        conditional_statement = f"""<tr><td>Conditional Subject </td><td>{student.conditional_subject}</td></tr>"""
    else:
        conditional_statement = ""

    contents = f"""
    <html>
    <body>
        <h1>Enrollment: CERTC Online Review</h1>
        <table>
          <ul>
            <tr><td>Name </td> <td>{student.student.last_name}, {student.student.first_name}, {student.student.middle_name}</td></tr>
            <tr><td>Course </td><td>{student.student.course}</td></tr>
            <tr><td>Date Graduated </td><td>{student.student.date_graduated}</td></tr>
            <tr><td>Honors </td><td>{student.student.honors}</td></tr>
            <tr><td>Officer Position </td><td>{student.student.officer_position}</td></tr>
            <tr><td>Scholarships </td><td>{student.student.scholarships}</td></tr>
            <tr><td>Review Status </td><td>{student.review_status}</td></tr>
            {conditional_statement}
            <tr><td>Mobile Number </td><td>{student.student.mobile_number}</td></tr>
            <tr><td>Facebook Username </td><td>{student.student.facebook_username}</td></tr>
            <tr><td>ID picture</td><td>http://siliconcortex.pythonanywhere.com{student.id_picture.url} </td></tr>
            <tr><td>Payment picture </td><td>http://siliconcortex.pythonanywhere.com{student.payment_picture.url}</td></tr>
            <tr><td>ID picture</td><td><img src=" http://siliconcortex.pythonanywhere.com{student.id_picture.url} " alt="id picture" title="ID" style="display:block" width="200"/> </td></tr>
            <tr><td>Payment picture </td><td><img src=" http://siliconcortex.pythonanywhere.com{student.payment_picture.url} " alt="payment picture" title="Payment Proof" style="display:block" width="200"/> </td></tr>
          </ul>
        </table>
      </body>
    </html>""" #set the email content

    yag.send(to = ['lesliecaminade@gmail.com', 'lesliecaminade@protonmail.com'], subject = 'CERTC CuriousWeb New Enrollment', contents = contents) #send the email
