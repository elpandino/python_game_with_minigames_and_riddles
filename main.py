#copyright to Andrea Bandolfini and Leonardo Muschietti
#https://github.com/elpandino/python_game_with_minigames_and_riddles.git
import curses
import random
import time
import os
import pickle
import bisect
import sqlite3
from random import randint
import sys
print(" ")
print(" ")
print("                           LO SCHERLOCK HOLMES DEGLI INDOVINELLI")
print(" ")
print(" ")
re=input ("Premi invio per continuare... ")
print(" ")
print(" ")
print("Computer : Hey non ti avevo visto arrivare, sei nuovo da queste parti?")
print(" ")
print(" ")
re=input ("Premi invio per continuare... ")
print(" ")
print(" ")
print("Io : si sono arrivat* poco tempo fa, ho solo un'amica, lei si chiama Ely .")
print(" ")
print(" ")
re=input ("Premi invio per continuare... ")
print(" ")
print(" ")
print("Computer : Facciamo qualche domanda per conoscerci meglio")
print(" ")
print(" ")
re=input ("Premi invio per continuare... ")
print(" ")
print(" ")
#DOMANDE ALL'UTENTE
sesso=input("Computer : Sei Maschio o Femmina? m/f/no      ")
print(" ")
print(" ")
bimbo=input("Computer : Come ti chiami? (METTI SOLO IL NOME )       ")
print(" ")
bimbetto=bimbo.title()
print(" ")
if len (bimbetto)>6:
    print("i tuoi genitori potevano farlo più corto?")
    print(" ")
    print("Perciò penso proprio che ti chiamero pinco, o forse no???")
    print("vabbe per rispetto ti chiamero con il tuo vero nome")
    print(" ")                     
if bimbo=="pinco":
    print(" ")
    bimbetto="pinco nei tuoi sogni"
    print("seeee, e allora io sono pallino")
if bimbo=="Gumball":
    print(" ")
    bimebetto="Gumball nei tuoi sogni"
    print("seeee, e allora io sono Darwin")
    print(" ")
if bimbo=="Finn":
    print(" ")
    bimebetto="Finn nei tuoi sogni"
    print("seeee, e allora io sono jake")
    print(" ")
if bimbo=="Moritz":
    print(" ")
    bimebetto="Moritz nei tuoi sogni"
    print("seeee, e allora io sono Lennard") 
    print(" ")
if bimbo=="Jake":
    print(" ")
    bimbetto="Jake nei tuoi sogni"
    print("seeee, e allora io sono Finn") 
    print(" ")
if bimbo=="Goku":
    print(" ")
    bimebetto="Goku nei tuoi sogni"
    print("seeee, e allora io sono Vegeta") 
    print(" ")
if bimbo=="Franklin":
    print(" ")
    bimebetto="Franklin nei tuoi sogni"
    print("seeee, e allora io sono Michael") 
    print(" ")
if bimbo=="":
    print(" ")
    bimebetto=" nei tuoi sogni"
    print("seeee, e allora io sono ") 
    print(" ")               
    print("ma stai zitto e gioca")
    print(" ")
if sesso=="m":
    bimbone=len(bimbetto)+2
    print(" ")
    print(" ")
    print("Vabbene signorino, piacere...")
    print(" ")
    print("╔"+"═"*bimbone+"╗")
    print("║", bimbetto, "║")
    print("╚"+"═"*bimbone+"╝")
elif sesso=="f":
    bimbone=len(bimbetto)+2
    print(" ")
    print(" ")
    print("Vabbene signorina, piacere...")
    print(" ")
    print("♥"+"♥"*bimbone+"♥")
    print("♥", bimbetto, "♥")
    print("♥"+"♥"*bimbone+"♥")
elif sesso=="no":
    bimbone=len(bimbetto)+2
    print(" ")
    print(" ")
    print("Vabbene personaccia, piacere...")
    print(" ")
    print("☻"+"☻"*bimbone+"☻")
    print("☻", bimbetto, "☻")
    print("☻"+"☻"*bimbone+"☻")
else:
    bimbone=len(bimbetto)+2
    print(" ")
    print(" ")
    print("Vabbene..., piacere...?!")
    print(" ")
    print("◘"+"◘"*bimbone+"◘")
    print("◘", bimbetto, "◘")
    print("◘"+"◘"*bimbone+"◘")
