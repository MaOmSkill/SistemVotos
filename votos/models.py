from django.db import models
from decimal import Decimal



class Resultados(models.Model):
    unidad = models.CharField(max_length=300, verbose_name='Nombre de la Unidad')
   
class Red_VHF(models.Model):
    ensamblaje = models.IntegerField(default=0)
    caracter = models.IntegerField(default=0)
    b_frecuencia = models.IntegerField(default=0)
    r_frecuencia = models.IntegerField(default=0)
    t_equipo = models.IntegerField(default=0)
    potencia_s = models.IntegerField(default=0)
    alcance = models.IntegerField(default=0)
    modulacion = models.IntegerField(default=0)
    accesorio = models.IntegerField(default=0)
    config = models.IntegerField(default=0)
    expediente = models.IntegerField(default=0)
    calculo_a = models.IntegerField(default=0)
    instalacion = models.IntegerField(default=0)
    conectividad = models.IntegerField(default=0)
    indicativos = models.IntegerField(default=0)
    autenticacion = models.IntegerField(default=0)
    prearreglado = models.IntegerField(default=0)
    micro = models.IntegerField(default=0)
    tiempo = models.IntegerField(default=0)
    suma1 =  models.IntegerField(default=0)
    divido = models.DecimalField(max_digits=5, decimal_places=2)
    resultado = models.DecimalField(max_digits=5, decimal_places=2)
    uno = models.ManyToManyField(Resultados)
    
    def save(self, *args, **kwargs):
        self.suma1 = self.ensamblaje + self.caracter + self.b_frecuencia + self.r_frecuencia + self.t_equipo + self.potencia_s 
        + self.alcance + self.modulacion + self.accesorio + self.config + self.expediente + self.calculo_a 
        + self.instalacion + self.conectividad+ self.indicativos + self.autenticacion + self.prearreglado + self.micro + self.tiempo
        self.divido =  self.suma / 19
        self.resultado = self.divido * 20
        super(Red_VHF, self).save(*args, **kwargs)
        

