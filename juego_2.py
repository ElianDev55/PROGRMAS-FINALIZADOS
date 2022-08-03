import random
import os

os.system("cls")
print("""
      
░░█ █░█ █▀▀ █▀▀ █▀█   ▄█   █░█     ▄█   █▀▄ █▀▀   █▀▄ ▄▀█ █▀▄ █▀█ █▀   █▀▀ █░░   █▀█ █░█ █▀▀
█▄█ █▄█ ██▄ █▄█ █▄█   ░█   ▀▄▀     ░█   █▄▀ ██▄   █▄▀ █▀█ █▄▀ █▄█ ▄█   ██▄ █▄▄   ▀▀█ █▄█ ██▄

█▀▀ █▀█ █▄░█ █▀ █ █▀▀ ▄▀█   █▀ █▀█   █▀█ █░█ █▄░█ ▀█▀ █▀█ █▀   █▀▀ ▄▀█ █▄░█ ▄▀█
█▄▄ █▄█ █░▀█ ▄█ █ █▄█ █▀█   ▄█ █▄█   █▀▀ █▄█ █░▀█ ░█░ █▄█ ▄█   █▄█ █▀█ █░▀█ █▀█
      """)



def dados (numero):
    if numero == 1:
        a = print("""
KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK
KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK
KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK
KXXXXKXXXXXXXXXXXXKXXXXXXXXXXXXXXXXXXXXK
KXXXXKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK
KXXXXKXXXXXXXXXXXKKKKKXXXXXXXXXXXXXXXXXK
KXXXXKXXXXXKXXK0xl:::clkKXXXXXXXXXXXXXXK
KXXXXXXXKXXXXKk:........lOXXXXXKXXXXXXXK
KXXXXXXXXXXXXKl.........'dKXXXXXXXXXXXXK
KXXXXKXXKXXXXKd'........,xKXXXXKXXXXXXXK
KXXXXKXXXXXXXX0d:'....'ckKXXXXXKXXXXXXXK
KXXXXKXXXXXXXXXKKOxxxkOKXXXXXXXXXXXXXXXK
KXXXXKXXXXXXXXXXXXXXXXKKXXXXXXXXXXXXXXXK
KXXXXKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK
KXXXXKXXXXXXXXXXXXXXXXXKKXXXXXXXXXXXXXXK
KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKXXXKKXK
KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKXXKKXK
KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK
0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0
              """)
    elif numero == 2:
        a = print("""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMXxllokNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMO'     ;KMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWc       dMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMO'     :KMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMXkoloONMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXd:;;lOWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMK;     .oWMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMk.      :NMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNd.   .;OMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMXOxk0NMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
              """)
    elif numero == 3:
        a = print("""
'::::::::::::::::::::::::::::::::::::' 
.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.
.dMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMd.
.dMMMMMXd:,,:xNMMMMMMMMMMMMMMMMMMMMMMMd.
.xMMMMK:      cNMMMMMMMMMMMMMMMMMMMMMMx.
.dMMMM0'      ;KMMMMMMMMMMMMMMMMMMMMMMx.
.xMMMMWk,.  .:OWMMMMMMMMMMMMMMMMMMMMMMx.
.xMMMMMMN0OOKWMMNKkkk0NMMMMMMMMMMMMMMMx.
.xMMMMMMMMMMMMWO;.    'xNMMMMMMMMMMMMMx.
.xMMMMMMMMMMMMX;       .OMMMMMMMMMMMMMx.
.xMMMMMMMMMMMMNo.      ;KMMMMMMMMMMMMMx.
.xMMMMMMMMMMMMMNkc;;;:dXMMMWWNWMMMMMMMx.
.xMMMMMMMMMMMMMMMMWWWMMMMNk:,',lOWMMMMx.
.xMMMMMMMMMMMMMMMMMMMMMMWd.     .kMMMMx.
.xMMMMMMMMMMMMMMMMMMMMMMWo      .xMMMMx.
.xMMMMMMMMMMMMMMMMMMMMMMMXo'. .,dNMMMMd.
.dMMMMMMMMMMMMMMMMMMMMMMMMWX00KNMMMMMMd.
.xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx.
 cOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOc 
  ....................................  
              """)
    elif numero == 4:
        a = print("""
.oxxxxdddxxxdxxxxxxxxxxxxxxxxxddddxxxxo'
:XMNOoc:coONMMMMMMMMMMMMMMMMNkoc:coONMNc
:X0:      .cXMMMMMMMMMMMMMW0;      .lXNc
:0c        .dWMMMMMMMMMMMMX:        .xNl
:0l        .kWMMMMMMMMMMMMNc        .kNc
:XXo.     ,xNMMMMMMMMMMMMMMKl.    .,kNNc
;XMWXkddxONMMMMMMMMMMMMMMMMMWXkddx0NMMNc
;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc
;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc
;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc
;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc
;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc
;XMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMNc
;XMNko::coONMMMMMMMMMMMMMMMMNkl::coONMNc
:X0;      .cKMMMMMMMMMMMMMW0;      .cXNl
:0c        .dWMMMMMMMMMMMMX:        .xNl
:0l        .kMMMMMMMMMMMMMNc        .kNl
;XXo.    .,xNMMMMMMMMMMMMMMKl.    .,kWNc
;KWNKkdodOXNWWWWWWWWWWWWWWWWNKkdodOXWWXc
.cllllllllllllllllllllllllllllllllllllc.
              """)
    elif numero == 5:
        a = print("""
WWWWWWWWWWWWNWWWWWWWWWWWNWWNNWWWWWWWWWWW
NNNNXklccd0NNNNNNNNNNNNNNNNNNKdcclxKNNNN
NNNKc     'kNNNNNNNNNNNNNNNNO,     ;0NNN
NNNO'      lNNNNNNNNNNNNNNNNd.     .kNNN
NNNXd'.  .c0NNNNNNNNNNNNNNNNKl.  .'dXNNN
NNNNNXOkk0NNNNNNNNNNNNNNNNNNNNKOkOXNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNKOkkOKNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNKo'.  .'oKNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNx.      .xNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNO,      ,ONNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNN0dc::cd0NNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNKkxxOXNNNNNNNNNNNNNNNNNNXOxxkKNNNNN
NNNXx'   .;ONNNNNNNNNNNNNNNNO:.   .oXNNN
NNN0,      cXNNNNNNNNNNNNNNXl      .kNNN
NNNXl.    'kNNNNNNNNNNNNNNNNk'    .cKNNN
NNNNXOolld0NNNNNNNNNNNNNNNNNN0dllokXNNNN
WNNXXNNNNNNNXXXXXXXXXXXXXXXXXNNNNNNXXXNN
MNXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXNW
              """)
    elif numero == 6:
        a = print("""
KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
KXKK0xlllok0XXXXXXXXXXXXKKXX0xolllx0KKXK
KXKx;......:kKXXXXXXXXXXXKKk:......;xKXK
KXk;........c0XXXXXXXXXXXX0c........;OXK
KXO:........l0XXXXXXXXXXXX0l........:OXK
KXKkc'....,lOXXXXXXXXXXXXXXOl,....'ckKXK
KXXKKOdooxOKXXXXXXXXXXXXXXXXKOxoodOKXKXK
KXXKko:;;coOKXXXXXXXXXXXXXXKOoc;;:lkKXXK
KXKo'......,dKXXXXXXXXXXXXKx,......'o0XK
KXk;........:OXXXXXXXXXXXX0c........;kXK
KX0c........l0XKXXXXXXXXXXKl........:OXK
KXKOl,....;o0KXXXXXXXXXXXXX0d;'...,lOKXK
KXXXK0xddk0KXXXXXXXXXXXXXXKXK0kddx0KXXXK
KXX0xc;,,;lkKXXKXXXXXXXXXXXKkl;,,;cx0XXK
KX0l.......'dKXXXXXXXXXXKXKd'.......l0XK
KXk,........c0XKXXXXXXXXKX0:........;kXK
KX0l.......'dKKXXXXXXXXXKKKd'.......l0XK
KXX0dc,',;cxKXKXXXXXXXXXKKXKxc;,,,cd0XXK
KXKXXK0000KXXXXXXXXXXXXXXXXXXK0000KXXKXK
0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0
              """)



