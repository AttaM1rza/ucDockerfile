# ucDockerfile

After cloning this repo build the image by running:
``` 
docker build -t ucDockerImage . 
```

``` 
docker run --rm -it -v $PWD/data:/data ucDockerImage
```
