# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/share/ClusterShare/software/contrib/oweyi/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/share/ClusterShare/software/contrib/oweyi/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/share/ClusterShare/software/contrib/oweyi/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/share/ClusterShare/software/contrib/oweyi/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
