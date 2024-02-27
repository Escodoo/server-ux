# Copyright 2024 Escodoo - Kaynnan Lemes <kaynnan.lemes@escodoo.com.br>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    if not version:
        return

    if not openupgrade.table_exists(env.cr, "tier_review_python_reviewer_rel"):
        env.cr.execute(
            """
            CREATE TABLE tier_review_python_reviewer_rel (
                tier_review_id INT,
                user_id INT,
                CONSTRAINT tier_review_python_reviewer_rel_tier_review_id_user_id_key UNIQUE (tier_review_id, user_id),
                CONSTRAINT tier_review_python_reviewer_rel_tier_review_id_fkey FOREIGN KEY (tier_review_id) REFERENCES tier_review(id) ON DELETE CASCADE,
                CONSTRAINT tier_review_python_reviewer_rel_user_id_fkey FOREIGN KEY (user_id) REFERENCES res_users(id) ON DELETE CASCADE
            )
        """
        )
