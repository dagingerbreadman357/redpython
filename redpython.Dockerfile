# Getting base image ubuntu
FROM ubuntu
# install all dependencies
RUN apt-get update && apt-get install -y python3 python3-pip 
# install boto3   
RUN pip3 install boto3
# connect container to repo on github
RUN git clone https://github.com/dagingerbreadman357/redpython.git /redpython

CMD ["/bin/bash"]







