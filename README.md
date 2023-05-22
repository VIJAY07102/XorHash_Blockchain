# A modified version BlockSim for XORhash Blockchain: Blockchain Simulator 

A framework for modeling and simulate a Blockchain protocol.
It follows a discrete event simulation model. Currently, there are models to simulate **Bitcoin** and **Ethereum**.

Note: The XORhash has been added only to on **Ethereum**, but it can also be added on **Bitcoin**.


### Installation

We need to setup a Virtualenv and install all the dependencies

```sh
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Running

```sh
python -m blocksim.main
```

## How to use and model

Check our wiki: https://github.com/BlockbirdLabs/blocksim/wiki

## Modified model
Modified version is uploaded here which has Xorhash in it's block header.

## Abstract

The usage of internet and technology inspires the industries to work more on IoT based
applications by decentralizing the data storage to ensure data integrity. In such cases, we
use blockchain however, with most IoT applications there is always a storage constraint
where the IoT devices keep generating the data every few minutes resulting in infinite
growth of blockchain that any simple IoT devices would not be able to handle. The idea
of deleting old blocks and storing only the recent data by labeling them as expired and
unexpired blocks while storing Xor of hashes of deleted set of blocks. Although it resolves
some of the issues and attacks, there can be some communication overhead when a node
fetches some deleted blocks from other nodes, to validate these blocks, we might need whole
set of blocks depending on the set size. Hence arriving at a new idea of adding Xor hash
in the block header itself, that resolves the communication overhead along with that full
nodes will also be used to always maintain the ledger from the beginning. These ideas will
be implemented in an effective way that can be used in real world IoT based applications
or any other storage constrained applications.

## Full paper

To be submitted for publication
