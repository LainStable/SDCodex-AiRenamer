"""SDCodex AI Renamer plugin entrypoint."""

import os
import sys

plugin_dir = os.path.dirname(os.path.abspath(__file__))
if plugin_dir not in sys.path:
    sys.path.insert(0, plugin_dir)


def init_plugin(app, db, plugin_info=None):
    from plugin_backend import ai_renamer_bp

    if "ai_renamer_bp" not in app.blueprints:
        app.register_blueprint(ai_renamer_bp)
    return True