print(" ")
print("Computer : che figata di nome : stupendo")
print(" ")
print(" ")
rqe=input("Premi invio per continuare... ")
print(" ")
print(" ")
print("Computer : Dunque, tu devi sapere che Ely è scomparsa l'ultima persona che l'ha vista è Paolo per raggiungerlo, se vuoi parlarci dovrai affrontare alcune sfide, create da me.")
print(" ")
print(" ")
rye=input("Premi invio per continuare... ")
print(" ")
print(" ")
print(bimbetto, " : Aspetta ma perchè fatti da te?  ")
print(" ")
print(" ")
rle=input("Premi invio per continuare... ")
print(" ")
print(" ")
print("Computer : Okay, mi hai scoperto ,l'ho rapita io............ ")
print(" ")
print(" ")
rre=input("Premi invio per continuare... ")
print(" ")
print(" ")
print("Computer : Sono gentile, ti farò sentire il suo l'ultimo messaggio vocale, era indirizzato a te... sappi però che ora te la dovrai vedere con me!!!")
print(" ")
print(" ")
rhe=input("Premi invio per continuare... ")
print(" ")
print(" ")
print("Ely : Non sarò io a guidarti, ma uno dei miei amici, ADDIO, forse un giorno ci rincontreremo.")
print(" ")
print(" ")
rse=input("Premi invio per continuare... ")
print(" ")
print(" ")
gino=input("Scrivi il nome che vorresti che avesse la tua guida :   ")
print(" ")
print(" ")
rdfge=input ("Premi invio per continuare... ")
print(" ")
print(" ")
print(gino, " : Perfetto d'ora in poi non potrai più tirarti indietro, se pensi di non potercela fare chiudi il gioco, non cerchiamo persone deboli...")
print(" ")
print(" ")
rwe=input ("Premi invio per continuare... ")
print(" ")
print(" ")
print(gino, " : Via con il primo indovinello, e ricordati che a ogni errore dovrai ricominciare")
print(" ")
print(" ")
klre=input ("Premi invio per continuare... ")
print(" ")
print(" ")
sgg=input("Computer : Se la usi ha sei gambe, altrimenti ne ha quattro, che cos'è? (scrivi tutto in minuscolo) : ")
print(" ")
print(" ")
if sgg=="sedia":
    print(gino, " : RISPOSTA CORRETTA, COMPLIMENTI!!! ")
else:
    print(gino, " : MI DISPIACE LA RISPOSTA NON E' CORRETTA, la risposta corretta era : 'sedia'")
    print("                               GAME OVER")
    print(" ")
    print(" ")
    kqlrre=input ("Premi invio per finire... ")
    exit()
print(" ")
print(" ")
kqlre=input ("Premi invio per continuare... ")
print(" ")
print(" ")
print(gino, " : Via con il secondo indovinello, altro giro altra corsa................... ")  
print(" ")
print(" ")
klsre=input ("Premi invio per continuare... ")
print(" ")
print(" ")
fjyf=input("Computer : Cos'è che è caldo quando è fresco? (scrivi solo il nome in minuscolo) : ")
print(" ")
print(" ")
if fjyf=="pane":
    print(gino, "RISPOSTA CORRETTA, COMPLIMENTI!!!")
else:
    print(gino, "MI DISPIACE, LA RISPOSTA NON E' CORRETTA, la risposta corretta era : 'pane'")
    print("            GAME OVER")
    sfd=input ("Premi invio per finire...")
    exit()
print(" ")
print(" ")
print(gino, " : molto bene, adesso ti aspettera un momento ricreativo, sei pronto?")
print(" ")
print(" ")
fgfgfgfgfgfgfgfgfgfg=input ("Premi invio per continuare...")
print(" ")
print(" ")
print("Computer : solo per te ho trovato questo sudoku, sono sicuro che ti divertirai, sappi però che se non lo finisci rimarrai a questo livello")
print(" ")
print(" ")
gigghgh=input ("Premi invio per continuare...")
print(" ")
print(" ")
class Block(object):
    """Store a single 3x3 block in the complete field."""

    def __init__(self):
        self._block = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __setitem__(self, point, value):
        """Set the value, check that value is not already in the block."""
        # n == -n, as n < 0 means user generated abs(n).
        if abs(self._block[point[1] + 3 * point[0]]) == abs(value):
            self._block[point[1] + 3 * point[0]] = value
            return
        if value != 0 and (value in self._block or -value in self._block):
            raise ValueError("Block already contains %d" % value)
        self._block[point[1] + 3 * point[0]] = value

    def __getitem__(self, point):
        """Return the value at the given point."""
        return self._block[point[1] + 3 * point[0]]


