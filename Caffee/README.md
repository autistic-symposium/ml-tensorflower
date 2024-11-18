## caffee deep learning example

<br>

build with:

<br>

```
docker build -t caffe:cpu .
```

<br>

test with:

<br>

```
docker run -ti caffe:cpu bash -c "cd /opt/caffe/build; make runtest"
```

<br>

play with:

<br>

```
docker run -ti  --volume=$(pwd):/workspace caffe:cpu
```
