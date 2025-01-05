from tkinter import*
def add_number():
  num1=int(entry1.get())
  num2=int(entry2.get())
  result_label=label.config(text=f"Result: {num1+num2}")
root=TK()
entry1=Entry(root)
entry1.pack()
entry2=Entry(root)
entry2.pack()
Button(root,text="Add",command=add_number).pack()

result_label=Label(root)
result_label.pack()

root.mainloop()
