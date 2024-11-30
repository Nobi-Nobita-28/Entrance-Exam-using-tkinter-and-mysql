from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import MySQLdb
# import pygame

def play_sound(sound_file):
    pass
    # pygame.mixer.init()
    # pygame.mixer.music.load(sound_file)
    # pygame.mixer.music.play()

con = MySQLdb.connect("localhost", "root", "root2004", "regs")

def connect():
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    global s1, s2, s3, s4, s5, s6, s7, s8, s9
    s1 = StringVar()
    s2 = StringVar()
    s3 = StringVar()
    s4 = StringVar()
    s5 = StringVar()
    s6 = StringVar()
    s7 = StringVar()
    s8 = StringVar()
    s9 = StringVar()
    cur = con.cursor()
    s1 = e1.get()
    s2 = e2.get()
    s3 = e3.get()
    s4 = e4.get()
    s5 = e5.get()
    s6 = e6.get()
    s7 = e7.get()
    s8 = e8.get()
    s9 = e9.get()
    if not validate_email(s8):
        messagebox.showerror("Error", "Invalid email address. Please enter a valid email.")
        return
    if validate_email(s8):
        sql = "insert into regs.form value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        user = (s1, s2, s3, s4, s5, s6, s7, s8, s9)
        cur.execute(sql, user)
        con.commit()
        con.close()
    root.withdraw()
    messagebox.showinfo("Connected", "Registered Successfully...")
    open_third_window()

def open_second_window():
    # t.destroy()
    t.withdraw()
    # c = Tk()
    # root = Tk()
    global root
    root = Toplevel(t) 
    # c.configure(bg='#3FFFF3')
    root.title("Registration Form")
    root.geometry("1400x700")
    # c.state("zoomed")
    # root.state("zoomed") 
    # bg = PhotoImage(file = "C:\\Users\\sanju\\Downloads\\VS Project (2)\\VS Project\\books-beach rm.png") 
    bg = PhotoImage(file = "yourname.png")    
    # bg = PhotoImage(file = "D:\\Desktop\\Codes\\Projects\\Suji\\yourname.png")    
    canvas1 = Canvas(root, width = 1400, height = 745) 
    canvas1.pack(fill = "both", expand = True) 
    canvas1.create_image( 0, 0, image = bg, anchor = "nw") 
    global e1, e2, e3, e4, e5, e6, e7, e8, e9
    e1 = StringVar()
    e2 = StringVar()
    e3 = StringVar()
    e4 = StringVar()
    e5 = StringVar()
    e6 = StringVar()
    e7 = StringVar()
    e8 = StringVar()
    e9 = StringVar()

    canvas1.create_text(1100,40, text="Registration Form", font=("Copperplate Gothic Bold", 32), fill="red")
    canvas1.create_text(1000,115, text="Name :", font=("Times new roman", 22,))
    e1 = Entry(root,font=("Times new roman", 17))
    e1.place(x=1120, y=100)
    canvas1.create_text(1000,175, text="STD:", font=("Times new roman", 22))
    e2 = Entry(root,font=("Times new roman", 17))
    e2.place(x=1120, y=160)
    canvas1.create_text(1000,230, text="Department:", font=("Times new roman", 22))
    e3 = Entry(root,font=("Times new roman", 17))
    e3.place(x=1120, y=215)
    canvas1.create_text(1000,290, text="Want To Became:", font=("Times new roman", 22))
    e4 = Entry(root,font=("Times new roman", 17))
    e4.place(x=1120, y=270)
    canvas1.create_text(1000,350, text="Father Name:", font=("Times new roman", 22))
    e5 = Entry(root,font=("Times new roman", 17))
    e5.place(x=1120, y=335)
    canvas1.create_text(1000,410, text="Address:", font=("Times new roman", 22))
    e6 = Entry(root,font=("Times new roman", 17))
    e6.place(x=1120, y=390)
    canvas1.create_text(1000,470, text="Contact No:", font=("Times new roman", 22))
    e7 = Entry(root,font=("Times new roman", 17))
    e7.place(x=1120, y=455)
    canvas1.create_text(1000,520, text="Email Id:", font=("Times new roman", 22))
    e8 = Entry(root,font=("Times new roman", 17))
    e8.place(x=1120, y=510)
    canvas1.create_text(1000,570, text="School/College:", font=("Times new roman", 22))
    e9 = Entry(root,font=("Times new roman", 17))
    e9.place(x=1120, y=565)
    b1 = Button(root, text="SUBMIT", font=("Copperplate Gothic bold", 15), width=10, bg="#E72949", command=connect)
    b1.place(x=1050, y=650)
    root.mainloop()

