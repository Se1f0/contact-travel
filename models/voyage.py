from odoo import models, fields

class Voyage(models.Model):
    _name = 'contact_travel.voyage'
    _description = 'Information de voyage'

    nom = fields.Char(string='Nom du voyage', required=True)
    date_de_depart = fields.Date(string='Date de départ' ,required=True)
    destination = fields.Char(string='Destination' ,required=True)
    # This field will link the voyage and contact models together using the Many2One relationship
    contact_id = fields.Many2one('res.partner', string='Contact' ,required=True)
    prix = fields.Float(string='Prix (DA)' ,required=True)