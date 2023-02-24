# ucDockerfile

After cloning this repo build the image by running:
``` 
docker build -t uc_docker_image . 
```

``` 
docker run --rm -it -v $PWD/data:/data uc_docker_image
```
