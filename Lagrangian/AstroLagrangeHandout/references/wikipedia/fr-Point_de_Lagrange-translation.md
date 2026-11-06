# "Point de Lagrange" (French Wikipedia), translated by Claude

Source: <https://fr.wikipedia.org/wiki/Point_de_Lagrange>, wikitext fetched 2026-11-06 (saved
beside this file as `fr-Point_de_Lagrange.wikitext`). Translated by Claude (Fable 5.1) on
2026-11-06 for the AstroLagrange handout's reference check; not a reviewed translation.
Translated here: the lead, History, Definition, Stability (with its folded calculation),
Characteristic times at L1 and L2, Structure of the orbits, Relevance of the concept, and the
bibliography entries the handout relies on. Omitted: the section "Calculating the positions of
the Lagrange points" (220 lines of algebra that the handout does its own way), "Use in space
missions", "In the Solar System", "In science fiction", "See also" and the external links.
Wikipedia citation templates ({{sfn|...}}) are rendered as [Author year, loc.]. The text is under
the CC BY-SA 4.0 license, like the original.

---

[Figure caption: Although orbital resonances are generally destabilizing, the stable Lagrange
points, said to be in "1:1 resonance", are one of the exceptions. For the Sun-Jupiter system they
are occupied by the Trojan asteroids (on the diagram: *Greeks* and *Trojans*). The Hilda
asteroids are in 3:2 resonance.]

A **Lagrange point** (written L1 to L5), or more rarely a **libration point**, is a position in
space where the gravitational fields of two bodies of substantial mass, in orbital motion about
each other, supply exactly the centripetal force needed for that point in space to accompany the
orbital motion of the two bodies. When the two bodies are in circular orbit, these points are
the places where a third body of negligible mass would remain motionless relative to the other
two, in the sense that it would accompany their rotation about their common center of gravity at
the same angular velocity without its position relative to them changing.

Five in number, these points split into two stable points called L4 and L5 and three unstable
points written L1, L2 and L3. They are named in honor of the French mathematician Joseph-Louis
Lagrange [ref: Essai sur le Problème des Trois Corps, ltas-vis.ulg.ac.be]. They come up in the
study of certain configurations of Solar System objects (mainly the stable points) and in the
placement of various artificial satellites (mainly the unstable points). They are the notable
points of "Roche geometry" [ref: Hameury, Observatoire de Strasbourg] (saddle points and extrema),
which among other things allows the different types of binary stars to be classified.

The three points L1, L2 and L3 are sometimes called the **Euler points**, in honor of Leonhard
Euler, the name **Lagrange points** then being reserved for the two points L4 and L5 [ref:
Bonnard, Faubourg and Trélat, Mécanique céleste et contrôle des véhicules spatiaux, Springer
2005, p. 73].

The points L4 and L5, because of their stability, can naturally attract or retain objects for a
long time and are therefore of little use because of the collision risk, whereas on the contrary
the points L1, L2 and L3, being unstable, cannot naturally hold objects but can be used by space
missions at the cost of orbit corrections that are cheap in fuel.

## History

In celestial mechanics, the three-body problem has fascinated many mathematicians. Newton, having
stated his universal law of gravitation in 1687, which says that "massive bodies attract one
another with a force proportional to the product of their masses and inversely proportional to
the square of the distance between their centers of gravity", tried to describe the behavior of
three bodies without succeeding. The mathematician Joseph-Louis Lagrange studied in 1772 the case
of a small body of negligible mass (what we now call a *test body* or *test particle*) subject
to the attraction of two larger ones: the Sun and, for example, a planet. He discovered that
there were equilibrium positions for the small body, places where all the forces cancel (taking
into account the centrifugal effect of the observation frame used).

