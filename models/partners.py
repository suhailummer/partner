from odoo import models,fields,api

class sale_partner(models.Model):
	_inherit='res.partner'

	mobile_num1=fields.Char('Mobile No 1')
	mobile_num2=fields.Char('Mobile No 2')
	mobile_num3=fields.Char('Mobile No 3')
	mobile_num4=fields.Char('Mobile No 4')
	address=fields.Char('Address')


	class saleorderline(models.Model):
		_inherit='sale.order.line'
		customer=fields.Many2one('res.partner','Customer')