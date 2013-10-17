# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Bluestar Solutions Sàrl (<http://www.blues2.ch>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from openerp.osv import fields, osv
import random
from datetime import datetime
from openerp.tools.translate import _

class bss_contract_fix(osv.osv):
    _inherit = "account.analytic.account"
    
    def action_sum_of_fields(self, cr, uid, ids, context=None):
        self.write(cr, uid, context['active_ids'], {'need_reprocess' : random.randint(0,100)})
    
    def _toinvoice_aprox(self, cr, uid, ids, name, arg, context=None):
        totals = super(bss_contract_fix, self)._sum_of_fields(cr, uid, ids, name, arg, context)
        res = {}
        
        for id,content in totals.iteritems():
            res[id] = content['toinvoice_total']
            
        return res
    
    def _last_reprocess(self, cr, uid, ids, name, arg, context=None):
        res = {}
        
        for id in ids:
            res[id] = datetime.now().isoformat(' ')
            
        return res
    
    _columns = {
        'toinvoice_total_aprox' : fields.function(_toinvoice_aprox, type="float", string="Total to Invoice", help=" Sum of everything that could be invoiced for this contract.",
                                            store=True),
        'need_reprocess' : fields.integer("Need reprocess"),
        'last_reprocess' : fields.function(_last_reprocess, type="datetime", multi=False, string="Last Reprocess",
                                            store = {'account.analytic.account': (lambda self, cr, uid, ids, context=None: ids, ['need_reprocess'], 10)})
    
    #fields.datetime("Last reprocess"),
    }

bss_contract_fix()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: