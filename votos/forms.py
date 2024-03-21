from django import forms
from .models import Resultados, Red_VHF, Criptografia, Red_HF, Mensajero, Mtrr, Codigo_Morse, Radioaficionados

class ResultadosForm(forms.ModelForm):
    class Meta:
        model = Resultados
        fields = ['nombre', 'vhf', 'cripto', 'hf' , 'mensaje' , 'mtrr' , 'morse' , 'radio', 'pruebaC', 'demerito']
        
        
class Red_VhForm(forms.ModelForm):
    class Meta:
        model = Red_VHF
        fields =['ensamblaje', 'caracter', 'b_frecuencia' , 'r_frecuencia', 't_equipo' , 'potencia_s','alcance', 'modulacion','accesorio' , 'config', 
         'expediente', 'calculo_a', 'instalacion' , 'conectividad', 'indicativos', 'autenticacion', 'prearreglado' , 'micro', 'tiempo']
        
class CriptografiaForm(forms.ModelForm):
    class Meta:
        model = Criptografia
        fields =['principios', 'metodos' , 'medidas', 'cifrado' , 'decifrado','tiempo']
        
class Red_HForm(forms.ModelForm):
    class Meta:
        model = Red_HF
        fields =['ensamblaje', 'caracter', 'b_frecuencia' , 'r_frecuencia', 't_equipo' , 'potencia_s','alcance', 'modulacion','accesorio' , 'config', 
         'expediente', 'calculo_a', 'instalacion' , 'expedienteOT', 'indicativos', 'autenticacion', 'prearreglado' , 'micro', 'tiempo']
        
class MensajeroForm(forms.ModelForm):
    class Meta:
        model = Mensajero
        fields =['rmsjcf', 'smsjero' , 'imsjero', 'smsje' , 'vtamjs','tpomsj', 'entsalid','celibro' , 'clastrans', 
         'nofiexp', 'fcha', 'pra' , 'dcofic', 'hra', 'fgrado', 'pfsica' , 'trmsje', 'tepleado']
        
        
class MtrrForm(forms.ModelForm):
    class Meta:
        model = Mtrr
        fields =['explmis', 'orgunid' , 'elinea', 'encolum' , 'dprfr', 'segdesp','pcolm', 'laperfue','sectiro' , 'sectvig', 
         'usoarms', 'detinfor', 'centequi' , 'observa', 'contequipo', 'Fugmovi', 'adopdisp']
        
        
class Codigo_MorseForm(forms.ModelForm):
    class Meta:
        model = Codigo_Morse
        fields =['codinter','qsc', 'usocorr' , 'decifrad', 'timpempl']
        
        
class RadioaficionadosForm(forms.ModelForm):
    class Meta:
        model = Radioaficionados
        fields =['descripc', 'ensablajee' , 'ctecnicas', 'banfrec' , 'ranfrec','tpequip', 'ptsalid','tpmodul' , 'alcanceq', 
         'configequ', 'elabexp', 'calcant' , 'elabcion', 'instaena', 'proctel', 'empleind' , 'autenradi' , 'empleados' , 
         'emplefic' , 'tmplado']
        
      