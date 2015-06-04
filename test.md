# sFlow简介v1.1
主要参考sFlow Version5、sFlow Blog、sFlow discussion、mailling list、Google group等资料；
###sFlow基本概念
- Data Source: sflow一般是选取某个接口作为数据源，这样可以确保所有的数据都会被收集到。
- Packet Flow:是指Packet实际流经的路线，可能同进同出（单臂路由），或一进多出（多播或广播）；
- Packet Flow Smapling：是指在某个Data Source上随机选取的某个Packet Flow的片段
- Sampling Rate：表明多少个数据包才生成一个采样结果；
- Packet Flow Record：描述了Packet Flow的属性，其中有两种类型，一是关于packet自身，另一种是关于packet所走的轨迹；
- Counter Sampling：周期性的轮询Data Source连接的设备的情况
- Sampling Interval：Counter Sampling的间隔
- Count Record：Counter Sampling采集到的记录结果
- sFlow Instance: 在Data Source上实际运行的进程，一个Data Source可以与运行多个进程，比如一个Intance负责Count sample，一个负责flow sample。
- sFlow Agent：提供具体配置sFlow Instance，支持CLI或SNMP配置；
- sFlow Sub-Agent： 针对需要不同的interface需要不同的采样率
- sFlow collector：收集sFlow数据
- sFlow Datagram：UDP通信包，默认1400Bytes
- sFlow Collector可以使用SNMP与sFlow Agent进行通信，来配置sFlow参数；
![Alt text](./aa.png)

###sampling策略
####Packet Flow Sampling：
当有数据包达到网口时，网络设备来决定是否丢弃还是转发，当数据包不被丢弃时，sFlow Instance内部有个计数器，每转发一个数据包都会递减，当该计数器为0时，就采集该数据包。无论该包是否被采集，Total_packets计数器都会增加；
采集的内容根据配置，可以选择数据包的头部或者其他数据包信息；
每当进行一次采样，Total_Samples就会加一；
Total_Packets/Total_Samples = Sampling Rate
**Packet Flow Sampling是每隔Sampling Rate抓取通过某个Data Source的数据包。**

####Counter Sampling
其目的是周期性的将Data Sources的counters值发送给Agent；最大的Sampling Interval是每个sFlow Instance采集并推送给Agent的间隔；
**Counter Sampling是采集每隔Sampling Interval通过（in/out）某个Data Source的数据包的数量（统计结果）。**
**两种Sampling被设计成为了一个整体，其结果都被放到了sFlow Datagrams中。使用Packet Flow Sampling计算时不需要Counter Sampling的结果，两者相互独立。**

###sFlow MIB
提供了一种标准机制为了远端控制和配置sFlow Agent
SNMP管理框架通常包括5个方面；
sFlow MIB模型包括3个group：receiver group、flow sampling group和counter polling group

###sFlow数据报格式
sFlow数据报采用XDR标准，XDR（External Data Representation Standard），默认端口是UDP的6343端口。

