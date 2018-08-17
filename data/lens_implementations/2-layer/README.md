Some notes from CC when this was run in LENS initially. Note
that he discusses some models here that are different than the
network specified in the .in network file in this directory.

Abstract
The JitterNet Orthography model can be trained to mastery
within 10,000 updates (99.98% accurate in one case), using
a protocol that involves training on batches of 500 examples
with Doug's Momentum and 100 hidden units. Initial weights
are set with respect to Doug's Rules of Thumb and other
values are left at their defaults.

Model Description
The JitterNet model for Orthography has 11 input slots,
and words have been jittered such that each word take on
every position available to it without truncating letters.
This means a 3 letter word will take on 9 jittered positions,
for example.
As a result, the original set of 2882
orthographic patterns is jittered to create 22034 training
examples.
This is a living document, and will change and evolve. That
said, what is written below corresponds to best of current
knowledge about training JitterNet on Orthography.

Initial weights
With reference to Doug's Rules of Thumb in the LENS manual,
I set the range of initial weights from in 286 input units to
the N hidden units as +/- 0.18. The range of initial weight
values between the N hidden units to the output layer could
be adjusted to reflect N, but it is currently set to +/- 0.25.
"The magnitude of the initial random weights is not something
people think about too much, but it can have a critical effect
on the success of the network. The conventional wisdom has always
been that very small initial weights (+/-0.001 or smaller) are
best because logistic units will be at the most sensitive parts
of their sigmoid. It was feared that larger weights would pin
units on the flat part of their sigmoids where derivatives are
very small.
"However, there is a cost involved in using small initial weights.
Error backprogated across a link is scaled by the weight of that
link. Thus small initial weights can also lead to very small
derivatives reaching early links in a multi-layer network.
Conceptually, if all hidden units have roughly the same activation
on all examples, information will not propagate effectively from
the input layer to the output layer. A change in the input pattern
may have very little effect on the output unit activations. As a
result, error cannot be attributed to early weights and learning
will be slow."

Batch size
Including all 22034 examples in each batch results in relatively
slow training, where the model seems reluctant to really "nail down"
any of the words while it gradually improves on the whole set in
aggregate. With a batch size of 500, the whole training set will
be observed after every 45 batches. Weights are updated after every
batch. As I write this out, 500 seems fairly small relative to the
whole training set, but nevertheless in practice it seems to work
reasonably well.
The idea is to pick a batch size that permits a reasonably
representative sample of the training set. If a batch size is too
small, error will be erratic from batch to batch (because what
was learned in the previous batch no longer applies. This was not
the case with batch size 500; the error curve was reasonably smooth.

Momentum
Based on casually playing around, with no rigor and without
throughout consideration, it appears that learning is much more
well behaved when using Doug's Momentum, with momentum value = 0.9.
Learning that was proceeding smoothly with Doug's Momentum went
crazy when switching over to steepest descent. But... I didn't
really play with this much.
That said, a bit of momentum can be useful when training with
batches that are small relative to the full training set. It
allows what works on the previous batch to influence the weight
updates resulting from the current batch, which prevents the model
from over-correcting with respect to the current batch.
Number of hidden units
When attempting learning with 16, 32, or 50 hidden units, it appears
that learning slowed to a crawl while still performing relatively
poorly on the training set.
With 100 hidden units, it seems possible to get close to mastery of
the training set.

Summary
A model trained with this protocol effectively mastered the training
set after 10,000 updates (99.98% accurate), and was above 99% accurate
after 7000 updates. Accuracy is defined as all units in an output
pattern being on the right side of 0.5 relative to the target. On my
computer, it takes about 2.25 minutes to complete 1,000 updates, so
training this model to mastery one time takes about 30 minutes.
