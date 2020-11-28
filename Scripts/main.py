from datetime import datetime
import datetime as dt
import humanize
import time
import csv
import PySimpleGUI as sg
import prettytable
import threading
import os
import sys

cou = True
now = ""
now_ = ""

tr = False
sg.theme("Black")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # print('no path')
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


icon = resource_path("Python.ico")
layout = [
    [sg.Output(size=(50, 1), key="out2")],
    [sg.Output(size=(50, 10), key="out")],
    [sg.Text("Study Bruh", font=("Helvetica", 25))],
    [
        sg.Submit("Start", key="start"),
        sg.Submit("Stop", key="Stop"),
        sg.Submit("Today", key="today"),
        sg.Submit("All", key="all"),
        sg.Submit("Exit", key="exit"),
    ],
]

# layout = [[sg.Output(size=(60,10))],
#           [sg.Button('Go'), sg.Button('Nothing'), sg.Button('Exit')]  ]

window = sg.Window("Study Bruh!", layout, icon=icon)


def updater():
    global tr, now
    while True:
        if tr:
            now_ = datetime.now()
            dif = now_ - now
            window.FindElement("out2").Update(
                f"""=========================================
Studing for last:{humanize.precisedelta(dif)}
=========================================
            """
            )
        else:
            pass


def filler(fn):
    def inner(*args, **kwargs):
        # fn(*args, **kwargs)
        window.FindElement("out").Update("")
        print("=========================================")
        returned_value = fn(*args, **kwargs)

        print("=========================================")
        return returned_value

    return inner


@filler
def start():
    global now, tr
    now = datetime.now()
    print("Started:", str(now.strftime("%H:%M")))

    tr = False


@filler
def end():
    global now_
    now_ = datetime.now()
    dif = now_ - now
    print("Ended:", str(now_.strftime("%H:%M")))
    with open("records.csv", "a+") as f:
        wr = csv.writer(f)
        wr.writerow([f"{dt.date.today()}", f"{humanize.precisedelta(dif)}"])


@filler
def read(c):
    if c == "today":
        list1 = []
        with open("records.csv", "r") as f:
            wr = csv.reader(f)
            # print(*wr)
            for i in wr:
                # print(i)
                if len(i) == 0:
                    # print(i)
                    pass
                else:
                    if i[0] == str(dt.date.today()):
                        i[0] = humanize.naturaldate(dt.date.today())
                        # print(i)
                        list1.append(i)
            # print(list1)
            # cols =
    else:
        list1 = []
        with open("records.csv", "r") as f:
            wr = csv.reader(f)
            # print(*wr)
            for i in wr:
                # print(i)
                if len(i) == 0:
                    # print(i)
                    pass
                else:
                    # if i[0] == str(dt.date.today()):
                    i[0] = humanize.naturaldate(datetime.strptime(i[0], "%Y-%m-%d"))
                    # print(i)
                    list1.append(i)
    a = prettytable.PrettyTable()
    a.field_names = ["Day", "How Long?"]
    for i in list1:
        a.add_row(i)
    # a.align["Day"] = "r"
    # a.align["How Long?"] = "l"
    # a.add_column(cols[0], *list1[0])
    # a.add_column(cols[1], *list1[1])
    print(a)
    # wr.writerow([f"{dt.date.today()},{humanize.precisedelta(dif)}"])


aas = threading.Thread(target=updater)
aas.daemon = True
# window.read()
# aas.start()
while True:  # Event Loop

    try:
        # print(type(sg.WIN_CLOSED()))
        event, values = window.read()
        if cou:
            aas.start()
            cou = False
        if event == "start":
            if not tr:

                start()
                tr = True
        elif event == "Stop":
            if tr:
                end()
                tr = False
        elif event == "today":
            read("today")
        elif event == "all":
            read("all")
        elif event == "exit":
            window.close()
            break
        # elif event == WIN_CLOSED:
        #     break
        elif event == sg.WIN_CLOSED:
            break
        # if event == 'Go':
        #     print('About to go to call my long function')
        #     long_function()
        #     print('Long function has returned from starting')
        # elif event == '-THREAD DONE-':
        #     print('Your long operation completed')
    except Exception as e:
        window.close()
        # window.close()
        print(e)
        # break
# window.close()

# start()
# # time.sleep(5)

# end()
# read("todasy")
