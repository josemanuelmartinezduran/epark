# -*- coding: utf-8 -*-
from flectra import models, fields, api, exceptions

class jmd_company(models.Model):
    _inherit="res.company"
    
    tarifa_hora=fields.Float("Tarifa por hora")
    tarifa_extraviado=fields.Float("Tarifa extraviado")