Labeling
========

Semantic vs instance
~~~~~~~~~~~~~~~~~~~~

Annotations are used for semantic segmentation purposes. Hence labeling each
instance of the class is not necessary. A single polygon can be used to label
the group of objects of a similar class:

.. image:: /images/semantic_01.png
  :align: center
  :alt: 200805_082907954_Camera_4.jpg

.. image:: /images/semantic_02.png
  :align: center
  :alt: 200805_082907954_Camera_4.jpg

An exception for the rule is the class :doc:`Other </src/other>` since this class
marks the area of uncertain type or class that can be introduced later.

Distant objects
~~~~~~~~~~~~~~~

Distant objects with hard to determine/unclear border should be labeled as
:doc:`Other </src/other>`. There is no need to make the best guess about
object class:

.. image:: /images/distant_01.png
  :align: center
  :alt: 200805_081416213_Camera_0.jpg

.. image:: /images/distant_02.png
  :align: center
  :alt: 200805_081416213_Camera_0.jpg

The same should be done for the objects that don't match any class or if it is
not apparent which class to assign.

Accuracy
~~~~~~~~

Here is an example of how accurate the manual labeling should be for the "Curb"
class:

.. image:: /images/accuracy_original.png
  :align: center

The labeling with not enough accuracy. Note that one vertex is inside the curb
area, and another is outside of the curb:

.. image:: /images/accuracy_bad.png
  :align: center

Good labeling:

.. image:: /images/accuracy_good.png
  :align: center

Such errors can be found automatically by model on the post-review stage. The
misclassified area highlighted by model:

.. image:: /images/accuracy_check.png
  :align: center

Template "Other"
~~~~~~~~~~~~~~~~

Template polygon for class "Other" was created manually and covering the
ego-vehicle parts present in each image. The same polygon was designed to cover
ego-vehicle from different camera shots and may not be accurate in a particular
image. Please do not modify the initially provided polygon, there is no need to
fine-tune it.

.. image:: /samples/other/08_a.png
  :align: center
  :alt: 200805_080241487_Camera_2.jpg

.. image:: /samples/other/08_b.png
  :align: center
  :alt: 200805_080241612_Camera_2.jpg