class Block(object):
    """Store a single 3x3 block in the complete field."""

    def __init__(self):
        self._block = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __setitem__(self, point, value):
        """Set the value, check that value is not already in the block."""
        # n == -n, as n < 0 means user generated abs(n).
        if abs(self._block[point[1] + 3 * point[0]]) == abs(value):
            self._block[point[1] + 3 * point[0]] = value
            return
        if value != 0 and (value in self._block or -value in self._block):
            raise ValueError("Block already contains %d" % value)
        self._block[point[1] + 3 * point[0]] = value

    def __getitem__(self, point):
        """Return the value at the given point."""
        return self._block[point[1] + 3 * point[0]]


class Sudoku(object):

    def __init__(self):
        self._field = [Block() for i in range(9)]
        # Cached values used in solve() and populate()
        self._values = list(range(1, 10))
        self._points = [(x, y) for y in range(9) for x in range(9)]

    def clear(self):
        """Reset the game to empty."""
        for b in self._field:
            b._block = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def candidates(self, point):
        """Return all candidates at the point (x, y)."""
        candidates = set()
        previous = self[point]
        for i in self._values:
            try:
                self[point] = i
            except ValueError:
                pass
            else:
                candidates.add(i)
        self[point] = previous
        return candidates

    def populate(self, n=36):
        """Populate ca. n fields of the Sudoku.
        Clear the Sudoku, run the solver using random values and
        remove as many values as possible.
        """
        # Randomize the list of points and values
        random.shuffle(self._points)
        random.shuffle(self._values)
        self.clear()
        self.solve()

        for point in self._points:
            if self[point] == 0:
                continue
            val = self[point]
            for v in self.candidates(point):
                if v == val:
                    continue
                self[point] = v
                if self.solve(True):
                    self[point] = val
                    break
            else:
                if (81 - sum(b._block.count(0) for b in self._field) < n):
                    self[point] = val
                    break
                self[point] = 0

        for point in self._points:
            self[point] *= -1

    def __str__(self):
        """Represent the Sudoku as a string (for debugging purposes)."""
        s = ""
        for y in range(9):
            for x in range(9):
                s += '%d ' % self[x, y]
                if (x + 1) % 3 == 0:
                    s += " "
            s += "\n"
            if (y + 1) % 3 == 0:
                s += "\n"
        return s.strip()

    def __getitem__(self, p):
        pb = (p[0] // 3, p[1] // 3)
        block = self._field[pb[1] + 3 * pb[0]]

        return block[p[0] % 3, p[1] % 3]

    def __setitem__(self, p, val):
        if self[p] < 0 and val >= 0:
            raise ValueError("Value at point %s is pre-defined" % str(p))
        if val != 0:
            for i in range(9):
                if i != p[1] and abs(self[p[0], i]) == abs(val):
                    raise ValueError("Already in column: %d" % val)
                if i != p[0] and abs(self[i, p[1]]) == abs(val):
                    raise ValueError("Already in row: %d" % val)

        pb = (p[0] // 3, p[1] // 3)
        block = self._field[pb[1] + 3 * pb[0]]

        block[p[0] % 3, p[1] % 3] = val

    def is_solved(self):
        return all(0 not in self._field[i]._block for i in range(0, 9))

    def solve(self, reset=False):
        """Solve the Sudoku.
        If 'reset' is True, just check whether the sudoku can be solved,
        after return the sudoku will be identical to before the call.
        """
        if self.is_solved():
            return True

        field = None
        for x in range(9):
            if field is not None:
                break
            for y in range(9):
                if self[x, y] == 0:
                    field = (x, y)
                    break

        if field is None:
            return True

        for new in self._values:
            try:
                self[field] = new
            except ValueError:
                continue
            else:
                if self.solve(reset):
                    if reset:
                        self[field] = 0
                    return True
                else:
                    self[field] = 0


class CursesUI(object):
    """Command-line 'curses' interface."""

    def __init__(self):
        self._screen = curses.initscr()
        self._sudoku = Sudoku()

        # Draw the borders
        self._screen.vline(0, 4 * 3 - 2, curses.ACS_VLINE, 2 * 9 - 1)
        self._screen.vline(0, 4 * 6 - 2, curses.ACS_VLINE, 2 * 9 - 1)
        self._screen.hline(2 * 3 - 1, 0, curses.ACS_HLINE, 4 * 9 - 3)
        self._screen.hline(2 * 6 - 1, 0, curses.ACS_HLINE, 4 * 9 - 3)
        self._screen.addch(2 * 3 - 1, 4 * 3 - 2, curses.ACS_PLUS)
        self._screen.addch(2 * 3 - 1, 4 * 6 - 2, curses.ACS_PLUS)
        self._screen.addch(2 * 6 - 1, 4 * 3 - 2, curses.ACS_PLUS)
        self._screen.addch(2 * 6 - 1, 4 * 6 - 2, curses.ACS_PLUS)
        self._draw_sudoku()
        curses.noecho()
        curses.cbreak()
        self._screen.keypad(1)

    def __enter__(self, *a):
        return self

    def __exit__(self, *a):
        curses.nocbreak()
        self._screen.keypad(0)
        curses.echo()
        curses.endwin()

    def _draw_sudoku(self):
        for y in range(0, 9):
            for x in range(0, 9):
                value = self._sudoku[x, y]
                attr = curses.A_BOLD if value < 0 else 0
                # Mark cells with only one possible solution.
                #if len(self._sudoku.candidates((x,y))) == 1:
                #    attr  |= curses.A_UNDERLINE
                self._screen.addch(2 * y, 4 * x, ord('0') + abs(value), attr)

    def _print_string(self, string):
        self._screen.move(20, 0)
        self._screen.deleteln()
        self._screen.addstr(string)

    def _help(self):
        self._print_string("Commands: (q)uit, (p)opulate, (P)opulate, "
                           "(r)eset, (c)andidates, (s)olve")

    def main(self):
        x = 0
        y = 0
        self._help()
        while True:
            self._screen.move(y, x)
            c = chr(self._screen.getch())
            if c == ':':
                self._print_string(":")
                curses.echo()
                #self._screen.move(20, 0)
                c = self._screen.getstr()
                curses.noecho()
            if c == 'q':
                break  # Exit the while()
            elif c == 'h':
                self._help()
            elif c in ('p', 'P'):
                if c == 'P':
                    self._print_string("Enter number of fields: ")
                    curses.echo()
                    n = int(self._screen.getstr())
                    curses.noecho()
                else:
                    n = 36
                start = time.time()
                self._sudoku.populate(n)
                end = time.time()
                self._draw_sudoku()
                self._print_string("Populated with %d fields in %.3f seconds"
                                   % (n, end - start))
            elif c == 's':
                if not self._sudoku.solve():
                    self._print_string("Could not solve sudoku")
                self._draw_sudoku()
            elif c == 'r':
                self._sudoku = Sudoku()
                self._draw_sudoku()
            elif c == 'c':
                point = (x // 4, y // 2)
                self._print_string("Candidates for %s are: %s" %
                                   (point, self._sudoku.candidates(point)))
            elif c == chr(curses.KEY_LEFT):
                x -= x >= 4 and 4 or 0
            elif c == chr(curses.KEY_RIGHT):
                x += x + 4 < 4 * 9 and 4 or 0
            elif c == chr(curses.KEY_UP):
                y -= y >= 2 and 2 or 0
            elif c == chr(curses.KEY_DOWN):
                y += y + 2 < 2 * 9 and 2 or 0
            elif c in "0123456789":
                try:
                    self._sudoku[x // 4, y // 2] = ord(c) - ord('0')
                    self._screen.addch(y, x, c)
                    # If single-candidate cells should be highlighted, use the
                    # following instead of self._screen.addch():
                    #self._draw_sudoku()
                except Exception as e:
                    self._print_string(str(e))
                else:
                    if self._sudoku.is_solved():
                        self._print_string("Solved")
                    else:
                        self._print_string("")
            else:
                self._print_string("Error: Invalid command '%s'" % c)


if __name__ == '__main__':
     with CursesUI() as ui:
        ui.main()

print(" ")
print(" ")
domandaovvia=input("Computer : non mi aspettavo che tu fossi così tanto inteligente, comunque ti sei divertito?  si/no  ")
print(" ")
print(" ")
print("Computer : sono molto contento, ma adesso ti aspetta il 3 indovinello il quale salirà di difficoltà!!!!")
print(" ")
print(" ")
h=input("Premi invio per continuare...")


print(gino, "via con il terzo indovinello, buona fortuna")
print(" ")
print(" ")
ballo=input("Computer : non hanno lancette, ma fanno rumore allo scoccare di ogni ora, cosa sono? (scrivi solo il nome al plurale in minuscolo) :    ")
print(" ")
print(" ")
if ballo =="campane" :
    print(gino, "RISPOSTA CORRETTA, COMPLIMENTI!!!")
else:
    print(gino, "MI DISPIACE, LA RISPOSTA NON E' CORRETTA, la risposta corretta era : 'campane'")
    print("         GAME OVER")
    exit()
print(" ")
print(" ")
print("Computer : okay, siamo solo agli inizi, ci sarà modo di farti perdere")
print(" ")
print(" ")
print(gino, " : Via con il quarto indovinello... ")
print(" ")
print(" ")
jygg0=input("Computer : Si spoglia quando ha freddo, che cos'è? (scrivi solo il nome in minuscolo) : ")
print(" ")
print(" ")
if jygg0=="albero" :
   print(gino, "RISPOSTA CORRETTA, COMPLIMENTI!!! ")
else:
   print(gino, "MI DISPIACE, LA RISPOSTA NON E' CORRETTA, la risposta corretta era : 'albero'")
   print("         GAME OVER")
   exit()
print(" ")
print(" ")
uykguhg=input("Premi invio per continuare")
print(" ")
print(" ")
db = sqlite3.connect('database.db')
c=db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS data(name TEXT , highscore REAL)")
db.commit()

def welcome(name,highscore): # Display the welcoming message 
    print("                    Ciao {} ! \n\n         Benvenuto nei giochi matematici \n\n                    Il tuo punteggio più alto è : {}\n\n____________________________________________________________\n\n".format(name,highscore))
    input("Premi invio per iniziare")
    
def main():
    print("____________________________________________________________\n\n                         [Giochi Matematici]\n\n____________________________________________________________\n")
    data=c.execute("SELECT * FROM data")

    # Count the number of the table's rows 
    x=0
    for i in data:
        x=x+1
        
    if x==0: # If empty (first run)
        # Ask about the user name
        ask=True
        while ask:
            try:
                name = input("[+]Pinello : PerFavore reinserisci il tuo nome : ")
                if name=="" or len(name)==0:
                    print("Metti un nome valido !")
                else:
                    ask=False                
            except valueError:
                print("Please Enter a valid value")
                askName()
                
        print("\n___________________________________________________________\n")
        c.execute("INSERT INTO data VALUES(?,?)",(name,"0")) # Set the name in database 
        db.commit()  
        welcome(name,"0")
        highscore=0
        
    else: # User played before
        data=c.execute("SELECT * FROM data")
        for i in data: # Get the name and highscore        
            name=i[0]
            highscore=i[1]
        welcome(name,highscore)
        
    score=0
    lose=False
    while lose!=True:
        calc=random.randint(0,1) # Generate a random calculation type 0=[+] 1=[*]

        if calc==0: #(+)
            fnum=random.randint(2,50) # First number
            snum=random.randint(2,50) # Second number
            result=fnum+snum
            inp="[+] {} + {} = " # User input text
            
        else: #(*)
            fnum=random.randint(1,10)
            snum=random.randint(1,10)
            result=fnum * snum
            inp="[+] {} * {} ="
            
        def askUser(): # Ask user what is the result
                userInput=input(inp.format(fnum,snum))
                try:
                    userInput=int(userInput) # Try to make input as int
                    return userInput
                except: # If user input a text or leaft it empty
                    print("Inserisci una risposta valida..")
                    askUser() # Reask again
        userInput=askUser()
        
        if userInput==result: # Correct answer 
             score=score+1 
             if score>highscore: # If this score is the high score 
                 c.execute("UPDATE data SET highscore =  ? WHERE name = ?",(score,name)) # Change highscore in database
                 db.commit()
                 print("Giusto ! , punteggio più alto raggiunto ! il tuo punteggio : {} ".format(score)) # Show message
             else: # The score is not the highscore
                 print("Giusto ! il tuo punteggio è di : {}".format(score))

        else: # Wrong answer
            score=0
            print("Oops ! Risposta Sbagliata!")
            userAgain=input("[+] Vuoi giocare di nuovo? (s,n) : ").lower()
            if userAgain=="n":
                print("alla prossima !")
                db.close()
                lose=True
main()
print(" ")
print(" ")
print(gino, " : Ti sei divertito, io si solo a guardarti WuW, comunque adesso rinizia il difficile : mica sei venuto qui per giocare!!!")
print(" ")
print(" ")
hfr=input("Premi invio per continuare...")
print(" ")
print(" ")
domandaovvissima=input("Computer : sei pronto per il secondo indovinello? si/si")
print(" ")
print(" ")
print("Computer : Perfetto!!")
print(" ")
print(" ")
rh=input("Premi invio per continuare...")
print(" ")
print(" ")
print("Computer : Ecco a te il prossimo indovinello")
print(" ")
print(" ")
eh=input("Premi invio per continuare...")
print(" ")
print(" ")
print("Computer : Serve solo quando si getta, cosa è? (scrivi in minuscolo solo il nome) ")
print(" ")
print(" ")
terza=input("  ")
print(" ")
print(" ")
if terza=="ancora":
    print("Computer : molto bene, adesso ti aspetta il sesto indovinello, che sarà molto più difficile.")
    print(" ")
    print(" ") 
    th=input("Premi invio per continuare...")
    print(" ")
    print(" ") 
else:
    print("Computer : RISPOSTA SBAGLIATA, quella corretta era 'ancora' ")
    print(" ")
    print(" ") 
    print("            GAME OVER!!!!!!!")
    print(" ")
    print(" ") 
    print("Computer : Ritenta e sarai più fortuati")
    print(" ")
    print(" ") 
    hthhfv=input("Premi invio per finire...")
    exit()
print(" ")
print(" ")
print(gino," : e via con il sesto, so che puoi farcela!!!")
print(" ")
print(" ")
print("Premi invio per continuare... ")
print(" ")
print(" ")
khhhhhj=input("Computer : Una volta scoperto non esiste più. Cos’è? (scrivi in minuscolo e solamente il nome)   ")
print(" ")
terzhh=input("  ")
print(" ")
print(" ")
if terzhh=="segreto":
    print("Computer : MOLTO BENE, adesso ti aspetta il settimo indovinello, che sarà molto più difficile.")
    print(" ")
    print(" ") 
    th=input("Premi invio per continuare...")
    print(" ")
    print(" ") 
else:
    print("Computer : RISPOSTA SBAGLIATA, quella corretta era segreto")
    print(" ")
    print(" ") 
    print("            GAME OVER!!!!!!!")
    print(" ")
    print(" ")
    print("Premi invio per uscire")
    print(" ")
    exit()

print(" ")
print(" ")

print("Visto il tuo impegno costante, adesso ci sarà un piccolo giochino come ricompensa")
class Field:
    def __init__(self, size):
        self.size = size
        self.icons = {
            0: ' . ',
            1: ' * ',
            2: ' ▲ ',
            3: ' @ ',
        }
        self.snake_coords = []
        self._generate_field()
        self.add_entity()

    def add_entity(self):
        
        while(True):
            i = randint(0, self.size-1)
            j = randint(0, self.size-1)
            entity = [i, j]
            
            if entity not in self.snake_coords:
                self.field[i][j] = 3
                break

    def _generate_field(self):
        self.field = [[0 for j in range(self.size)] for i in range(self.size)]

    def _clear_field(self):        
        self.field = [[j if j!= 1 and j!= 2 else 0 for j in i] for i in self.field]


    def render(self, screen):
        size = self.size
        self._clear_field()


        # Render snake on the field
        for i, j in self.snake_coords:
            self.field[i][j] = 1

        # Mark head
        head = self.snake_coords[-1]
        self.field[head[0]][head[1]] = 2

        for i in range(size):
            row = ''
            for j in range(size):
                row += self.icons[ self.field[i][j] ]

            screen.addstr(i, 0, row)

    def get_entity_pos(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == 3:
                    return [i, j]

        return [-1, -1]


    def is_snake_eat_entity(self):
        entity = self.get_entity_pos()
        head = self.snake_coords[-1]
        return entity == head


class Snake:
    def __init__(self, name):
        self.name = name
        self.direction = curses.KEY_RIGHT

        # Init basic coords
        self.coords = [[0, 0], [0, 1], [0, 2], [0, 3]]
        
    def set_direction(self, ch):

        # Check if wrong direction
        if ch == curses.KEY_LEFT and self.direction == curses.KEY_RIGHT:
            return
        if ch == curses.KEY_RIGHT and self.direction == curses.KEY_LEFT:
            return
        if ch == curses.KEY_UP and self.direction == curses.KEY_DOWN:
            return
        if ch == curses.KEY_DOWN and self.direction == curses.KEY_UP:
            return 

        self.direction = ch

    def level_up(self):
        # get last point direction
        a = self.coords[0]
        b = self.coords[1]

        tail = a[:]

        if a[0] < b[0]:
            tail[0]-=1
        elif a[1] < b[1]:
            tail[1]-=1
        elif a[0] > b[0]:
            tail[0]+=1
        elif a[1] > b[1]:
            tail[1]+=1

        tail = self._check_limit(tail)
        self.coords.insert(0, tail)

    def is_alive(self):
        head = self.coords[-1]
        snake_body = self.coords[:-1]
        return head not in snake_body

    def _check_limit(self, point):
        # Check field limit
        if point[0] > self.field.size-1:
            point[0] = 0
        elif point[0] < 0:
            point[0] = self.field.size-1
        elif point[1] < 0:
            point[1] = self.field.size-1
        elif point[1] > self.field.size-1:
            point[1] = 0

        return point

    def move(self):
        # Determine head coords
        head = self.coords[-1][:]

        # Calc new head coords
        if self.direction == curses.KEY_UP:
            head[0]-=1
        elif self.direction == curses.KEY_DOWN:
            head[0]+=1
        elif self.direction == curses.KEY_RIGHT:
            head[1]+=1
        elif self.direction == curses.KEY_LEFT:
            head[1]-=1

        # Check field limit
        head = self._check_limit(head)

        del(self.coords[0])
        self.coords.append(head)
        self.field.snake_coords = self.coords

        if not self.is_alive():
            sys.exit()


        # check if snake eat an entity
        if self.field.is_snake_eat_entity():
            curses.beep()
            self.level_up()
            self.field.add_entity()




    def set_field(self, field):
        self.field = field


def main(screen):
    # Configure screen
    screen.timeout(0)

    # Init snake & field
    field = Field(10)
    snake = Snake("Joe")
    snake.set_field(field)

    while(True):
        # Get last pressed key
        ch = screen.getch()
        if ch != -1:
            # If some arrows did pressed - change direction
            snake.set_direction(ch)

        # Move snake
        snake.move()
        
        # Render field
        field.render(screen)
        screen.refresh()
        
        time.sleep(.4)

if __name__=='__main__':
    curses.wrapper(main)

print(" ")
print(" ")
print(gino," : Sappi che d'ora in poi saranno molto difficili, vai e vinci!!!")
print(" ")
print(" ")
print("Premi invio per continuare... ")
print(" ")
print(" ")
khhhhhj=input("Computer : Una volta scoperto non esiste più. Cos’è? (scrivi in minuscolo e solamente il nome)   ")
print(" ")
terzhdh=input("  ")
print(" ")
print(" ")
if terzhdh=="segreto":
    print("Computer : MOLTO BENE, adesso ti aspetta il settimo indovinello, che sarà molto più difficile.")
    print(" ")
    print(" ") 
    th=input("Premi invio per continuare...")
    print(" ")
    print(" ") 
else:
    print("Computer : RISPOSTA SBAGLIATA, quella corretta era segreto")
    print(" ")
    print(" ") 
    print("            GAME OVER!!!!!!!")
    print(" ")
    print(" ")
    print("Premi invio per uscire")
    print(" ")
    exit()

















































































































































































































































































































































































































































































































































































































































































































































































































































#millesima riga (non ci arriveremo mai)