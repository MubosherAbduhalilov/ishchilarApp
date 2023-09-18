import sqlite3
from datetime import datetime
from tkinter import *
root=Tk()
root.configure(bg='#ACFFEC')
conn=sqlite3.connect("ishchi_malumotlari.db")
conn1=sqlite3.connect("keldi_ketdi.db")
conn2=sqlite3.connect("ishchilar_keldi_ketdisi.db")
cur=conn.cursor()
cur1=conn1.cursor()
cur2=conn2.cursor()
def reg():
	def ishchilar_qoshish():
		k=fne.get().split()
		c=''
		for i in k:
			c+=i
		if fne.get() == '' or fne.get().isspace() or not c.isalpha() or tre.get() == '' or tre.get().isspace() or not tre.get().isdigit() or om_e.get() == '' or tre.get().isspace() or not om_e.get().isdigit() or len(fne.get().split())!=2:
			xatolik["text"] = "nom, telefon raqam yoki oylik maosh xato!!!"
		else:
			cur.execute("Select * From Info")
			info_len=len(cur.fetchall())
			cur.execute(f"Insert into Info Values({info_len+1},'{fne.get()}',{tre.get()},0,0,'100',{om_e.get()},'0')")
			conn.commit()
			fne.delete(0,END)
			tre.delete(0, END)
			om_e.delete(0,END)
			xatolik["text"] = "Bazaga muvaffaqiyatli qo\'shildi"
	top=Toplevel()
	top.geometry("550x400")
	top.configure(bg='#ACFFEC')
	lbl=Label(top,text="Ro\'yxatdan o'tish",font=("consolass",20,"bold"),bg='#ACFFEC',width=32)
	lbl.grid(row=0,column=0,columnspan=2,pady=(15,10))
	xatolik = Label(top,font=("consolass", 13, "bold"),foreground="red",bg='#ACFFEC', width=48)
	xatolik.grid(row=1, column=0, columnspan=2)
	fn=Label(top,text="To\'liq nom",font=("consolass",18,"bold"),bg='#ACFFEC')
	fn.grid(row=2,column=0,padx=(10,5),pady=(10,3))
	fne=Entry(top,cursor="hand2",font=("consolass",18,"bold"),width=25)
	fne.grid(row=2,column=1,padx=(10,5),pady=(10,3))
	ogoh = Label(top,text="To\'liq nom-ism va familiya, ular orasida bo\'sh joy bo\'lishi shart",font=("consolass", 13, "bold"), foreground="red", bg='#ACFFEC', width=48)
	ogoh.grid(row=3, column=0, columnspan=2)
	tr=Label(top,text="Telefon raqam",font=("consolass",18,"bold"),bg='#ACFFEC')
	tr.grid(row=4,column=0,padx=(10,5),pady=(10,3))
	tre=Entry(top,cursor="hand2",font=("consolass",18,"bold"),width=25)
	tre.grid(row=4,column=1,padx=(10,5),pady=(10,3))
	ogoh = Label(top,text="Telefon raqam - faqat raqam bo\'lishi kerak.(bo\'sh kataklarsiz)",font=("consolass", 13, "bold"), foreground="red", bg='#ACFFEC', width=48)
	ogoh.grid(row=5, column=0, columnspan=2)
	om = Label(top, text="Oylik maosh", font=("consolass", 18, "bold"), bg='#ACFFEC')
	om.grid(row=6, column=0, padx=(10, 5), pady=(10, 3))
	om_e = Entry(top, cursor="hand2", font=("consolass", 18, "bold"), width=25)
	om_e.grid(row=6, column=1, padx=(10, 5), pady=(10, 3))
	ogoh = Label(top,text="Oylik maosh - faqat raqam bo\'lishi kerak.(bo\'sh kataklarsiz)",font=("consolass", 13, "bold"), foreground="red", bg='#ACFFEC', width=48)
	ogoh.grid(row=7, column=0, columnspan=2)
	bq=Button(top,text="Bazaga qo\'shish",font=("consolass",18,"bold"),width=20,command=ishchilar_qoshish,bg="#A2FF82")
	bq.grid(row=8,columnspan=2,pady=(10,3))
def bir(ls):
	b=''
	for i in ls:
		b+=i
	return b.isdigit()
def malumotlar():
	top=Toplevel()
	top.geometry("500x240")
	top.configure(bg=root['bg'])
	def searching_from_base():
		top.geometry("500x400")
		if len(qach_e.get().split())==3 and bir(qach_e.get().split()):
			cur2.execute(f'Select * From Keldi_ketdi Where toliq_nom == "{kimdir_e.get()}" And kun == "{qach_e.get()}"')
			f3=cur2.fetchall()
			if len(f3)!=0:
				for i in range(len(f3)):
					f=list(f3[i])
					if f[1]==kimdir_e.get():
						kimdir_e.delete(0,END)
						qach_e.delete(0,END)
						ism=Label(top,text=f'Ism-familiya - {f[1]}',font=("consolass",18,"bold"),bg=top['bg'])
						ism.grid(row=5, columnspan=2,sticky="W",padx=(15,15))
						telraq = Label(top, text=f'Telefon raqam - {f[2]}', font=("consolass", 18, "bold"),bg=top['bg'])
						telraq.grid(row=6, columnspan=2,sticky="W",padx=(15,15))
						sana=f[3].split()
						Sana = Label(top, text=f'Sana - {sana[0]}-yil {sana[1]}-oy {sana[2]}-kun', font=("consolass", 18, "bold"),bg=top['bg'])
						Sana.grid(row=7, columnspan=2,sticky="W",padx=(15,15))
						kel = Label(top, text=f'Keldi - {f[4]}', font=("consolass", 18, "bold"),bg=top['bg'])
						kel.grid(row=8, columnspan=2,sticky="W",padx=(15,15))
						ket = Label(top, text=f'Ketdi - {f[5]}', font=("consolass", 18, "bold"),bg=top['bg'])
						ket.grid(row=9, columnspan=2,sticky="W",padx=(15,15))
			else:
				xatolik3['text']='Xato kiritdingiz yoki bu ishchi yoki sana bazada mavjud emas'
		else:
			xatolik3['text'] = 'Sanani xato kiritdingiz'

	mal_l=Label(top,text="Ishchilarning ma\'lumotlarini olish",font=("consolass",19,"bold"),width=32,bg=root['bg'])
	mal_l.grid(row=0,columnspan=2,pady=(15,5))
	cur.execute("Select * From Info")
	conn.commit()
	if len(cur.fetchall())>0:

		xatolik3=Label(top,font=("consolass",13,"bold"),bg=root['bg'],fg='red')
		xatolik3.grid(row=1,columnspan=2,pady=(3,3))
		kimdir=Label(top,text="Ishchini kiriting",font=("consolass",16,"bold"),bg=root['bg'])
		kimdir.grid(row=2,column=0,pady=(5,5),padx=(15,15))
		kimdir_e = Entry(top, font=("consolass", 16, "bold"),width=20)
		kimdir_e.grid(row=2, column=1)
		qach = Label(top, text="Sana yil oy kun", font=("consolass", 16, "bold"), bg=root['bg'])
		qach.grid(row=3, column=0, pady=(5, 5), padx=(15, 15))
		qach_e = Entry(top, font=("consolass", 16, "bold"), width=20)
		qach_e.grid(row=3, column=1)
		ogoh = Label(top,text='Sana faqat raqam bo\'lishi shart. Masalan: 2022 6(06 emas) 12.', font=("consolass", 13, "bold"), bg=root['bg'], fg='red')
		ogoh.grid(row=4, columnspan=2)
		qach_e.bind('<Return>',lambda event: searching_from_base())
	else:
		xatolik2 = Label(top, text="Afsuski, bazada ishchilar yo\'q,\nasosiy oynaga o\'tib ishchilar qo\'shing",font=("consolass", 16, "bold"), bg=top["bg"], fg="red")
		xatolik2.grid(row=1, column=0, pady=(10, 10), padx=(40, 0))
def time_minus_time(ft,lt):
	bta=int(ft)-int(lt)
	bt=int(str(ft)[str(ft).index('.') + 1:])
	qt=int(str(lt)[str(lt).index('.') + 1:])
	c=0
	if bt==0 and qt!=0:
		bt=60
		c=1
	if qt==0 and bt !=0:
		qt=60
		c=1
	if len(str(bt))==1:
		bt=int(str(bt)+'0')
	if len(str(qt))==1:
		qt=int(str(qt)+'0')
	if len(str(bt-qt))==1:
		bt_m_qt=int(((bt-qt)/6)*10)
	else:
		bt_m_qt=int(((bt-qt)/60)*10)
	return float(f'{bta-c}.{bt_m_qt}')
