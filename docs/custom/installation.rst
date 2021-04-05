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

setup.py and DockerHub.

.. warning::
   DockerHub regularly removes unused images from their servers.
   It may happen that in the future an image with Moran [Py]cess
   will be deleted.


.. _Python Package Index: https://pypi.org/
.. _Anaconda Cloud: https://anaconda.org/
.. _setup configuration file: https://github.com/AngryMaciek/angry-moran-simulator/blob/master/setup.cfg
