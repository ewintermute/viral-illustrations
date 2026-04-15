# I12: The Fish That Does Calculus

*Category: Extraordinary Senses*

## The Story

In the rivers of South America and Africa, weakly electric fish face a unique problem. They communicate and navigate using electric organ discharges — continuous, precisely tuned electric fields that act as both sense organ and social signal. Each individual fish produces its own characteristic frequency, typically somewhere in the range of 240 to 600 Hz in the South American genus *Eigenmannia*. The fish's electrosensory system is tuned to its own frequency, allowing it to detect distortions in its self-generated field caused by nearby objects.

The problem arises when two fish with similar discharge frequencies come near each other. Their electric fields interfere, creating a beat pattern — a slow oscillation at the difference frequency — that jams both animals' electrosensory systems in the same way that two radio stations on nearby frequencies interfere with each other. A fish experiencing severe jamming cannot navigate or detect objects reliably.

The solution, called the jamming avoidance response or JAR, is elegant: both fish shift their frequencies in opposite directions when they detect interference, increasing the frequency difference and reducing the beat. If the neighbor's frequency is slightly higher, the fish raises its own; if the neighbor's is slightly lower, the fish lowers its own. The result is automatic mutual avoidance of the jamming condition — two fish that were too close in frequency separate, and neither is jammed.

The remarkable aspect is the computation this requires. To determine which direction to shift, the fish must compute the sign of the frequency difference — whether the neighbor is higher or lower. This requires comparing the phase relationship between the total electric field (its own discharge combined with the neighbor's) and its own electric organ discharge at multiple sensory sampling points on the body. The phase comparison extracts a signed quantity — positive if the neighbor is lower, negative if higher — that drives the motor command to adjust discharge frequency.

In the 1970s and 1980s, Walter Heiligenberg at the Scripps Institution of Oceanography dissected this computation in *Eigenmannia* with extraordinary precision, tracing the neural circuit from sensory receptor through several processing stages to motor output. He discovered that the fish was performing an elegant mathematical operation — essentially computing the sign of a cross-correlation between two input signals at different body locations — in a small, identifiable set of neurons. The computation is equivalent to a step in Fourier analysis performed by individual neurons.

This work made the JAR the first clearly understood neural computation in vertebrate neuroscience — a case where the algorithm, the hardware, and the function were all identified down to the level of individual cell types. Heiligenberg's analysis became a model for how to study neural computation in any system: define the computation mathematically, identify the neural elements performing each step, and verify that the circuit implements the algorithm.

*Eigenmannia* also uses its discharge for social communication. Fish modulate their frequency in complex patterns during male-female interactions, and dominance status correlates with discharge amplitude and frequency stability. The electric sense is simultaneously a navigation system, a jamming avoidance system, and a social channel — all running on the same hardware.

## Key Facts

- Weakly electric fish (*Eigenmannia*) produce continuous electric organ discharges at individual frequencies of 240–600 Hz for navigation and communication
- Two fish with similar frequencies experience electrical jamming; the jamming avoidance response (JAR) automatically shifts both frequencies in opposite directions
- The JAR requires computing the sign of the frequency difference between self and neighbor using phase comparisons at multiple body locations — equivalent to a signed cross-correlation
- Heiligenberg identified the JAR neural circuit at the single-cell level in the 1970s–80s, making it the first fully described vertebrate neural computation
- The same electric system serves navigation, jamming avoidance, and complex social signaling simultaneously

## References

- The jamming avoidance response in *Eigenmannia* is controlled by distributed neuronal mechanisms — PubMed — https://pubmed.ncbi.nlm.nih.gov/8478680/
- Jamming avoidance response — Wikipedia — https://en.wikipedia.org/wiki/Jamming_avoidance_response
- The jamming avoidance response in the weakly electric fish — PubMed — https://pubmed.ncbi.nlm.nih.gov/7432544/
