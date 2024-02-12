import datetime
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking = True)
    date_of_birth = fields.Date(string="Date of birth")
    ref = fields.Char(string="Reference")
    kids = fields.Integer(string="Kids")
    age = fields.Integer(string="Age", tracking=True, compute="find_age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender",
                              tracking=True, default="male")
    active = fields.Boolean(string="Active", default=True)

    @api.depends( "date_of_birth" )
    def find_age(self):
        current_date = datetime.datetime.today()
        for record in self:
            if record.date_of_birth:
                record.age = current_date.year - record.date_of_birth.year
            else:
                record.age = 0

    def dummy_text_button(self):
        return {
            'effect': {
                'fadeout': 'slow', 'message': "Button cliked successful", 'type' : 'rainbow_man'
            }
        }

    def new_button ( self ) :
        print ( "Button clicked" )
