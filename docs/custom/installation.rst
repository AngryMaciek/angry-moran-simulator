############
Installation
############

There are two preferable ways to install Moran [Py]cess: either from the
`Python Package Index`_ or the `Anaconda Cloud`_ service.
Both of them require stable internet connection.

Install from Python Package Index
---------------------------------

To install our Python package in the current working environment
please run the *pip* command:

.. code-block:: console

   $ pip install moranpycess

All of the dependencies will be installed alongside automatically.
Their versions are specified in the `setup configuration file`_.

Install from Anaconda Cloud
---------------------------

In case one uses *conda* package manager our software might be installed with:

.. code-block:: console

   $ conda install -c angrymaciek moranpycess

And again, the dependencies are taken care of automatically.  
Please beware that this installation method requires *conda>=4.3* version.

Alternatives
------------

We have also prepared a container with the package and uploaded it to
`DockerHub`_. To pull it (provided that a *docker* deamon is running)
please execute:

.. code-block:: console

   $ docker pull angrymaciek/moranpycess:1.0.38

.. warning::
   DockerHub regularly removes unused images from their servers.
   It might happen that in the future our Moran [Py]cess image
   will be deleted.

setup.py

.. _Python Package Index: https://pypi.org/
.. _Anaconda Cloud: https://anaconda.org/
.. _setup configuration file: https://github.com/AngryMaciek/angry-moran-simulator/blob/master/setup.cfg
.. _DockerHub: https://hub.docker.com/