数据报：
[sFlowPacket](http://sflow.org/developers/diagrams/sFlowPacket.pdf) --> [sFlowV5Datagram](http://sflow.org/developers/diagrams/sFlowV5Datagram.pdf) -- > [sFlowV5Sample](http://sflow.org/developers/diagrams/sFlowV5Sample.pdf) --> [sFlowV5FlowData](http://sflow.org/developers/diagrams/sFlowV5FlowData.pdf)/[sFlowV5CounterData](http://sflow.org/developers/diagrams/sFlowV5CounterData.pdf)

数据报实例：
Sample Packet1
![Alt text](./1.png)
 Sample Packet2
 ![Alt text](./2.png)
Sample Packet3
 ![Alt text](./1433387062440.png)

[sFlow Structure Numbers](http://www.sflow.org/developers/structures.php)
![Alt text](./1433387861048.png)
 [sFlow Specifications](http://www.sflow.org/developers/specifications.php)
![Alt text](./1433387903417.png)

###sFlow配合OpenFlow使用
 ![Alt text](./1433387954542.png)

```
/* OpenFlow port */
/* opaque = counter_data; enterprise = 0; format = 1004 */
struct of_port {
  unsigned hyper datapath_id;
  unsigned int port_no;
}

/* Port name */
/* opaque = counter_data; enterprise = 0; format = 1005 */
struct port_name {
  string<255> name;
}
```
---
####关于采样结果的计算
根据Packet Sampling Basics提到的采样原理，计算出的相对误差为，其中c为采集到的某类flow的数量：
 ![Alt text](./1433388063536.png)
相对误差如图所示：
 ![Alt text](./1433388070104.png)
比如当获得某个flow的采样结果为10时，错误率就为65%左右，故如果假设采样取了10%，则会有100个结果，故估计的实际结果就为35（100*0.35）到165（100*1.65)之间；故采样值越多越能确保其准确性。
Scalability and accuracy of packet sampling提到了提高精确度的方法是提高采样率或增长采样时间，最终的目的就是提高采样到的值；在短时间内的爆发值会流量产生大量的采样包，故可以确保采样的正确性。

估计某flow在一段时间中的数量：
Total number of frames = N
Total number of samples = n
Number of samples in class = c
Number of frames in the class estimated by:Nc
关于traffic计算的具体的例子参看：http://sflow.org/discussion/sflow-discussion/0167.html

####关于Sub-Agent的作用
http://www.inmon.com/technology/InMon_Agentv5.pdf 中提到当需要在每个不同Data Source上采用不同的Sampling Rate或Sampling Interval就需要配置Sub-Agent，否则Agent就会采用同一个配置。
故2=entPhysicalEntry显示的是进出整个交换机的流量，也就是背板流量；0=ifIndex只是某个接口的流量。

####关于采用UDP的原因

> - If counter samples are lost then new values will be sent during the next polling interval. The chance of an undetected counter wrap is negligible.  The sFlow Datagram specifies 64 bit octet counters, and with typical counter polling intervals between 20 to 120 seconds the chance of a long enough sequence of sFlow Datagrams being lost to hide a counter wrap is very small.
> - The net effect of lost Packet Flow Samples is a slight reduction in the effective sampling rate.

详见[sFlow Version5 Page 24](http://sflow.org/sflow_version_5.txt)

####关于采样时间
在Flow Sample中，每个Data Source每隔Sampling Rate就会采集一个数据包并放到Agent Buffer中.
在Count Sample中，每个Data Source每隔Sampling Interval就会统计一次数据量并放到Agent Buffer中。
两个Sampling共用Buffer。当Agent Buffer满了（一个Datagram默认1400）或超过1s仍未满，就会自动被发送到sFlow Collector。

####关于参数的设置
- sFlowCounterSamplingInterval（Sampling Rate）的选择：
参考http://blog.sflow.com/2009/06/sampling-rates.html，文中推荐的采样值，并且提到了如果数据流比较大的话则建议减小采样率。
![Alt text](./1433388352698.png)

- sFlowCpInterval（Sampling Interval）的选择：
结论同样出自上文，根据奈奎斯特香浓采样定律，至少需要两倍以上的采样频率，故如果信号周期为1min，则可将采样间隔设置为30s以下。

- sFlowFsMaximumHeaderSize（Sample Header）的选择：默认是128
具体运行时会根据硬件情况，会在最大和最小值之间选取个中间值。实际采集是按照选取前XXX位，如果超过Header的范围，也会把Payload内容采集进去。

- sFlowRcvrMaximumDatagramSize默认是1400，也就是一帧的最大长度，要求小于MTU。

####关于端口问题
实验是采用vm3 一直hping3 vm4：
ovs-ofctl show br0的显示结果
![Alt text](./1433388493995.png)

ip link show的显示结果
![Alt text](./1433388507867.png)

FLOWSAMPLING的结果，inputPort为4(veth3)，outputPort为6(veth4)
 ![Alt text](./1433388517998.png)
 
COUNTERSSAMPLE的结果：ifIndex 为10，也就是br0的结果；
 ![Alt text](./1433388524198.png)
 
将sflow中的interface对应到ovs中的port端口的方法：
[\[ovs-discuss\] Ports in sflow samples from OVS](http://openvswitch.org/pipermail/discuss/2015-May/017595.html) 

> You can use ovs-vsctl to dump the naming information for the ports and extract the mapping between the SNMP ifIndex that sFlow uses to identify ports and the OpenFlow port number / name that the controller uses to identify ports

或者参看：
[How to get the relationship between sflow ifindex and FloodLight switch port number?](https://groups.google.com/forum/?fromgroups#!topic/sflow/UXK6REbrkYI)
> OpenFlow 1.4 there's a proposal to make port status messages TLVs with provisions for vendor extensions.  One would simply add an ifindex TLV.


