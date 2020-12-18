from tkinter import *
from decimal import *            
from math import *               

root = Tk()                    
root.title('Калькулятор')       
root.resizable(False, False)   

buttons = ( ('M', 'm-', 'm+', 'mc'),
            ('Sqrt', 'X^2', 'Sin', 'Cos'),
            ('7', '8', '9', '/'),       
            ('4', '5', '6', '*'),        
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
          )

buttons1 = (('2', '4', '8', '10', '16', '0'),)
    

activeStr = ''  
stack = []      
memory = 0      
wdth = 6       
deg = 0
temp_str = '10'
temp_str2 = '10'
temp_str3 = 0
D = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     
def calculate():                            
    
    global stack
    global label
    global memory
    
    result = 0
    
    operand2 = Decimal(stack.pop())             
    operation = stack.pop()
    operand1 = Decimal(stack.pop())
    
    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
            if operand1 == 0 or operand2 == 0: 
                result = 'Error'                
            else:
                result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    if operation == 'Sqrt':                   
        result = sqrt(operand1)
    if operation == 'X^2':
        result = operand1 ** 2
    if operation in ('Sin', 'Cos'):
        if deg == 1:
            operand1 = radians(operand1)
        if operation == 'Sin':
            result = sin(operand1)
        else:
            result = cos(operand1)
    if operation == 'M':
        if operand1 == 0:
            result = 'Cannot remember 0'
        else:
            memory = operand1
            result = 'Memorized'                
    if operation == 'm-':
        if memory == 0:
            result = 'Error'                   
        else:
            result = memory - operand1
    if operation == 'm+':
        result = memory + operand1
    if operation in ('2', '4', '8', '10', '16'):
        if operation == 2:
            base = operation
            while operand1 > 0:
                result = str(result)
                result = str(operand1 % base) + result
                operand1 //= base
        operation = str(operation)
    
    result = str(result)
    
    if operation in ('2', '4', '8', '16'):
        label.configure(text = result,
                        font = ("Times New Roman", 15, "bold"))
    elif result.isalnum == False:
        label.configure(text=result,
                        font = ("Times New Roman", 15, "bold"))
    else:
        result = Decimal(result)
        if len(str(result)) > 7:
            if result >= 1.0000E+30:
                label.configure(text='Num too large',
                                font = ("Times New Roman", 15, "bold"))
            elif result >= 1.0000E+6:
                result = '{:1E}'.format(result)
                label.configure(text = result,
                                font = ("Times New Roman", 9))
            else:
                result = str(result)
                if result.find('.') == 1:
                    if result.count('0') >= 4:
                        result = result[:10]
                        label.configure(text = result,
                                        font = ("Times New Roman", 9))
                    else:
                        result = result[:5]
                        label.configure(text = result,
                                        font = ("Times New Roman", 15, "bold"))
                else:
                    result = result[:5]
                    label.configure(text = result,
                                        font = ("Times New Roman", 15, "bold"))
        else:
            result = str(result)
            label.configure(text = result,
                            font = ("Times New Roman", 15, "bold"))
    
    activeStr = str(result)
 
