from tkinter import *
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading

###########Functionality Part
totaltime=60
time=0
wrongwords=0
elapsedtimeinminutes=0
def start_timer():
    startButton.config(state=DISABLED)
    global time
    textArea.config(state=NORMAL)
    textArea.focus()

    for time in range(1,61):
        elapsed_timer_label.config(text=time)
        remainingtime=totaltime-time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        root.update()

    textArea.config(state=DISABLED)
    resetButton.config(state=NORMAL)

def count():
    global wrongwords
    while time!=totaltime:
        entered_paragraph=textArea.get(1.0,END).split()
        totalwords=len(entered_paragraph)

    totalwords_count_label.config(text=totalwords)

    para_word_list=paraLabel['text'].split()

    for pair in list(zip(para_word_list,entered_paragraph)):
        if pair[0]!=pair[1]:
            wrongwords+=1

    wrongwords_count_label.config(text=wrongwords)

    elapsedtimeinminutes=time/60
    wpm=(totalwords-wrongwords)/elapsedtimeinminutes
    wpm_count_label.config(text=wpm)
    gross_wpm=totalwords/elapsedtimeinminutes
    accuracy=wpm/gross_wpm*100
    accuracy=round(accuracy)
    accuracy_percent_label.config(text=str(accuracy)+'%')


def start():
    t1=threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()


def reset():
    global time,elapsedtimeinminutes
    time=0
    elapsedtimeinminutes=0
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    textArea.config(state=NORMAL)
    textArea.delete(1.0,END)
    textArea.config(state=DISABLED)

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    wpm_count_label.config(text='0')
    accuracy_percent_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrongwords_count_label.config(text='0')

def shuffle():
    random.shuffle(paraList)
    paraLabel.config(text=paraList[0])
    reset()


# start GUI
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('breeze')
root.geometry('940x735+210+10')

        # root.resizable(0,0) with this method you cannot resize size of the window but i am not gonna use that

mainframe = Frame(root,bd=4)
mainframe.grid()

# start title frame
titleframe = Frame(mainframe,bg='aquamarine4')
titleframe.grid(row=0, column=0)

titlelabel = Label(titleframe, text='Typing Test', font=('onyx', 28, 'bold'), bg='khaki4', fg='white',
                   width=111, bd=10)
titlelabel.grid(pady=5)
# end title frame

# start paragraph frame
paraFrame = Frame(mainframe)
paraFrame.grid(row=1, column=0)

paraList= ['The computer is a miraculous invention of science. It can store data and perform difficult calculations within a very short time. Its main features are speed and accuracy. Thus computers aids in speedy transactions and telecommunication. It is now widely used in schools, colleges, libraries, hospitals, offices, and banks. In factories, it is used to save manual and mental labor and for quality control. It is also used in research work in various fields like space research. Now computer courses of different levels are being introduced in schools and colleges. The introduction of computers in selected fields is a must for efficient service.',
          'You may already know that it is important to have a king-sized breakfast every morning. Do you know why? Your body is famished in the morning because you haven’t eaten for about 8–10 hours. Breakfast is therefore the first meal of the day, and hence, the most important one as well. Imagine driving a car without fuel; this is exactly how your body feels without the fuel provided by a nutritious breakfast. Many people these days resort to skipping breakfast in a bid to lose weight. Nutritionists are appalled by this trend since it is mandatory to have breakfast within two hours of waking up.',
          'Positive thinking is an attitude or a mindset characterized by optimism and happiness. A positive person hopes for the best and anticipates success in his life. Although many may scoff at the idea of always being positive, it has a plethora of benefits not only for the mind but also for the body. Positivity imparts happiness to the soul and makes one lighter. This causes us to exude goodwill and joy. People are drawn towards such individuals. Being negative in one‟swords and actions causes the exact opposite reaction. It is a known fact that people try to avoid people who relay negativity.',
           'Atoms of radioactive elements can be spilled. According to Albert Einstein, mass and energy are interchangeable under certain conditions. When the atom splits, the process is called nuclear fission. In this case, a tiny amount of mass is converted into energy. The energy thus released cannot do much damage. However, a number of subatomic particles called neutrons are also released during this process. Each neutron will hit a radioactive element releasing more neutrons in the process. This results in a chain reaction and a tremendous amount of energy is created. This energy is converted into heat which expands uncontrollably causing an explosion.',
           'Agriculture is the largest profession in our country. A huge number of people are depended on this occupation. People who do agricultural work, we address them as a farmer. Two-third of the entire population is connected with agriculture directly or indirectly. It is one of the important professions for the entire world. Except for agriculture, food production will be stopped and the world could face a food crisis. Farmers are really hard workers. They work so hard to grow vegetables for us. Now there is so much technology that has made agriculture really easy and effective. This is a really important profession for us.',
           'The Internet is a really important thing that has connected the entire world with a special network. It has brought lots of changes to people’s life. The business and education system has been changed completely. Today we will take a look at some advantages and disadvantages of the internet. The biggest impact of the internet is on education. The learning opportunity has been really easy. The Internet has a huge resource that you can find within seconds. You can share your knowledge with the entire world. And most importantly connectivity has been developed globally. That has made the business opportunity easier.',
           'City life is really interesting to me. I have spent most of the time in Mumbai with my family. Now I am living in Delhi. So I have seen bad and good side of city life. The most important and advantage of city life is people are busy here. They don’t care about things that are not related with them. There are lots of work opportunities for people. People come from the countryside to find jobs here. The biggest disadvantages are the environment and traffic jams. I hate traffic jams. It becomes a reason to waste huge time. Overall, city life is average for me.',
           'The banking system was a revolutionary idea that changed the economical system worldwide. The banking system was started around 2000 BC, but modern banking is not that old. The bank is a really important part of our regular life. It is really easy for any citizen to create a new bank account and store money with security.There are different types of public and private banks in every country. We should create an account of the trusted banks that has a reputation for a long time. Right now, the online banking system has been started worldwide. It has changed the old traditional money transaction system.',
           'In my last summer vacation, we spend the whole time is a village near Sylhet, Bangladesh. Sylhet is the most beautiful place in the country. I loved spending time there. My father has a good friend here and he was inviting us to visit his place a long time ago. He and his family have visited us a few times. And finally, my father decided to visit his place in the summer vacation. We went there on a journey by train. I love the train journey. The cutest and amazing thing was the tea gardens there. I loved the place so much.',
           'If we take a look at the life of successful people, then we will see all of them said to get up early in the morning. And it’s important for our health and mental growth. A morning walk is also really important for us. It helps us to remain healthy. The air is so fresh and good at that time. You can see the difference between normal day and morning, and the morning is too beautiful. If you walk regularly in the morning, you might stay away from lots of common health issues. Especially the people who want to lose weight, they need to walk a lot in the morning.'
           ]