def open_third_window():
    global m
    m = Tk()
    m.configure(bg='plum2')
    m.title("Evaluation Test")
    # m.geometry("1600x1100")
    m.state("zoomed")
    l = Label(m, text="Do You Know Your Scholarship", font=("Copperplate Gothic Bold", 50,"bold"), bg="plum2")
    l.place(x=100, y=110)
    l1 = Label(m, text="Amount ??", font=("Copperplate Gothic Bold", 50,"bold"), bg="plum2")
    l1.place(x=480, y=220)
    l2 = Label(m, text="Do The Evalution Test", font=("Copperplate Gothic Bold", 47,), bg="plum2")
    l2.place(x=300, y=370)
    b1 = Button(m, text="Software", font=("Copperplate Gothic Bold", 20), width=10, bg="hotpink", command=lambda: cate_selct("software"))
    b1.place(x=150, y=530)
    b2 = Button(m, text="Accountance", font=("Copperplate Gothic Bold", 20), width=11, bg="hotpink", command=lambda: cate_selct("accountance"))
    b2.place(x=550, y=530)
    b3 = Button(m, text="General", font=("Copperplate Gothic Bold", 20), width=10, bg="hotpink", command=lambda: cate_selct("general"))
    b3.place(x=950, y=530)
    m.mainloop()

def cate_selct(category):   
    global cate
    cats = category
    def cat_choice(category):
        if category == "software":
            open_software_test()
        elif category == "accountance":
            open_tally_test()
        elif category == "general":
            open_gk_test()
    # cate.withdraw()
    cate = Tk()
    cate.title("Instructions")
    # cate.geometry("1600x1500")
    cate.config(bg="#52FCFF")
    cate.state("zoomed")
    i_tit = Label(cate, text="Instructions", font=("Copperplate Gothic Bold", 44,"bold"), bg="#52FCFF", fg="#FF0808")
    i_tit.place(x=450, y=30)
    i_tit = Label(cate, text="1. There are a total of 10 questions waiting for you", font=("Copperplate Gothic Bold", 30,"bold"), bg="#52FCFF")
    i_tit.place(x=100, y=130)
    i_tit = Label(cate, text="2. When you're done, hit that submit button", font=("Copperplate Gothic Bold", 30,"bold"), bg="#52FCFF")
    i_tit.place(x=100, y=210)
    i_tit = Label(cate, text="3. You've got just 1 minute to answer each question", font=("Copperplate Gothic Bold", 30,"bold"), bg="#52FCFF")
    i_tit.place(x=100, y=280)
    i_tit = Label(cate, text=" You're all set! Ready to rock this quiz?", font=("Copperplate Gothic Bold", 30,"bold"), bg="#52FCFF")
    i_tit.place(x=210, y=350)
    i_tit = Label(cate, text=" Hit the Start Button!", font=("Copperplate Gothic Bold", 30,"bold"), bg="#52FCFF", fg="#FF4FC7")
    i_tit.place(x=410, y=420)
    i_tit = Label(cate, text="Best Of Luck...", font=("Copperplate Gothic Bold", 30,"bold"), bg="#52FCFF", fg="#AA00FF")
    i_tit.place(x=480, y=490)
    bw = Button(cate, text="START", font=("copperplate gothic bold", 22), width=10, bg="#7FFF8F", command=lambda: cat_choice(cats))
    bw.place(x=550, y=560)
    cate.mainloop()

def open_software_test():
    cate.destroy()
    m.withdraw()
    category = "Software"
    questions = [
            "1. Which of the following is not a type of software?",
            "2. Which of the following is part of system software?",
            "3. A mistake in an algorithm that generates incorrect results or output is called?",
            "4. The process of finding errors/defects/bugs in the software program is called?",
            "5. Which of the following is not application software?",
            "6. Which of the following is the address operator?",
            "7. MicrosoftWord,MicrosoftExcel,and Gooogle Docs are the examples of ",
            "8. Which of the following are examples of presentation graphics software?",
            "9. C++ is a ___ type of language?",
            "10.  Which one of the following represents the tab?"
    ]
    options = [
            ["System software", "Driver software", "Application software", "Utility software"],
            ["Operating system", "Utility software", "Browser software", "Both a and b"],
            ["Logical error", "Syntax error", "Compile-time error", "Procedural error"],
            ["Debugging", "Interpreting", "Compiling", "Testing"],
            ["MS-Word", "Google Docs", "Adobe Acrobat", "Turbo C compiler"],
            ["@","#","&","%"],
            ["An Operating Software","System Software","Utility Software","Application Software"],
            ["Microsoft PowerPoint","Corel Presentations","Apple KeyNote","All of the Above"],
            ["High-Level Language","Low-Level Language","Middle-Level Language","None of the Above"],
            ["New Line","Tab","Row","None of the Above"]
        ]
    answers = [1, 3, 0, 3, 3, 2, 3, 1, 2, 0]  
    software_window = Toplevel(t)
    software_app = Test(software_window,t,category,questions,options,answers)

def open_tally_test():
    cate.destroy()
    m.withdraw()  
    category = "Accountance"
    questions = [
            "1. Good will is",
            "2. The expanded accounting equation is used by which statement? ",
            "3. What type of balance do asset accounts have?",
            "4. The kind of debts which are needed to be repaid in a short term is known as?",
            "5. Interest on capital will be paid to the partners if provided for in the partnership deed but only out of:?",
            "6. If the date of drawing is not given, interest on Total Drawings is calculated for",
            "7.  Recording financial transaction is part of?",
            "8.  Examining of financial information refers to?",
            "9. Capital + Liabilities = ?",
            "10.  What occurs when expenses are greater than income?"
    ]
    options = [
            ["Tangible asset","Intangible asset","Fictitious asset","Both b and c"],
            ["Cash Flow Statement","Balance Sheet","Income Statement","None of the above"],
            ["Debit","Contra","Credit","All of the above"],
            ["Fixed Liabilities","Current Liabilities","Depreciating Assets","Intangible Assets"],
            ["Profits","Reserves","Accumulated profits","Goodwill"],
            ["4 Months","5 Months","6 Month","1 Year"],
            ["Accounting","Book Keeping","Data Entry","Journal"],
            ["Analysis","Auditing","Recording","Balance Sheet"],
            ["Revenue","Assets","Unearned Income","Voucher",],
            ["Net Loss","Debts","Net Profit","Decrease in Assets",]
    ]
    answers = [1, 2, 0, 1, 0, 3, 0, 1, 1, 2]
    tally_window = Toplevel(t)
    tally_app = Test(tally_window,t,category,questions,options,answers)

def open_gk_test():
    cate.destroy()
    m.withdraw()  
    category = "General"
    questions = [
            "1. What is the capital of TamilNadu?",
            "2. During the first world war which country signed the peace treaty (1918)in germany?",
            "3. What is the launch date for Chandrayaan 3 mission?",
            "4. India is the _____ country to successfully land a spacecraft on the moon?",
            "5. What is the landing schedule for Chandrayaan 3?",
            "6. Which of the following folders is commonly used in the deleted emails?",
            "7.What is the largest ocean in the world ?",
            "8.What is the tallest mountain in the world?",
            "9.Which planet is known as the Red Planet?",
            "10.Which of the following has no Skeleton at all?"
    ]
    options = [
            ["Madurai", "NewDelhi","Trichy","Chennai",],
            ["Russia","USA","England", "Austria",],
            ["07 july 2023", "09 july 2023", "27 july 2023", "14 july 2023"],
            ["First","Second", "Third", "Fourth",],
            ["12 Aug 2023","23 sep 2023","23 Aug 2023","12 Sep 2023" ],
            ["junk","draft","sent","trash"],
            ["Atlantic","Pacific ","Indian","Artic"],
            ["Mount Everest","Mount fuji ","Mount Kilimanjaro","Mount McKinley"],
            ["Saturn","Earth ","Mars","Jupiter"],
            ["Spongue","Jelly fish","Start fish","Silver fish"]
    ]
    answers = [3, 2, 3, 3, 2, 3, 1, 0, 2, 0]
    gk_window = Toplevel(t)
    gk_app = Test(gk_window,t,category,questions,options,answers)