def convert(n, to_base=10, from_base=10):

    print(n, to_base, from_base)
    
    if isinstance(n, str):
        n = int(n, from_base)
    if n >= to_base:
        return convert(n // to_base, to_base) + D[n % to_base]
    else:
        return D[n]

def click1(text):
    
    global temp_str
    global temp_str2
    global temp_str3

    
    temp_str = label1['text']
    label1.configure(text=text,
                     font = ("Times New Roman", 15, "bold"))
    temp_str3 = text
    from_base = int(temp_str)
    to_base = int(temp_str3)
    n = int(label['text'])
    result = convert(n,to_base, from_base)
    label.configure(text = str(result))
    activeStr = '0'
    
def click(text):   

    global activeStr
    global stack
    global memory
    global deg
    global stackNS
    global temp_str2

    if text == 'CE':       
        stack.clear()                  
        activeStr = ''
        label.configure(text='0',
                        font = ("Times New Roman", 15, "bold"))             
        label1.configure(text = '10')
        label2.configure(text = 'RAD')
        deg = 0
    elif text == 'mc':                                                      
        memory = 0
        label.configure(text='Memory is empty')                             
    elif text == 'Del':
        if label['text'].isalpha():
            activeStr = ''                                              
            label.configure(text='0',
                            font = ("Times New Roman", 15, "bold"))
        if len(label['text']) == 1 or Decimal(label['text']) >= 1.000000e+6: 
            activeStr = ''                                                   
            label.configure(text='0',
                            font = ("Times New Roman", 15, "bold"))
        elif len(stack) == 1:                                               
            activeStr = str(stack.pop())                                    
            activeStr = activeStr[:-1]
            label.configure(text=activeStr)
        else:                                                              
            activeStr = activeStr[:-1]
            label.configure(text=activeStr)
    elif '0' <= text <= '9':
            if activeStr == '0':
                activeStr = ''
                label.configure(text='0')
            else:
                activeStr += text             
                label.configure(text=activeStr)
    elif text in ('NS', 'DG/RD'):
        if text == 'NS':
            root_NS = Tk()
            root_NS.title('NS')
            root_NS.resizable(False, False)
            for col in range(5):
                button = Button(root_NS,
                                width = 4,
                                font = ("Times New Roman", 15, "bold"),
                                bg = "#e5ebee",
                                foreground = '#215b7a',
                                text=buttons1[0][col],
                                command = lambda row = row,
                                                 col = col: click1(buttons1[0][col]))
                button.grid(row = row,
                            column = col,
                            sticky = "nsew")
                root_NS.grid_rowconfigure(1, weight = 1)  
                root_NS.grid_columnconfigure(5, weight = 1)
        else:
            stack.clear()
            activeStr = ''
            label.configure(text = '0',
                            font = ("Times New Roman", 15, "bold"))
            if deg == 0:
                deg = 1
                label2.configure(text='DEG')
            else:
                deg = 0
                label2.configure(text='RAD')
    elif text == '.':                                                       
        if activeStr.find('.') == -1:                                       
            activeStr += text                   
            label.configure(text=activeStr)
    elif text in ('Sqrt', 'X^2', 'Cos', 'Sin', 'M', 'm+', 'm-', 'mc'):                               
        if activeStr.isalpha():                                            
            label.configure(text='Error')
        else:
            stack.append(label['text'])
            stack.append(text)                                         
            stack.append(0)                                         
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
    else:                                      
        if len(stack) >= 2:                                                                  
            stack.append(label['text'])         
            calculate()                         
            stack.clear()       
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')

label1 = Label(root,
               text = '10',
               font = ("Times New Roman", 15, "bold"),
               bg = "#f6f8f9",                        
               foreground = "#455660")                            

label1.grid(row=0,                                    
            column = 0,
            columnspan = 1,
            sticky = "nsew")

label2 = Label(root,
               text = 'RAD',
               font = ("Times New Roman", 15, "bold"),
               bg = "#f6f8f9",                        
               foreground = "#455660",)                            

label2.grid(row=0,                                    
           column = 1,
           columnspan = 1,
           sticky = "nsew")

button = Button(root,                               
                text = 'DG/RD',
                width = wdth,
                font = ("Times New Roman", 15, "bold"),
                bg = "#e5ebee",
                foreground = "#215b7a",
                command = lambda text = 'DG/RD': click(text))
                                                                
button.grid(row = 0,
            column = 3)                                         

button = Button(root,                                            
                text = 'NS',
                width = wdth,
                font = ("Times New Roman", 15, "bold"),
                bg = "#e5ebee",
                foreground = "#215b7a",
                command = lambda text = 'NS': click(text))     
                                                                
button.grid(row = 0,
            column = 2)
                
label = Label(root,                                                      
              text = '0',                             
              font = ("Times New Roman", 15, "bold"),
              bg = "#f6f8f9",                        
              foreground = "#455660",                
              width = 14)                            

label.grid(row=1,                                    
           column = 0,
           columnspan = 2,
           sticky = "nsew")                                                                        

button = Button(root,                               
                text = 'CE',
                width = wdth,
                font = ("Times New Roman", 15, "bold"),
                bg = "#e5ebee",
                foreground = "#F30000",
                command = lambda text = 'CE': click(text))
                                                                
button.grid(row = 1,
            column = 3)                                         

button = Button(root,                                            
                text = 'Del',
                width = wdth,
                font = ("Times New Roman", 15, "bold"),
                bg = "#e5ebee",
                foreground = "#F30000",
                command = lambda text = 'Del': click(text))     
                                                                
button.grid(row = 1,
            column = 2)

for row in range(6):                                            
    for col in range(4):
        button = Button(root,
                        width = wdth,
                        font = ("Times New Roman", 15, "bold"),
                        bg = "#e5ebee",
                        foreground = '#215b7a',
                        text=buttons[row][col],
                        command = lambda row = row,
                                         col = col: click(buttons[row][col]))
                    
        button.grid(row = row + 2,
                    column = col,
                    sticky = "nsew")                                    
       
root.grid_rowconfigure(4, weight = 1)    
root.grid_columnconfigure(5, weight = 1) 

root.mainloop()                                              