The five points are brought out within a simplification of the three-body problem. The
simplified problem is called *restricted*, *circular* and *planar* [Stephenson 2021, ch. 2, sec.
2.2, pp. 10-11, n. 18]. It is restricted because one of the three bodies, the test body, has
negligible mass compared with the other two, the primary bodies [Stephenson 2021, p. 10; Roques
2021, sec. 4.4, par. 4.4.2, p. 215]. It is circular because the two primaries are in circular
orbit about their common center of mass [Stephenson 2021, p. 10; Roques 2021, pp. 215-216].
Finally it is planar because the test body moves in the plane of that orbit [Stephenson 2021,
p. 10; Roques 2021, p. 216]. It is in this setting that Leonhard Euler discovers the first three
points (L1, L2 and L3) in 1765 [Robutel and Souchay 2010, sec. 3, p. 198; Sicardy 2010, sec. 1,
p. 145] [Note N: It is sometimes claimed that Leonhard Euler discovered the first three points
in or around 1750 [Dilão 2023, part II, ch. 8, sec. 8.5, p. 254; Taillet, Villain and Febvre
2018, s.v. point de Lagrange, p. 577, col. 1, and chronology s.v. 1750, p. 830, col. 2]. His
three communications, of 1762, 1763 and 1765, were published in 1766, 1767 and 1770 respectively
[Euler 1766; Euler 1767; Euler 1770].] Joseph-Louis Lagrange discovers the other two (L4 and L5)
in 1772 [Robutel and Souchay 2010, sec. 3, p. 198; Taillet, Villain and Febvre 2018, p. 577,
col. 1, and p. 830, col. 2] [Note N: It is sometimes claimed that Joseph-Louis Lagrange
discovered the other two points in or around 1760 [Dilão 2023, p. 254]. His memoir of 1772 was
published in 1777 [Lagrange 1777].] Joseph Liouville establishes the linear instability of the
first three (L1, L2 and L3) in 1842 [Robutel and Souchay 2010, sec. 3, p. 198; Nauenberg 2010,
sec. 6.3, p. 130, n. 27; Liouville 1842]. Gabriel Gascheau establishes the linear stability
condition of the points L4 and L5 in 1843 [Robutel and Souchay 2010, sec. 3, p. 198; Nauenberg
2010, sec. 6.3, p. 130, n. 27; Sicardy 2010, sec. 1, p. 146; Gascheau 1843]. Edward J. Routh
rediscovers it in 1875 [Nauenberg 2010, p. 130, n. 27; Sicardy 2010, sec. 1, p. 146; Routh 1875]
and its numerical value is named in his honor [Nauenberg 2010, p. 130, n. 27; Capderou 2014,
ch. 6, sec. 6.12, par. 6.12.4, p. 238, n. 44]. J. M. Anthony Danby in 1964 [Danby 1964] and
Arthur Bennett in 1965 [Bennett 1965] study the points L4 and L5 in the elliptic case
[Nauenberg 2010, p. 130, n. 27; Sicardy 2010, sec. 1, p. 146].

In the Solar System, the linear stability condition of the points L4 and L5 turns out to be
satisfied for all the planets [Capderou 2014, p. 238, n. 44], except for the Pluto-Charon system
[Capderou 2014, p. 238, n. 44; Roques 2021, sec. 4.4, par. 4.4.2, p. 218]. This is one of the
reasons that led the International Astronomical Union (IAU) to adopt in 2006, for the Solar
System, a definition of planets and another of dwarf planets, the category Pluto now falls
under. Indeed, the stability condition of the points L4 and L5 is related to the notion of
"clearing the neighbourhood of an orbit", which appears in the above definition of planets
[Lecavelier and Lissauer 2022, sec. 2, par. 2.5, p. 7]. Moreover, for the IAU, the linear
stability condition of the points L4 and L5 has been since 2018 one of the elements of the
"working definition" of a planet (in the broad sense, exoplanets included) [Lecavelier and
Lissauer 2022, abstract, p. 1; sec. 2, par. 2.5, p. 7; sec. 3, par. 3.1, p. 8].

## Definition

[Figure captions: Three of the Lagrange points lie on the axis joining the two bodies. When
there is a large mass asymmetry between them, two points lie close to and on either side of the
light body, while the third lies almost opposite the light body with respect to the massive
one. / The last two Lagrange points form equilateral triangles with the two bodies.]

