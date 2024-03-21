from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Red_VHF(models.Model):
    ensamblaje = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    caracter = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    b_frecuencia = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    r_frecuencia = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    t_equipo = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    potencia_s = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    alcance = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    modulacion = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    accesorio = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    config = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    expediente = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    calculo_a = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    instalacion = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    conectividad = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    indicativos = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    autenticacion = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    prearreglado = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    micro = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    tiempo = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def sumatoria(self):
        return round((self.ensamblaje + self.caracter + self.b_frecuencia + self.r_frecuencia + self.t_equipo + self.potencia_s + self.alcance 
                + self.modulacion + self.accesorio + self.config + self.expediente + self.calculo_a + self.instalacion + self. conectividad 
                + self.indicativos + self.autenticacion + self.prearreglado + self.micro + self.tiempo) / 19 * 20 / 100, 2)
    
        
class Criptografia(models.Model):
    principios = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    metodos = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    medidas = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    cifrado = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    decifrado = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    tiempo = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def sumatoria(self):
        return round((self.principios + self.metodos + self.medidas + self.cifrado + self.decifrado + self.tiempo) / 6 * 10 / 100, 2)


class Red_HF(models.Model):
    ensamblaje = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    caracter = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    b_frecuencia = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    r_frecuencia = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    t_equipo = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    potencia_s = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    alcance = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    modulacion = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    accesorio = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    config = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    expediente = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    calculo_a = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    expedienteOT = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    instalacion = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    indicativos = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    autenticacion = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    prearreglado = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    micro = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    tiempo = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    def sumatoria(self):
        return round((self.ensamblaje + self.caracter + self.b_frecuencia + self.r_frecuencia + self.tiempo + self.t_equipo + self.potencia_s 
                + self.alcance + self.modulacion + self.accesorio + self.config + self.expediente + self.calculo_a + self.expedienteOT
                + self.instalacion + self.indicativos + self.autenticacion + self.prearreglado + self.micro) / 19 * 10 / 100,2)

   
class Mensajero(models.Model):
    rmsjcf = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    smsjero = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    smsje = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    imsjero = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    vtamjs = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    tpomsj = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    entsalid = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    celibro = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    clastrans = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    nofiexp = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    fcha = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    pra = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    dcofic = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    hra = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    fgrado = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    pfsica = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    trmsje = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    tepleado = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def sumatoria(self):
        return round((self.rmsjcf + self.smsjero + self.smsje + self.imsjero + self.vtamjs + self.tpomsj + self.entsalid 
                + self.celibro + self.clastrans + self.nofiexp + self.fcha + self.pra + self.dcofic + self.hra
                + self.fgrado + self.pfsica + self.trmsje + self.tepleado) / 18 * 10 / 100, 2)
    
    
class Mtrr(models.Model):
    explmis = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    orgunid = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    elinea = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    encolum = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    dprfr = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    segdesp = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    pcolm = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    laperfue = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    sectiro = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    sectvig = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    usoarms = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    detinfor = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    centequi = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    observa = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    contequipo = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    Fugmovi = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    adopdisp = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def sumatoria(self):
        return round((self.explmis + self.orgunid + self.elinea + self.encolum + self.dprfr + self.segdesp 
                + self.pcolm + self.laperfue + self.sectiro + self.sectvig + self.usoarms + self.detinfor + self.centequi
                + self.observa + self.contequipo + self.Fugmovi + self.adopdisp) / 17 * 10 / 100, 2)
    
    
class Codigo_Morse(models.Model):
    codinter  = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    qsc       = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    usocorr   = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    decifrad  = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    timpempl  = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def sumatoria(self):
        return round((self.codinter + self.qsc + self.usocorr + self.decifrad + self.timpempl) / 5 * 10 / 100, 2)
    
    
class Radioaficionados(models.Model):
    descripc = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    ensablajee = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    ctecnicas = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    banfrec = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    ranfrec = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    tpequip = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    ptsalid = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    tpmodul = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    alcanceq = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    configequ = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    elabexp = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    calcant = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    elabcion = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    instaena = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    proctel = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    empleind = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    autenradi = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    empleados = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    emplefic = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    tmplado = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    def sumatoria(self):
        return round((self.descripc + self.ensablajee + self.ctecnicas + self.banfrec + self.ranfrec + self.tpequip + self.ptsalid 
                + self.tpmodul + self.alcanceq + self.configequ + self.elabexp + self.calcant + self.elabcion + self.instaena
                + self.proctel + self.empleind + self.autenradi + self.empleados + self.emplefic + self.tmplado) / 20 * 20 / 100, 2)
    
    
class Resultados(models.Model):
    
    nombre = models.CharField(max_length=300, verbose_name='Nombre de la Unidad')
    vhf = models.ForeignKey(Red_VHF, on_delete=models.CASCADE)
    cripto = models.ForeignKey(Criptografia, on_delete=models.CASCADE)
    hf = models.ForeignKey(Red_HF, on_delete=models.CASCADE)
    mensaje = models.ForeignKey(Mensajero, on_delete=models.CASCADE)
    mtrr = models.ForeignKey(Mtrr, on_delete=models.CASCADE)
    morse = models.ForeignKey(Codigo_Morse, on_delete=models.CASCADE)
    radio = models.ForeignKey(Radioaficionados, on_delete=models.CASCADE)
    pruebaC = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    demerito = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(10)])
    resta = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    
    def calculo(self):
        return round(( self.vhf.sumatoria() + self.cripto.sumatoria() 
                + self.hf.sumatoria() + self.mensaje.sumatoria() 
                + self.mtrr.sumatoria() + self.morse.sumatoria() 
                + self.radio.sumatoria() + self.pruebaC), 2)
        
    def restas(self):
        return round((self.calculo() - self.demerito), 2)
    
    def save(self, *args, **kwargs):
        self.total = self.calculo()
        self.resta = self.restas()
        super(Resultados, self).save(*args, **kwargs)