class Test:
    def __init__(self, root, main_window,category,questions,options,answers):
        self.category = category
        self.root = root
        self.root.geometry("500x500")
        self.main_window = main_window
        self.root.title(self.category+" Test")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.result_shown = False
        self.frame = Frame(self.root)
        self.frame.pack()
        self.timer_label = Label(self.frame, text="", font=("Lucida Console", 12,"bold"), fg="red")
        self.timer_label.pack(pady=10)

        self.question_label = Label(self.frame, text="", font=("Comic Sans MS", 20,"bold"), wraplength=350, justify="left")
        self.question_label.pack(pady=20)

        self.answer_var = IntVar()
        self.option_buttons = []
        self.questions = questions
        self.options = options
        self.answers = answers
        self.user_answers = []

        self.current_question_index = 0
        self.remaining_time = 0
        self.timer_id = None

        self.display_question()

    def display_question(self):
        question = self.questions[self.current_question_index]
        self.question_label.config(text=question)
        self.answer_var.set(-1)
        self.start_timer()
        self.update_options()

    def update_options(self):
        for option_button in self.option_buttons:
            option_button.destroy()
        self.option_buttons = []

        options = self.options[self.current_question_index]
        for i, option in enumerate(options):
            option_button = Radiobutton(self.frame, text=option, font=("Comic Sans MS",16), variable=self.answer_var, value=i)
            option_button.pack(anchor="w", padx=10)
            self.option_buttons.append(option_button)

        if hasattr(self, 'submit_button') and self.submit_button.winfo_exists():
            self.submit_button.destroy()

        self.submit_button = Button(self.frame, text="Submit",width=8, font=("Comic Sans MS",16), bg="#66E04E", command=self.submit_answer)
        self.submit_button.pack()

    def update_timer(self):
        if self.remaining_time > 0:
            self.timer_label.config(text=f"Time left: {self.remaining_time} seconds")
            self.remaining_time -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            if not self.result_shown: 
                self.submit_answer()

    def start_timer(self):
        self.remaining_time = 60
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.update_timer()    

    def submit_answer(self):
        answer_index = self.answer_var.get()
        self.user_answers.append(answer_index)
        if len(self.user_answers) < len(self.questions):
            self.current_question_index += 1
            self.display_question()
        else:
                self.calculate_score()
    def calculate_score(self):
        # global score
        correct_count = 0
        for user_answer, correct_answer in zip(self.user_answers, self.answers):
            if user_answer == correct_answer:
                correct_count += 1
        total_questions = len(self.questions)
        score = (correct_count / total_questions) * 100
        # score_dis(score)
        self.show_result(score)

    def show_result(self, score):
        if not self.result_shown: 
            self.result_shown = True 
            self.root.withdraw()  
        # self.root.withdraw() 
        if score > 50:
            result = "Pass"
        else:
            result = "Fail"
        if score >= 90:
            schlr_percent = 50
        elif score >= 80:
            schlr_percent = 30
        elif score >= 70:
            schlr_percent = 20
        elif score >= 60:
            schlr_percent = 10
        else:
            schlr_percent = 0        
        con = MySQLdb.connect("localhost", "root", "root2004", "regs")
        # con = MySQLdb.connect("localhost", "root", "mysql_03", "regs")
        cur = con.cursor()
        sql = "insert into regs.results value(%s,%s,%s,%s,%s,%s)"
        user = (s1,s3,s9,self.category,str(score),result)
        cur.execute(sql, user)
        con.commit()
        con.close()
        result_window = Toplevel() 
        result_window.geometry("580x600")
        result_window.title("Test Result")
        play_sound("chipi-chipi.mp3")
        result_window.configure(bg="#CCFF90")
        # schlr_percent = 50
        rslt = Label(result_window,text="Result", font=("copperplate Gothic Bold",40),fg="#00C853",bg="#CCFF90")
        rslt.place(x=196,y=15)
        namel = Label(result_window,text="Name :", font=("copperplate Gothic Bold",24),bg="#CCFF90")
        namel.place(x=60,y=100)
        namev = Label(result_window,text=s1, font=("copperplate Gothic Bold",22),bg="#CCFF90")
        namev.place(x=330,y=100)
        categoryl = Label(result_window,text="Category :", font=("copperplate Gothic Bold",24),bg="#CCFF90")
        categoryl.place(x=60,y=160)
        categoryv = Label(result_window,text=self.category, font=("copperplate Gothic Bold",22),bg="#CCFF90")
        categoryv.place(x=330,y=160)
        scorel = Label(result_window,text="Score : ", font=("copperplate Gothic Bold",24),bg="#CCFF90")
        scorel.place(x=60,y=210)
        scorev = Label(result_window,text=str(score), font=("copperplate Gothic Bold",22),bg="#CCFF90")
        scorev.place(x=330,y=210)

        def scholor():
            sch1 = Label(result_window,text="Congratulations", font=("copperplate Gothic Bold",22),fg='#FFB900',bg="#CCFF90")
            sch1.place(x=140,y=260)
            sch1 = Label(result_window,text="You're Eligible To Get", font=("copperplate Gothic Bold",22),bg="#CCFF90")
            sch1.place(x=100,y=300)
            sch2 = Label(result_window,text=f'{schlr_percent}% Scholarship...', font=("copperplate Gothic Bold",22),bg="#CCFF90")
            sch2.place(x=130,y=340)

        def failed():
            sch1 = Label(result_window,text="You Have Failed!", font=("copperplate Gothic Bold",28),fg="#FF0505",bg="#CCFF90")
            sch1.place(x=110,y=290)
            sch1 = Label(result_window,text="Better Luck Next Time...", font=("copperplate Gothic Bold",28),fg="#FFB900",bg="#CCFF90")
            sch1.place(x=50,y=330)

        if score >=50:
            scholor()
        else:
            failed()

        tnk = Label(result_window,text="Thank You...", font=("copperplate Gothic Bold",36),fg="purple",bg="#CCFF90")
        tnk.place(x=120,y=480)
        result_window.mainloop()

    def on_close(self):
        self.root.destroy()
        self.main_window.deiconify()

