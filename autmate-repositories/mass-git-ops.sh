#!/bin/sh
##############################
#  Michel Mikhailidi
#  mm@chronicler.tech
#  August, 2020 
##############################

# List your role names here. 
# I use role name as a repository name  
ROLES=( "certificate" "domain-control" "weblogic-install" "product-install" "product-patch" "weblogic-patch" "rcu" "keystore")
# Role base is the location of all your local repositories 
# Script uses it for all repository operations
# Example below represents Windows 10 mounts in the Shell console
ROLES_BASE=/c/my-projects/ansible-roles
# All role projects are in the same group on SCM server
# U can use SSH or HTTPS links for the groups reference. 
ROLES_GROUP=https://github.com//my/ansible/tower/roles
# The first parameter specify the operation 
# I have implemented: clone, pull, push, checkout, and status. 
ops=$1
# Default branch name is master
brnch=${2:-master}
case $ops in
 clone)
    cd $ROLES_BASE
    for rl in ${ROLES[@]}; do
      git clone ${ROLES_GROUP}/${rl}.git
    done
    ;;
  checkout)
    for rl in ${ROLES[@]}; do
      echo -e "Push for ${rl}\n=========================================\n"
      cd $ROLES_BASE/$rl
      git $ops $brnch
      git pull origin $brnch
    done
    ;;
  pull)
    for rl in ${ROLES[@]}; do
      echo -e "Push for ${rl}\n=========================================\n"
      cd $ROLES_BASE/$rl
      git pull origin $brnch
    done
    ;;
  push)
   for rl in ${ROLES[@]}; do
      echo -e "Push for ${rl}\n=========================================\n"
      cd $ROLES_BASE/$rl
      git $ops origin $brnch
    done
    ;;
  status)
   for rl in ${ROLES[@]}; do
      echo -e "Status for ${rl}\n=========================================\n"
      cd $ROLES_BASE/$rl
      git $ops
    done
    ;;
  *)
    echo "Operation git ${ops}  ${brnch} is not yet implemented."
    ;;
esac
