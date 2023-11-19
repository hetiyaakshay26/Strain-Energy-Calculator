from tkinter import *
from math import sqrt

root = Tk()
root.title("Strain Energy Calculation")

#defining functions
#gradually applied load
def gradual():
    load_a=float(load.get())
    area_a=float(area.get())
    length_a=float(length.get())
    young_a=float(young.get())
    #stress for gradually applied load
    stress_a=round(load_a/area_a,3)

    #strain energy
    strainenergy=round(((stress_a*stress_a)*area_a*length_a)/(2*young_a),3)
    strainenergy=strainenergy/1000
    #elongation
    elongation=round((stress_a*length_a)/(young_a),3)
    #sending to label
    stressop.configure(text=stress_a)
    strainenergyop.configure(text=strainenergy)
    elongationop.configure(text=elongation)

def sudden():
    load_a=float(load.get())
    area_a=float(area.get())
    length_a =float(length.get())
    young_a =float(young.get())
    #stress
    stress_a=round((2*load_a)/area_a,3)
    #strain energy
    sreainenergy=round((((stress_a*stress_a)*(area_a*length_a))/(2*young_a)),3)
    sreainenergy=sreainenergy/1000
    #elongation
    elongation=round((stress_a*length_a)/young_a,3)
    # sending to label
    stressop.configure(text=stress_a)
    strainenergyop.configure(text=sreainenergy)
    elongationop.configure(text=elongation)

def impact():
    load_a = float(load.get())
    area_a = float(area.get())
    length_a = float(length.get())
    young_a = float(young.get())
    height_a=float(height.get())
    #stress
    stress_a=round((load_a/area_a)*(1+sqrt(1+((2*height_a*area_a*young_a)/(load_a*length_a)))),3)
    #strain energy
    strainenergy=round(((stress_a*stress_a)*(area_a*length_a))/(2*young_a),3)
    strainenergy=strainenergy/1000
    #elongation
    elongation=round((stress_a*length_a)/young_a,3)
    #sending to label
    stressop.configure(text=stress_a)
    strainenergyop.configure(text=strainenergy)
    elongationop.configure(text=elongation)

root.geometry("1000x300")
# getting input of load ,area,mod.of elasticity,length,height.
l=StringVar()
a=StringVar()
ln=StringVar()
load_label=Label(root,text="Enter load (N) = ").grid(row=1,column=1,padx=5,pady=5)
load=Entry(root,textvariable=l,width=20,bg="#ffe590")
load.grid(row=1,column=2,padx=5,pady=5)
area_label=Label(root,text="Enter area (mm^2) = ").grid(row=2,column=1,padx=5,pady=5)
area=Entry(root,textvariable=a,width=20,bg="#ffe590")
area.grid(row=2,column=2,padx=5,pady=5)
young_label=Label(root,text="Enter Modulus of elasticity (N/mm^2) = ").grid(row=3,column=1,padx=5,pady=5)
young=Entry(root,width=20,bg="#ffe590")
young.grid(row=3,column=2,padx=5,pady=5)
length_label=Label(root,text="Enter Length (mm) = ").grid(row=4,column=1,padx=5,pady=5)
length=Entry(root,width=20,bg="#ffe590")
length.grid(row=4,column=2,padx=5,pady=5)
height_label=Label(root,text="Enter height (mm) = ").grid(row=5,column=1,padx=5,pady=5)
height=Entry(root,width=20,bg="#ffe590")
height.grid(row=5,column=2,padx=5,pady=5)
height_label2=Label(root,text="*For impact load only").grid(row=5,column=3,padx=5,pady=5)

#buttons to select type of loading
geadual=Button(root,text="Gradually applied load",command=gradual,bg="blue",width=20).grid(row=10,column=1,padx=5,pady=5)
sudden=Button(root,text="suddenly applied load",command=sudden,bg="yellow",width=20).grid(row=11,column=1,padx=5,pady=5)
impact=Button(root,text="impact load",bg="red",command=impact,width=20).grid(row=12,column=1,padx=5,pady=5)


#output
#stress
stress_label=Label(root,text="Stress (N/mm^2) = ",width=20).grid(row=1,column=4,padx=5,pady=5)
stressop=Label(root,bg="powder blue",width=20)
stressop.grid(row=1,column=5,padx=5,pady=5)

#strain_energy
strain_energy_label=Label(root,text="strain energy (Nm) = ",width=20).grid(row=2,column=4,padx=5,pady=5)
strainenergyop=Label(root,bg="powder blue",width=20)
strainenergyop.grid(row=2,column=5,padx=5,pady=5)

#elongation
elongation_label=Label(root,text="Elongation (mm) = ",width=20).grid(row=3,column=4,padx=5,pady=5)
elongationop=Label(root,bg="powder blue",width=20)
elongationop.grid(row=3,column=5,padx=5,pady=5)


root.mainloop()