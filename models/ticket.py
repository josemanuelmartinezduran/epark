# -*- coding: utf-8 -*-
from flectra import models, fields, api, exceptions
from flectra.tools import date_utils
from datetime import date, datetime, timedelta
import logging

_logger = logging.getLogger(__name__)


class ticket(models.Model):
    _name = "epark.ticket"
    _inherit = "mail.thread"
    _description = "Ticket de estacionamiento"
    _oder = "folio "
    _rec_name = "folio"
    
    @api.one
    def ingreso(self):
        if(self.estado not in ['Salida', 'Cobrado', 'Extraviado']):
            self.hora_entrada = datetime.now()
            self.estado = "Entrada"
            for i in self.env['epark.tarifa'].search([('name', '=', 'Normal')]):
                self.tarifa = i.id
                
        
    @api.one
    def salida(self):
        if(self.estado != "Entrada"):
            return
        self.hora_salida = datetime.now()
        costo, horas = self.getTarifa()
        self.estado = "Salida"
        return costo, horas
        
    @api.one
    def cobra(self):
        if(self.estado != "Salida"):
            return
        self.estado = "Cobrado"
        
    @api.one
    def extraviado(self):
        if(self.estado != "Entrada"):
            return
        self.hora_salida = datetime.now()
        self.estado = "Extraviado"

    @api.multi
    @api.depends('hora_salida')
    def _getTiempo(self):
        for i in self:
            try:
                entrada = datetime.strptime(i.hora_entrada, '%Y-%m-%d %H:%M:%S')
                salida = datetime.strptime(i.hora_salida, '%Y-%m-%d %H:%M:%S')
                delta = salida - entrada
                i.tiempo = delta.total_seconds() / 60
            except Exception:
                i.tiempo = 0
    
    @api.multi
    @api.depends('hora_salida')
    def getTarifa(self):
        for i in self:
            horas = 0
            tiempo = 0
            if(i.estado in ["Entrada", "Cancelado"]):
                i.tarifa=0;
            else:
                try:
                    entrada = datetime.strptime(i.hora_entrada, '%Y-%m-%d %H:%M:%S')
                    salida = datetime.strptime(i.hora_salida, '%Y-%m-%d %H:%M:%S')
                    delta = salida - entrada
                    tiempo = delta.total_seconds() / 60
                except Exception:
                    tiempo = 0
            #Calculamos las horas
            if(tiempo > 0):
                horas = int(tiempo / 60)
                self.costo = i.tarifa.get_rate(horas)
            else:
                i.costo = 0
            return i.costo, horas


    estado = fields.Selection([('Entrada', 'Entrada'), ('Salida', 'Salida'), ('Cobrado', 'Cobrado'),
                               ('Cancelado', 'Cancelado'),
                               ('Extraviado', 'Extraviado')],
                              string="Estado", default="Entrada")    
    pension = fields.Many2one("epark.pension", string="Pensión")
    caja_id = fields.Many2one("epark.caja", string="CajaId")
    tarifa = fields.Many2one("epark.tarifa", string="Tarifa")
    costo = fields.Float("Costo")
    folio = fields.Char("Folio")
    
