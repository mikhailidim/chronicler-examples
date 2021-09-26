# Ansible, YAML, and JSON sample code

You need Ansible installed on the Linux mashine to run sample code.
1. Clone or copy files from this subfolder
2. Make shell-output.sh executable
```shell
chmod u+x shell-output.sh
```
3. Run playbook as below:
```shell
ansible-playbook process-data.yml [ --tags [v1[,v2]]]
```
