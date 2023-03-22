from random import randint


class Game:
	def __init__(self):
		self.n=0
		self.m=0
		self.Matrix=None
		self.kraj=False
		self.rekurzija=1
		self.row=0
		self.column=0

	def main(self):
		self.dimenzije()
		self.pocetnoStanje()
		self.prikazTable()
		prviIgra=self.koIgraPrvi()
		for i in range(int((self.m * self.n) / 2) + 1):
			if(self.kraj == False):
				if(prviIgra == "C"):
					if(i%2 == 0): self.igracX()
					else: 
						if(self.krajIgreO()):
							self.minimax(prviIgra)
				else: 
					if(i%2 == 0): 
						if(i == 0): 
							self.Matrix[0][1]='X'
							self.Matrix[1][1]='X'
							self.prikazTable()
						else: 
							if(self.krajIgreX()):
								self.minimax(prviIgra)
					else: self.igracO()

	def minimax(self,prviIgra):
		i=0
		j=0
		if(prviIgra=="C"):
			l, ri, rj = self.max(self.rekurzija,"O",i,j)
			while not(self.proveriPotez(ri,rj,"O")):
				rj = randint(0,self.m)
				ri = randint(0,self.n)
			self.odigrajPotez(ri,rj,"O")
		else:
			l, ri, rj = self.max(self.rekurzija,"X",i,j)
			while not(self.proveriPotez(ri,rj,"X")):
				rj = randint(0,self.m)
				ri = randint(0,self.n)
			self.odigrajPotez(ri,rj,"X")
		self.prikazTable()

	def max(self, rekurzija, igrac, ri, rj):
		if(rekurzija == 0):
			if(igrac == "X"):
				return self.izracunajPoteze("X") - self.izracunajPoteze("O"), ri, rj
			else:
				return self.izracunajPoteze("O") - self.izracunajPoteze("X"), ri, rj

		eval = -self.n * self.m
		row=ri
		col=rj
		
		for i in range(self.n):
			for j in range(self.m):
				if(self.odigrajPotez(i, j, igrac)):
					if(igrac=="O"):
						l = self.min(rekurzija-1, "X")
					else:
						l = self.min(rekurzija-1, "O")
					self.obrisiPotez(i, j, igrac)
					if(l > eval):
						eval = l
						row=i
						col=j
						self.column=j
						self.row=i
		return eval, row, col

	def min(self, rekurzija, igrac):
		if(rekurzija == 0):
			if(igrac == "O"):
				return self.izracunajPoteze("X") - self.izracunajPoteze("O")
			else:
				return self.izracunajPoteze("O") - self.izracunajPoteze("X")

		eval = self.n * self.m
		row=0
		column=0
		for i in range(self.n):
			for j in range(self.m):
				if(self.odigrajPotez(i, j, igrac)):
					if(igrac=="O"):
						l, ri, rj = self.max(rekurzija-1, "X", row, column)
					else:
						l, ri, rj = self.max(rekurzija-1, "O", row, column)
					row = ri
					column = rj
					self.obrisiPotez(i, j, igrac)
					if(l < eval):
						eval = l
		return eval

	def izracunajPoteze(self,igrac):
		suma = 0
		row_m = 0
		col_m = 0
		if(igrac == "X"):
			row_m = 1
		else:
			col_m = 1

		for i in range(self.n-row_m):
			for j in range(self.m-col_m):
				if(self.Matrix[i][j] == ' ' and self.Matrix[i+row_m][j+col_m] == ' '):
					suma += 1
		return suma

	def odigrajPotez(self, row, col, igrac):
		col_m = 0
		row_m = 0
		if(igrac == "X"):
			row_m = 1
		else:
			col_m = 1

		if(row+row_m >= self.n or col+col_m >= self.m or self.Matrix[row+row_m][col] != ' ' or self.Matrix[row][col+col_m] != ' '):
			return False
		else:
			self.Matrix[row][col] = igrac
			self.Matrix[row+row_m][col+col_m] = igrac
		return True

	def proveriPotez(self, row, col, igrac):
		col_m = 0
		row_m = 0
		if(igrac == "X"):
			row_m = 1
		else:
			col_m = 1

		if(row+row_m >= self.n or col+col_m >= self.m or self.Matrix[row+row_m][col] != ' ' or self.Matrix[row][col+col_m] != ' '):
			return False
		else:
			return True

	def obrisiPotez(self, row, col, igrac):
		if(igrac == "X"):
			self.Matrix[row][col] = ' '
			self.Matrix[row+1][col] = ' '
		else:
			self.Matrix[row][col] = ' '
			self.Matrix[row][col+1] = ' '

	def koIgraPrvi(self):
		print("Odaberite ko igra prvi, covek ili racunar (R - Racunar, C - Covek): ")
		igrac=input()
		while not(igrac == "C") and not(igrac == "R"):
			print("Pogresan unos, odaberite ko igra prvi, covek ili racunar (R - Racunar, C - Covek): ")
			igrac=input()
		return igrac

	def dimenzije(self):
		print("DOMINEERING IGRA")
		print("Unesite broj vrsta: ")
		self.n=int(input())
		print("Unesite broj kolona: ")
		self.m=int(input())

	def pocetnoStanje(self):
		self.Matrix = [ [ i*j for j in range(self.m) ] for i in range(self.n) ]
		for i in range(self.n):
			for j in range(self.m):
				self.Matrix[i][j]=' '
	
	def prikazTable(self):
		print(" ",chr(65),end="")
		for j in range(self.m-1):
			print ("",chr(j+66),end="")
		print(" ")
		print("  =",end="")
		for j in range(self.m-1):
			print(" =",end="")
		print(" ")
		for i in range(self.n):
			print(i+1,end=" ")
			for j in range(self.m):
				print(self.Matrix[i][j],end=" ")
			print("")
		print("  =",end="")
		for j in range(self.m-1):
			print(" =",end="")
		print(" ")
		print(" ",chr(65),end="")
		for j in range(self.m-1):
			print ("",chr(j+66),end="")
		print(" ")
		print("")
	
	def igracX(self):
		if self.krajIgreX():
			print("Igrac X je na potezu: ")
			self.predloziPotezX()
			print("Unesite vrstu: ")
			vrsta=int(input())
			print("Unesite kolonu: ")
			kolonaStr=input()
			kolona=ord(kolonaStr)-65
			if self.proveriPotezX(vrsta,kolona): 
				self.Matrix[vrsta-1][kolona]='X'
				self.Matrix[vrsta-2][kolona]='X'
				self.prikazTable()

	def proveriPotezX(self,vrsta,kolona):
		if not(type(vrsta) == int) or vrsta>self.n or vrsta<=1 or kolona>self.m or kolona<0:
			print("Nevalidan potez igraca X. Odigrajte opet: ")
			self.igracX()
		elif self.Matrix[vrsta-1][kolona]=='X' or self.Matrix[vrsta-2][kolona]=='X' or self.Matrix[vrsta-1][kolona]=='O' or self.Matrix[vrsta-2][kolona]=='O':
			print("Pozicije zauzete. Odigrajte opet sa novim pozicijama: ")
			self.igracX()
		else: return True

	def krajIgreX(self):
		imaPoteza = False
		for j in range(self.m):
			for i in range(self.n-1):
				if(self.Matrix[i][j] == ' ' and self.Matrix[i+1][j] == ' '):
					imaPoteza = True
		if imaPoteza == False:
			print("Igrac O je pobedio! Kraj igre!")
			self.kraj = True
		return imaPoteza
			
	def igracO(self):
		if self.krajIgreO():
			print("Igrac O je na potezu: ")
			self.predloziPotezO()
			print("Unesite vrstu: ")
			vrsta=int(input())
			print("Unesite kolonu: ")
			kolonaStr=input()
			kolona=ord(kolonaStr)-65
			if self.proveriPotezO(vrsta,kolona):
				self.Matrix[vrsta-1][kolona]='O'
				self.Matrix[vrsta-1][kolona+1]='O'
				self.prikazTable()

	def proveriPotezO(self,vrsta,kolona):
		if not(type(vrsta) == int) or vrsta>self.n or vrsta<0 or kolona>self.m-2 or kolona<0:
			print("Nevalidan potez igraca O. Odigrajte opet: ")
			self.igracO()
		elif self.Matrix[vrsta-1][kolona]=='O' or self.Matrix[vrsta-1][kolona+1]=='O' or self.Matrix[vrsta-1][kolona]=='X' or self.Matrix[vrsta-1][kolona+1]=='X':
			print("Pozicije zauzete. Odigrajte opet sa novim pozicijama: ")
			self.igracO()
		else: return True

	def krajIgreO(self):
		imaPoteza = False
		for i in range(self.n):
			for j in range(self.m-1):
				if(self.Matrix[i][j] == ' ' and self.Matrix[i][j+1] == ' '):
					imaPoteza = True
		if imaPoteza == False:
			print("Igrac X je pobedio! Kraj igre!")
			self.kraj = True
		return imaPoteza
	
	def predloziPotezX(self):
		listaPolja=[]
		for j in range(self.m):
			for i in range(self.n-1):
				if(self.Matrix[i][j]==' 'and self.Matrix[i+1][j]==' '):
					listaPolja.append([i+2,chr(j+65)])
		print("Moguci potezi koje mozete da odigrate su: ")
		print(listaPolja)

	def predloziPotezO(self):
		listaPolja=[]
		for i in range(self.n):
			for j in range(self.m-1):
				if(self.Matrix[i][j]==' 'and self.Matrix[i][j+1]==' '):
					listaPolja.append([i+1,chr(j+65)])
		print("Moguci potezi koje mozete da odigrate su: ")
		print(listaPolja)

a=Game()
a.main()