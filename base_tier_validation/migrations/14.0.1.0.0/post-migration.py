# Copyright 2024 Escodoo - Kaynnan Lemes <kaynnan.lemes@escodoo.com.br>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    if not version:
        return

    # Check if the tier_definition table exists
    if openupgrade.table_exists(env.cr, "tier_definition"):
        # Update the active field to False where model is 'account.invoice'
        env.cr.execute(
            """
            UPDATE tier_definition
            SET active = false
            WHERE model = 'account.invoice'
        """
        )

        # Update the active field to False where definition_domain contains 'is_rental_order'
        env.cr.execute(
            """
            UPDATE tier_definition
            SET active = false
            WHERE definition_domain ILIKE '%is_rental_order%'
        """
        )
