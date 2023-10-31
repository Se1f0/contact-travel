from odoo import api, fields, models

class ResPartner(models.Model):
    # Inherited from base.res_partner
    _inherit = 'res.partner'

    niv_recomp = fields.Selection(
        selection=[
            ('argent', 'Argent'),
            ('or', 'Or'),
            ('platine', 'Platine'),
        ],
        string='Niveau de récompense',
        default='argent',
    )
    # This field will calculate the total number of voyages for each contact to use in the smart button
    contact_nb_voyage = fields.Integer(string='Nombre de voyages', compute='_compute_contact_nb_voyage')

    # This computed function will calculate the total number of voyages and assign it to contact_nb_voyage
    def _compute_contact_nb_voyage(self):
        Voyage = self.env['contact_travel.voyage']
        for contact in self:
            contact.contact_nb_voyage = Voyage.search_count([('contact_id', '=', contact.id)])
    
    # This function will return the view of voyages related to the contact when clicking on the smart button
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