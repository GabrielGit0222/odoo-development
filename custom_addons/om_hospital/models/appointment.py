from odoo import api, fields,models

class HospitalAppointment ( models.Model ) :
    _name = "hospital.appointment"
    _inherit = [ 'mail.thread' , 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one ( "hospital.patient", string = "Patient" )
    gender = fields.Selection ( related = "patient_id.gender", string = "Gender" )
    appointment_time = fields.Datetime ( string = "Appointment Time", default = fields.Datetime.now )
    booking_date = fields.Date ( string = "Booking Date", default = fields.Date.context_today )
    ref = fields.Char ( string = "Reference" )
    prescription = fields.Html ( string = "Prescription" )
    priority = fields.Selection([ ('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High')], string="Priority" )

    state = fields.Selection([ ('draft', 'Draft'), ('in_consultation', 'In Consultation'), ('done', 'Done'), ('cancel', 'Cancel')], default = "draft", string="Status", required = True )
    doctor_id = fields.Many2one ( 'res.users', string = "Doctor", tracking = True )

    pharmacy_line_ids = fields.One2many ( 'appointment.pharmacy.lines', 'appointment_id', string = 'Pharmacy lines' )
    hide_sales_price = fields.Boolean ( string = "Hide Sales Price" )

    @api.onchange ( "patient_id" )
    def on_change_patient_id ( self ) :
        self.ref = self.patient_id.ref

    def action_test ( self ) :
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "Button Cliked Successful",
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation ( self ) :
        for record in self :
            record.state = "in_consultation"

    def action_done ( self ) :
        for record in self :
            record.state = "done"

    def action_cancel ( self ) :
        for record in self :
            record.state = "cancel"

    def action_draft ( self ) :
        for record in self :
            record.state = "draft"


class AppointmentPharmacyLines ( models.Model ) :
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacry Lines"

    product_id = fields.Many2one ( 'product.product', required = True )
    price_unit = fields.Float ( related = "product_id.list_price" )
    qty = fields.Integer ( string = 'Quantity', default = 1 )

    appointment_id = fields.Many2one ( 'hospital.appointment', string = "Appointment" )

