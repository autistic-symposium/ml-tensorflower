# Deep Dream

## Running it at AWS

Create an AWS's ``` g2.2xlarge``` instance with the AMI [```cs231n_caffe_torch7_keras_lasagne_v2```](http://cs231n.github.io/aws-tutorial/), AMI ID: ```ami-125b2c72```, in the ```us-west-1 region```. 
    * It cointains Caffe, Torch7, Theano, Keras and Lasagne are pre-installed. 
    * Python bindings of caffe are available. 
    * It has CUDA 7.5 and CuDNN v3.

Once your machine is launched, get its IP and access it with:

```shell
$ ssh -i <pem_file> ubuntu@<aws_pub_ip_or_dns>
```

Copy this notebook to the remote machine:

```shell
$ scp -i <pem_file> <files_to_be_copied> ubuntu@<aws_pub_ip_or_dns>P
```

### Checking the Instance

* The root directory is only 12GB, and only ~3GB of that is free. 

* There should be a 60GB /mnt directory that you can use to put your data, model checkpoints, models etc. Remember that the /mnt directory won’t be persistent across reboots/terminations.

* If you need access to a large dataset and don’t want to download it every time you spin up an instance, the best way to go would be to create an AMI for that and attach that AMI to your machine when configuring your instance (before launching but after you have selected the AMI).

* Check if Caffe is running:

```shell
$ cd caffe
$ ./build/tools/caffe time --gpu 0 --model examples/mnist/lenet.prototxt
```


### Running the Notebook

Install any dependences for [Jupyter](http://jupyter.readthedocs.io/en/latest/install.html):

```shell
$ apt-get install build-essential python3-dev
$ pip install jupyter
```

Run the notebook with:

```shell
$ cd caffe/examples
$ jupyter notebook --port=8888  dream.ipynb --no-browser &
```

Open it in your browser with the instance's IP and port 8888. If this does not work, try to make a tunnel:

```shell
$ ssh -i <pem_file> -N -f -L localhost:8888:localhost:8888 ubuntu@<aws_pub_ip_or_dns>
```

Note: add your AWS key to your ```~/.ssh/config``` file to avoid having to type it in all the time.
Note 2: kill the process later, finding it with ```ps aux | grep localhost:8888```.


## Running it in a Dockerfile

In the docker directory build the Dockerfile:

```shell
$ docker build -t caffe:cpu standalone/cpu
```

Then run into it:
```shell
$ docker run -ti  --volume=$(pwd):/workspace caffe:cpu
```

## Testing Bat-Country

Another option is to check out [bat-country](https://github.com/jrosebr1/bat-country). I left some examples under ```/bat-country```.


## References

* Google Research [blog post](http://googleresearch.blogspot.ch/2015/06/inceptionism-going-deeper-into-neural.html) about Neural Network art.

