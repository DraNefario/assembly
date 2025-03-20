import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = True

registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00

flag_zero = False

#memoria = MemoriaCache('ProjetoArq_1/arquivos_memoria/mov_mov_add.bin')
#memoria = MemoriaCache('ProjetoArq_1/arquivos_memoria/inc_dec.bin')
#memoria = MemoriaCache('ProjetoArq_1/arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('ProjetoArq_1/arquivos_memoria/programa_simples.bin')
memoria = MemoriaCache('ProjetoArq_1/arquivos_memoria/fibonacci_10.bin')

def buscarEDecodificarInstrucao():
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    instrucao = memoria.getValorMemoria(registrador_cp)

    print(instrucao)

    if instrucao == 0x40:
        print('MOV Reg, Byte')
        return 0x40
    if instrucao == 0x01:
        print('ADD Reg, Reg ')
        return 0x01
    if instrucao == 0x10:
        print('INC Reg')
        return 0x10
    if instrucao == 0x20:
        print('DEC Reg')
        return 0x20
    if instrucao == 0x00:
        print('ADD Reg, Byte')
        return 0x00
    if instrucao == 0x30:
        print('SUB Reg, Byte')
        return 0x30
    if instrucao == 0x31:
        print('SUB Reg, Reg')
        return 0x31
    if instrucao == 0x41:
        print('MOV Reg, Reg')
        return 0x41
    if instrucao == 0x50:
        print('JMP Byte')
        return 0x50
    if instrucao == 0x60:
        print('CMP Reg, Byte')
        return 0x60
    if instrucao == 0x61:
        print('CMP Reg, Reg')
        return 0x61
    if instrucao == 0x79:
        print('JZ Byte')
        return 0x79
    if instrucao == 0x70:
        print('JZ Byte')
        return 0x79

    return -1

def lerOperadoresExecutarInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    print ('Implementar a lerOperadoresExecutarInstrucao')
    if idInstrucao == 0x40:
        operador1 = memoria.getValorMemoria(registrador_cp +1)
        operador2 = memoria.getValorMemoria(registrador_cp +2)

        if operador1 == 0x02:
            registrador_ax = operador2
        elif operador1 == 0x03:
            registrador_bx = operador2
        elif operador1 == 0x04:
            registrador_cx = operador2
        elif operador1 == 0x05:
            registrador_dx = operador2

    
    if idInstrucao == 0x01:
        operador1 = memoria.getValorMemoria(registrador_cp +1)
        operador2 = memoria.getValorMemoria(registrador_cp +2)

        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax += registrador_ax
            if operador2 == 0x03:
                registrador_ax += registrador_bx
            if operador2 == 0x04:
                registrador_ax += registrador_cx
            if operador2 == 0x05:
                registrador_ax += registrador_dx
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx += registrador_ax
            if operador2 == 0x03:
                registrador_bx += registrador_bx
            if operador2 == 0x04:
                registrador_bx += registrador_cx
            if operador2 == 0x05:
                registrador_bx += registrador_dx
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx += registrador_ax
            if operador2 == 0x03:
                registrador_cx += registrador_bx
            if operador2 == 0x04:
                registrador_cx += registrador_cx
            if operador2 == 0x05:
                registrador_cx += registrador_dx
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx += registrador_ax
            if operador2 == 0x03:
                registrador_dx += registrador_bx
            if operador2 == 0x04:
                registrador_dx += registrador_cx
            if operador2 == 0x05:
                registrador_dx += registrador_dx
    
    if idInstrucao == 0x10:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)

        if operador1 == 0x02:
            registrador_ax += 1
        elif operador1 == 0x03:
            registrador_bx += 1
        elif operador1 == 0x04:
            registrador_cx += 1
        elif operador1 == 0x05:
            registrador_dx += 1
    
    if idInstrucao == 0x20:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)

        if operador1 == 0x02:
            registrador_ax -= 1
        elif operador1 == 0x03:
            registrador_bx -= 1
        elif operador1 == 0x04:
            registrador_cx -= 1
        elif operador1 == 0x05:
            registrador_dx -= 1
    

    if idInstrucao == 0x00:
        operador1 = memoria.getValorMemoria(registrador_cp +1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02:
            registrador_ax = registrador_ax + operador2
        elif operador1 == 0x03:
            registrador_bx = registrador_bx + operador2
        elif operador1 == 0x04:
            registrador_cx = registrador_cx + operador2
        elif operador1 == 0x05:
            registrador_dx = registrador_dx + operador2
    
    if idInstrucao == 0x30:
        operador1 = memoria.getValorMemoria(registrador_cp +1)
        operador2 = memoria.getValorMemoria(registrador_cp +2)

        if operador1 == 0x02:
            registrador_ax = registrador_ax - operador2
        elif operador1 == 0x03:
            registrador_bx = registrador_bx - operador2
        elif operador1 == 0x04:
            registrador_cx = registrador_cx - operador2
        elif operador1 == 0x05:
            registrador_dx = registrador_dx - operador2

    
    if idInstrucao == 0x31:
        operador1 = memoria.getValorMemoria(registrador_cp +1)
        operador2 = memoria.getValorMemoria(registrador_cp +2)

        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax -= registrador_ax
            if operador2 == 0x03:
                registrador_ax -= registrador_bx
            if operador2 == 0x04:
                registrador_ax -= registrador_cx
            if operador2 == 0x05:
                registrador_ax -= registrador_dx
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx -= registrador_ax
            if operador2 == 0x03:
                registrador_bx -= registrador_bx
            if operador2 == 0x04:
                registrador_bx -= registrador_cx
            if operador2 == 0x05:
                registrador_bx -= registrador_dx
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx -= registrador_ax
            if operador2 == 0x03:
                registrador_cx -= registrador_bx
            if operador2 == 0x04:
                registrador_cx -= registrador_cx
            if operador2 == 0x05:
                registrador_cx -= registrador_dx
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx -= registrador_ax
            if operador2 == 0x03:
                registrador_dx -= registrador_bx
            if operador2 == 0x04:
                registrador_dx -= registrador_cx
            if operador2 == 0x05:
                registrador_dx -= registrador_dx

    
    if idInstrucao == 0x41:
        operador1 = memoria.getValorMemoria(registrador_cp +1)
        operador2 = memoria.getValorMemoria(registrador_cp +2)

        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax = registrador_ax
            if operador2 == 0x03:
                registrador_ax = registrador_bx
            if operador2 == 0x04:
                registrador_ax = registrador_cx
            if operador2 == 0x05:
                registrador_ax = registrador_dx
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx = registrador_ax
            if operador2 == 0x03:
                registrador_bx = registrador_bx
            if operador2 == 0x04:
                registrador_bx = registrador_cx
            if operador2 == 0x05:
                registrador_bx = registrador_dx
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx = registrador_ax
            if operador2 == 0x03:
                registrador_cx = registrador_bx
            if operador2 == 0x04:
                registrador_cx = registrador_cx
            if operador2 == 0x05:
                registrador_cx = registrador_dx
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx = registrador_ax
            if operador2 == 0x03:
                registrador_dx = registrador_bx
            if operador2 == 0x04:
                registrador_dx = registrador_cx
            if operador2 == 0x05:
                registrador_dx = registrador_dx

    
    if idInstrucao == 0x79:
        operador1= memoria.getValorMemoria(registrador_cp + 1)
    
        
        if flag_zero:
            registrador_cp = operador1
    

    if idInstrucao == 0x60:
        operador1 = memoria.getValorMemoria(registrador_cp +1)
        operador2 = memoria.getValorMemoria(registrador_cp +2)

        if operador1 == 0x02:
            if registrador_ax == operador2:
                flag_zero = True
            else:
                flag_zero = False
        
        if operador1 == 0x03:
            if registrador_bx == operador2:
                flag_zero = True
            else:
                flag_zero = False

        if operador1 == 0x04:
            if registrador_cx == operador2:
                flag_zero = True
            else:
                flag_zero = False

        if operador1 == 0x05:
            if registrador_dx == operador2:
                flag_zero = True
            else:
                flag_zero = False
        
    
    if idInstrucao == 0x61:
        operador1 = memoria.getValorMemoria(registrador_cp +1)
        operador2 = memoria.getValorMemoria(registrador_cp +2)

        if operador1 == 0x02:
            if registrador_ax == operador2:
                flag_zero = True
            else:
                flag_zero = False
        
        if operador1 == 0x03:
            if registrador_bx == operador2:
                flag_zero = True
            else:
                flag_zero = False

        if operador1 == 0x04:
            if registrador_cx == operador2:
                flag_zero = True
            else:
                flag_zero = False

        if operador1 == 0x05:
            if registrador_dx == operador2:
                flag_zero = True
            else:
                flag_zero = False
            
    
    if idInstrucao == 0x50:
        operador1= memoria.getValorMemoria(registrador_cp + 1)
    
        registrador_cp = operador1
    
    if idInstrucao == 0x70:
        operador1= memoria.getValorMemoria(registrador_cp + 1)
    
        
        if flag_zero:
            registrador_cp = operador1


 



def calcularProximaInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    print ('Implementar a calcularProximaInstrucao')
    if idInstrucao == 0x40:
        registrador_cp = registrador_cp + 3
    if idInstrucao == 0x01:
        registrador_cp = registrador_cp + 3
    if idInstrucao == 0x10:
        registrador_cp = registrador_cp + 2
    if idInstrucao == 0x20:
        registrador_cp = registrador_cp + 2
    if idInstrucao == 0x00:
        registrador_cp = registrador_cp + 3
    if idInstrucao == 0x30:
        registrador_cp = registrador_cp + 3
    if idInstrucao == 0x31:
        registrador_cp = registrador_cp + 3
    if idInstrucao == 0x41:
        registrador_cp = registrador_cp + 3
    if idInstrucao == 0x79:
        if flag_zero == 1:
            registrador_cp = registrador_cp 
        else:
            registrador_cp = registrador_cp + 2
    if idInstrucao == 0x50:
        registrador_cp = registrador_cp 
    if idInstrucao == 0x70:
        if flag_zero == 1:
            registrador_cp = registrador_cp 
        else:
            registrador_cp = registrador_cp + 2
    if idInstrucao == 0x60:
        registrador_cp = registrador_cp + 3
    if idInstrucao == 0x61:
        registrador_cp = registrador_cp + 3



def dumpRegistradores():
    if CPU_DEBUG:
        print(f'CP[{registrador_cp:02X}] \
            AX[{registrador_ax:02X}]  \
            BX[{registrador_bx:02X}]  \
            CX[{registrador_cx:02X}]  \
            DX[{registrador_dx:02X}]  \
            ZF[{flag_zero}] ')

if __name__ == '__main__':
    while (True):
        #Unidade de Controle
        idInstrucao = buscarEDecodificarInstrucao()

        #ULA
        lerOperadoresExecutarInstrucao(idInstrucao)  

        dumpRegistradores() 

        #Unidade de Controle
        calcularProximaInstrucao(idInstrucao)

        #apenas para nao ficar em loop voce pode comentar a linha abaixo =)
        sys.stdin.read(1)
    