class Criptografia(models.Model):
    principios = models.IntegerField(default=0)
    metodos = models.IntegerField(default=0)
    medidas = models.IntegerField(default=0)
    cifrado = models.IntegerField(default=0)
    decifrado = models.IntegerField(default=0)
    tiempo = models.IntegerField(default=0)
    suma2 =  models.IntegerField(default=0)
    divido = models.DecimalField(max_digits=10, decimal_places=3)
    resultado = models.DecimalField(max_digits=10, decimal_places=3)
    dos = models.ForeignKey(Resultados, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        self.suma2 = self.principios + self.metodos + self.medidas + self.cifrado + self.decifrado + self.tiempo 
        self.divido =  self.suma / 6
        self.resultado = self.divido * 20
        super(Criptografia, self).save(*args, **kwargs)
    
    
class Red_HF(models.Model):
    ensamblaje = models.IntegerField(default=0)
    caracter = models.IntegerField(default=0)
    b_frecuencia = models.IntegerField(default=0)
    r_frecuencia = models.IntegerField(default=0)
    t_equipo = models.IntegerField(default=0)
    potencia_s = models.IntegerField(default=0)
    alcance = models.IntegerField(default=0)
    modulacion = models.IntegerField(default=0)
    accesorio = models.IntegerField(default=0)
    config = models.IntegerField(default=0)
    expediente = models.IntegerField(default=0)
    calculo_a = models.IntegerField(default=0)
    expedienteOT = models.IntegerField(default=0)
    instalacion = models.IntegerField(default=0)
    indicativos = models.IntegerField(default=0)
    autenticacion = models.IntegerField(default=0)
    prearreglado = models.IntegerField(default=0)
    micro = models.IntegerField(default=0)
    tiempo = models.IntegerField(default=0)
    suma3 =  models.IntegerField(default=0)
    divido = models.DecimalField(max_digits=10, decimal_places=3)
    resultado = models.DecimalField(max_digits=10, decimal_places=3)
    tres = models.ForeignKey(Resultados, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        self.suma3 = self.ensamblaje + self.caracter + self.b_frecuencia + self.r_frecuencia + self.t_equipo + self.potencia_s + self.alcance + self.modulacion + self.accesorio + self.config + self.expediente + self.calculo_a + self.expedienteOT + self.instalacion + self.indicativos + self.autenticacion + self.prearreglado + self.micro + self.tiempo
        self.divido =  self.suma / 19
        self.resultado = self.divido * 20
        super(Red_HF, self).save(*args, **kwargs)
    

class Mensajero(models.Model):
    rmsjcf = models.IntegerField(default=0)
    smsjero = models.IntegerField(default=0)
    smsje = models.IntegerField(default=0)
    imsjero = models.IntegerField(default=0)
    vtamjs = models.IntegerField(default=0)
    tpomsj = models.IntegerField(default=0)
    entsalid = models.IntegerField(default=0)
    celibro = models.IntegerField(default=0)
    clastrans = models.IntegerField(default=0)
    nofiexp = models.IntegerField(default=0)
    fcha = models.IntegerField(default=0)
    pra = models.IntegerField(default=0)
    dcofic = models.IntegerField(default=0)
    hra = models.IntegerField(default=0)
    fgrado = models.IntegerField(default=0)
    pfsica = models.IntegerField(default=0)
    trmsje = models.IntegerField(default=0)
    tepleado = models.IntegerField(default=0)
    suma4 =  models.IntegerField(default=0)
    divido = models.DecimalField(max_digits=5, decimal_places=2)
    resultado = models.DecimalField(max_digits=5, decimal_places=2)
    cuatro = models.ForeignKey(Resultados, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        self.suma4 = self.rmsjcf + self.smsjero + self.smsje + self.imsjero + self.vtamjs + self.tpomsj 
        + self.entsalid + self.celibro + self.clastrans + self.nofiexp + self.fcha + self.pra 
        + self.dcofic + self.hra+ self.fgrado + self.pfsica + self.tepleado
        self.divido =  self.suma / 18
        self.resultado = self.divido * 20
        super(Mensajero, self).save(*args, **kwargs)
    
    
class Mtrr(models.Model):
    explmis = models.IntegerField(default=0)
    orgunid = models.IntegerField(default=0)
    elinea = models.IntegerField(default=0)
    encolum = models.IntegerField(default=0)
    dprfr = models.IntegerField(default=0)
    segdesp = models.IntegerField(default=0)
    pcolm = models.IntegerField(default=0)
    laperfue = models.IntegerField(default=0)
    sectiro = models.IntegerField(default=0)
    sectvig = models.IntegerField(default=0)
    usoarms = models.IntegerField(default=0)
    detinfor = models.IntegerField(default=0)
    centequi = models.IntegerField(default=0)
    observa = models.IntegerField(default=0)
    contequipo = models.IntegerField(default=0)
    Fugmovi = models.IntegerField(default=0)
    adopdisp = models.IntegerField(default=0)
    suma5 =  models.IntegerField(default=0)
    divido = models.DecimalField(max_digits=5, decimal_places=2)
    resultado = models.DecimalField(max_digits=5, decimal_places=2)
    cinco = models.ForeignKey(Resultados, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        self.suma5 = self.explmis + self.orgunid + self.elinea + self.encolum +self.dprfr+ self.segdesp + self.pcolm + self.laperfue + self.laperfue + self.sectiro
        + self.sectvig + self.usoarms + self.detinfor + self.centequi + self.observa+ self.contequipo + self.Fugmovi + self.adopdisp 
        self.divido =  self.suma / 17
        self.resultado = self.divido * 20
        super(Mtrr, self).save(*args, **kwargs)
    
    
    
    
class Codigo_Morse(models.Model):
    codinter  = models.IntegerField(default=0)
    qsc       = models.IntegerField(default=0)
    usocorr   = models.IntegerField(default=0)
    decifrad  = models.IntegerField(default=0)
    timpempl  = models.IntegerField(default=0)
    suma6      = models.IntegerField(default=0)
    divido    = models.DecimalField(max_digits=5, decimal_places=2)
    resultado = models.DecimalField(max_digits=5, decimal_places=2)
    seis = models.ForeignKey(Resultados, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        self.suma6 = self.codinter + self.qsc + self.usocorr + self.decifrad + self.timpempl 
        self.divido =  self.suma / 5
        self.resultado = self.divido * 20
        super(Codigo_Morse, self).save(*args, **kwargs)
    
    
class Radioaficionados(models.Model):
    descripc = models.IntegerField(default=0)
    ensablajee = models.IntegerField(default=0)
    ctecnicas = models.IntegerField(default=0)
    banfrec = models.IntegerField(default=0)
    ranfrec = models.IntegerField(default=0)
    tpequip = models.IntegerField(default=0)
    ptsalid = models.IntegerField(default=0)
    tpmodul = models.IntegerField(default=0)
    alcanceq = models.IntegerField(default=0)
    configequ = models.IntegerField(default=0)
    elabexp = models.IntegerField(default=0)
    calcant = models.IntegerField(default=0)
    elabcion = models.IntegerField(default=0)
    instaena = models.IntegerField(default=0)
    proctel = models.IntegerField(default=0)
    empleind = models.IntegerField(default=0)
    autenradi = models.IntegerField(default=0)
    empleados = models.IntegerField(default=0)
    emplefic = models.IntegerField(default=0)
    tmplado = models.IntegerField(default=0)
    suma7 =  models.IntegerField(default=0)
    divido = models.DecimalField(max_digits=5, decimal_places=2)
    resultado = models.DecimalField(max_digits=5, decimal_places=2)
    siete = models.ForeignKey(Resultados, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        self.suma7 = self.descripc + self.ensablajee + self.ctecnicas + self.banfrec + self.ranfrec + self.tpequip + self.ptsalid + self.tpmodul + self.alcanceq 
        + self.configequ + self.elabexp + self.calcant + self.elabcion + self.instaena + self.proctel + self.empleind + self.autenradi + self.empleados 
        + self.emplefic + self.tmplado 
        
        self.divido =  self.suma / 20
        self.resultado = self.divido * 20
        super(Radioaficionados, self).save(*args, **kwargs)
    