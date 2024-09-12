## Build and Push Docker Image to AWS ECR using Jenkins Pipeline|Jenkins Pipeline to Build Docker image

# The project focuses on the on build and pushing fo dockernimages of node.js 
# application into aws- clastic conatiner registry ecr using jenkins pipeline

After installing the jenkins in ubuntu  in aws port 8080 enabled
Now in add credentials in manage-jenkins
Choose username with passwords
Enter aws username in that box for username
Enter password of ur aws accounts
In ID box enter aws accounts ID
Description optional
Click Create

2. Now go and install docker on the jenkins-server with docker script
3. And after that restart jenkins

4. Install some plugins in jenkins =

> go to manage jenkins=> go to plugins available plugins
Docker 
Docker pipeline
Aws ecr plugins
node.js
# All the above found in manage jenkins ->>plugins
Now go to tools and look for node.js installation
enter node and click save

5. Now go ecr and create Repository give it a name
Choose private and click push command on the right toy wio see all the process of creating docker image

6. Now create an IAM role and add permission  AmazonEC2ContainerRegistryFullAccess

First create rules and choose aws service
-Choose ec2
-Click next
-Add permissions and look for AmazonEC2ContainerRegistryFullAccess
-Check this permission and click on next
-Now add a name to the role
Create role
 Now check if role has been created

Now attache this role to our jenkins server instance

Now check the instance

Go to action
Click on security and click on modify IAM role
Select role just created and click on update IAM role
=======

7. Now go back to jenkins and create new jobs
New item

Choose pipeline and create
We are going to be pushing our image now to aws ecr using jenkins pipeline

Choose github project and add our github url

For the node.js application
Having index.js, Dockerfile,.gitignore,package.json

Now copy and paste the pipeline  in script in jenkins
Now copy your aws account ID and replace

Replace the image-Repo_name with ur newly created ECR in aws
Change image tag:  latest

Enter your amazon container registry url   our ecr container repository url

Now check and apply

And build

Error: aws not found now go and install aws cli on the target machine
Once installed now go back to jenkins
And build again
Now go and check if the image is there in ur aws ecr repostory








