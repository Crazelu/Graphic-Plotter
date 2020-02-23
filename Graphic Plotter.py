import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

class Plotter(tk.Tk):
    global name_
    name_ = 'scatter'
    def __init__(self):
        super().__init__()
        self.title('Graphic Plotter')
        self.geometry('600x600')
        
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text3 = tk.StringVar()
        self.text4 = tk.StringVar()
        self.text5 = tk.StringVar()
        
        self.text1.set('1,2,3,4,5')
        self.text2.set('2,4,6,8,10')
      
        
        self.label1 = tk.Label(self, text = 'X-coordinates').pack(anchor = tk.W)
        self.input_entry1 = tk.Entry(self, textvar= self.text1)
        self.input_entry1.pack(fill=tk.BOTH, padx=20, pady=20)

        self.label2 = tk.Label(self, text = 'Y-coordinates').pack(anchor = tk.W)
        self.input_entry2 = tk.Entry(self, textvar= self.text2)
        self.input_entry2.pack(fill=tk.BOTH, padx=20, pady=20)
        
        self.label3 = tk.Label(self, text = 'X-axis Label').pack(anchor = tk.W)
        self.input_entry3 = tk.Entry(self, textvar= self.text3)
        self.input_entry3.pack(fill=tk.BOTH, padx=20, pady=20)
        
        self.label4 = tk.Label(self, text = 'Y-axis Label ').pack(anchor = tk.W)
        self.input_entry4 = tk.Entry(self, textvar= self.text4)
        self.input_entry4.pack(fill=tk.BOTH, padx=20, pady=20)
        
        self.label5 = tk.Label(self, text = 'Plot Title').pack(anchor = tk.W)
        self.input_entry5 = tk.Entry(self, textvar= self.text5)
        self.input_entry5.pack(fill=tk.BOTH, padx=20, pady=20)
        
        
        self.radio_btn1 = tk.Radiobutton(self, text = 'Scatter Plot', value=1, command = lambda: self.clicked('scatter')).pack()
        self.radio_btn2 = tk.Radiobutton(self, text = 'Histogram', value=2, command = lambda: self.clicked('hist')).pack()
        self.radio_btn3 = tk.Radiobutton(self, text = 'Pie Chart', value=3, command = lambda: self.clicked('pie')).pack() 
        
        self.button = tk.Button(self, text='Plot', bg='purple',fg='lightblue',command = lambda: self.plot(name_))
        self.button.pack(fill=tk.BOTH, padx=15, pady=15) 
    
    def clicked(self,value):
        global name_
        name_ = value
        return name_
    
    def plot(self,name_):
        work1 = self.text1.get()
        work2 = self.text2.get()
        plot_list1 = np.array(work1.split(','))
        plot_list2 = np.array(work2.split(','))
        colormap = np.array(['r', 'g', 'b', 'purple', 'lightblue'])
        x_label = self.text3.get()
        y_label = self.text4.get()
        title = self.text5.get()
        
        if name_ == 'scatter':
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.scatter(plot_list1, plot_list2, color = colormap)
            return (plt.show())
        
        if name_ == 'hist':
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.hist([plot_list1, plot_list2], bins = len(plot_list1), color = colormap[3:], rwidth = 1)
            return (plt.show())
        
        if name_ == 'pie':
            plt.title(title)
            plt.pie(plot_list2, colors = colormap, shadow=True)
            return (plt.show())
       
        
if __name__ == '__main__':
    Plotter().mainloop()
            
