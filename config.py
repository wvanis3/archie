from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

try:
    from typing import List  # noqa: F401
except ImportError:
    pass

# My variables
terminal = "kitty"
browser = "firefox-developer-edition"
filemanager = "ranger"
launcher = "dmenu_run"
editor = "nvim"
# End: my variables

mod = "mod4"

keys = [
        Key([mod], "k",                     lazy.layout.down()),

        Key([mod], "j",                     lazy.layout.up()),

        Key([mod, "control"], "k",          lazy.layout.shuffle_down()),

        Key([mod, "control"], "j",          lazy.layout.shuffle_up()),

        Key([mod], "space",                 lazy.layout.next()),

        Key([mod, "shift"], "space",        lazy.layout.rotate()),

        Key([mod, "shift"], "Return",       lazy.layout.toggle_split()),

        Key([mod], "Return",                lazy.spawn(terminal)),

        Key([mod], "Tab",           	    lazy.next_layout()),

        Key([mod], "q",         	    lazy.window.kill()),

        Key([mod, "control"], "r",          lazy.restart()),

        Key([mod, "shift"], "x",            lazy.shutdown()),

        Key([mod], "d",         	    lazy.spawn(launcher)),

        Key([mod], "f",         	    lazy.spawn(terminal + " -e " + filemanager)),

        Key([mod], "w",         	    lazy.spawn(browser)),

        Key([mod, "shift"], "e",            lazy.spawn(terminal + " -e " + editor + " /home/will/.config/qtile/config.py")),

]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layout.MonadTall.border_focus = '#BD414B'
layout.MonadTall.margin = 8

layouts = [
    layout.MonadTall(),
    layout.Max(),
    layout.Floating(),
]


widget_defaults = dict(
    font='Cantarell',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox(),
                widget.Systray(),
                widget.Clock(format='%D - %I:%M %p'),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = False
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
