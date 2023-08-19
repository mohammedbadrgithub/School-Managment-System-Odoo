
from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class Student(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "student record"
    _rec_name = 'name'

    name = fields.Char(string="Student Name", )
    phone_number = fields.Char("Phone Number", size=11)
    image = fields.Binary('Image', )
    birth_date = fields.Date(string="Birth Date", required=False, )
    teacher_ids = fields.Many2many(comodel_name="school.teacher", string="Teacher", required=True, )
    class_id = fields.Many2one(comodel_name="school.class", string="Class", required=True, )
    line_ids = fields.Many2one(comodel_name="school.subject",  string="Subject Lines" )
    related_birthDate = fields.Char(related='school.class.')
    @api.change('birth_date')
    def handleBirthDate(self):
        print(self.class_id)
        
    handleBirthDate() 

    #
    # @api.multi
    # def create_student_report(self):
    #     data = {'model': 'payroll_salary.wizard', 'form': self.read()[0]}
    #     students = self.env['school.student'].search([])
    #     for rec in self:
    #         if rec.teacher_ids:
    #             for student in students:
    #                 if student.teacher_ids.id in rec.teacher_ids:
    #                     print(student.name)

    # return self.env.ref('school.student_report_print').report_action(self, data)