lista_de_nombres = []
lista_de_puntos = []
lol = input("ENTER PARA CONTINUAR :")
os.system("cls")
nombre_jugador_1 = input("NOMBRE DEL JUGADOR 1 ES.....")
lista_de_nombres.append(nombre_jugador_1)
a = 0
while a == 0:
    os.system("cls")
    nombre_jugador_2 = input("NOMBRE DEL JUGADOR 2 ES.....")
    if lista_de_nombres[0] == nombre_jugador_2:
        print("ESTE NOMBRE YA HASIDO ESCOGIDO POR OTRO JUGADOR")
    else:
        lista_de_nombres.append(nombre_jugador_2)
        a = 1

puntos_1 = 0
puntos_2 = 0
guardado = 0
while  puntos_1 <= 50 and puntos_2 <= 50 :
    os.system("cls")
    lanzar_dado_1 = input(f"ENTER PARA LANZAR EL DADO EL JUGADOR {nombre_jugador_1}  ")
    dado_1 = random.randrange(1,6)
    puntos_1 += dado_1
    print(dados(dado_1))
    print(f"""
          
  _____  _    _ _   _ _______           _ ______     
 |  __ \| |  | | \ | |__   __|/\       | |  ____|  _ 
 | |__) | |  | |  \| |  | |  /  \      | | |__    (_)
 |  ___/| |  | | . ` |  | | / /\ \ _   | |  __|      
 | |    | |__| | |\  |  | |/ ____ \ |__| | |____   _ 
 |_|     \____/|_| \_|  |_/_/    \_\____/|______| (_)          {puntos_1}
                                                     
                                                     

          """)
    lol = input("ENTER PARA CONTINUAR :")
    os.system("cls")
    lanzar_dado_2 = input(f"ENTER PARA LANZAR EL DADO EL JUGADOR {nombre_jugador_2}  ")
    dado_2 = random.randrange(1,6)
    puntos_2 += dado_2
    print(dados(dado_2))
    print(f"""
          
  _____  _    _ _   _ _______           _ ______     
 |  __ \| |  | | \ | |__   __|/\       | |  ____|  _ 
 | |__) | |  | |  \| |  | |  /  \      | | |__    (_)
 |  ___/| |  | | . ` |  | | / /\ \ _   | |  __|      
 | |    | |__| | |\  |  | |/ ____ \ |__| | |____   _ 
 |_|     \____/|_| \_|  |_/_/    \_\____/|______| (_)          {puntos_2}
                                                     
                                                     
          """)
    lol = input("ENTER PARA CONTINUAR :")
    
    
    if dado_1 == dado_2:
        guardado = puntos_1 + puntos_2
    if dado_1 > dado_2:
        puntos_1 += guardado
        guardado = 0
    else:
        puntos_2 += guardado
        guardado = 0
        