t = Tk()
t.configure(bg='#3FFFF3')
t.title("NOBI CENTRE")
t.geometry("1380x800")
t.resizable(False,False)

image_path = "disney_princess.jpg"
# image_path = "C:\\Users\\sanju\\Pictures\\Saved Pictures\\crt.jpg"
# image_path = "D:\\Desktop\\Codes\\Projects\\Suji\\disney_princess.jpg"
image = Image.open(image_path)
desired_width = 300
desired_height = 200

image = image.resize((desired_width, desired_height))
tk_image = ImageTk.PhotoImage(image)

label = Label(t, image=tk_image)
label.place(x=35, y=20)
l = Label(t, text="NOBI CENTRE", font=("Copperplate Gothic Bold", 90), fg="#6308B8", bg="#3FFFF3")
l.place(x=340, y=20)

l1 = Label(t, text="COMPUTER EDUCATION", font=("Copperplate Gothic Bold", 40), fg="#663399", bg="#3FFFF3")
l1.place(x=450, y=160)

l2 = Label(t, text="WELCOME TO TECHNICAL EVALUATION", font=("Copperplate Gothic Bold", 40), bg="#3FFFF3")
l2.place(x=110, y=300)

# l2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
l3 = Label(t, text="ALL THE BEST", font=("Copperplate Gothic Bold", 35),fg="#FF0055", bg="#3FFFF3")
l3.place(x=480, y=420)

# l3.place(relx = 0.5, rely = 0.5, anchor = CENTER)
l4 = Label(t, text="LET'S  WE ", font=("Copperplate Gothic Bold", 30), bg="#3FFFF3")
l4.place(x=420, y=550)

b = Button(t, text="Register", font=("copperplate gothic bold", 22), width=10, bg="#DD7BFF", command=open_second_window)
b.place(x=665, y=550)

# t.state('zoomed')
# ico = PhotoImage(file = 'c:\\Users\\sanju\\Pictures\\Saved Pictures\\qm.png') 
# ico = PhotoImage(file = 'D:\\Desktop\\Codes\\Projects\\Suji\\qm.png') 
ico = PhotoImage(file = 'qm.png') 
t.iconphoto(True, ico) 
t.mainloop()

