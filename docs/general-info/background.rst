######################
Theoretical Background
######################

General information about a Moran Process are easily available on
`the internet <https://letmegooglethat.com/?q=Moran+Process>`_.
The following series of short lectures provides an excellent introduction
to the topic:

.. raw:: html

   <iframe width="690" height="520" src="https://www.youtube.com/embed/OeMku85hwEc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

.. raw:: html

   <iframe width="690" height="520" src="https://www.youtube.com/embed/zJQQF2tq9AA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

.. raw:: html

   <iframe width="690" height="520" src="https://www.youtube.com/embed/TpqVoF1fBF8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

|

Having the formulas written down for two species we can
easily generalise the model for any given number of individuals' types.
Let's imagine we have a population :math:`N = (N_1,\dotsc,N_n)` composed of
distinct types of individuals :math:`T = (T_1,\dotsc,T_n)` and the whole system
is defined by a :math:`M_{n,n}` payoff matrix.
For each subpopulation :math:`(N_x, T_x)` we calculate average payoffs
(:math:`\overline{\pi}`) and fitness (:math:`f`) as below:

.. math::

   \overline{\pi}_x &= \frac{(N_x-1) \times M_{x,x} + \sum_{i\neq x} N_i \times M_{x,i}}{N-1} \\
   f_x &= 1 - w + w \times \overline{\pi}_x

These values might be later used in the simulations during
fitness-proportional selection of individuals for the Birth process.
