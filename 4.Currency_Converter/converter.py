from tkinter import *
# Class for currency converter application
class CurrencyConverter:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        window.configure(bg= "blue")
        # Labels for the widgets in application window
        Label(window, font= "Helvetica 12 bold", bg= "blue",text=  "Amount to convert").grid(row= 1, column= 1, sticky= W)
        Label(window, font= "Helvetica 12 bold", bg= "blue",text= "Conversion rate").grid(row= 2, column= 1, sticky= W)
        Label(window, font= "Helvetica 12 bold", bg= "blue",text= "Converted amount").grid(row= 3, column= 1, sticky= W)
        
        # Create objects and add entry functions
        self.amounttoConvertVar = StringVar()
        Entry(window, textvariable = self.amounttoConvertVar, justify = RIGHT).grid(row=1,column=2)
        self.conversionRateVar = StringVar()
        Entry(window, textvariable = self.conversionRateVar, justify = RIGHT).grid(row=2,column=2)
        self.convertedAmountVar = StringVar()
        lblConvertedAmount =Label(window,font="Helvetica 12 bold",bg="blue", textvariable = self.convertedAmountVar).grid(row=3,column=2,sticky = E)

        # Create convert and clear buttons . When clicked they will call their respective functions.
        btConvertedAmount = Button(window, text = "Convert",font="Helvetica 12 bold",bg="blue",fg="white",command = self.ConvertedAmount).grid(row = 4,column=2,sticky = E)
        btdelete_all = Button(window, text = "Clear",font="Helvetica 12 bold",bg="red",fg="white",command = self.delete_all).grid(row = 4,column=6,padx=25,pady=25,sticky = E)

        window.mainloop()

    # Function to convert the amount 
    def ConvertedAmount(self):
        amt = float(self.conversionRateVar.get())
        convertedAmountVar= float(self.amounttoConvertVar.get()) * amt
        self.convertedAmountVar.set(format(convertedAmountVar, '10.2f'))

    # Function to clear data
    def delete_all(self):
        self.amounttoConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")

CurrencyConverter()