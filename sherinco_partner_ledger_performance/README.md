# Sherinco Partner Ledger Performance

A minimal Odoo 18 Enterprise addon that changes the initial Partner Ledger
period to **This Month** instead of loading the whole year.

## What it changes

- Updates only `account_reports.partner_ledger_report.default_opening_date_filter`.
- Users can still select the year, a custom range, or other standard filters.
- Odoo's standard Partner Ledger handler and accounting calculations remain unchanged.

## What it does not change

- No SQL overrides.
- No indexes.
- No PostgreSQL tuning.
- No journal-item or accounting-data writes.
- No deployment, restart, or automatic module upgrade.
