import win32com.client as win32
def Emailer():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    # mail.To = recipient
    # mail.Subject = subject
    # mail.HtmlBody = text
    # mail.send
    mail.Display(True)
Emailer()