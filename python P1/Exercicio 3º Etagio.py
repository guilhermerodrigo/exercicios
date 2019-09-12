import tkinter
import tkinter.messagebox

guia=tkinter.Tk()

rotulo=tkinter.Label(guia, text="Digite a velocidade do veiculo")
rotulo.pack()

campo = tkinter.Entry(guia)
campo.pack()

def multar():
    velocidade=float(campo.get())
    
    if velocidade>80:
        multa=(velocidade - 80)* 5
        tkinter.messagebox.showinfo("Multa Aplicada!", "Veiculo multado!! Valor da multa:R$" +str(multa))
    else:
        tkinter.messagebox.showinfo("Veiculo sem multa", "O veiculo está nos limites de velocidade")
    
botao = tkinter.Button(guia, text="Checar Multa",command=multar)
botao.pack()

guia.mainloop()
