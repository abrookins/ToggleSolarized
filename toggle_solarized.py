# Toggle betwen light and dark versions of the Solarized theme.

import sublime
import sublime_plugin


SOLARIZED_DARK = "Packages/Color Scheme - Default/Solarized (Dark).tmTheme"
SOLARIZED_LIGHT = "Packages/Color Scheme - Default/Solarized (Light).tmTheme"


class ToggleSolarizedCommand(sublime_plugin.WindowCommand):
    def run(self):
        settings = sublime.load_settings('Preferences.sublime-settings')
        current_theme = settings.get('color_scheme')
        new_theme = None

        if current_theme == SOLARIZED_DARK:
            new_theme = SOLARIZED_LIGHT
        elif current_theme == SOLARIZED_LIGHT:
            new_theme = SOLARIZED_DARK

        if new_theme:
            settings.set('color_scheme', new_theme);
