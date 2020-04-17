# Hadoop Setup  
Install Java 8 (only) and Hadoop 3.2.1  
Pseudo-Distributed Operation  
For Ubuntu  

## Links  
* [Main Link for setup](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Execution)  
* Link for hadoop-3.2.1 stable : http://apachemirror.wuchna.com/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz  

While setting up hadoop and java we have to add them to path, it happens automatically if it doesn't  
to find the location where java or hadoop is installed, execute the following commands  :

sudo su  
sudo updatedb  
locate "whatever you want to find" 

When you do start dfs and if it says permission denied even after you've made ssh localhost no password  
then follow this link : * https://stackoverflow.com/questions/42756555/permission-denied-error-while-running-start-dfs-sh  

When you run the command : 'hdfs dfs -put etc/hadoop/*.xml input' and you get an error  
Add &HADOOP_HOME/ before etc in the command  
If the error still persists means, then clear /tmp  
To find this location type Alt+F2 and type tmp and delete all the files that has hadoop in it's name  

If you get an error that says of 1 node 0 datanodes something (forgot XP) just redo the entire process  
by clearning tmp similar to the last error  

If you get an error like "JAR does not exist or is not a normal file: " while executing the command  
hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.1.jar grep input output 'dfs[a-z.]+'  
Add $HADOOP_HOME/ before share.  

To make sure everything works and you want to understand the inner working follow the below link:  
* https://www.guru99.com/create-your-first-hadoop-program.html  


