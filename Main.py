from symbol_table import SymbolTable
from Parser import Parser
from Code import Code

class Main:
    file = open("Fill.asm")
    readlines = file.readlines()

    symbol_table  = SymbolTable()
    Code = Code()

    rom_address = 0
    ram_address = 16

    # First Pass
    for i in readlines:
        firstPass = Parser(i)
        type = firstPass.commandType()
        symbol = firstPass.symbol(type)

        if type == "A_COMMAND" or type == "C_COMMAND": rom_address+=1
        elif type =="L_COMMAND": symbol_table.add_entry('white', rom_address, 'LAB')

    # Second Pass
    for i in readlines:
        machine_command = ''
        secondPass = Parser(i)
        type = secondPass.commandType()
        symbol = secondPass.symbol(type)
        if symbol:
            if (type == "A_COMMAND"):
                if symbol[0].isdigit():
                     binary = symbol
                else:
                    if symbol_table.contains(symbol):
                        binary = symbol_table.get_address(symbol)
                    else:
                        binary = ram_address
                        symbol_table.add_entry(symbol, ram_address, 'VAR')
                        ram_address += 1

                    machine_command = '{0:016b}\n'.format(int(binary)).strip()

        elif (type=="C_COMMAND"):
            dest = secondPass.dest()
            comp = secondPass.comp()
            jmp = secondPass.jmp()
            dest = Code.dest(dest)
            comp = Code.comp(comp)
            jmp = Code.dest(jmp)

            # print("COMP:",secondPass.comp(), "DEST:",secondPass.dest(),"JMP:", secondPass.jmp())
            # print(comp,dest,jmp)
            machine_command = '111{0}{1}{2}\n'.format(comp, dest, jmp).strip()




main = Main()
# main.start()