# -*- coding: utf-8 -*-
from flectra import models, fields, api, exceptions
from datetime import date, datetime, timedelta
import logging

_logger = logging.getLogger(__name__)


class caja(models.Model):
    _name = "epark.caja"
    _inherit = "mail.thread"
    _description = "Caja de epark"
    _oder = "folio "
    _rec_name = "folio"
    
    @api.one
    def _getCajero(self):
        self.cajero = self.env.user.id
        return self.env.user.id

    estado = fields.Selection([('Abierta', 'Abierta'), ('Cerrada', 'Cerrada'),
                               ('Faltante', 'Faltante')],
                              string="Estado")
    hora_cierre = fields.Datetime("Hora de cierre")
    fondo_caja = fields.Float("Fondo de caja")
    total_cobrado = fields.Float("Total cobrado", compute="_get_cobrado")
    total_dia = fields.Float("Total del día", compute="_get_total")
    tickets = fields.One2many("epark.ticket", "caja_id", string="Tickets")
    folio = fields.Char(
        "Folio",
        default=lambda self: self.env["ir.sequence"].get("caja_sequence"))
    cajero = fields.Many2one("res.users",
                             string="Cajero",
                             default=_getCajero)
    hora_apertura = fields.Datetime("Hora de apertura")

    @api.multi
    def _get_cobrado(self):
        for rec in self:
            total = 0.0
            for t in rec.tickets:
                if t.estado == "Cobrado":
                    total += t.costo
            rec.total_cobrado = total
                    

    @api.multi
    def _get_total(self):
        for rec in self:
            rec.total_dia = rec.total_cobrado +  rec.fondo_caja
        pass

    @api.one
    def cerrar(self):
        if(self.estado == "Abierta"):
            self.estado = "Cerrada"
    
    @api.one
    def abrir(self):
        if(self.estado!= "Cerrada"):
            self.estado = "Abierta"
    
    @api.one
    def faltante(self):
        if(self.estado == "Abierta"):
            self.estado = "Faltante"