random.shuffle(paraList)
paraLabel = Label(paraFrame,text=paraList[0],wraplength=912,justify=LEFT,font=('arial', 14, 'bold'),width=111, bg='DarkKhaki')
paraLabel.grid(row=0, column=0)
# end paragraph frame

# text area frame
textFrame = Frame(mainframe)
textFrame.grid(row=2, column=0)

textArea = Text(textFrame, font=('times new roman', 14, 'bold'), width=100, height=10, bd=4, relief=RAISED, wrap='word', state=DISABLED)
textArea.grid()
# end text area frame

frame_output=Frame(mainframe)
frame_output.grid(row=3,column=0)

elapsed_time_label=Label(frame_output,text='Elapsed Time',font=('Tahoma',12,'bold'),fg='red')
elapsed_time_label.grid(row=0,column=0,padx=5)

elapsed_timer_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
elapsed_timer_label.grid(row=0,column=1,padx=5)

remaining_time_label=Label(frame_output,text='Remaining Time',font=('Tahoma',12,'bold'),fg='red')
remaining_time_label.grid(row=0,column=2,padx=5)

remaining_timer_label=Label(frame_output,text='60',font=('Tahoma',12,'bold'))
remaining_timer_label.grid(row=0,column=3,padx=5)

wpm_label=Label(frame_output,text='WPM',font=('Tahoma',12,'bold'),fg='red')
wpm_label.grid(row=0,column=4,padx=5)

wpm_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
wpm_count_label.grid(row=0,column=5,padx=5)

totalwords_label=Label(frame_output,text='Total Words',font=('Tahoma',12,'bold'),fg='red')
totalwords_label.grid(row=0,column=6,padx=5)

totalwords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
totalwords_count_label.grid(row=0,column=7,padx=5)

wrongwords_label=Label(frame_output,text='Wrong Words',font=('Tahoma',12,'bold'),fg='red')
wrongwords_label.grid(row=0,column=8,padx=5)

wrongwords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
wrongwords_count_label.grid(row=0,column=9,padx=5)

accuracy_label=Label(frame_output,text='Accuracy',font=('Tahoma',12,'bold'),fg='red')
accuracy_label.grid(row=0,column=10,padx=5)

accuracy_percent_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
accuracy_percent_label.grid(row=0,column=11,padx=5)

# start button frame
buttonFrame = Frame(mainframe)
buttonFrame.grid(row=4, column=0)

startButton = ttk.Button(buttonFrame, text='Start', width=6, command=start)
startButton.grid(row=0, column=0, padx=10)

resetButton = ttk.Button(buttonFrame, text='Reset', width=6, state=DISABLED, command=reset)
resetButton.grid(row=0, column=1, padx=10)

exitButton = ttk.Button(buttonFrame, text='Exit', width=6, command=root.destroy)
exitButton.grid(row=0, column=2, padx=10)

shuffleTextButton = ttk.Button(buttonFrame, text='Shuffle', width=6, command=shuffle)
shuffleTextButton.grid(row=0, column=3, padx=10)
# end button frame

root.mainloop()
# end GUI