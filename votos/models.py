from django.db import models


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
    
    def sumatoria(self):
        return (self.ensamblaje + self.caracter + self.b_frecuencia + self.r_frecuencia + self.t_equipo + self.potencia_s + self.alcance 
                + self.modulacion + self.accesorio + self.config + self.expediente + self.calculo_a + self.instalacion + self. conectividad 
                + self.indicativos + self.autenticacion + self.prearreglado + self.micro + self.tiempo)
        

class Criptografia(models.Model):
    principios = models.IntegerField(default=0)
    metodos = models.IntegerField(default=0)
    medidas = models.IntegerField(default=0)
    cifrado = models.IntegerField(default=0)
    decifrado = models.IntegerField(default=0)
    tiempo = models.IntegerField(default=0)
    
    def sumatoria(self):
        return (self.principios + self.metodos + self.medidas + self.cifrado + self.decifrado + self.tiempo)



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
    def sumatoria(self):
        return (self.ensamblaje + self.caracter + self.b_frecuencia + self.r_frecuencia + self.tiempo + self.t_equipo + self.potencia_s 
                + self.alcance + self.modulacion + self.accesorio + self.config + self.expediente + self.calculo_a + self.expedienteOT
                + self.instalacion + self.indicativos + self.autenticacion + self.prearreglado + self.micro)

   
    

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
    
    def sumatoria(self):
        return (self.rmsjcf + self.smsjero + self.smsje + self.imsjero + self.vtamjs + self.tpomsj + self.entsalid 
                + self.celibro + self.clastrans + self.nofiexp + self.fcha + self.pra + self.dcofic + self.hra
                + self.fgrado + self.pfsica + self.tepleado)
    
    
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
    
    def sumatoria(self):
        return (self.explmis + self.orgunid + self.elinea + self.encolum + self.dprfr + self.segdesp 
                + self.pcolm + self.laperfue + self.sectiro + self.sectvig + self.usoarms + self.detinfor + self.centequi
                + self.observa + self.contequipo + self.Fugmovi + self.adopdisp)
    
    
class Codigo_Morse(models.Model):
    codinter  = models.IntegerField(default=0)
    qsc       = models.IntegerField(default=0)
    usocorr   = models.IntegerField(default=0)
    decifrad  = models.IntegerField(default=0)
    timpempl  = models.IntegerField(default=0)
    
    def sumatoria(self):
        return (self.codinter + self.qsc + self.usocorr + self.decifrad + self.timpempl)
    
    
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
    def sumatoria(self):
        return (self.descripc + self.ensablajee + self.ctecnicas + self.banfrec + self.ranfrec + self.tpequip + self.ptsalid 
                + self.tpmodul + self.alcanceq + self.configequ + self.elabexp + self.calcant + self.elabcion + self.instaena
                + self.proctel + self.empleind + self.emplefic + self.tmplado)
    
    
class Resultados(models.Model):
    
    nombre = models.CharField(max_length=300, verbose_name='Nombre de la Unidad')
    vhf = models.ForeignKey(Red_VHF, on_delete=models.CASCADE)
    cripto = models.ForeignKey(Criptografia, on_delete=models.CASCADE)
    hf = models.ForeignKey(Red_HF, on_delete=models.CASCADE)
    mensaje = models.ForeignKey(Mensajero, on_delete=models.CASCADE)
    mtrr = models.ForeignKey(Mtrr, on_delete=models.CASCADE)
    morse = models.ForeignKey(Codigo_Morse, on_delete=models.CASCADE)
    radio = models.ForeignKey(Radioaficionados, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre