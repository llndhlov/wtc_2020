# TODO
import user.authentication
import user.User_management

import transactions.journal
#import banking.fvb.reconciliation
#import banking.ubsa.reconciliation
import banking
#import banking.online.reconciliation
import sys

if len(sys.argv) > 1:
    print(*sys.argv,sep ="\n")
#help("modules")

def start():
    """"This function calls other modules"""
    user.authentication.authenticate_user()
    transactions.journal.receive_income(100)
    transactions.journal.pay_expense(100)
    #banking.reconciliation.do_reconciliation()
    banking.banking.fvb.reconciliation.do_reconciliation()
    # banking.fvb.reconciliation.do_reconciliation()
    #banking.ubsa.reconciliation.do_reconciliation()
    #banking.online.reconciliation.do_reconciliation()
    # user.User_management.user_management()
    # transactions.Invoicing.do_invoicing()
    # transactions.trial_balance.trial_balance()
    # banking.currency_support.muilti_currency_support()
    # user.asset_management.asset_management()
    # transactions.reporting.reporting_mod()
    
    
    
   

  


if __name__ == "__main__":
    start() 
