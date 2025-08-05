from tkinter import *;from tkinter.ttk import Combobox;from time import time,strftime,localtime;import time,questions as q,os,configparser
class Quiz(): 
    def __init__(self,root): 
        self.error_message="";config=configparser.ConfigParser();config.read('settings.ini')
        try:self.mode=str(config['settings']['mode']);self.amount=int(config['settings']['amount']);self.difficulty=int(config['settings']['difficulty']);self.password=str(config['settings']['password']);self.do_name=config.getboolean('settings','name');self.do_save=config.getboolean('settings','save');self.do_results=config.getboolean('settings','results');self.color=str(config['settings']['color'])
        except(ValueError,KeyError)as e:self.error_message="Error reading settings.ini:\n"+str(e);self.mode="quiz";self.amount=5;self.difficulty=2;self.password=str(config['settings']['password']);self.do_name=True;self.do_save=True;self.do_results=True;self.color="grey"
        global background_color;background_color="#b3b3b3"if self.color=="grey"else self.color
        self.answers=q.Answers if self.mode=="quiz"else(q.gen_questions(),q.Math_Answers)[1] if self.mode=="math"else None;self.questions=q.Questions if self.mode=="quiz"else(q.gen_questions(),q.Math_Questions)[1] if self.mode=="math"else None
        self.results=[];self.start_time=0.0;self.start_date="";self.counter=0;self.length=len(self.questions);self.correct=0;self.incorrect=0;self.early_finish=False;self.name="";self.name_said=False;self.name_done=False;self.answer_length=30
        root.geometry("360x300");root.configure(bg=background_color)if self.color!="error"else(root.configure(bg="#b3b3b3"),setattr(self,"color","error"))
        self.quiz_frame=Frame(padx=10,pady=10,bg=background_color);self.quiz_frame.grid()
        self.quiz_heading=Label(self.quiz_frame,text="Quiz Program",font=("arial","25"),bg=background_color);self.quiz_heading.grid(row=0)
        self.quiz_entry=Entry(self.quiz_frame,font=("Arial","26"),width=(12));self.quiz_entry.grid(row=2,padx=1,pady=1)
        self.quiz_entry_instructions_color=Label(self.quiz_frame,text="Please enter your answer above",font=("arial","12"),fg="#FFFF00",bg=background_color);self.quiz_entry_instructions_color.grid(row=3,padx=1,pady=1)
        self.quiz_entry_instructions_color.config(text="Color setting invalid, defaulting to grey.",fg="#FF0000")if self.color=="error"and self.error_message==""else None
        self.quiz_entry_instructions_color.config(fg="#000000")if self.color=="white"or self.color=="#FFFFFF"else None
        self.quiz_entry_instructions_color.config(text=self.error_message,fg="#FF0000")if self.error_message!=""else None
        self.quiz_instructions=Label(self.quiz_frame,text="Press start quiz to start answering questions!",font=("arial","22"),wraplength=350,width=20,height=3,bg=background_color);self.quiz_instructions.grid(row=4)
        self.button_frame=Frame(self.quiz_frame,bg=background_color);self.button_frame.grid(sticky="ew")
        self.buttonswitch_left("default");self.buttonswitch_right("default")
    def buttonswitch_right(self,case): 
        l=[["results","#aaaeff",lambda:self.open_results(),"normal"],["finish","#ffe600",lambda:[setattr(self,"early_finish",True),self.buttonswitch_left("end"),self.open_results()],"normal"]];self.right_button_ref_list=[]
        state=0 if case=="default"else(1 if case=="finish"else 0);self.make_button=Button(self.button_frame,text=l[state][0],bg=l[state][1],fg="#000000",font=("Arial",20,"bold"),width=9,state=l[state][3],command=l[state][2]);self.make_button.grid(padx=3,row=0,column=1);self.right_button_ref_list.append(self.make_button)
    def buttonswitch_left(self,case): 
        l=[["Start Quiz","#00ff08",lambda:[self.buttonswitch_left("begin"),self.question_answer()],"normal"],["Submit","#00ff08",lambda:self.question_answer(),"normal"],["Submit","#00ff08",lambda:print("how did you press this??"),"disabled"]];self.left_button_ref_list=[]
        state=0 if case=="default"else(1 if case=="begin"else(2 if case=="end"else 0));self.buttonswitch_right("finish")if case=="begin"else None;self.start_time=time.time()if case=="begin"else None;self.start_date=strftime("%Y-%m-%d %H:%M:%S",localtime())if case=="begin"else None;self.buttonswitch_right("default")if case=="end"else None;self.write_to_file(self.results)if case=="end"else None;root.unbind('<Return>')if case=="end"else None;self.quiz_entry.config(state=DISABLED)if case=="end"else None
        self.make_button=Button(self.button_frame,text=l[state][0],bg=l[state][1],fg="#000000",font=("Arial",20,"bold"),width=9,state=l[state][3],command=l[state][2]);self.make_button.grid(padx=3,row=0,column=0);self.left_button_ref_list.append(self.make_button)
    def open_results(self): ResultsWindow(root)if self.do_results else None
    def open_settings(self): SettingsWindow(root)
    def blank_checker(self):b=bool(self.quiz_entry.get().strip());self.quiz_entry_instructions_color.config(text="this cannot be blank.",fg="#FF0000")if b else None;return b
    def question_answer(self):
        d=[];c=self.counter
        if c==0 and self.quiz_entry.get()==self.password:
            self.open_settings()
            return
        if not self.blank_checker()and c>0:self.quiz_entry_instructions_color.config(text="this cannot be blank.",fg="#FF0000");return
        if self.blank_checker()and c>0 and self.mode=="math": 
            try:int(self.quiz_entry.get())
            except ValueError:self.quiz_entry_instructions_color.config(text="this must be a number.",fg="#FF0000");return
        if c==0 and self.do_name:self.quiz_instructions.config(text="Please submit your name.");root.bind('<Return>',lambda event:self.question_answer())
        if self.name_said: 
            if not self.blank_checker():self.quiz_entry_instructions_color.config(text="this cannot be blank.",fg="#FF0000");return
            self.name=self.quiz_entry.get()[0:self.answer_length];self.quiz_entry.delete(0,END);self.quiz_entry_instructions_color.config(fg="#000000")if self.color=="white"or self.color=="#FFFFFF"else self.quiz_entry_instructions_color.config(text="Please enter your answer above",fg="#FFFF00");self.quiz_instructions.config(text="Press start quiz to start answering questions!");self.name_done=True
        self.name_said=True if c==0 and self.do_name else self.name_said
        if self.name_done or not self.do_name: 
            if not self.name_done:self.name="disabled";root.bind('<Return>',lambda event:self.question_answer())
            if c<self.length: 
                if c==0:self.start_taken_time=time.time()
                self.quiz_instructions.config(text=self.questions[c],fg="#9C0000")
            if c>0: 
                cl1=c-1;answer=self.quiz_entry.get().strip().lower()[0:self.answer_length];self.quiz_entry_instructions_color.config(text="Please enter your answer above",fg="#FFFF00");d.append([c,self.questions[cl1],answer]);self.quiz_entry.delete(0,END);correct_answer=self.answers[cl1]
                end_taken_time=time.time()
                if answer in correct_answer:self.quiz_entry_instructions_color.config(text="Correct!",fg="#00ff08");d.append(["correct"]);self.correct+=1
                else:self.quiz_entry_instructions_color.config(text="Incorrect!",fg="#ff0000");d.append(["incorrect"]);self.incorrect+=1
                elapsed_time=end_taken_time-self.start_taken_time;minutes=int(elapsed_time//60);seconds=round(elapsed_time%60,2);d.append([minutes,seconds]);d=sum(d,[]);self.results.append(d);self.start_taken_time=time.time();print(d)
            self.counter+=1
            if self.counter>self.length:self.buttonswitch_left("end");self.open_results();self.quiz_entry.config(state=DISABLED);self.quiz_entry_instructions_color.config(text="Quiz Finished! go to results page for results!",fg="#00FFFF")if self.do_results else self.quiz_entry_instructions_color.config(text="Quiz Finished! Talk to your operator!",fg="#00FFFF")
    def write_to_file(self,data): 
        if not self.do_save:return
        with open("results.txt","a")as r: 
            end_time=time.time();elapsed_time=end_time-self.start_time;elapsed_minutes=int(elapsed_time//60);elapsed_seconds=round(elapsed_time%60,2);date=self.start_date
            r.write(f"""\n-------------------------------------------TEST RESULTS----------------------------------------------------------\nName: {self.name}\nTest started: {date}\nQuestions correct: {self.correct}/{self.length}\nThe formatting is as follows:\nQuestion Number : Question Text : Given Answer : Correct or Wrong : minutes : seconds\n""")
            for tracker in range(len(data)):r.write(f"\n{data[tracker][0]} : {data[tracker][1]} : {data[tracker][2]} : {data[tracker][3]} : {data[tracker][4]} : {data[tracker][5]}\n")
            early_finish_text="Quiz was finished early."if self.early_finish else"";r.write(f"\n\nTest Finished in: {elapsed_minutes} minutes and {elapsed_seconds} seconds.\n{early_finish_text}\n\n")
            with open("summary_results.txt","a")as r:r.write(f"{strftime('%m-%d',localtime())}: {self.correct}/{self.length} Questions Correct.\n")
class ResultsWindow(): 
    def __init__(self,parent): 
        self.results_window=Toplevel(parent);self.results_window.title("Results");self.results_window.geometry("360x425");self.results_window.configure(bg=background_color)
        self.results_frame=Frame(bg=background_color,master=self.results_window);self.results_frame.grid(sticky="n")
        self.results_window.grid_rowconfigure(0,weight=1);self.results_window.grid_columnconfigure(0,weight=1)
        self.results_heading=Label(self.results_frame,text="Results",font=("arial","25"),bg=background_color);self.results_heading.grid(row=0,column=0,sticky="n")
        self.results_label=Label(self.results_frame,text="These are the results of the 5 most \n recent quizzes out of X total\n quizzes, the lower the older.",font=("arial","14"),justify="left",wraplength=350,bg=background_color);self.results_label.grid(row=1,column=0)
        self.results_list=Listbox(self.results_frame,font=("Arial","14"),width=27,height=5,bg='lime');self.results_list.grid(row=2,column=0,padx=1,pady=1)
        def show_results(): 
            with open("summary_results.txt","r")as r:lines=r.readlines();[self.results_list.insert(END,lines[-(i+1)].strip())or(self.results_list.config(bg='#f6edab')if i>=4 else None)for i in range(min(5,len(lines)))]
        show_results()
        def restart_quiz():[w.destroy()for w in root.winfo_children()];Quiz(root)
        self.results_info=Label(self.results_frame,text="You can see more in-depth results (what \nquestions were wrong specifically) by \ngoing to the file. If the box is yellow, then \nthere are more results in the file than shown here.",font=("arial","14"),justify="left",wraplength=350,bg=background_color);self.results_info.grid(row=3,column=0)
        self.results_button_frame=Frame(self.results_frame,background=background_color);self.results_button_frame.grid(sticky="ew",row=4)
        l=[["Restart","#f44336",lambda:restart_quiz(),"0","0"],["To File","#aaaeff",lambda:os.startfile("results.txt"),"0","1"]];self.button_ref_list=[]
        [Button(self.results_button_frame,text=i[0],bg=i[1],fg="#000000",font=("Arial",20,"bold"),width=9,command=i[2]).grid(row=i[3],column=i[4],padx=5,pady=5)for i in l]
class SettingsWindow(): 
    def __init__(self,parent): 
        config=configparser.ConfigParser();config.read('settings.ini');self.config_list=[config['settings']['mode'],config['settings']['name'],config['settings']['save'],config['settings']['results'],config['settings']['amount'],config['settings']['difficulty'],config['settings']['password'],config['settings']['color']]
        self.settings_window=Toplevel(parent);self.settings_window.title("Settings");self.settings_window.geometry("460x410");self.settings_window.configure(bg=background_color)
        self.settings_frame=Frame(bg=background_color,master=self.settings_window);self.settings_frame.pack(fill="both",expand=True)
        def restart_quiz():[w.destroy()for w in root.winfo_children()];Quiz(root)
        self.settings_heading=Label(self.settings_frame,text="Settings",font=("arial","25"),bg=background_color);self.settings_heading.pack(pady=(5,0))
        self.settings_label=Label(self.settings_frame,text="This is the settings window, you can change several settings down below.",font=("arial","14"),justify="left",wraplength=350,bg=background_color);self.settings_label.pack(pady=(0,10))
        self.settings_label_ref_list=[]
        def create_labels(type): 
            label_row_frame=Frame(self.settings_frame,bg=background_color);label_row_frame.pack(fill="x")
            labels=["Mode","Name","Save","Results"]if type=="optionmenus"else["Amount","Length","Password","Color"]
            [self.settings_label_ref_list.append(Label(label_row_frame,text=l,font=("arial",14),wraplength=350,bg=background_color,anchor="center"))or self.settings_label_ref_list[-1].pack(side=LEFT,expand=True,fill="x",padx=5)for l in labels]
        create_labels("optionmenus")
        self.optionmenu_frame=Frame(self.settings_frame,bg=background_color);self.optionmenu_frame.pack(fill="x",pady=(5,0));self.optionmenus_ref_dict={}
        def create_optionmenus(): 
            optionmenus=[["mode","quiz","math",0,0],["name","True","False",0,1],["save","True","False",0,2],["results","True","False",0,3]]
            for i in range(len(optionmenus)): 
                default_state=StringVar();default_state.set(self.config_list[i])
                self.optionmenu=OptionMenu(self.optionmenu_frame,default_state,optionmenus[i][1],optionmenus[i][2]);self.optionmenu.config(font=("arial",12),bg=background_color,fg="#000000",highlightthickness=0,bd=1,width=6,relief="groove");self.optionmenu["menu"].config(font=("arial",12),bg=background_color,fg="#000000");self.optionmenu.pack(side=LEFT,expand=True,fill="x",padx=5);self.optionmenus_ref_dict.update({optionmenus[i][0]:self.optionmenu})
        create_labels("comboboxes")
        self.comboboxes_frame=Frame(self.settings_frame,bg=background_color);self.comboboxes_frame.pack(fill="x",pady=(5,0));self.comboboxes_ref_dict={}
        def create_comboboxes(): 
            comboboxes=[["amount","5","10","15","20",0,0],["length","5","10","15","20",0,1],["password","","","","",0,2],["color","grey","white","black","green",0,3]]
            for i in range(len(comboboxes)): 
                counter=i+4;default_state=StringVar();default_state.set(comboboxes[i][0])
                self.comboboxes=Combobox(self.comboboxes_frame,values=[comboboxes[i][1],comboboxes[i][2],comboboxes[i][3],comboboxes[i][4]],font=("arial",12),width=8);self.comboboxes.pack(side=LEFT,expand=True,fill="x",padx=5);self.comboboxes.set(self.config_list[counter]);self.comboboxes_ref_dict.update({comboboxes[i][0]:self.comboboxes})
        self.settings_mode_info=Label(self.settings_frame,text="The mode setting allows the 'quiz' and 'math' modes, quiz will run thequestions set in questions.py, while math with randomly generate math questions. Read README.txt for explanation on what the settings do.",font=("arial",14),justify="left",wraplength=450,bg=background_color);self.settings_mode_info.pack(pady=(10,0))
        self.settings_button_frame=Frame(self.settings_frame,background=background_color);self.settings_button_frame.pack(pady=(10,0));self.button_ref_list=[]
        settings_button_details_list=[["Exit","#f44336",lambda:restart_quiz(),"0","0"],["Apply","#aaaeff",lambda:apply_changes(),"0","1"]];self.button_ref_list=[]
        [Button(self.settings_button_frame,text=i[0],bg=i[1],fg="#000000",font=("Arial",20,"bold"),width=9,command=i[2],anchor="center",justify="center").pack(side=LEFT,expand=True,fill="x",padx=10)for i in settings_button_details_list]
        def input_checker(input):error=False;[self.settings_label_ref_list[i].config(fg="red")or self.settings_label.config(fg="red",text="There are settings left blank, the errors are indicated in red.")or(error:=True)if input[i]==""else None for i in range(len(input))];[self.settings_label_ref_list[i].config(fg="red")or self.settings_label.config(fg="red",text="There are letters where there shouldnt be, the errors are indicated in red.")or(error:=True)if i in[4,5]and not input[i].isdigit()else None for i in range(len(input))];return not error
        def apply_changes():
            input_list=[i.get()for i in self.comboboxes_ref_dict.values()];input_list[1]=input_list[1]=="True";input_list[2]=input_list[2]=="True";input_list[3]=input_list[3]=="True";input_list[4]=int(input_list[4]);input_list[5]=int(input_list[5]);self.config_list=input_list
            if input_checker(input_list): 
                config=configparser.ConfigParser();config.read('settings.ini')
                [config['settings'].update({list(config['settings'].keys())[i]:str(input_list[i])})for i in range(len(input_list))];with open('settings.ini','w')as f:config.write(f)
                self.settings_label.config(fg="green",text="Settings applied, restart the program for some changes to take effect.")
                [self.optionmenus_ref_dict[list(self.optionmenus_ref_dict.keys())[i]].set(input_list[i])for i in range(len(input_list))];[self.comboboxes_ref_dict[list(self.comboboxes_ref_dict.keys())[i]].set(input_list[i+4])for i in range(4)]
                def close_settings():self.settings_window.destroy();root.deiconify();root.quit()
                root.withdraw();self.settings_window.protocol("WM_DELETE_WINDOW",close_settings)
                self.settings_window.grab_set()
                self.settings_window.focus_force()
                self.settings_window.transient(root)
                root.update()
                self.settings_window.wait_window()
                root.deiconify()
                root.focus_force()
                root.update()
        def close_settings():self.settings_window.destroy();root.deiconify();root.quit()
        self.settings_window.protocol("WM_DELETE_WINDOW",close_settings)
        self.settings_window.grab_set()
        self.settings_window.focus_force()
        self.settings_window.transient(root)
        root.update()
        self.settings_window.wait_window()
        root.deiconify()
        root.focus_force()
        root.update()
def apply_changes():
    input_list=[i.get()for i in root.children['!frame2'].children.values()];input_list[1]=input_list[1]=="True";input_list[2]=input_list[2]=="True";input_list[3]=input_list[3]=="True";input_list[4]=int(input_list[4]);input_list[5]=int(input_list[5])
    config=configparser.ConfigParser();config.read('settings.ini')
    [config['settings'].update({list(config['settings'].keys())[i]:str(input_list[i])})for i in range(len(input_list))];with open('settings.ini','w')as f:config.write(f)
    root.children['!frame2'].children['!label'].config(fg="green",text="Settings applied, restart the program for some changes to take effect.")
    [root.children['!frame2'].children['!optionmenu'+str(i)].set(input_list[i])for i in range(4)];[root.children['!frame2'].children['!combobox'+str(i)].set(input_list[i+4])for i in range(4)]
root=Tk();Quiz(root);root.mainloop()