def ish_mal(bkv,bktv):
	root.geometry("550x450")
	def yangilash():
		cur1.execute("Delete From Ish_Mal")
		conn1.commit()
		fr.destroy()
		kel_va_ket()
	def keldi_ketdi():
		global count1
		def keldi_ketdilar():
			def toldirish():
				now = datetime.now()
				cur.execute('Select * From Info')
				conn.commit()
				s = cur.fetchall()
				ls=[]
				ls1=[]
				for i in s:
					ls1.append(i[1])
					if i[-1]!=str(now.year)+' '+str(now.month)+' '+str(now.day):
						ls.append(i[1])
				def baz_joy():
					if '.' not in keldi_e.get() or '.' not in ketdi_e.get() or keldi_e.get()[-1]=='.' or ketdi_e.get()[-1]=='.':
						xatolik3['text'] = "Xato kiritildi!!!"
					else:
						try:
							float(keldi_e.get())
							float(ketdi_e.get())
							now = datetime.now()
							cur1.execute("Select * From Ish_Mal")
							f=cur1.fetchall()
							jami_k_v=time_minus_time(float(f[0][1]),float(f[0][0]))*3600
							n=nom['text'].split()[:2]
							n=n[0] + ' ' + n[1]
							cur.execute(f"Select * From Info Where toliq_nom=='{n}'")
							f1=cur.fetchall()
							ikv=f1[0][3];jmv=f1[0][4]
							oraliq=time_minus_time(float(ketdi_e.get()),float(keldi_e.get()))*3600;ik=(ikv+oraliq)/((jmv+jami_k_v)/100)
							cur.execute(f"Update Info Set ishga_kelgan_vaqtlari={ikv+oraliq},ish_koeffitsenti={ik},jami_vaqt={jmv+jami_k_v},kun='{str(now.year)+' '+str(now.month)+' '+str(now.day)}' Where toliq_nom=='{n}'")
							cur2.execute("Select * From Keldi_ketdi")
							f2=cur2.fetchall()
							keldi_ketdi_len=len(f2)
							cur2.execute(f"Insert into Keldi_ketdi Values({keldi_ketdi_len+1},'{f1[0][1]}',{f1[0][2]},'{str(now.year)+' '+str(now.month)+' '+str(now.day)}','{keldi_e.get()}','{ketdi_e.get()}')")
							conn.commit()
							conn1.commit()
							conn2.commit()
							nom.destroy();xatolik3.destroy();keldi.destroy();keldi_e.destroy();ketdi.destroy();ketdi_e.destroy();ogoh.destroy();btn.destroy()
							keldi_ketdilar()
						except:
							xatolik3['text'] = "Xato kiritildi!!!"
				cur1.execute("Select * From Ish_Mal")
				f = cur1.fetchall()
				if len(s)!=0:
					if ishchi_e.get() in ls:
						nom = Label(top, text=f"{ishchi_e.get()}\nkelish: {f[0][0]}, ketish: {f[0][1]}", font=("consolass", 18, "bold"), bg=top["bg"], width=32)
						nom.grid(row=1, columnspan=2, pady=(5, 10), padx=(10, 10))
						xatolik3 = Label(top, font=("consolass", 13, "bold"), bg=top["bg"], fg="red")
						xatolik3.grid(row=2, columnspan=2)
						keldi = Label(top, text="Keldi", font=("consolass", 18, "bold"), bg=top["bg"])
						keldi.grid(row=3, column=0, pady=(10, 10), padx=(10, 10), sticky="W")
						keldi_e = Entry(top, font=("consolass", 18, "bold"), width=20)
						keldi_e.grid(row=3, column=1, pady=(10, 10))
						ketdi = Label(top, text="Ketdi", font=("consolass", 18, "bold"), bg=top["bg"])
						ketdi.grid(row=4, column=0, pady=(10, 10), padx=(10, 10), sticky="W")
						ketdi_e = Entry(top, font=("consolass", 18, "bold"), width=20)
						ketdi_e.grid(row=4, column=1, pady=(10, 0))
						ogoh = Label(top, text="Faqat raqamdan iborat vaqtni kiriting.Masalan 8.00,9.30.", font=("consolass", 13, "bold"), bg=top["bg"],fg="red")
						ogoh.grid(row=5, columnspan=2)
						btn = Button(top, text="Bazaga joylash", font=("consolass", 15, "bold"), bg='#A2FF82',command=baz_joy)
						btn.grid(row=6, column=1, pady=(10, 10), padx=(10, 10))
						ishchi.destroy()
						ishchi_e.destroy()
						qid.destroy()
						exit.destroy()
					elif ishchi_e.get() in ls1:
						xatolik1 = Label(top, text="Bu ishchining keldi-ketdisi to\'ldirib bo\'lingan",
										 font=("consolass", 13, "bold"), bg=top["bg"], fg="red")
						xatolik1.grid(row=4, columnspan=2, pady=(10, 10), padx=(10, 0))
					else:
						xatolik1 = Label(top, text="Afsuski bazada bunday ishchi mavjud emas",
										 font=("consolass", 13, "bold"), bg=top["bg"], fg="red")
						xatolik1.grid(row=4, columnspan=2, pady=(10, 10), padx=(10, 0))

			cur.execute('Select * From Info')
			conn.commit()
			ls1 = cur.fetchall()
			if len(ls1) == 0:
				xatolik2 = Label(top, text="Afsuski, bazada ishchilar yo\'q,\nasosiy oynaga o\'tib ishchilar qo\'shing",
								 font=("consolass", 16, "bold"), bg=top["bg"], fg="red")
				xatolik2.grid(row=1, column=0, pady=(10, 10), padx=(40, 0))
			else:
				ishchi = Label(top, text="Ishchini kiriting", font=("consolass", 16, "bold"), bg=root['bg'])
				ishchi.grid(row=1, column=0,pady=(10,10))
				ishchi_e = Entry(top, font=("consolass", 16, "bold"), width=20)
				ishchi_e.grid(row=1, column=1,pady=(10,10))
				qid = Button(top, text="Qidirish", font=("consolass", 16, "bold"), bg='#A2FF82', command=lambda:toldirish(),width=17)
				qid.grid(row=2, column=0, padx=(10, 10), pady=(5, 5))
				exit = Button(top, text="Chiqish", font=("consolass", 16, "bold"), bg='#A2FF82',command=lambda: top.destroy(),width=17)
				exit.grid(row=2, column=1, padx=(10, 10), pady=(5, 5))
		top=Toplevel()
		top.geometry("500x350")
		top.configure(bg=root["bg"])
		now = datetime.now()
		keldi_ketdi_l=Label(top,text=f"Keldi-Ketdi {now.year}-yil {now.month}-oy {now.day}-kun",font=("consolass",20,"bold"),bg=top["bg"],width=28)
		keldi_ketdi_l.grid(row=0,columnspan=2,pady=(10,0))
		keldi_ketdilar()
	def change_info():
		top=Toplevel()
		top.geometry('510x200')
		top.configure(bg=root['bg'])
		def searching_from_base():
			top.geometry('500x420')
			def change():
				if om_e.get() == '' or not om_e.get().isdigit() or om_e.get().isspace():
					ogoh["text"] = "nom, telefon raqam yoki oylik maosh xato!!!"
				else:
					cur.execute(f"Update Info Set oyligi = {om_e.get()} Where toliq_nom == '{f3[0][1]}'")
					om.destroy()
					om_e.destroy()
					btn1.destroy()
					ogoh1.destroy()
			def change1():
				if tr_e.get() == '' or tr_e.get().isspace() or not tr_e.get().isdigit():
					ogoh["text"] = "nom, telefon raqam yoki oylik maosh xato!!!"
				else:
					cur.execute(f"Update Info Set telefon_raqam = {tr_e.get()} Where toliq_nom == '{f3[0][1]}'")
					tr.destroy()
					tr_e.destroy()
					btn.destroy()
					ogoh.destroy()
			cur.execute(f'Select * From Info Where toliq_nom == "{kimdir_e.get()}"')
			f3 = cur.fetchall()
			if len(f3) != 0:
				kimdir_e.delete(0, END)
				ism = Label(top, text=f'Ism-familiya - {f3[0][1]}', font=("consolass", 18, "bold"), bg=top['bg'])
				ism.grid(row=4, columnspan=2, sticky="W", padx=(15, 15))
				tr = Label(top, text="Telefon raqam", font=("consolass", 18, "bold"), bg=root['bg'])
				tr.grid(row=5, column=0, padx=(10, 10))
				tr_e = Entry(top, font=("consolass", 18, "bold"), width=20)
				tr_e.grid(row=5, column=1)
				ogoh = Label(top, text="Telefon raqam - faqat raqam bo\'lishi kerak.(bo\'sh kataklarsiz)",font=("consolass", 13, "bold"), foreground="red", bg='#ACFFEC', width=48)
				ogoh.grid(row=6, column=0, columnspan=2)
				btn = Button(top, text="O\'zgartirish", font=("consolass", 15, "bold"), bg='#A2FF82', command=change1)
				btn.grid(row=7, column=1, padx=(10, 10),pady=(5,5))
				om = Label(top, text="Oylik maosh", font=("consolass", 18, "bold"), bg=root['bg'])
				om.grid(row=8, column=0, padx=(10, 10))
				om_e = Entry(top, font=("consolass", 18, "bold"), width=20)
				om_e.grid(row=8, column=1)
				ogoh1 = Label(top, text="Oylik maosh - faqat raqam bo\'lishi kerak.(bo\'sh kataklarsiz)",font=("consolass", 13, "bold"), foreground="red", bg='#ACFFEC', width=48)
				ogoh1.grid(row=9, column=0, columnspan=2)
				btn1 = Button(top, text="O\'zgartirish", font=("consolass", 15, "bold"), bg='#A2FF82',command=change)
				btn1.grid(row=10, column=1, padx=(10, 10),pady=(5,5))
			else:
				xatolik3['text'] = 'Xato kiritdingiz bu ishchi yoki sana bazada mavjud emas'

		mal_l = Label(top, text="Ishchilarning ma\'lumotlarini o\'zgartirish", font=("consolass", 19, "bold"), width=32,bg=root['bg'])
		mal_l.grid(row=0, columnspan=2, pady=(15, 5))
		cur.execute("Select * From Info")
		conn.commit()
		if len(cur.fetchall())>0:

			xatolik3 = Label(top, font=("consolass", 13, "bold"), bg=root['bg'], fg='red')
			xatolik3.grid(row=1, columnspan=2, pady=(3, 3))
			kimdir = Label(top, text="Ishchini kiriting", font=("consolass", 18, "bold"), bg=root['bg'])
			kimdir.grid(row=2, column=0, pady=(5, 5), padx=(15, 15))
			kimdir_e = Entry(top, font=("consolass", 18, "bold"), width=20)
			kimdir_e.grid(row=2, column=1)
			ogoh2 = Label(top, text='Ishchi nomiga yaxshilab e\'tibor bering',font=("consolass", 13, "bold"), bg=root['bg'], fg='red')
			ogoh2.grid(row=3, columnspan=2)
			kimdir_e.bind('<Return>', lambda event: searching_from_base())
		else:
			xatolik2 = Label(top, text="Afsuski, bazada ishchilar yo\'q,\nasosiy oynaga o\'tib ishchilar qo\'shing",font=("consolass", 16, "bold"), bg=top["bg"], fg="red")
			xatolik2.grid(row=1, column=0, pady=(10, 10), padx=(40, 0))
	def delete_employee():
		def atom():
			cur.execute("Delete From Info")
			top.destroy()
			conn.commit()
		def bomba():
			cur.execute(f"Select * From Info Where toliq_nom == '{kimdir1_e.get()}'")
			conn.commit()
			if len(cur.fetchall())!=0:
				cur.execute(f"Delete From Info Where toliq_nom == '{kimdir1_e.get()}'")
				top.destroy()
				conn.commit()
			else:
				xatolik['text']='Bu ishchi avvaldan bazada mavjud emas'
		top=Toplevel()
		top.geometry("510x200")
		top.configure(bg=root['bg'])
		mal_o = Label(top, text="Ishchilarni o\'chirish", font=("consolass", 19, "bold"), width=32,bg=root['bg'])
		mal_o.grid(row=0, columnspan=2, pady=(15, 5))
		cur.execute('Select * From Info')
		conn.commit()
		if len(cur.fetchall())>0:
			xatolik = Label(top, font=("consolass", 13, "bold"), bg=root['bg'], fg='red')
			xatolik.grid(row=1, columnspan=2, pady=(3, 3))
			kimdir1 = Label(top, text="Ishchini kiriting", font=("consolass", 18, "bold"), bg=root['bg'])
			kimdir1.grid(row=2, column=0, pady=(5, 5), padx=(15, 15))
			kimdir1_e = Entry(top, font=("consolass", 18, "bold"), width=20)
			kimdir1_e.grid(row=2, column=1)
			kimdir1 = Button(top, text=" Barchani o\'chirish", font=("consolass", 15, "bold"), bg='#A2FF82',command=atom)
			kimdir1.grid(row=3, column=1, pady=(5, 5), padx=(15, 15))
			kimdir1 = Button(top, text="O\'chirish", font=("consolass", 15, "bold"), bg='#A2FF82',command=bomba)
			kimdir1.grid(row=3, column=0, pady=(5, 5), padx=(15, 15))
		else:
			xatolik2 = Label(top, text="Afsuski, bazada ishchilar yo\'q,\nasosiy oynaga o\'tib ishchilar qo\'shing",font=("consolass", 16, "bold"), bg=top["bg"], fg="red")
			xatolik2.grid(row=1, column=0, pady=(10, 10), padx=(40, 0))
	def oylikchiq():
		def oylik():
			cur.execute(f"Select * From Info Where toliq_nom == '{kimdir_e.get()}'")
			ochuf=cur.fetchall()
			conn.commit()
			if len(ochuf)>0:
				oylik_hisobi=(ochuf[0][-2]/100)*float(ochuf[0][-3])
				oylik_lab=Label(top,text=f'{kimdir_e.get()}\nOylik maoshi - {oylik_hisobi}so\'m',font=('consolass',16,'bold'),width=30,bg=root['bg'])
				oylik_lab.grid(row=4,columnspan=2,pady=(15,0))
			else:
				xatolik3['text']='Bu ishchi bazada mavjud emas!!!'
		top=Toplevel(root)
		top.geometry("500x300")
		top.configure(bg=root['bg'])
		och = Label(top,text='Oylik chiqarish', font=("consolass", 20, "bold"), bg=root['bg'], width=32)
		och.grid(row=0, columnspan=2, pady=(15, 0))
		cur.execute('Select * From Info')
		conn.commit()
		if len(cur.fetchall())>0:
			oy = Label(top, text='Oylik kelish va ketishga qarab belgilanadi', font=("consolass", 15, "bold"), bg=root['bg'], width=32,fg='blue')
			oy.grid(row=1, columnspan=2)
			xatolik3 = Label(top, font=("consolass", 13, "bold"), bg=root['bg'], fg='red')
			xatolik3.grid(row=2, columnspan=2, pady=(3, 3))
			kimdir = Label(top, text="Ishchini kiriting", font=("consolass", 16, "bold"), bg=root['bg'])
			kimdir.grid(row=3, column=0, pady=(5, 5))
			kimdir_e = Entry(top, font=("consolass", 18, "bold"), width=20)
			kimdir_e.grid(row=3, column=1,sticky="W")
			ogoh2 = Label(top, text='Ishchi nomiga yaxshilab e\'tibor bering', font=("consolass", 13, "bold"),bg=root['bg'], fg='red')
			ogoh2.grid(row=4, columnspan=2)
			kimdir_e.bind('<Return>', lambda event: oylik())
		else:
			xatolik2 = Label(top, text="Afsuski, bazada ishchilar yo\'q,\nasosiy oynaga o\'tib ishchilar qo\'shing",font=("consolass", 16, "bold"), bg=top["bg"], fg="red")
			xatolik2.grid(row=1, column=0, pady=(10, 10), padx=(40, 0))
	fr=Frame(root,bg=root["bg"])
	ishchilar = Label(fr, text="Ishchilarga oid masalalar", font=("consolass", 20, "bold"), bg=root["back"], width=32)
	ishchilar.grid(row=0, columnspan=2, pady=(15, 15))
	bkelv = Label(fr, text=f"Ishxonadagi kelish vaqti {bkv}", font=("consolass", 17, "bold"), bg=root["back"], width=32)
	bkelv.grid(row=1, columnspan=2,pady=(5,5))
	bketv = Label(fr, text=f"Ishxonadan ketish vaqti {bktv}", font=("consolass", 17, "bold"), bg=root["back"], width=32)
	bketv.grid(row=2, columnspan=2,pady=(5,5))
	yan=Button(fr, text="Kelish va ketish vaqtlarini yangilash", font=("consolass", 15, "bold"), command=yangilash, bg="#A2FF82",width=32)
	yan.grid(row=3,columnspan=2,pady=(5,5))
	ish_kel_ket = Button(fr, text="Ishchilarning kelish va ketish vaqtlari", font=("consolass", 15, "bold"),command=keldi_ketdi, bg="#A2FF82",width=32)
	ish_kel_ket.grid(row=4, columnspan=2,pady=(5,5))
	ish_q = Button(fr, text="Ishchilar qo\'shish", font=("consolass", 15, "bold"), command=reg, bg="#A2FF82",width=20)
	ish_q.grid(row=5, column=1, pady=(10, 10))
	mal = Button(fr, text="Ma\'lumotlar", font=("consolass", 15, "bold"), bg="#A2FF82",width=20,command=malumotlar)
	mal.grid(row=5, column=0, pady=(10, 10),padx=(10,0))
	mal_o = Button(fr, text="Ma\'lumotlarni o\'zgartirish", font=("consolass", 15, "bold"), bg="#A2FF82", width=20, command=change_info)
	mal_o.grid(row=6, column=0, pady=(10, 10), padx=(10, 0))
	ish_o = Button(fr, text="Ishchilarni o\'chirish", font=("consolass", 15, "bold"), bg="#A2FF82", width=20, command=delete_employee)
	ish_o.grid(row=6, column=1, pady=(10, 10), padx=(10, 0))
	och = Button(fr, text="Oylik chiqarish", font=("consolass", 15, "bold"), bg="#A2FF82", width=32,command=oylikchiq)
	och.grid(row=7, columnspan=2, pady=(10, 10), padx=(10, 0))
	fr.grid(row=0,column=0)