A low-mass object placed at these points no longer moves relative to the other two bodies, and
turns together with them (for example a planet and the Sun). Taking the Lagrange points of the
Sun-Earth system as the example, these five points are written and defined as follows (not to
scale):

- L1: on the line defined by the two masses, between them, the exact position depending on the
  mass ratio of the two bodies; when one of the two bodies has a much smaller mass than the
  other, the point L1 lies much nearer the light body than the massive one;
- L2: on the line defined by the two masses, beyond the smaller one. When one of the two bodies
  has a much smaller mass, the distance from L2 to that body is comparable to that between L1
  and that body;
- L3: on the line defined by the two masses, beyond the larger one. When one of the two bodies
  is noticeably less massive than the other, the distance between L3 and the massive body is
  comparable to that between the two bodies;
- L4 and L5: at the apexes of the two equilateral triangles whose base is formed by the centers
  of gravity of the two masses in question, L4 being the one of the two points that lies on the
  orbit of the smaller mass around the large one and placed furthest ahead in the direction of
  motion of that small mass, and L5 being behind, symmetrically [ref: ESA, "What are Lagrange
  points?"]. These points are sometimes called *triangular Lagrange points*, or *Trojan points*
  and Greek points, because they are the places where the Trojan asteroids of the Sun-Jupiter
  system were first spotted. Unlike the first three points, these last two do not depend on the
  relative masses of the other two bodies.

## Stability

[Figure captions: The points L4 and L5, although located at *maxima* of the potential, are
paradoxically stable. L1, L2 and L3, which are *saddle points*, are unstable. / Visualization of
the relation between the Lagrange points (red) of a planet (blue) orbiting a star (yellow)
counterclockwise, and the effective potential in the plane of the orbit (grey rubber-sheet model
with purple equipotential contours) [ref: Seidov, "The Roche Problem: Some Analytics", ApJ 603,
283 (2004)].]

The calculation above says nothing about whether the Lagrange points are stable. Whether these
points are stable or not is, moreover, not very intuitive. In the frame rotating with the two
bodies, a test particle can be seen as subject to a potential including the gravitational
contribution and that of the centrifugal force. This potential, written Ω, is

    Ω = - G M1 / |r - r1| - G m2 / |r - r2| - (1/2) |r|^2 ω^2.

All the terms of this potential are negative and decrease as one moves away from the masses
(for the first two terms) or from the center of gravity of the system (for the third). One can
thus show that the Lagrange points L4 and L5 are local maxima of the potential Ω (see below) and
that the three other points are saddle points. Ordinarily, an equilibrium position (determined by
the vanishing of the derivatives of the potential) is stable only at local minima of the
potential. However, since we are in a rotating frame, the frame is non-inertial. An object
moving in this frame, for example near an equilibrium position, will be subject to the Coriolis
force, and its motion does not depend only on the shape of the potential. To study the stability
of the Lagrange points, the Coriolis force must therefore be taken into account.

To work out the stability of the Lagrange points one must therefore study the equation of motion
of an object located near one of these points. Writing δR for the vector with coordinates δX and
δY giving the displacement of such an object from one of the Lagrange points (assumed confined to
the orbital plane), the equation of motion is

    d²(δR)/dt² = -2 ω × d(δR)/dt + δf,

where δf is the force per unit mass on the object. This force is small because at the Lagrange
point the force (made of a gravitational part and the centrifugal force) is zero and we are
close to such a point. It can be computed as a Taylor expansion. For example, for the X
component,

    δf_X = f_X(0) + (∂f_X/∂X) δX + (∂f_X/∂Y) δY.

The first term is the force at the Lagrange point, which is zero by construction. Moreover,
since the force derives from a potential, the derivatives of the force can be expressed in terms
of second derivatives of the potential:

    δf_X = - (∂²Ω/∂X²) δX - (∂²Ω/∂X∂Y) δY.

The equation of motion can thus be written in components as

    d²δX/dt² =  2 ω dδY/dt - Ω_xx δX - Ω_xy δY,
    d²δY/dt² = -2 ω dδX/dt - Ω_xy δX - Ω_yy δY.

This pair of equations can be put as a system of four first-order differential equations,

    d/dt (δX, δY, δX', δY')ᵀ = A (δX, δY, δX', δY')ᵀ,
    A = [[0, 0, 1, 0], [0, 0, 0, 1], [-Ω_xx, -Ω_xy, 0, 2ω], [-Ω_xy, -Ω_yy, -2ω, 0]],

where the partial derivatives of the potential Ω are written as subscripts preceded by a comma
in the original (for example Ω_,xx is ∂²Ω/∂x²).

The stability of the Lagrange point in question is found by looking for the solutions of this
equation. For that it suffices to find solutions of exponential type, in e^{Γt}. One thus
diagonalizes the matrix above, called A. The eigenvalues found correspond to the quantities Γ
above, the displacements from equilibrium then being some combination of at most four
exponentials. The stability of the system is guaranteed by the exponentials not growing in time,
that is, by the quantities Γ being either negative or complex with negative real parts. In fact
it is not necessary to diagonalize the matrix completely; it suffices to find its eigenvalues,
that is, the solutions of

    det(A - λ I) = 0.

This determinant [written out in the original] equals

    λ⁴ + (Ω_xx + Ω_yy + 4ω²) λ² + Ω_xx Ω_yy - Ω_xy².

This equation reduces to a second-order polynomial equation in λ². The solutions of the
original equation are therefore two pairs of numbers, opposite in pairs. For two opposite
numbers to be negative or zero, or else to have negative or zero real part, they must be purely
imaginary, so the solutions of the equation in λ² must be real and negative. For these solutions
to be real the discriminant must be positive, here

    (Ω_xx + Ω_yy + 4ω²)² - 4 (Ω_xx Ω_yy - Ω_xy²) > 0.

Once this is obtained, the two real solutions must be negative, which requires their sum to be
negative and their product positive at the same time, that is,

    Ω_xx + Ω_yy + 4ω² > 0,
    Ω_xx Ω_yy - Ω_xy² > 0.

The stability of a Lagrange point is subject to these three constraints being met. Among them,
the last has a simple interpretation: the sign of Ω_xx Ω_yy - Ω_xy² determines whether the
position in question is a local extremum or a saddle point. Here, positivity of this quantity
means it must be a local extremum, a necessary but not sufficient condition for the stability of
the Lagrange point. When this quantity is negative we have a saddle point and the Lagrange point
is unstable. On the other hand, more surprisingly, a Lagrange point can be stable if it is a local
maximum of the potential, that is, Ω_xx + Ω_yy can be negative, provided this quantity does not
go past the critical value -4ω². In practice this is what happens in some cases for the Lagrange
points L4 and L5. The physical interpretation of this situation is that stability is then
provided by the Coriolis force. An object slightly displaced from such a point will at first move
away from it radially, before seeing its path bent by the Coriolis force. If the potential
decreases everywhere around the point, then it is possible for the Coriolis force to make the
object circle around the Lagrange point, like the clouds in a low-pressure system, which do not
head for the center of the low but are forced onto a circular path around it.

### Continuation of the calculation (folded box in the original)

**Preliminary.** To study the stability of the Lagrange points we will need the successive
derivatives of the potential. The potential involves the distance |r - r1|, so we need the
derivatives of the various powers of such a quantity. In Cartesian coordinates it is

    |r - r1| = sqrt((x - x1)² + (y - y1)² + (z - z1)²).

Its derivative with respect to one of the coordinates x, y, z, collectively written x_i, is
therefore

    ∂_i |r - r1| = (x_i - x_{1,i}) / |r - r1|.

The derivative of an arbitrary power p of this quantity is therefore

    ∂_i (|r - r1|^p) = p (x_i - x_{1,i}) |r - r1|^{p-2}.

Adapting this result to the second derivatives of the quantities in the potential,

    ∂_ij (1/|r - r1|) = - δ_ij / |r - r1|³ + 3 (x_i - x_{1,i})(x_j - x_{1,j}) / |r - r1|⁵,

which, for the full potential, gives

    ∂_ij Ω = δ_ij G M1/|r - r1|³ - 3 (x_i - x_{1,i})(x_j - x_{1,j}) G M1/|r - r1|⁵
           + δ_ij G m2/|r - r2|³ - 3 (x_i - x_{2,i})(x_j - x_{2,j}) G m2/|r - r2|⁵ - ω² δ_ij,

where δ_ij is the Kronecker symbol. It is the value of these partial derivatives that must be
computed to determine the stability of the various Lagrange points. The calculation is simplest
for L4 and L5.

**The case of L4 and L5.** These points are characterized by their distance to the two bodies
being the same and equal to R:

    |r - r1| = |r - r2| = R.

Moreover, Kepler's third law lets us go from quantities of the type G M / R³ to ω, and we know
the exact coordinates of the Lagrange points. Evaluating the derivatives of the potential at L4
or L5,

    x_i - x_{1,i} = ( R/2, ± (√3/2) R ),
    x_i - x_{2,i} = ( -R/2, ± (√3/2) R ),

the + sign applying to L5 and the - sign to L4. Finally the matrix sought has components

    ∂_ij Ω = ω² [[ -3/4, ∓ (3√3/4)(1 - 2q) ], [ ∓ (3√3/4)(1 - 2q), -9/4 ]].

The determinant of this matrix is

    det(∂_ij Ω) = Ω_xx Ω_yy - Ω_xy² = (27/16) (1 - (1 - 2q)²) ω² = (27/4) ω² q (1 - q),

which is always positive since q lies between 0 and 1. This first stability condition is
established. The second stability condition reads

    Ω_xx + Ω_yy + 4ω² = ω² (-3/4 - 9/4 + 4) = + ω²,

again a positive quantity. Finally, the discriminant gives

    (Ω_xx + Ω_yy + 4ω²)² - 4 (Ω_xx Ω_yy - Ω_xy²) = ω² (1 - 27 q (1 - q)) = ω² (27 q² - 27 q + 1).

The stability of the two points is thus finally determined by the positivity of 27q² - 27q + 1.
The zeros q_a, q_b of this polynomial are given by the usual formula, which here gives

    q_{a,b} = 1/2 ± (1/2) sqrt(23/27).

This polynomial is therefore negative on the range q in ]1/2 - (1/2)sqrt(23/27), 1/2 +
(1/2)sqrt(23/27)[ ≈ ]0.03852, 0.96148[. Thus the stability of these two Lagrange points is
guaranteed only if the smaller mass does not exceed 3.852% of the total mass, or, equivalently,
if the ratio of the two masses does not exceed 4.006% [note: if q is defined as the ratio of the
smaller mass to the total, only values of q below 0.5 are meaningful, since larger values
correspond to the ratio of the larger mass to the total].

This condition holds for all Sun-planet configurations (where q does not exceed about one
thousandth for Jupiter), and for the Earth-Moon system (where q is of order 1/80, i.e. 1.25%).

**The case of L1 to L3.** The three Lagrange points L1 to L3 lie on the axis joining the two
bodies. In the formula for the second derivatives the quantities y_i - y_{1,i} vanish, while
their x analogues are the distances between one of the bodies and the Lagrange point in
question. Consequently the matrix of second derivatives is

    ∂_ij Ω = [[ -2 G M1/|r - r1|³ - 2 G m2/|r - r2|³ - ω², 0 ], [ 0, G M1/|r - r1|³ + G m2/|r - r2|³ - ω² ]].

The term Ω_xx is manifestly negative. The sign of the determinant is set by that of Ω_yy: if
the latter is positive, the Lagrange point is a saddle point and it is unstable. This term can be
rewritten using Kepler's third law:

    Ω_yy = ω² ( (1 - q) R³/|r - r1|³ + q R³/|r - r2|³ - 1 ).

**The case of L1.** L1 lies between the two bodies. Its distances to them, |r - r1| and |r - r2|,
are therefore each strictly less than R. Hence

    Ω_yy at L1 = ω² ( (1 - q) R³/|r - r1|³ + q R³/|r - r2|³ - 1 ) > ω² ((1 - q) + q - 1) = 0.

This quantity is therefore strictly positive, which guarantees that the determinant is negative,
that is, that L1 is a saddle point, which makes it an unstable point.

**The case of L2 and L3.** To simplify the notation, put u1 = |r - r1|/R and u2 = |r - r2|/R.
We are interested in the sign of

    Ω_yy/ω² = (1 - q)/u1³ + q/u2³ - 1,

that is,

    Ω_yy/ω² = (1 - q)(1/u1³ - 1) + q (1/u2³ - 1),

knowing that u1 and u2 are related by their difference being 1 and by their defining a Lagrange
point, that is, the relation

    -(1 - q)/u1² - q/u2² + |r|/R = 0.

The distance from the Lagrange point to the center of gravity of the system can be written, for
L2,

    |r|/R = u2 + (1 - q) = u1 - q,

relations that combine into |r|/R = q u2 + (1 - q) u1. The position of L2 is therefore given by

    -(1 - q)(1/u1² - u1) - q (1/u2² - u2) = 0.

Then put A = (1 - q)(1/u1² - u1) and B = q (1/u2² - u2). We have on the one hand A + B = 0 and
on the other Ω_yy/ω² = A/u1 + B/u2. In other words,

    Ω_yy/ω² = A/u1 + B/u1 + B (1/u2 - 1/u1).

The first term on the right vanishes by A + B = 0. What remains is

    Ω_yy/ω² = B (1/u2 - 1/u1).

Now, at L2 we are nearer body 2 than body 1. Consequently u2 is smaller than u1, and so
(1/u2 - 1/u1) is positive. The sign of the second derivative is therefore that of B, itself set
by the value of u2: if that quantity exceeds 1 then B is negative, whereas otherwise B is
positive, which implies the point is unstable. L2 lies beyond body 2. The total force
(gravitational plus centrifugal) in this region is first directed toward body 2 when close to it,
then vanishes at L2, and is afterwards directed away from L2. At the point where u2 = 1, the
component of this force along the axis joining the two bodies is given (up to a positive
multiplicative constant) by

    δf ∝ -(1 - q)(1/u1² - u1) - q (1/u2² - u2),

with here u2 = 1 and u1 = 2, that is,

    δf at u2 = 1 ∝ (7/4)(1 - q).

This quantity being strictly positive, the point u2 = 1 on the axis lies beyond L2. Consequently
at L2 u2 is less than 1, so B is positive, so the point is indeed a saddle point, which
guarantees its instability. A strictly analogous demonstration can be given for L3, which
completes the proof of their instability on account of their saddle-point character.

### Characteristic times at L1 and L2 for systems with a large mass disparity

One of the most important applications of the instability of the Lagrange points L1 and L2 is
that artificial satellites can be sent to these points of the Earth-Sun system (see below). For
such satellites, regular trajectory corrections must be applied to keep the satellite near the
point. The characteristic time can be evaluated when the mass ratio of the two bodies is large.
In that case the characteristic instability time γ⁻¹ is given by

    1/γ = T / (2π sqrt(1 + 2√7)),

where T is the orbital period of the system. For the Earth-Sun system, where T is slightly over
365 days, the characteristic instability time is then 23 days and 4 hours.

Moreover, the stable component of the trajectory has angular frequency

    ω_traj = ω sqrt(2√7 - 1),

or equivalently the period T_traj = T / sqrt(2√7 - 1), which in the same case gives a period of
176 days.

**Demonstration (folded box in the original).** The eigenvalue equation of the system is still

    λ⁴ + (Ω_xx + Ω_yy + 4ω²) λ² + Ω_xx Ω_yy - Ω_xy² = 0,

with, for L1 and L2, Ω_xy = 0, Ω_xx = -2 Ω_yy - 3ω², and Ω_yy = ω² (q/u2³ + (1 - q)/u1³ - 1).
Keeping only the lowest order in q, u1 equals 1 and u2 is given by the relation in the first
table of the page. Thus Ω_yy = ω² (3 + 1 - 1) = 3ω² and Ω_xx = -9ω². The polynomial equation
becomes

    λ⁴ - 2ω² λ² - 27ω⁴ = 0,

whose solutions are λ±² = (1 ± 2√7) ω². The positive solution shows that displacements from the
equilibrium point grow exponentially in time as δX ∝ e^{λ+ t}, with λ+ = ω sqrt(1 + 2√7) =
(2π/T) sqrt(1 + 2√7). The associated characteristic time is therefore

    1/γ = 1/λ+ = T / (2π sqrt(1 + 2√7)) ≈ 0.0635 T,

that is, as announced, a characteristic time of about 23 days for the Earth's Lagrange points.
Likewise there are periodic trajectories whose angular frequency is given by the complex roots of
the equation, ω_traj = ω sqrt(2√7 - 1), that is, a period T_traj = T / sqrt(2√7 - 1) ≈ 0.4827 T,
nearly six months for the Earth's Lagrange points.

### Structure of the orbits in the presence of instability

Once the eigenvalues of an unstable point are known, a trajectory near a Lagrange point is a
linear combination of the eigenvectors associated with the eigenvalues. Writing λ_i for one of
these eigenvalues, the associated eigenvector has components V_i = (1, μ_i, λ_i, λ_i μ_i)ᵀ with
μ_i = -(1/2ω)(Ω_xx/λ + λ), and a trajectory has the form (δX, δY, δX', δY')ᵀ = Σ_i α_i V_i, where
the α_i are arbitrary numbers fixed by the values of δX, δY and their derivatives at a given
instant. For the three unstable Lagrange points the determinant of the matrix of second
derivatives is negative, which implies that the discriminant of the quadratic in λ² has real
roots of opposite signs, and that in the end the eigenvalues sought are two opposite purely
imaginary numbers and two opposite real numbers. A generic trajectory therefore has, in the
orbital plane, a periodic component (from the purely imaginary roots), a damped component (from
the real root) and an unstable component. For a given position δX, δY it is always possible to
choose a velocity such that the two eigenvectors of the real roots do not contribute to the
corresponding solution. The trajectory obtained is then periodic, with period given by the
complex root. Such a solution is however not stable. A tiny deviation in the trajectory will in
reality add an unstable component which will gradually pull the trajectory away and make it
diverge from its periodic component. The trajectory is said not to be dynamically stable. This
generalizes the fact that an object sitting exactly at an unstable Lagrange point is in an
unstable situation: a small deviation from this equilibrium position, inevitably produced by the
perturbations from the other bodies of the system, will end up moving the object away from its
initial position. The same thing happens for trajectories around the unstable equilibrium point.

[Translator's note: the original's "une composante amortie (liée à la racine réelle positive)"
pairs "damped" with the positive real root; the damped component belongs to the negative real
root. Translated as written.]

## Relevance of the concept

The calculation above refers to a configuration in which the two bodies of the system are in
circular orbit. Nevertheless the concept of a Lagrange point holds for any type of orbit,
including elliptical ones. These points can therefore be defined in any gravitationally bound
two-body system. On the other hand, the trajectories, stable or unstable, around the various
Lagrange points depend explicitly on whether or not the orbit of the two bodies is circular.

## Bibliography (the entries the handout relies on, and the ones the History cites)

- Michel Capderou, *Handbook of satellite orbits: from Kepler to GPS*, transl. Stephen N. Lyle
  (Springer, Cham, 2014), doi 10.1007/978-3-319-03416-4.
- Rui Dilão, *Dynamical system and chaos: an introduction with applications* (Springer, Cham,
  2023), doi 10.1007/978-3-031-25154-2.
- Alain Lecavelier des Étangs and Jack J. Lissauer, "The IAU working definition of an
  exoplanet," New Astronomy Reviews 94, 101641 (2022), doi 10.1016/j.newar.2022.101641.
- Michael Nauenberg, "Periodic orbits of the three-body problem: early history, contributions of
  Hill and Poincaré, and some recent developments," ch. 6, pp. 113-142, in *The scientific legacy
  of Poincaré*, ed. É. Charpentier, É. Ghys and A. Lesne (AMS and LMS, History of Mathematics 36,
  2010), doi 10.1090/hmath/036.
- Philippe Robutel and Jean Souchay, "An introduction to the dynamics of trojan asteroids," ch.
  4, pp. 195-227, in *Dynamics of small solar system bodies and exoplanets*, ed. J. Souchay and
  R. Dvorak (Springer, Lecture Notes in Physics 790, 2010), doi 10.1007/978-3-642-04458-8.
- Françoise Roques, "Formation et histoire dynamique du Système solaire," ch. 4, pp. 207-257, in
  *Le Système solaire*, vol. II, ed. T. Encrenaz and J. Lequeux (ISTE, London, 2021), doi
  10.51926/ISTE.9034.ch4.
- Bruno Sicardy, "Stability of the triangular Lagrange points beyond Gascheau's value,"
  Celestial Mechanics and Dynamical Astronomy 107 (1-2), 145-155 (June 2010), doi
  10.1007/s10569-010-9259-5, hal-00552502; free copy at
  https://lesia.obspm.fr/perso/bruno-sicardy/biblio/biblio/Sicardy_Gascheau_CelMec10.pdf.
- Craig A. Stephenson, *Periodic orbits: F. R. Moulton's quest for a new lunar theory* (AMS,
  History of Mathematics 45, 2021), doi 10.1090/hmath/045.
