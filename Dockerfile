FROM ubuntun:22.04 
RUN apt-get update
WORKDIR /app
COPY . /app
CMD ["bash"]
