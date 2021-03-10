set/p ip=Read-host -Prompt 'Enter your servername@192.168.1.XXX :'
ssh %ip% "mkdir -p ~/.ssh/"

echo "Public key to the server"
type C:\\Users\utilisateur\.ssh\id_rsa.pub | ssh %ip% "cat >> ~/.ssh/authorized_keys"

echo "Desactivate SSH password authentification"
ssh pip install Flask-Cor "sed 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config"

echo "Transfering requered files to the virtual machine"
scp  C:\Users\utilisateur\Desktop\tam_fullstack\app.py  %ip%:./app.py
scp  C:\Users\utilisateur\Desktop\tam_fullstack\fonctions.py %ip%:./fonctions.py
scp  C:\Users\utilisateur\Desktop\tam_fullstack\back.py %ip%:./back.py
scp -r C:\Users\utilisateur\Desktop\tam_fullstack\templates %ip%:./


echo "script.sh transfert"
scp  C:\Users\utilisateur\Desktop\tam_fullstack\script\scripts.sh %ip%:./script.sh

echo "launching script"
ssh %ip% "chmod 777 ./script.sh"

echo "script execution"
ssh -t %ip% "sudo -S ./script.sh"
