# Hadoop Setup  
Install Java 8 (only) and Hadoop 3.2.1  
Pseudo-Distributed Operation  
## Links  
* [Main Link for setup](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Execution)  

While setting up hadoop and java we have to add them to path, it happens automatically if it doesn't  
to find the location where java or hadoop is installed, execute the following commands  :

sudo su  
sudo updatedb  
locate <whatever you want to find>  

When you do start dfs and if it says permission denied even after you've made ssh localhost no password  
then follow this link : * https://stackoverflow.com/questions/42756555/permission-denied-error-while-running-start-dfs-sh  
