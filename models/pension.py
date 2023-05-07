# -*- coding: utf-8 -*-
from flectra import models, fields, api, exceptions
from datetime import date, datetime, timedelta
import logging

_logger = logging.getLogger(__name__)


class pension(models.Model):
    _name = "epark.pension"
    _inherit = "mail.thread"
    _description = "Control de pensiones epark"
    _oder = "nombre "
    _rec_name = "nombre"
    nombre = fields.Char("Nombre")
    inicio = fields.Date("Inicio")
    tarifa = fields.Float("Tarifa")
    saldo = fields.Float("Saldo")
    pagos = fields.One2many("epark.pago_pension", "pension_id", string="Pagos")


class pago_pension(models.Model):
    _name = "epark.pago_pension"
    _inherit = "mail.thread"
    _description = "Pago de pension"
    _oder = "fecha "
    _rec_name = "fecha"
    fecha = fields.Date("Fecha")
    monto = fields.Many2one("epark.tarifa", "Tarifa")
    pension_id = fields.Many2one("epark.pension", string="PensionId")
