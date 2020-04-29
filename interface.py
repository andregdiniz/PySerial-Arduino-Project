import timeit
import time
from tkinter import *
from PIL import Image, ImageTk
import serial

#Variaveis para gerenciamento de botões OK
global cont
cont = True 
global cont1
cont1 = True 
global cont2
cont2 = True 
global cont3
cont3 = True 
global cont4
cont4 = True 
global cont5
cont5 = True 
global cont6
cont6 = True 
global cont7
cont7 = True 
global cont8
cont8 = True 
global cont9
cont9 = True 
global cont10
cont10 = True 
#Variaveis para gerenciamento de botões Clean
global contc
contc = -1
global contc1
contc1 = -1
global contc2
contc2 = -1
global contc3
contc3 = -1
global contc4
contc4 = -1
global contc5
contc5 = -1
global contc6
contc6 = -1
global contc7
contc7 = -1
global contc8
contc8 = -1
global contc9
contc9 = -1
global contc10
contc10 = -1 


def comando(op):

  #Variaveis para gerenciamento de botões OK
  global cont
  global cont1
  global cont2
  global cont3
  global cont4
  global cont5
  global cont6
  global cont7
  global cont8
  global cont9
  global cont10
  #Variaveis para gerenciamento de botões Clean
  global contc
  global contc1
  global contc2
  global contc3
  global contc4
  global contc5
  global contc6
  global contc7
  global contc8
  global contc9
  global contc10
  #variaveis para os textos de informação do usuário
  global texto20
  global texto21
  global texto22
  global texto23
  global texto24
  global texto25
  global texto26
  global texto27
  global texto28
  global texto29
  global texto30
  global texto31
  global texto32
  global texto33
  global texto34
  global texto35
  global texto36
  global texto37
  global texto38
  global texto39
  global texto40
  global texto41
              
  #Condições para o botão de OK
  if(op==1):
      if(cont == True):
          copo1 = temp1.get()
          sen_command(copo1)
          k = str('l34601')
          sen_command(k)
          if(contc == 0):
              texto31.destroy()
          contc = 1
          cont = False    
          texto20 = Label(text='Tempo do recipiente 1 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto20.place(x=450,y=198)

  if(op==2):
      if(cont1 == True):
          copo2 = temp2.get() 
          sen_command(copo2)
          l = str('l82702')
          sen_command(l)
          if(contc1 == 0):
              texto32.destroy()
          contc1 = 1
          cont1 = False
          texto21 = Label(text='Tempo do recipiente 2 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto21.place(x=450,y=238)

  if(op==3):
      if(cont2 == True):
          copo3 = temp3.get() 
          sen_command(copo3)
          m = str('l18603')
          sen_command(m)
          if(contc2 == 0):
              texto33.destroy()
          contc2 = 1
          cont2 = False
          texto22 = Label(text='Tempo do recipiente 3 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto22.place(x=450,y=278)

  if(op==4):
      if(cont3 == True):
          copo4 = temp4.get() 
          sen_command(copo4)
          n = str('l19804')
          sen_command(n)
          if(contc3 == 0):
              texto34.destroy()
          contc3 = 1
          cont3 = False
          texto23 = Label(text='Tempo do recipiente 4 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto23.place(x=450,y=318)

  if(op==5):
      if(cont4 == True):
          copo5 = temp5.get() 
          sen_command(copo5)
          o = str('l82705')
          sen_command(o)
          if(contc4 == 0):
              texto35.destroy()
          contc4 = 1
          cont4 = False
          texto24 = Label(text='Tempo do recipiente 5 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto24.place(x=450,y=358)

  if(op==6):
      if(cont5 == True):
          copo6 = temp6.get() 
          sen_command(copo6)
          p = str('l92806')
          sen_command(p)
          if(contc5 == 0):
              texto36.destroy()
          contc5 = 1
          cont5 = False
          texto25 = Label(text='Tempo do recipiente 6 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto25.place(x=450,y=398)

  if(op==7):
      if(cont6 == True):
          copo7 = temp7.get() 
          sen_command(copo7)
          q = str('l34407')
          sen_command(q)
          if(contc6 == 0):
              texto37.destroy()
          contc6 = 1
          cont6 = False
          texto26 = Label(text='Tempo do recipiente 7 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto26.place(x=450,y=438)

  if(op==8):
      if(cont7 == True):
          copo8 = temp8.get() 
          sen_command(copo8)
          r = str('l92808')
          sen_command(r)
          if(contc7 == 0):
              texto38.destroy()
          contc7 = 1
          cont7 = False
          texto27 = Label(text='Tempo do recipiente 8 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto27.place(x=450,y=478)

  if(op==9):
      if(cont8 == True):
          copo9 = temp9.get() 
          sen_command(copo9)
          s = str('l93709')
          sen_command(s)
          if(contc1 == 0):
              texto39.destroy()
          contc8 = 1
          cont8 = False
          texto28 = Label(text='Tempo do recipiente 9 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto28.place(x=450,y=518)

  if(op==10):
      if(cont9 == True):
          copo10 = temp10.get() 
          sen_command(copo10)
          t = str('l23210')
          sen_command(t)
          if(contc9 == 0):
              texto40.destroy()
          contc9 = 1
          cont9 = False
          texto29 = Label(text='Tempo do recipiente 10 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto29.place(x=450,y=558)

  if(op==11):
      if(cont10 == True):
          copo11 = temp11.get() 
          sen_command(copo11)
          u = str('l98411')
          sen_command(u)
          if(contc10 == 0):
              texto41.destroy()
          contc10 = 1
          cont10 = False
          texto30 = Label(text='Tempo do recipiente 11 adicionado!', fg = 'black', bg='white', font="-weight bold -size 8")
          texto30.place(x=450,y=598)
               
  #Condição para o botão de START 
  if(op==12):
      x = str('l10623')
      sen_command(x)
  #Condição para o botão de RESET
  if(op==13):
      y = str('l10724')
      sen_command(y)
      cont = 0
      cont1 = 0
      cont2 = 0
      cont3 = 0
      cont4 = 0
      cont5 = 0
      cont6 = 0
      cont7 = 0
      cont8 = 0
      cont9 = 0
      cont10 = 0 

  #Condições para os botões de CLEAN
  if(op==14):
      if(contc == 1):
          z = str('l10412')
          sen_command(z)
          texto20.destroy()
          texto31 = Label(text='Tempo do recipiente 1 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto31.place(x=450,y=198)
          contc = 0
          cont = True
            
  if(op==15):
      if(contc1 == 1):
          a = str('l12213')
          sen_command(a)
          texto21.destroy()
          texto32 = Label(text='Tempo do recipiente 2 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto32.place(x=450,y=238)
          cont1 = True
          contc1 = 0

  if(op==16):
      if(contc2 == 1):
          b = str('l76314')
          sen_command(b)
          texto22.destroy()
          texto33 = Label(text='Tempo do recipiente 3 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto33.place(x=450,y=278)
          cont2 = True
          contc2 = 0

  if(op==17):
      if(contc3 == 1):
          c = str('l53615')
          sen_command(c)
          texto23.destroy()
          texto34 = Label(text='Tempo do recipiente 4 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto34.place(x=450,y=318)
          cont3 = True
          contc3 = 0

  if(op==18):
      if(contc4 == 1):
          d = str('l76616')
          sen_command(d)
          texto24.destroy()
          texto35 = Label(text='Tempo do recipiente 5 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto35.place(x=450,y=358)
          cont4 = True
          contc4 = 0

  if(op==19):
      if(contc5 == 1):
          e = str('l36517')
          sen_command(e)
          texto25.destroy()
          texto36 = Label(text='Tempo do recipiente 6 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto36.place(x=450,y=398)
          cont5 = True
          contc5 = 0

  if(op==20):
      if(contc6 == 1):
          f = str('l22418')
          sen_command(f)
          texto26.destroy()
          texto37 = Label(text='Tempo do recipiente 7 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto37.place(x=450,y=438)
          cont6 = True
          contc6 = 0 

  if(op==21):
      if(contc7 == 1):
          g = str('l37919')
          sen_command(g)
          texto27.destroy()
          texto38 = Label(text='Tempo do recipiente 8 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto38.place(x=450,y=478)
          cont7 = True
          contc7 = 0

  if(op==22):
      if(contc8 == 1):
          h = str('l12320')
          sen_command(h)
          texto28.destroy()
          texto39 = Label(text='Tempo do recipiente 9 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto39.place(x=450,y=518)
          cont8 = True
          contc8 = 0

  if(op==23):
      if(contc9 == 1):
          i = str('l93521')
          sen_command(i)
          texto29.destroy()
          texto40 = Label(text='Tempo do recipiente 10 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto40.place(x=450,y=558)
          cont9 = True
          contc9 = 0

  if(op==24):
      if(contc10 == 1):
          j = str('l23322')
          sen_command(j)
          texto30.destroy()
          texto41 = Label(text='Tempo do recipiente 11 apagado! Digite novamente.', fg = 'black', bg='white', font="-weight bold -size 8")
          texto41.place(x=450,y=598)
          cont10 = True
          contc10 = 0
        
#Função que pega a porta USB usada pelo arduino
def create_porta():
    global portaUSB
    aux = temp.get()
    portaUSB = serial.Serial(aux, 9600)
    
#Função que faz a comunicação serial com o arduino
def sen_command(cod):
    portaUSB.write(cod.encode())

janela = Tk() #Cria uma janela
janela.title('Projeto Histotecnico - v: 2.1') #Titulo da janela
janela.geometry('750x750') #Tamanho da janela
janela.configure(bg='white') #Cor da janela

#Para informar qual a entrada USB utilizada
text_Port = Label(text='Informe a Porta:').place(x=25,y=95) # Texto para informar a porta do arduino
temp = StringVar () # Variavel que pega o que for digitado
porta = Entry(janela, textvariable = temp).place(x=120,y=95) # Cria um campo para digitar a porta
botao_port  = Button(text='OK', command = create_porta).place(x=250,y=95) #Cria botão para confirmar a porta

#Informações do Copo 1
texto1 = Label(text='Digite o tempo do Recipiente 1 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto1.place(x=25,y=195)
temp1 = StringVar () # Variavel que pega o que for digitado
porta1 = Entry(janela, textvariable = temp1).place(x=235,y=198) # Cria um campo para digitar a porta
botao_port1  = Button(text='OK', command = lambda: comando(1)).place(x=365,y=195) #Cria botão para confirmar a porta
botao_port13 =  Button(text='CLEAN', command = lambda: comando(14)).place(x=395,y=195) #Limpa o campo digitado

#Informações do Copo 2
texto2 = Label(text='Digite o tempo do Recipiente 2 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto2.place(x=25,y=235)
temp2 = StringVar () # Variavel que pega o que for digitado
porta2 = Entry(janela, textvariable = temp2).place(x=235,y=238) # Cria um campo para digitar a porta
botao_port1  = Button(text='OK', command = lambda: comando(2)).place(x=365,y=235) #Cria botão para confirmar a porta
botao_port14 =  Button(text='CLEAN', command = lambda: comando(15)).place(x=395,y=235) #Limpa o campo digitado

#Informações do Copo 3
texto3 = Label(text='Digite o tempo do Recipiente 3 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto3.place(x=25,y=275)
temp3 = StringVar () # Variavel que pega o que for digitado
porta3 = Entry(janela, textvariable = temp3).place(x=235,y=278) # Cria um campo para digitar a porta
botao_port2  = Button(text='OK', command = lambda: comando(3)).place(x=365,y=275) #Cria botão para confirmar a porta
botao_port15 =  Button(text='CLEAN', command = lambda: comando(16)).place(x=395,y=275) #Limpa o campo digitado

#Informações do Copo 4
texto4 = Label(text='Digite o tempo do Recipiente 4 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto4.place(x=25,y=315)
temp4 = StringVar () # Variavel que pega o que for digitado
porta4 = Entry(janela, textvariable = temp4).place(x=235,y=318) # Cria um campo para digitar a porta
botao_port3  = Button(text='OK', command = lambda: comando(4)).place(x=365,y=315) #Cria botão para confirmar a porta
botao_port16 =  Button(text='CLEAN', command = lambda: comando(17)).place(x=395,y=315) #Limpa o campo digitado

#Informações do Copo 5
texto5 = Label(text='Digite o tempo do Recipiente 5 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto5.place(x=25,y=355)
temp5 = StringVar () # Variavel que pega o que for digitado
porta5 = Entry(janela, textvariable = temp5).place(x=235,y=358) # Cria um campo para digitar a porta
botao_port4  = Button(text='OK', command = lambda: comando(5)).place(x=365,y=355) #Cria botão para confirmar a porta
botao_port17 =  Button(text='CLEAN', command = lambda: comando(18)).place(x=395,y=355) #Limpa o campo digitado

#informações do copo 6
texto6 = Label(text='Digite o tempo do Recipiente 6 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto6.place(x=25,y=395)
temp6 = StringVar () # Variavel que pega o que for digitado
porta6 = Entry(janela, textvariable = temp6).place(x=235,y=398) # Cria um campo para digitar a porta
botao_port5  = Button(text='OK', command = lambda: comando(6)).place(x=365,y=395) #Cria botão para confirmar a porta
botao_port18 =  Button(text='CLEAN', command = lambda: comando(19)).place(x=395,y=395) #Limpa o campo digitado

#Informações do Copo 7
texto7 = Label(text='Digite o tempo do Recipiente 7 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto7.place(x=25,y=435)
temp7 = StringVar () # Variavel que pega o que for digitado
porta7 = Entry(janela, textvariable = temp7).place(x=235,y=438) # Cria um campo para digitar a porta
botao_port6  = Button(text='OK', command = lambda: comando(7)).place(x=365,y=435) #Cria botão para confirmar a porta
botao_port19 =  Button(text='CLEAN', command = lambda: comando(20)).place(x=395,y=435) #Limpa o campo digitado

#Informações do Copo 8
texto8 = Label(text='Digite o tempo do Recipiente 8 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto8.place(x=25,y=475)
temp8 = StringVar () # Variavel que pega o que for digitado
porta8 = Entry(janela, textvariable = temp8).place(x=235,y=478) # Cria um campo para digitar a porta
botao_port7  = Button(text='OK', command = lambda: comando(8)).place(x=365,y=475) #Cria botão para confirmar a porta
botao_port20 =  Button(text='CLEAN', command = lambda: comando(21)).place(x=395,y=475) #Limpa o campo digitado

#Informações do Copo 9
texto9 = Label(text='Digite o tempo do Recipiente 9 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto9.place(x=25,y=515)
temp9 = StringVar () # Variavel que pega o que for digitado
porta9 = Entry(janela, textvariable = temp9).place(x=235,y=518) # Cria um campo para digitar a porta
botao_port8  = Button(text='OK', command = lambda: comando(9)).place(x=365,y=515) #Cria botão para confirmar a porta
botao_port21 =  Button(text='CLEAN', command = lambda: comando(22)).place(x=395,y=515) #Limpa o campo digitado

#Informações do Copo 10
texto10 = Label(text='Digite o tempo do Recipiente 10 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto10.place(x=18,y=555)
temp10 = StringVar () # Variavel que pega o que for digitado
porta10 = Entry(janela, textvariable = temp10).place(x=235,y=558) # Cria um campo para digitar a porta
botao_port9  = Button(text='OK', command = lambda: comando(10)).place(x=365,y=555) #Cria botão para confirmar a porta
botao_port22 =  Button(text='CLEAN', command = lambda: comando(23)).place(x=395,y=555) #Limpa o campo digitado

#Informações do Copo 11
texto11 = Label(text='Digite o tempo do Recipiente 11 : ', fg = 'blue', bg='white', font="-weight bold -size 10")
texto11.place(x=18,y=595)
temp11 = StringVar () # Variavel que pega o que for digitado
porta11 = Entry(janela, textvariable = temp11).place(x=235,y=598) # Cria um campo para digitar a porta
botao_port10  = Button(text='OK', command = lambda: comando(11)).place(x=365,y=595) #Cria botão para confirmar a porta
botao_port23 =  Button(text='CLEAN', command = lambda: comando(24)).place(x=395,y=595) #Limpa o campo digitado

#Texto informativo
texto12 = Label(text='Por favor, informe os tempos em minutos!', fg = 'red',bg='white', font="-weight bold -size 11")
texto12.place(x=25,y=150)

texto12 = Label(text='Histotecnico FCS', fg = 'green',bg='white', font="-weight bold -size 25")
texto12.place(x=230,y=5)


#Texto de apresentação

texto13 = Label(text='Software desenvolvido por:', fg = 'black',bg='white')
texto13.place(x=565,y=35)
texto14 = Label(text='André Gomes Diniz', fg = 'black',bg='white', font="-weight bold -size 8")
texto14.place(x=590,y=65)
texto15 = Label(text='E-mail para contato:', fg = 'black',bg='white')
texto15.place(x=590,y=95)
texto16 = Label(text='andreg.diniz97@hotmail.com', fg = 'black',bg='white', font="-weight bold -size 8")
texto16.place(x=565,y=125)

#Botão de start
botao_port11  = Button(text='START', command = lambda: comando(12)).place(x=150,y=650) #Cria botão para confirmar a porta

#Botão de reset
botao_port12 = Button(text='RESET', command= lambda: comando(13)).place(x=250,y=650)


#deixa a janela em execução até fechar
janela.mainloop()
