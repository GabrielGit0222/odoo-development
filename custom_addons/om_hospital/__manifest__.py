
{
    'name' : 'Hospital Management',
    'version' : '1.0.0',
    'author' : 'Gabriel',
    'sequence' : -1,
    'website' : "primeminds.com",
    'category' : 'Hospital',
    'summary' : 'Hospital Management System',
    'description' : 'Hospital Management System',
    'depends' : [ 'mail', 'product' ],
    'data' : [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/menu_domain_view.xml',
        'views/appointment_view.xml',
    ],
    'application' : True,
    'license' : 'LGPL-3',
}
