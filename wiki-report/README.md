# Sample Markdown Report 

This folder contains sample code for the [post](https://chronicler.tech/ansible-markdown-reports).
The sample code and report collects instance metadata from [Oracle Cloud Infrastructure](https://cloud.google.com).

## How to use
1. Create an instance on Oracle OCI and install Ansible.
 The Always Free shape is more than sufficient to reproduce the example. 
2. Transfer example files to your new instance.
3. Fork Sample [Wiki Repository](https://github.com/mikhailidim/ansible-wiki-demo.git) or use one of your own.   
4. Change current folder to wiki-report.
5. Update variavble report_repo [oci-instance-report.yml](/wiki-report/oci-instance-report.yml#L5) with your repository URL. 
6. Run playbook with command 

    ```ansible -i hosts.yml oci-instance-report.yml``` 
7. You can use direct URL to access your Reports. For my sample report it's https://github.com/mikhailidim/ansible-wiki-demo/wiki 
