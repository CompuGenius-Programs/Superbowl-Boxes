from datetime import timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from dotenv import load_dotenv
import random, smtplib, datetime, os
load_dotenv()

now = datetime.datetime.now()

print("Copyright (c) %d CompuGenius Programs" % now.year)
print("http://compugeniusprograms.tk")
print("Press enter to continue...")
input()

organizer = input("Who is the organizer of this game? ")
num_players = int(input("How many players? "))
used_boxes = []
box = ['     ' for i in range(100)]
price = float(input("How much does each box cost? "))

names = []
emails = []
boxess = []
costs = []

class Player():
    def player(n):
        cost = 0
        boxes = []
        name = str(input("Name of player number %d: " % (n+1)))
        email = str(input("%s's email: " % name))
        box_amount = int(input("How many boxes is %s buying? " % name))

        name_split = name.split()
        name_initials = []
        for namess in range(len(name_split)):
                name_initials.append(name_split[namess][0])
        initials = name_initials[0] + name_initials[-1]

        for i in range(box_amount):
            cost += price
            b = random.randint(0,99)
            while b in used_boxes:
                b = random.randint(0,99)
            boxes.append(b)
            used_boxes.append(b)
            box[b] = initials

        cost = "$" + "%.2f" % cost

        boxes = [int(x) for x in boxes]
        boxes.sort()
        for i in range(len(boxes)):
            boxes[i] = str(boxes[i]).zfill(2)
            boxes[i] = str(boxes[i])[0] + ',' + str(boxes[i])[1]
        boxes = str(boxes)
        boxes = boxes.strip('[')
        boxes = boxes.strip(']')
        boxes = boxes.replace("'", " ")

        save_info(name, email, boxes, cost)

        if (n + 1) == num_players:
            email_main()

def superbowl_information():
    global date, superbowl_number
    now = datetime.datetime.now()
    superbowl_number = now.year - 1966
    def get_date(month, year, day_num):
        first_date = datetime.date(year, month, 1)
        first_day = first_date.weekday()
        day_inc = day_num + (7 if first_day > day_num else 0) - first_day
        return first_date + timedelta(days=day_inc)

    date = get_date(2, 2019, 6)
    date = str(date).split('-')
    date = str(date[1] + '-' + date[2] + '-' + date[0])

def display_boxes():
    global boxes_chart
    superbowl_information()
    chart = """
     |  0.  |  1.  |  2.  |  3.  |  4.  |  5.  |  6.  |  7.  |  8.  |  9.  |
=========================================
 0. | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |
=========================================
 1. | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |
=========================================
 2. | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |
=========================================
 3. | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |
=========================================
 4. | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |
=========================================
 5. | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |
=========================================
 6. | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |
=========================================
 7. | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |
=========================================
 8. | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |
=========================================
 9. | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |
""" % (box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7], box[8], box[9], box[10], box[11], box[12], box[13], box[14], box[15], box[16], box[17], box[18], box[19], box[20], box[21], box[22], box[23], box[24], box[25], box[26], box[27], box[28], box[29], box[30], box[31], box[32], box[33], box[34], box[35], box[36], box[37], box[38], box[39], box[40], box[41], box[42], box[43], box[44], box[45], box[46], box[47], box[48], box[49], box[50], box[51], box[52], box[53], box[54], box[55], box[56], box[57], box[58], box[59], box[60], box[61], box[62], box[63], box[64], box[65], box[66], box[67], box[68], box[69], box[70], box[71], box[72], box[73], box[74], box[75], box[76], box[77], box[78], box[79], box[80], box[81], box[82], box[83], box[84], box[85], box[86], box[87], box[88], box[89], box[90], box[91], box[92], box[93], box[94], box[95], box[96], box[97], box[98], box[99])
    header = "Superbowl %s Boxes, %s" % (superbowl_number, date)
    boxes_chart = str(header.center(50, ' ') + chart)

my_address = os.getenv("EMAIL")
password = os.getenv("PSWRD")

def save_info(name, email, boxes, cost):
    global names, emails, boxess, costs
    names.append(name)
    emails.append(email)
    boxess.append(boxes)
    costs.append(cost)

def get_info():
    global names, emails, boxess, costs
    return names, emails, boxess, costs

def read_template(filename): 
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def email_main():
    display_boxes()
    names, emails, boxess, costs = get_info()
    message_template = read_template('message.txt')

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(my_address, password)

    for name, email, boxes, cost in zip(names, emails, boxess, costs):
        msg = MIMEMultipart()

        message = message_template.substitute(PERSON_NAME=name.title(), ORGANIZER_NAME=organizer.title(), BOXES_CHART=boxes_chart, BOXES=boxes, COST=cost)

        msg['From']="Superbowl Boxes Generator"
        msg['To']=email
        msg['Subject']="Your Boxes For %s's Game" % organizer.title()

        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)
        del msg

    s.quit()

for n in range(num_players):
    Player.player(n)
