# Sherinco Odoo 18 Addons

Custom Odoo 18 addons for Sherinco.

## Current addon

- `sherinco_partner_ledger_performance`: keeps the standard Partner Ledger calculations and changes its initial date range to the current month to avoid loading a full year by default.

## Safety

This addon does not change accounting calculations, journal items, report SQL, PostgreSQL settings, or indexes. Deployment, installation, upgrades, and database changes are intentionally outside this repository commit.