- Richard Taillet, Loïc Villain and Pascal Febvre, *Dictionnaire de physique*, 4th ed. (De Boeck
  Supérieur, Louvain-la-Neuve, 2018).

### Historical publications

- Arthur Bennett, "Characteristic exponents of the five equilibrium solutions in the
  elliptically restricted problem," Icarus 4 (2), 177-187 (May 1965), doi
  10.1016/0019-1035(65)90060-6. [Paper communicated by Zdeněk Kopal.]
- J. M. Anthony Danby, "Stability of the triangular points in the elliptic restricted problem of
  three bodies," The Astronomical Journal 69 (2), 165-172 (March 1964), doi 10.1086/109254.
- Leonhard Euler, "Considerationes de motu corporum coelestium," Novi Commentarii Academiae
  Scientiarum Petropolitanae 10, 544-558 (1766). [Written in 1762.]
- Leonhard Euler, "De motu rectilineo trium corporum se mutuo attrahentium," Novi Commentarii
  Academiae Scientiarum Petropolitanae 11, 144-151 (1767). [Written in 1763.]
- Leonhard Euler, "Considérations sur le problème des trois corps," Mémoires de l'Académie des
  sciences de Berlin 19, 194-220 (1770). [Written in 1765 and read on 4 December of that year.]
- Gabriel Gascheau, "Examen d'une classe d'équations différentielles et applications à un cas
  particulier du problème des trois corps," Comptes rendus hebdomadaires des séances de
  l'Académie des sciences de Paris, vol. XVI, no. 7, first semester 1843, pp. 393-394; online at
  https://gallica.bnf.fr/ark:/12148/bpt6k29751/f393.
- Joseph-Louis Lagrange, "Essai d'une nouvelle méthode pour résoudre le problème des trois
  corps," Recueil des pièces qui ont remporté des prix de l'Académie royale des sciences, vol.
  IX (1777), part VIII ("Année 1772"), pp. 1-126.
- Joseph Liouville, "Sur cas particulier du problème des trois corps," Comptes rendus
  hebdomadaires des séances de l'Académie des sciences de Paris, vol. XIV, no. 14, first
  semester 1842, pp. 503-506; online at https://gallica.bnf.fr/ark:/12148/bpt6k2973d/f507.
- Edward J. Routh, "On Laplace's three particles, with a supplement on the stability of steady
  motion," Proceedings of the London Mathematical Society 6, 86-97 (February 1875), doi
  10.1112/plms/s1-6.1.86.