def kel_va_ket():
	root.geometry("550x320")
	def kel_ket():
		if kel_vaq_e.get() == '' or ket_vaq_e.get() == '' or kel_vaq_e.get().isspace() or ket_vaq_e.get().isspace() or kel_vaq_e.get().isalpha() or ket_vaq_e.get().isalpha():
			xatolik1["text"]="kelish yoki ketish vaqti xato kiritildi"
		else:
			cur1.execute(f"Insert into Ish_Mal Values('{kel_vaq_e.get()}','{ket_vaq_e.get()}')")
			conn1.commit()
			ish_mal(kel_vaq_e.get(),ket_vaq_e.get())
			fr.destroy()
	fr=Frame(root,bg=root["bg"])
	ishchilar = Label(fr, text="Ishchilarga oid masalalar", font=("consolass", 20, "bold"), bg=root["back"], width=32)
	ishchilar.grid(row=0, columnspan=2, pady=(15, 15))
	xatolik1 = Label(fr, font=("consolass", 13, "bold"), bg=root["back"], width=32,fg="red")
	xatolik1.grid(row=1, columnspan=2)
	kel_vaq=Label(fr,text="Ishxonaga kelish vaqti",font=("consolass",16,"bold"),bg=root["back"])
	kel_vaq.grid(row=2,column=0,padx=(5,5),pady=(10,10))
	kel_vaq_e=Entry(fr,font=("consolass",18,"bold"))
	kel_vaq_e.grid(row=2,column=1,pady=(10,10))
	ket_vaq=Label(fr,text="Ishxonadan ketish vaqti",font=("consolass",16,"bold"),bg=root["back"])
	ket_vaq.grid(row=3,column=0,pady=(10,10))
	ket_vaq_e=Entry(fr,font=("consolass",18,"bold"))
	ket_vaq_e.grid(row=3,column=1,padx=(5,5),pady=(10,10))
	bq2 = Button(fr, text="Bazaga qo\'shish", font=("consolass", 15, "bold"), width=20,bg="#A2FF82",command=kel_ket)
	bq2.grid(row=4, columnspan=2, pady=(10, 10))
	fr.grid(row=0,column=0)
def start():
	cur1.execute("Select * From Ish_Mal")
	kk=cur1.fetchall()
	if len(kk)==0:
		kel_va_ket()
	else:
		ish_mal(kk[0][0],kk[0][1])
start()
root.mainloop()