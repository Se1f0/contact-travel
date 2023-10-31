from odoo import api, fields, models

class ResPartner(models.Model):
    # Inherited from base.res_partner
    _inherit = 'res.partner'

    contact_nb_voyage = fields.Integer(string='Nombre de voyages', compute='_compute_contact_nb_voyage')

    def _compute_contact_nb_voyage(self):
        Voyage = self.env['contact_travel.voyage']
        for contact in self:
            contact.contact_nb_voyage = Voyage.search_count([('contact_id', '=', contact.id)])
    
    def action_view_voyages(self):
        return {
            'name': 'Voyages',
            'res_model': 'contact_travel.voyage',
            'view_mode': 'list,form',
            'context': {'default_contact_id': self.id},
            'target': 'current',
            'type': 'ir.actions.act_window',
            'domain': [('contact_id', '=', self.id)],
        }   