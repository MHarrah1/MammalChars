# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:42:40 2019

@author: mitch
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mping
from matplotlib.widgets import Button
from matplotlib.gridspec import GridSpec

url = "https://raw.githubusercontent.com/zonination/datasets/master/file.csv"
data = pd.read_csv(url)

creature = data.iloc[:]['Creature']
mass = data.iloc[:]['Mass (grams)']/1000
heartRate = data.iloc[:]['Resting Heart Rate (BPM)']
longevity = data.iloc[:]['Longevity (Years)']
scale1 = []
scale2 = []
scale3 = []
for i in range(10):
    scale1.append(str(mass.max()*i*.125/1000))
    scale2.append(str(heartRate.max()*i*.125))
    scale3.append(str(longevity.max()*i*.125))

fig = plt.figure(figsize=(10.0,10.0))
gs = GridSpec(3, 4, left=0.1, right=0.95, wspace=0.4)
ax1 = fig.add_subplot(gs[:, 0])
ax2 = fig.add_subplot(gs[:, 1])
ax3 = fig.add_subplot(gs[:, 2])
ax4 = fig.add_subplot(gs[:, 3])
ax1.bar('Mass'+'\n'+str(mass[0])+' kg',mass[0])
ax2.bar('Mass (zoomed)'+'\n'+str(mass[0])+' kg',mass[0])
ax3.bar('Resting Heart Rate'+'\n'+str(heartRate[0])+' BPM',heartRate[0])
ax4.bar('Longevity'+'\n'+str(longevity[0])+' Year(s)',longevity[0])
plt.subplots_adjust(bottom = .4, top = .9)
fig.suptitle('Heart Rates, Mass, and Longevity of Select Mammels', fontsize = 15, fontweight = 'bold')
ax2.text(.5,95,creature[0],ha='center',size = 12,fontweight='bold')
ax1.set_ylabel('kilograms')
ax2.set_ylabel('kilograms')
ax3.set_ylabel('Beats Per Minute')
ax4.set_ylabel('Years')
ax1.set_ylim(0,mass.max())
ax2.set_ylim(0,mass[0])
ax3.set_ylim(0,heartRate.max())
ax4.set_ylim(0,longevity.max())

