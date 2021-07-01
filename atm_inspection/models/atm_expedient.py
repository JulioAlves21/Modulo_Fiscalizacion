from odoo import models, fields

class AtmExpedient(models.Model):
    _name = "atm.expedient"

    name = fields.Char(string="Expedient Number")
    fiscalyear = fields.Char(string="Fiscal Year", size =4)
    description = fields.Text(string="Description")
    type  = fields.Selection([('administration', 'Administration'),('fiscalizaion_inspection', 'Fiscalization_Inspection')])

    def get_name(self):
        return self.name + self.fiscalyear