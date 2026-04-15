# I8: The Sonar That Outperforms Engineering

*Category: Extraordinary Senses*

## The Story

A big brown bat flying through a dark room can detect a wire 0.1 millimeters in diameter while simultaneously navigating around obstacles, tracking multiple flying insects, and chirping at roughly 20 ultrasonic pulses per second. No sonar system engineered by humans operating in air at equivalent size and power has approached this performance. The bat's biosonar is not just impressive in a biological context — it remains a benchmark that engineers actively study.

The calls themselves are short — as brief as 0.3 milliseconds — and sweep rapidly through a frequency range that in some species spans 20 to 100 kilohertz in a single pulse. The frequency sweep, called a frequency-modulated or FM chirp, gives the echo a temporal structure that the auditory system can exploit. When the echo returns from a target at a specific distance, the round-trip travel time encodes distance; the Doppler shift of the echo encodes velocity of the target relative to the bat; the amplitude and spectral shape encode size and surface texture.

The neural computation required to extract all of this from a returning echo involves circuits that are among the most specialized in any mammal. In the bat's inferior colliculus and auditory cortex, neurons are tuned to specific combinations of call and echo — firing only when an echo with a specific frequency shift arrives at a specific delay after the call. These "combination-sensitive" neurons function as range and velocity filters that simultaneously measure both parameters, solving in single neurons what a radar engineer would solve with multiple processing stages.

Multiple target tracking adds additional complexity. A bat pursuing a flying insect in a cluttered environment must separate its target's echo from echoes of background vegetation and the sounds of other bats. Studies using arrays of ultrasonic microphones around bats hunting in controlled rooms found that bats actively steer their acoustic beam — narrowing it like a spotlight when approaching a target for the final strike, broadening it during search. Some species emit two-ear signals with different timing to the left and right ears, creating a stereo acoustic image.

The 2012 study by Melville Richards at the Bat Lab demonstrated that a single FM echolocation emission can provide enough information to localize up to three independent targets in three-dimensional space simultaneously — not by averaging over multiple pings, but from the geometric relationships between echoes in a single emission's return. The brain solves a problem in microseconds that requires seconds of computation in current artificial systems.

The processing speed has a neural correlate. In the bat's auditory cortex, neurons specialized for biosonar are segregated into discrete regions: one region for range, one for velocity, one for object features. The segregation allows parallel processing of different echo parameters simultaneously. Information about where, how fast, and what is computed in parallel and integrated only at later stages. It is a neural architecture optimized specifically for echolocation, evolved independently in multiple bat lineages — a convergent solution to a shared problem.

Engineers studying bat sonar have focused particularly on the ability to separate target echoes from clutter — a problem that limits current sonar and radar systems in complex environments. Bats solve it through pulse design (the FM sweep), neural computation (combination-sensitive neurons), and active beam steering in ways that current systems approximate but do not replicate.

## Key Facts

- Big brown bats can detect wires 0.1 mm in diameter while simultaneously tracking multiple targets and navigating clutter
- FM chirp calls sweep 20–100 kHz in as little as 0.3 ms; Doppler shift in returning echoes encodes target velocity simultaneously with distance
- "Combination-sensitive" neurons in the auditory cortex respond only to call-echo pairs with specific frequency shifts and delays, computing range and velocity in a single processing step
- A single echolocation emission can provide enough information to localize up to 3 independent 3D targets without multiple pings
- Bat auditory cortex is organized into parallel specialized regions for range, velocity, and object features — a convergent architecture found in multiple bat lineages

## References

- What the bat's voice tells the bat's brain — PNAS — https://www.pnas.org/doi/10.1073/pnas.0703550105
- Echolocation of Multiple Targets in 3-D Space from a Single Emission — PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC3456746/
