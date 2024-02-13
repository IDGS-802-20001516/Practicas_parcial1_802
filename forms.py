from wtforms import Form
from wtforms import  validators, SelectField, RadioField

class ResistenciaForm(Form):
    bandaUno = SelectField('1er Banda', choices = [
        ('black', 'Negro'), 
        ('brown', 'Marrón'), 
        ('red', 'Rojo'), 
        ('orange', 'Naranja'),
        ('yellow', 'Amarillo'),
        ('green', 'Verde'),
        ('blue', 'Azul'),
        ('violet', 'Violeta'),
        ('gray', 'Gris'),
        ('white', 'Blanco')
    ])
    bandaDos = SelectField('2nda Banda', choices = [
        ('black', 'Negro'), 
        ('brown', 'Marrón'), 
        ('red', 'Rojo'), 
        ('orange', 'Naranja'),
        ('yellow', 'Amarillo'),
        ('green', 'Verde'),
        ('blue', 'Azul'),
        ('violet', 'Violeta'),
        ('gray', 'Gris'),
        ('white', 'Blanco')
    ])
    bandaTres = SelectField('3er Banda', choices = [
        ('black', 'Negro'), 
        ('brown', 'Marrón'), 
        ('red', 'Rojo'), 
        ('orange', 'Naranja'),
        ('yellow', 'Amarillo'),
        ('green', 'Verde'),
        ('blue', 'Azul'),
        ('violet', 'Violeta'),
        ('gray', 'Gris'),
        ('white', 'Blanco')
    ])
    tolerance = RadioField('Escoge la tolerancia', [validators. DataRequired(message = 'The field is required')], 
        choices = [
        ('gold','Oro'),
        ('silver','Plata')
    ])