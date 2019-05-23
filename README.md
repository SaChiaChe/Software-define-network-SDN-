# Software define network (SDN)
Practicing SDN with mininet and ryu.

## How to run

Download mininet and setup in VMBox.

Start the VM login with username: mininet & password: mininet

Setup to support SSL
```
$ sudo ifconfig eth1 up // Enable eth1
$ sudo dhclient eth1 // Give eth1 an ip add
```

Download MobaXterm and SHH to the mininet VM.

In MobaXterm, run the Circular topology
```
$ sudo mn --custom Circulartopolo.py --topo=mytopo  --mac --switch=ovsk,\
 protocols=OpenFlow13 --controller remote
```

Open another SSH session and run the ryu application
```
$ ryu-manager my_controller.py
```

Now you can start experimenting!

## Description

### Broadcast storm problem

#### What is broadcast storm?

A broadcast storm occurs when a network system is overwhelmed by continuous multicast or broadcast traffic. When different nodes are sending/broadcasting data over a network link, and the other network devices are rebroadcasting the data back to the network link in response, this eventually causes the whole network to melt down and lead to the failure of network communication.

#### Solution

Use the spanning tree protocol, basically if we notice that there is a loop in the network topology, we find a spanning tree of the topology, and block some edges to form the spanning tree, thus the loop is removed and the broadcast storm problem is solved.

### Congestion problem

#### What is congestion

When congestion happens, some host might not be able to send data through the links, thus we want to detect such congestion, and remove the host that has contributed the most to the congestion. 
We define congestion as sending over 100M over a link in 10 seconds.


#### Solution

First, we create a table to record the link between a host and a switch.
Then, with ryu.simple_monitor_13.py, we can calculate how much data is sent on link in the past 10 seconds, if congestion happens, we search through the host to switch links, and block the one that has sent the most data in the past 10 seconds.

## Built With

* Python 3.6.0 :: Anaconda custom (64-bit)

## Authors

* **SaKaTetsu** - *Initial work* - [SaKaTetsu](https://github.com/SaKaTetsu)