if puntos_1 > puntos_2:
    print(f"""{nombre_jugador_1}
                                                                                                                                        
                                                  ..                                                            
                                   ..;'     ..',:lkxc:;;;;;;;,,,,'..     .;'.                                   
                                  .ckx;..  .;kKXNWWWWNNXXXXXXKK0OOx;.  ..,dkl.                                  
                                ..cOkdxd;...;kXNNWWWWNNNNXXXXKK00Ox;...,oxdkOl'.                                
                               .lxlcodl'.,cloOKXNNNNNNNXXXXXKK00OOxolc,.'cdoccdo.                               
                              .:0Ooxd,..,dl,,o0KKXXNNXXXXXXKKK00Okc,;ld;..,dxok0c.                              
                             .,lddxx;. .:xclxk0K0KKXXXXXKKKK000OOkxkxoxc. .;xxddl,.                             
                             .dkloxc.   .ldxxlcx0000000000000OOkc;lxkxl'   .cxolkx'                             
                             'x0xOO:.  ..':lol;;x00O000000OOOOxc',loo:'..  .;OOxOx'                             
                             'ldodd,..';;;;;;od:;ok0OOOOOOOOko:,;do;;;;;;,..,ododo,.                            
                             ;kkok0l.,:;;;;;;:do;;:ok0OOOOOxc,,;od:;;;;;;:,.c0xokO:                             
                             .lOkkxl,;:;::;;;,;lllloookOOkolollll:;;;:::;;;,cxkkOo.                             
                             .;ddookd:;;::;;;;;;;::;,:OKKO:';::;;;;;;;::;;;dkdodd,.                             
                              .d0OkOxc;,;:;;;;;;;;;;,c0XXOc,;;;;;;;;;;:;;;cxOkk0d'                              
                               .cxddoxOl;;;;;;;;;;;;,c0XX0c';;;;;;;;;;,,lkxoddxl..                              
                             .'..;dkkk0xlll;;;;;;;,;lOKXXKkl,,;;;;;,;clcx0kkkd:..'.                             
                            .;;. .;dkkxddk0x:,;;;cdkKXXXKKKOdl:;;;,:d0Odddkkd;. .;;.                            
                          ..;,. . ..':dkOOOOxlc;:x0KK00000OOOko;;cldOOOOkdc'..   .,;..                          
                .,''''''''',;,'''''',;codolloooc,,;;;;;;;;;,;;,,cooolloddc;,'''''',;,''''''''''.                
                .;;,,,:ooc;,,:ooc;,,:ooccoo:;coo:,,;col:,;col:,,;col;;looooool:;loooooc;,,,,,;;.                
                .;l;;,lKWKl,:kNW0c,cON0lxNNd:xNWKd:;xNXo,:kWW0o;:kWKlc0WNXKKX0llKWWWWWN0l;,;;c;.                
                 .ll;;:kWNx;lKMMNx;dXNd:xNNx:xNWNNOdONXo,:kNWWXkoOWKlc0WXkodol;lKWKdokXW0c,;cl'                 
                  :o:,;oXW0lxNXKN0dOXk:;dXXd:dXKkx0KKXKl';xXKxkKKKX0c:ONNKKK0d;l0W0c;c0WXo,:o:.                 
                  .ll;,:kXKO0Koo0XKK0c.'dKKo,oXKl':xKXKc.'dX0c'ckKX0:,kX0dccc;'cOXX0kOXN0c;lo.                  
                   ;o:''c0XXXk;'xXXXx'..lOOc.:dd;...:ll,..:ol,..,lxd;'d0K0Okkd:;kXKkOKXk:';o:                   
                   .cc..'xXXKl..;ddo,....''...........................',;:clod:;xKk;,xKk;.:c.                   
                    ':'..:ddc'.................';;;;;;;;;;;;;;;;,...............';;..;x0d::'                    
                    .',..........................,;;;;:;;:;;;;,........................,;:,.                    
                     .....',......'co;..       ....,;::;;::;,'...       ..;oc'......,'.....                     
                          .:'.   .l0Kk:.        .....','''''....        .:kKOl'.  .':.                          
                           .:,.  .':::.   ...     ............     ...   .:::,.  .,:.                           
                            .;;.     . ...:xc...      .,,.      ...cx:.....  .  .;;.                            
                             .';,.     .:x0X0d:.  ....l00l....  .cxKX0d:.     .,;'.                             
                               .';,.    .lOkko.   .cdOKXX0kdc.   .oOkkl.    .,;'.                               
                                 .',,'...,,.',.    .:OKK00k:.    .,'.,,...',;'.                                 
                                   ..',,'...       .;doccld:.       ...,,,'..                                   
                                       ..,,,,''........  ........'',,,,..                                       
                                           ..'',,,,,,,,,,',,,,,,,'...                                           
                                                   ..........                                                   
                                                                                    """)
    lolol = input("")
