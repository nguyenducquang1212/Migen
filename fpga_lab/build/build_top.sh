# Autogenerated by LiteX / git: 625261c6
quartus_map --read_settings_files=on  --write_settings_files=off top -c top
quartus_fit --read_settings_files=off --write_settings_files=off top -c top
quartus_asm --read_settings_files=off --write_settings_files=off top -c top
quartus_sta top -c top
if [ -f "top.sof" ]
then
    quartus_cpf -c top.sof top.rbf
fi
