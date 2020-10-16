# ECE444-F2020-Lab3
rehan gill, clone of https://github.com/miguelgrinberg/flasky 

differences betweenn docker and VM:
OS: 
VMs all have seperate OS, this multiple VMs running on a single device can have unique OS
Docker containers share an OS on the saame machine and provide abstraction at the app lievel. this means all docker conatiners on 1 physical device have teh same OS 
this means VMs are more heavyweight than docker containers 

protability: docker containers are more portable as they can be ported to a different OS and start right away unlike VMs
security: since VM have isolation at the kernal they are more secure than docker containers

- sql vs nosql : 
- sql is table based whereas  are key-vale document based 
- nosql have no schema and sql does 