else:
    print(f"""{nombre_jugador_2}
                                                                                                                                        
                                                  ..                                                            
                                   ..;'     ..',:lkxc:;;;;;;;,,,,'..     .;'.                                   
                                  .ckx;..  .;kKXNWWWWNNXXXXXXKK0OOx;.  ..,dkl.                                  
                                ..cOkdxd;...;kXNNWWWWNNNNXXXXKK00Ox;...,oxdkOl'.                                
                               .lxlcodl'.,cloOKXNNNNNNNXXXXXKK00OOxolc,.'cdoccdo.                               
                              .:0Ooxd,..,dl,,o0KKXXNNXXXXXXKKK00Okc,;ld;..,dxok0c.                              
                             .,lddxx;. .:xclxk0K0KKXXXXXKKKK000OOkxkxoxc. .;xxddl,.                             
                             .dkloxc.   .ldxxlcx0000000000000OOkc;lxkxl'   .cxolkx'                             
                             'x0xOO:.  ..':lol;;x00O000000OOOOxc',loo:'..  .;OOxOx'                             
                             'ldodd,..';;;;;;od:;ok0OOOOOOOOko:,;do;;;;;;,..,ododo,.                            
                             ;kkok0l.,:;;;;;;:do;;:ok0OOOOOxc,,;od:;;;;;;:,.c0xokO:                             
                             .lOkkxl,;:;::;;;,;lllloookOOkolollll:;;;:::;;;,cxkkOo.                             
                             .;ddookd:;;::;;;;;;;::;,:OKKO:';::;;;;;;;::;;;dkdodd,.                             
                              .d0OkOxc;,;:;;;;;;;;;;,c0XXOc,;;;;;;;;;;:;;;cxOkk0d'                              
                               .cxddoxOl;;;;;;;;;;;;,c0XX0c';;;;;;;;;;,,lkxoddxl..                              
                             .'..;dkkk0xlll;;;;;;;,;lOKXXKkl,,;;;;;,;clcx0kkkd:..'.                             
                            .;;. .;dkkxddk0x:,;;;cdkKXXXKKKOdl:;;;,:d0Odddkkd;. .;;.                            
                          ..;,. . ..':dkOOOOxlc;:x0KK00000OOOko;;cldOOOOkdc'..   .,;..                          
                .,''''''''',;,'''''',;codolloooc,,;;;;;;;;;,;;,,cooolloddc;,'''''',;,''''''''''.                
                .;;,,,:ooc;,,:ooc;,,:ooccoo:;coo:,,;col:,;col:,,;col;;looooool:;loooooc;,,,,,;;.                
                .;l;;,lKWKl,:kNW0c,cON0lxNNd:xNWKd:;xNXo,:kWW0o;:kWKlc0WNXKKX0llKWWWWWN0l;,;;c;.                
                 .ll;;:kWNx;lKMMNx;dXNd:xNNx:xNWNNOdONXo,:kNWWXkoOWKlc0WXkodol;lKWKdokXW0c,;cl'                 
                  :o:,;oXW0lxNXKN0dOXk:;dXXd:dXKkx0KKXKl';xXKxkKKKX0c:ONNKKK0d;l0W0c;c0WXo,:o:.                 
                  .ll;,:kXKO0Koo0XKK0c.'dKKo,oXKl':xKXKc.'dX0c'ckKX0:,kX0dccc;'cOXX0kOXN0c;lo.                  
                   ;o:''c0XXXk;'xXXXx'..lOOc.:dd;...:ll,..:ol,..,lxd;'d0K0Okkd:;kXKkOKXk:';o:                   
                   .cc..'xXXKl..;ddo,....''...........................',;:clod:;xKk;,xKk;.:c.                   
                    ':'..:ddc'.................';;;;;;;;;;;;;;;;,...............';;..;x0d::'                    
                    .',..........................,;;;;:;;:;;;;,........................,;:,.                    
                     .....',......'co;..       ....,;::;;::;,'...       ..;oc'......,'.....                     
                          .:'.   .l0Kk:.        .....','''''....        .:kKOl'.  .':.                          
                           .:,.  .':::.   ...     ............     ...   .:::,.  .,:.                           
                            .;;.     . ...:xc...      .,,.      ...cx:.....  .  .;;.                            
                             .';,.     .:x0X0d:.  ....l00l....  .cxKX0d:.     .,;'.                             
                               .';,.    .lOkko.   .cdOKXX0kdc.   .oOkkl.    .,;'.                               
                                 .',,'...,,.',.    .:OKK00k:.    .,'.,,...',;'.                                 
                                   ..',,'...       .;doccld:.       ...,,,'..                                   
                                       ..,,,,''........  ........'',,,,..                                       
                                           ..'',,,,,,,,,,',,,,,,,'...                                           
                                                   ..........                                                   
                                                                                    """)
    lolol = input("")