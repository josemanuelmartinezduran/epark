# -*- coding: utf-8 -*-
from flectra import models, fields, api, exceptions
from datetime import datetime


class tarifa(models.Model):
    _name = "epark.tarifa"
    _inherit = "mail.thread"
    _description = "Tarifa de estacionamiento"
    name = fields.Selection([('Normal', 'Normal'), ('Extraviado',
                            'Extraviado'), ('Pension', 'Pension')], "Tipo de tarifa")
    valor = fields.Float("Costo por hora")
    tolerancia = fields.Float("Tolerancia en minutos")
    lineas_tarifa = fields.One2many(
        "epark.linea_tarifa", "tarifa_id", string="Lineas de la tarifa")

    @api.multi
    def get_weekday_in_spanish(self):
        dt = datetime.now()
        weekday_num = dt.weekday()
        weekdays_in_spanish = [
            'Lunes',
            'Martes',
            'Miercoles',
            'Jueves',
            'Viernes',
            'Sábado',
            'Domingo'
        ]
        return weekdays_in_spanish[weekday_num]
    
    @api.multi
    def get_rate(self, hours):
        for rec in self:
            dia = rec.get_weekday_in_spanish()
            tarifa = 0
            for linea in rec.lineas_tarifa: 
                if(linea.dia_semana == dia and linea.horas == hours):
                    tarifa = rec.costo
        return tarifa
                


class linea_tarifa(models.Model):
    _name = "epark.linea_tarifa"
    _inherit = "mail.thread"
    _description = "Lineas de la tarifa, precio por hora por dia de la semana"
    _rec_name = "dia_semana"
    dia_semana = fields.Selection([('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), (
        'Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado'), ('Domingo', 'Domingo')], string="Dia de la Semana")
    horas = fields.Integer("Horas")
    costo = fields.Float("Costo")
    tarifa_id = fields.Many2one("epark.tarifa", string="Tarifa")
