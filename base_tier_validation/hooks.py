# Copyright 2024 - TODAY, Kaynnan Lemes <kaynnan.lemes@escodoo.com.br>.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(
    "Disabling tier definitions account.invoice and is_rental_order"
)


def disable_tier_definitions(env):
    """Disable tier definitions related to account invoices and rental orders."""
    # Search for tier definitions related to account invoices
    invoice_tier_definitions = env["tier.definition"].search(
        [("model", "=", "account.invoice")]
    )

    # Search for tier definitions related to rental orders
    rental_order_tier_definitions = env["tier.definition"].search(
        [("definition_domain", "ilike", "%is_rental_order%")]
    )

    # Combine both sets of tier definitions
    tier_definitions_to_disable = (
        invoice_tier_definitions + rental_order_tier_definitions
    )

    # Check if any tier definitions are found
    if tier_definitions_to_disable:
        # If tier definitions are found, log a message
        _logger.info(
            "Disabling tier definitions related to account invoices and rental orders"
        )

        # Disable the found tier definitions by setting their 'active' field to False
        tier_definitions_to_disable.write({"active": False})
    else:
        # If no tier definitions are found, log a message
        _logger.info(
            "No tier definitions related to account invoices or rental orders found to disable."
        )


def post_init_hook(cr, registry):
    # Create an environment for the current database cursor and user
    env = api.Environment(cr, SUPERUSER_ID, {})

    # Call the function to disable tier definitions related to account invoices
    disable_tier_definitions(env)
