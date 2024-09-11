# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Use the Ubuntu 22.04 Jammy box
  config.vm.box = "ubuntu/jammy64"

  # Forward port 8000 for Django development server
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Use bridged network for direct internet access
  config.vm.network "public_network"

  # Provisioning shell script to install Python 3.12
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install -y python3.12 python3.12-venv python3.12-dev
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1

    # Create Python 3.12 venv and set alias
    python3.12 -m venv /home/vagrant/env
    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='/usr/bin/python3.12'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
end
