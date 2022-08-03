import random
import os
os.system("cls")

a = input("""      
░█▀▀█ ▒█▀▀▄ ▀█▀ ▒█░░▒█ ▀█▀ ▒█▄░▒█ ▒█▀▀▀ 　 ▒█▀▀▀ ▒█░░░ 　 ▒█▄░▒█ ▒█░▒█ ▒█▀▄▀█ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▀█ 　 ▒█▀▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀▄ ▒█▀▀▀█ 
▒█▄▄█ ▒█░▒█ ▒█░ ░▒█▒█░ ▒█░ ▒█▒█▒█ ▒█▀▀▀ 　 ▒█▀▀▀ ▒█░░░ 　 ▒█▒█▒█ ▒█░▒█ ▒█▒█▒█ ▒█▀▀▀ ▒█▄▄▀ ▒█░░▒█ 　 ▒█▄▄█ ▒█▀▀▀ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█░▒█ ▒█░░▒█ 
▒█░▒█ ▒█▄▄▀ ▄█▄ ░░▀▄▀░ ▄█▄ ▒█░░▀█ ▒█▄▄▄ 　 ▒█▄▄▄ ▒█▄▄█ 　 ▒█░░▀█ ░▀▄▄▀ ▒█░░▒█ ▒█▄▄▄ ▒█░▒█ ▒█▄▄▄█ 　 ▒█░░░ ▒█▄▄▄ ▒█░░▀█ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄█ 

▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ 　 ▒█░░░ ░█▀▀█ 　 ▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▒█░▒█ ▒█▄░▒█ ▀█▀ ░█▀▀█ 
▒█▄▄█ ▒█░░▒█ ▒█▄▄▀ 　 ▒█░░░ ▒█▄▄█ 　 ▒█▒█▒█ ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█▒█▒█ ▒█░ ▒█▄▄█ 
▒█░░░ ▒█▄▄▄█ ▒█░▒█ 　 ▒█▄▄█ ▒█░▒█ 　 ▒█░░▒█ ▒█░▒█ ░▀▀█▄ ░▀▄▄▀ ▒█░░▀█ ▄█▄ ▒█░▒█ \n\n\nENTER PARA COMENZAR  """)
random = random.randrange(1,100)
contador = 0
respuesta = int(input("""
            ╔═══════════════╗

             DIGITE EL NUMERO 

            ╚═══════════════╝ \n\n"""))

while random != respuesta :
    contador += 1
    if respuesta < random:
        os.system("cls")
        print("""
              ╔════════════.✵.════════════╗
              
               !ES MAYOR EL NUMERO PENSADO¡
              
              ╚════════════.✵.════════════╝""")
        espacio = input("ENTER PARA CONTINUAR ")
        
    else:
                os.system("cls")
                print("""
              ╔════════════.✵.════════════╗
              
               !ES MENOR EL NUMERO PENSADO¡
              
              ╚════════════.✵.════════════╝""")
                espacio = input("ENTER PARA CONTINUAR ")
                
    
    os.system("cls")
    print(f"""
          
█▀▀ █▀█ █▄░█ ▀█▀ ▄▀█ █▀▄ █▀█ █▀█
█▄▄ █▄█ █░▀█ ░█░ █▀█ █▄▀ █▄█ █▀▄ -------------> {contador}""")
    respuesta = int(input("""
            ╔═══════════════╗

             DIGITE EL NUMERO 

            ╚═══════════════╝ \n\n"""))

os.system("cls")
print(f"""
          
█▀▀ █▀█ █▄░█ ▀█▀ ▄▀█ █▀▄ █▀█ █▀█
█▄▄ █▄█ █░▀█ ░█░ █▀█ █▄▀ █▄█ █▀▄ -------------> {contador}""")
print("""
                                                                                                                                        
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

finalizar = input("PRECIONE PARA FINALIZAR ENTER")