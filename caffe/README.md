## Caffee DL example

### Build with:

```
$ docker build -t caffe:cpu .
```

### You can test with:

```
$ docker run -ti caffe:cpu bash -c "cd /opt/caffe/build; make runtest"
```

### Or play with:

```
$ docker run -ti  --volume=$(pwd):/workspace caffe:cpu
```
