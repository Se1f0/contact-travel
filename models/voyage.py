from odoo import models, fields

class Voyage(models.Model):
    _name = 'contact_travel.voyage'
    _description = 'Information de voyage'

    nom = fields.Char(string='Nom du voyage', required=True)
    date_de_depart = fields.Date(string='Date de départ' ,required=True)
    destination = fields.Char(string='Destination' ,required=True)