class Index(object):
    indmass = mass[0]
    indheartRate = heartRate[0]
    indlongevity = longevity[0]
    indcreature = creature[0]
    
    def human(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[0]
        self.indmass = mass[0]
        self.indheartRate = heartRate[0]
        self.indlongevity = longevity[0]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def cat(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[1]
        self.indmass = mass[1]
        self.indheartRate = heartRate[1]
        self.indlongevity = longevity[1]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def smallDog(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[2]
        self.indmass = mass[2]
        self.indheartRate = heartRate[2]
        self.indlongevity = longevity[2]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def medDog(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[3]
        self.indmass = mass[3]
        self.indheartRate = heartRate[3]
        self.indlongevity = longevity[3]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def largeDog(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[4]
        self.indmass = mass[4]
        self.indheartRate = heartRate[4]
        self.indlongevity = longevity[4]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def hamster(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[5]
        self.indmass = mass[5]
        self.indheartRate = heartRate[5]
        self.indlongevity = longevity[5]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def monkey(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[7]
        self.indmass = mass[7]
        self.indheartRate = heartRate[7]
        self.indlongevity = longevity[7]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def horse(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[8]
        self.indmass = mass[8]
        self.indheartRate = heartRate[8]
        self.indlongevity = longevity[8]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def cow(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[9]
        self.indmass = mass[9]
        self.indheartRate = heartRate[9]
        self.indlongevity = longevity[9]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def pig(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[10]
        self.indmass = mass[10]
        self.indheartRate = heartRate[10]
        self.indlongevity = longevity[10]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def rabbit(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[11]
        self.indmass = mass[11]
        self.indheartRate = heartRate[11]
        self.indlongevity = longevity[11]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def elephant(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[12]
        self.indmass = mass[12]
        self.indheartRate = heartRate[12]
        self.indlongevity = longevity[12]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def giraffe(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[13]
        self.indmass = mass[13]
        self.indheartRate = heartRate[13]
        self.indlongevity = longevity[13]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
    def whale(self, event):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        self.indcreature = creature[14]
        self.indmass = mass[14]
        self.indheartRate = heartRate[14]
        self.indlongevity = longevity[14]
        ax1.bar('Mass'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax2.bar('Mass (zoomed)'+'\n'+str(self.indmass)+' kg',self.indmass)
        ax3.bar('Resting Heart Rate'+'\n'+str(self.indheartRate)+' BPM',self.indheartRate)
        ax4.bar('Longevity'+'\n'+str(self.indlongevity)+' Year(s)',self.indlongevity)
        ax2.text(.5,95,self.indcreature,ha='center',size = 12,fontweight='bold')
        ax1.set_ylabel('kilograms')
        ax2.set_ylabel('kilograms')
        ax3.set_ylabel('Beats Per Minute')
        ax4.set_ylabel('Years')
        ax1.set_ylim(0,mass.max())
        ax2.set_ylim(0,mass[0])
        ax3.set_ylim(0,heartRate.max())
        ax4.set_ylim(0,longevity.max())
        plt.draw()
        
callback = Index()

imgHuman = mping.imread('C:/Users/mitch/Pictures/Human.png')
imgCat = mping.imread('C:/Users/mitch/Pictures/Cat.png')
imgSDog = mping.imread('C:/Users/mitch/Pictures/SmallDog.png')
imgMDog = mping.imread('C:/Users/mitch/Pictures/MediumDog.png')
imgLDog = mping.imread('C:/Users/mitch/Pictures/LargeDog.png')
imgHamster = mping.imread('C:/Users/mitch/Pictures/Hamster.png')
imgMonkey = mping.imread('C:/Users/mitch/Pictures/Monkey.png')
imgHorse = mping.imread('C:/Users/mitch/Pictures/Horse.png')
imgCow = mping.imread('C:/Users/mitch/Pictures/Cow.png')
imgPig = mping.imread('C:/Users/mitch/Pictures/Pig.png')
imgRabbit = mping.imread('C:/Users/mitch/Pictures/Rabbit.png')
imgElephant = mping.imread('C:/Users/mitch/Pictures/Elephant.png')
imgGiraffe = mping.imread('C:/Users/mitch/Pictures/Giraffe.png')
imgWhale = mping.imread('C:/Users/mitch/Pictures/Whale.png')

axHuman = plt.axes([0.05,.225,.1,.1])
bHuman = Button(axHuman, '', image = imgHuman)
bHuman.on_clicked(callback.human)
axCat = plt.axes([.175,.225,.1,.1])
bCat = Button(axCat, '', image = imgCat)
bCat.on_clicked(callback.cat)
axsmallDog = plt.axes([.3,.225,.1,.1])
bsmallDog = Button(axsmallDog, '', image = imgSDog)
bsmallDog.on_clicked(callback.smallDog)
axmedDog = plt.axes([.425,.225,.1,.1])
bmedDog = Button(axmedDog, '', image = imgMDog)
bmedDog.on_clicked(callback.medDog)
axlargeDog = plt.axes([.55,.225,.1,.1])
blargeDog = Button(axlargeDog, '', image = imgLDog)
blargeDog.on_clicked(callback.largeDog)
axHamster = plt.axes([.675,.225,.1,.1])
bHamster = Button(axHamster, '', image = imgHamster)
bHamster.on_clicked(callback.hamster)
axMonkey = plt.axes([.8,.225,.1,.1])
bMonkey = Button(axMonkey, '', image = imgMonkey)
bMonkey.on_clicked(callback.monkey)
axHorse = plt.axes([0.05,.1,.1,.1])
bHorse = Button(axHorse, '', image = imgHorse)
bHorse.on_clicked(callback.horse)
axCow = plt.axes([.175,.1,.1,.1])
bCow = Button(axCow, '', image = imgCow)
bCow.on_clicked(callback.cow)
axPig = plt.axes([.3,.1,.1,.1])
bPig = Button(axPig, '', image = imgPig)
bPig.on_clicked(callback.pig)
axRabbit = plt.axes([.425,.1,.1,.1])
bRabbit = Button(axRabbit, '', image = imgRabbit)
bRabbit.on_clicked(callback.rabbit)
axElephant = plt.axes([.55,.1,.1,.1])
bElephant = Button(axElephant, '', image = imgElephant)
bElephant.on_clicked(callback.elephant)
axGiraffe = plt.axes([.675,.1,.1,.1])
bGiraffe = Button(axGiraffe, '', image = imgGiraffe)
bGiraffe.on_clicked(callback.giraffe)
axWhale = plt.axes([.8,.1,.1,.1])
bWhale = Button(axWhale, '', image = imgWhale)
bWhale.on_clicked(callback.whale)




















