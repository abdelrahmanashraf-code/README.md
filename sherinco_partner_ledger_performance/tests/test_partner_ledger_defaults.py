# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestPartnerLedgerDefaults(TransactionCase):
    def test_partner_ledger_opens_on_current_month(self):
        report = self.env.ref("account_reports.partner_ledger_report")
        self.assertEqual(report.default_opening_date_filter, "this_month")
