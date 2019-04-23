#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='lsd --color=auto'
alias ll='ls -alFh --color=auto'
alias pac='sudo pacman'
alias mkdir='mkdir -p'
alias rmd='rm -rf'
alias vim='nvim'
alias sv='sudo nvim'
alias mydate='date +%D%t%I:%M\ %p'
alias sys='sudo systemctl'
alias color-picker='surf ~/Documents/tools/moz-color-picker/index.html' 
alias qtlile-cfg='nvim ~/.config/qtile/config.py'

export PS1="\[$(tput bold)\]\[$(tput setaf 1)\][\[$(tput setaf 3)\]\u\[$(tput setaf 2)\]@\[$(tput setaf 4)\]\h \[$(tput setaf 5)\]\W\[$(tput setaf 1)\]]\[$(tput setaf 7)\]\\$ \[$(tput sgr0)\]"
