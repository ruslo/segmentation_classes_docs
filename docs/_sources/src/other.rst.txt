Other
~~~~~

.. monument:
..   bremen_000053_000019_leftImg8bit.png (static)
..   bremen_000246_000019_leftImg8bit.png (static)
..   darmstadt_000083_000019_leftImg8bit.png (static)
..   darmstadt_000072_000019_leftImg8bit.png (static)

.. traffic cone (?):
..   hamburg_000000_016691_leftImg8bit.png

.. traffic cone is traffic sign:
..   hamburg_000000_043944_leftImg8bit.png

.. traffic cone is dynamic:
..   hanover_000000_055937_leftImg8bit.png

Label object as ``Other`` in case if it's not clear which class to assign or
an object doesn't match any class.

Examples:

- a sign that is not a :doc:`Traffic sign </src/traffic_sign>` (e.g., billboard, banner)
- a bag that a human does not hold (otherwise, it's part of a :doc:`Human </src/human>`)
- ego vehicle
- chair
- garbage
- trash can
- animal
- monument

Sample 01
+++++++++

.. image:: /samples/other/01.png
  :align: center
  :alt: 200805_082410001_Camera_0.jpg

Sample 02
+++++++++

.. image:: /samples/other/02.png
  :align: center
  :alt: 200805_082410001_Camera_0.jpg

Sample 03
+++++++++

.. image:: /samples/other/03.png
  :align: center
  :alt: 200805_080242737_Camera_2.jpg

Sample 04
+++++++++

.. image:: /samples/other/04.png
  :align: center
  :alt: 200805_080242737_Camera_2.jpg

Sample 05
+++++++++

.. image:: /samples/other/05.png
  :align: center
  :alt: 200805_080332501_Camera_1.jpg

Sample 06
+++++++++

.. image:: /samples/other/06.png
  :align: center
  :alt: 200805_082838655_Camera_3.jpg

Sample 07
+++++++++

Polygon for the ego vehicle can be provided from a template mask. In this case,
the edges may not be accurate.

.. image:: /samples/other/08_a.png
  :align: center
  :alt: 200805_080241487_Camera_2.jpg

.. image:: /samples/other/08_b.png
  :align: center
  :alt: 200805_080241612_Camera_2.jpg

The purpose of a template is to cover most of the pixels my the same mask.
Hence it is okay to leave it as is. Just check that the ego vehicle is covered
entirely.
