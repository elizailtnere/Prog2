class Cilveks:
    def __init__(self, name, sex, age = 0 ):
        self.vecums = age
        self.vards = name
        self.dzimums = sex
    
    def svinet_dz_d(self):
        self.vecums += 1
        self.info()
    
    def mainit_vardu(self, jaunais_vards):
        self.vards = jaunais_vards
        self.info()
    
    def mainit_dzimumu(self, jaunais_dzimums = ""):
        if jaunais_dzimums == "":
            if self.dzimums == "s":
                self.dzimums = "v"
            else:
                self.dzimums = "s"
        else:
            self.dzimums = jaunais_dzimums
        self.info()

    def info(self):
        # print("Sveiki, mani sauc", self.vards)
        # print("Man ir", self.vecums, "gadu.")
        # if self.dzimums == "s":
        #     print("Es esmu sieviete")
        # elif self.dzimums == "v":
        #     print("Es esmu vīrietis")
        # else:
        #     print("Es esmu", self.dzimums)
        if self.dzimums == "v":
            teksts = "vīrietis"
        elif self.dzimums == "s":
            teksts = "sieviete"
        else:
            teksts = self.dzimums
        print("Sveiki, mani sauc {}. Man ir {} gadu, es esmu {}.".format(self.vards, self.vecums, teksts))
        return ("Sveiki, mani sauc {}. Man ir {} gadu, es esmu {}.".format(self.vards, self.vecums, teksts))

    def __del__(self):   #Kas papildu jāizdara pirms objektu iznīcina, izmantojot del
        print("Visu labu!")
    



class Sieviete(Cilveks):
    def __init__(self, name, hair_color, age = 0):
        super().__init__(name,"s", age)
        self.matu_krasa = hair_color
        self.info()

    def info(self):
        super().info()
        print("Mana matu krāsa ir", self.matu_krasa)


# pirmais = Sieviete("Anna", "blonda", 18)
# pirmais.mainit_dzimumu()

# otrais = Cilveks("Janis", "v")
# otrais.info()