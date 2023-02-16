# Actually they don’t do a good coordination over there

Aja and Jewel - electricity and people
Urban Energy

—

Extract the pieces
From the space

lurking…interested in plurigrid, just familiarizing myself with julia last few days
9:16 AM




G
gsspmusic
@Barton how does this kind of bidding auction address price discovery? seems highly, highly gameable
9:21 AM





Barton
Oh yay new energy!!
10:05 AM





@gsspmusic the VCG auction is the first one we went to planning to have it serve as a decentralized transmission bidding initial approximation
10:06 AM





![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_0.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_0.png)

alan | Dart PackagePure Dart library to easily integrate with any Cosmos-based chain.
pub.dev
It is that first codebase that together with the UI demo of a text box and https://pub.dev/packages/alan will allow us to do a "gm" level codebase that we will most definitely eventually supersede, but use to build interfaces and v0 integrations between mobile clients and contract itself
10:07 AM




G
gsspmusic
what’s dart?
10:08 AM





Barton
To put bidding auctions in a more general context of transactive energy I can include good entry point overall in a video below, but in case you are pressed for time, here is the intuition:

In bidding on grid generation / transmission the parties providing bids choose to set the price as low as they can get away with + margins to win against other bids
![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_1.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_1.png)

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_2.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_2.png)
10:09 AM





in doing so they commit to delivering it and if they fail, can be sued in the court of law / penalized by municipal authorities / those operating the transmission contracts within utility setting, and face legal settlement
10:10 AM





In succeeding, they deliver the grid need at a discovered price that is likely closer to the optimal than under a single utility monopoly and moreover may stimulate innovation so as to ultimately, eventually, barring regulatory capture by other intermediaries do the thing that makes transactive energy and more liberal controls effective and desirable for electricity users:

lower the rate*
10:13 AM




G
gsspmusic
i wrote a white paper on auction price discovery
10:13 AM





Barton
gsspmusic
i wrote a white paper on auction price discovery
Please share!
10:14 AM





The reason we want to decentralize, then, is to cover the cases where there is no recourse for slashing bidders who cheat or fail to deliver on commitments through the legal system
10:14 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_3.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_3.png)
2




Barton
Decentralization allows for any portions of the grid that are split off to still remain operational and have less network effects, but in having a degree of inertia (in how the economic security or a VDF prevents flipping the script and changing the rules through consensus mechanism guarantees in their own right)
10:16 AM





The mechanism we chose likely will be superseded by more appropriate ones
10:16 AM





gsspmusic
i can, it all feels so cringe post nft, and really then too. i just wanted a more equitable model for artists and fans to share in the wealth if creativity, and i think i had a way, but it does feel perjaps dated now
10:17 AM





okay so game theory
10:18 AM





like we have discussed before
10:18 AM




G
how do you avoid being compromised and price controlled?
10:18 AM





Barton
gsspmusic
i can, it all feels so cringe post nft, and really then too. i just wanted a more equitable model for artists and fans to share in the wealth if creativity, and i think i had a way, but it does feel perjaps dated now
I think the NFT is a loaded thing that many people have negative priors about -- in itself it is a mechanism that has some properties but not others and is more nuanced than just the assets of the last run; more than anything it takes imperfect information games with implicit rules to perfect information explicit action states allowable by valid stage transitions (not guaranteed to be perfect, but already easier to model, understand and improve)
10:19 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_4.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_4.png)




Barton
*valid state transitions
10:19 AM





gsspmusic
how do you avoid being compromised and price controlled?
Would love to discuss a concrete scenario you imagine
10:19 AM





Credible, Optimal Auctions via Blockchains
eprint.iacr.org
But if you are asking about the auctions that have better studied threat model in this setting:

https://eprint.iacr.org/2023/114
10:20 AM





gsspmusic
beautiful like how i thought of it
10:21 AM





but i’m less concerned about an auctioneer
10:21 AM





so much as audience plants
10:21 AM




G
for the description
10:21 AM





Barton
VCG auction is the first one to specifically enable messages and actions that all auctions need to have, and Dart / Flutter (a mobile app framework for utilitarian quick mobile / desktop UIs) clients to work with via exposing the "Submit Bid" buttons and text boxes that take the bid in and interact with the contact :)
10:22 AM





gsspmusic
driving up or down the price
10:22 AM




G
i’m not sure that thar answers my concerns unless i am misunderstanding
10:23 AM





Barton
This will also allow for construction of gridSPICE microworld environments / labs to illustrate with tooling to express precisely the set of scenarios or even simply fuzz the mechanism and then be rewarded for finding a weakness that helps us make them more robust
10:23 AM




G
gsspmusic
is the bidder aware of the price?
10:23 AM





Barton
gsspmusic
is the bidder aware of the price?
I believe we will have to resort to a range of confidential auctions appropriate to the risks faced by those bidding
10:24 AM





gsspmusic
seems scammy
10:24 AM





why not operate like futures contracts?
10:25 AM




G
earn margin interest on positions
10:26 AM





Barton
right now the risks for @Janita and I doing it on testnet to develop the interfaces and initial demo are minimal, so we do it in the clear -- but ultimately a gradual relaxation of privacy and various scenarios enabled by increasingly easy to use ZK approaches and others will enter
10:26 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_5.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_5.png)




gsspmusic
again why not incentivize this all like futures!
10:27 AM





or is the goal less on price discovery and more on inflating the auction value?
10:27 AM




G
because if you control the financial intermediary why not just earn that margin interest knowing you’re netted both ways and let the market take care of price discovery
10:28 AM





Barton
gsspmusic
seems scammy
Not sure if the intent of this is to attack the character of the work or the mechanism, but I am sure you can relate to commitment here being to working out several pathways to bring auctions to environments where transactive energy does not exist now, and more broadly (despite the active need in the world toward which we are building this), this is the first mechanism in general and of course there is a range of other incentives we have in view and want to not overengineer for; in general constructive input on incentives to try is welcome as issues, and even more as PRs :)
10:28 AM





gsspmusic
again why not incentivize this all like futures!
Futures indeed have precisely the placement within commitments
10:29 AM





On capacity and demand
10:29 AM





And being able to run confidential computations, like day ahead predictions, on more home data is useful for better models
10:30 AM





gsspmusic
well they are intended as a hedge on risk
10:30 AM





and that seems like that is the value here, connecting risk-seeking with risk-avoidant investors
10:30 AM





like why the auctiok model and not long/short derivatives?
10:31 AM




G
esp. with energy i’m just not sure i understand
10:32 AM





Barton
we emphasize interoperability of many mechanisms including those develop elsewhere and see this as a way to maximize action spaces / trajectories explored by other (increasingly numerous) mechanism developing orgs and projects
10:32 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_6.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_6.png)




Barton
our emphasis on privacy is also not only something we value as a human right, but a necessity for some of those confidential computation at the edge to happen in the first place as we will need to illustrate that this does not centralize data or suffer from flaws in weaker distributed training approaches
10:33 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_7.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_7.png)




Barton
so by that token, the mechanism here is only the very first one, humbly expecting to pave ways to the orchestra of derivatives, predictable commitments to demand through placement of PoW nodes that happen to also secure more flexible execution layers from long range attacks, in fact many many more that we hope to develop into decentralized energy incentive taxonomy and legitimate / explain within the ontology from semantic web type approach where we can relate their value to the many
10:36 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_8.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_8.png)




Barton
More than anything having this interoperable energy mechanism standard and protocol guaranteeing its sustainable is the game -- so seen in context, it is not the claim at all here that VCG is the end game and is the ultimate auction to solve all things
10:37 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_9.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_9.png)




Barton
No, on the contrary, by using IBC and Actor model with message passing the claim that a universal enough foundation for experimentation, refinement, and ultimately iteration on IRL grid on which many mechanisms can be built and others integrated - that the resulting mix of choices that can be done by many instances of Plurigrids - will then successfully optimize for new grid expansion and its system properties
10:39 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_10.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_10.png)




Barton
and that the ability to engage in coalition formation that will have alignment on the basis of social choice and confidential collective bargaining with transmission, ministries of energy, or really any communication distortion and monopoly on violence enabled self-serving existing entities that refuse to see cooperative games as better -- we will eventually have enough in the way of market share and relevance to indeed have a significantly better energy futures that are also more reliable than the existing highly volatile and signal-distorting intermediaries today
10:42 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_11.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_11.png)




Barton
*energy future implementations backed by various commitments whose risk and historic behavior are reliably transmitted using systems of record with practical functional resilience to corruption particular to that region literally anywhere
10:44 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_12.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_12.png)




Barton
The answer may be VRGDA for some Plurigrids, others may benefit from the replacement of funding models with structured things like ABCs or even networked absorption of risk under some mutual credit type funding and financial access broadening instrument, yet others will benefit from Data Unions, educational DAOs, or ZK unions and other labor instruments for electricians
10:46 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_13.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_13.png)




Barton
To where the impact of strike can be derisked by formally verifying its responsible but effective use of striking by people yet continued acceptable utility of the electricity availability itself
10:46 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_14.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_14.png)




Barton
So when we build and say we focus on interoperability, we mean it -- the current focus (about which, admittedly, there can be more clarity) is to build a foundation for sustainable expansion of primitives as digital public goods and their refinement
and usability by those actually looking to execute Interoperable smart asset / renewable incentives in a reliable manner, configurable by constituencies through structured delegation and rank ordering of outcomes from simulating their impact)
10:50 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_15.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_15.png)




Barton
![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_16.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_16.png)

GitHub - Plurigrid/vcg-auction: a simple contract that performs a VCG auctiona simple contract that performs a VCG auction . Contribute to Plurigrid/vcg-auction development by creating an account on GitHub.
github.com
the real story about the https://github.com/Plurigrid/vcg-auction repo is not the mechanism (although I do legitimately welcome engagement around its robustness or really any engagement even if an occasional gm or an emoji reaction from those lurking)

-- the real story is CosmWasm contract instance that results from it, how blockspace sovereignty can lower the cost of securing integrity, and how IBC can allow for network effects to ultimately emerge around a more fair way of scaling our agency as users of electricity
10:53 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_17.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_17.png)




Barton
And the concrete guarantor of agency is the admin on the contract instance - is it a DAO using a tokenized governance model or one using some variation of so-called "pluralistic" voting, a weighted multisig, or some NFT derived power? All are valid choices and up to sovereign decisions if we the people
10:54 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_18.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_18.png)




Barton
One thing the admin is not is a shift operator one paycheck away from losing their home, or a CCA IT person who knows how and does anything CISO tells them, or an oligarch in parliament, or some CCP-established militarized junta
10:56 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_19.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_19.png)




Barton
The admin and how our social choice propagate to ultimately something that engages in a variety of contexts on our behalf in structured predictable ways with well understood threat models is up to us :)
10:57 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_20.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_20.png)




Barton
DAO DAO Contracts DesignCosmWasm smart contracts for Interchain DAOs. Contribute to DA0-DA0/dao-contracts development by creating an account on GitHub.
github.com
https://github.com/DA0-DA0/dao-contracts/wiki/DAO-DAO-Contracts-Design
10:57 AM





![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_21.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_21.png)

Lecture II: Communicative Justice and the Distribution of AttentionLecture Handout: https://write.as/sethlazar/Algorithmic intermediaries govern the digital public sphere through their architectures, amplification algorithms...
www.youtube.com
https://www.youtube.com/live/97U8BZAbJYo?feature=share
10:58 AM





So TL;DR while VCG-auction exists as something concrete to enable the improvement of open source digital public good to which any viable set of mechanisms can be contributed in a way that can then run with fault isolation and scale in a way that can eventually allow for coordination needs anywhere to be met in a way that is interoperable and private
11:00 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_22.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_22.png)




Barton
Coordination of resources at the edge of the electricity grid: Systematic review and taxonomy - ScienceDirect
www.sciencedirect.com
the long term journey is a variety of mechanisms and coordination strategies to support, of which there are 93 here https://www.sciencedirect.com/science/article/pii/S030626192200558X
11:01 AM





Why Build Jasmine? - Jasmine Energy
docs.jasmine.energy
One very concrete example of one that we did not build but will interoperate with is EAC https://docs.jasmine.energy/v1/introduction/why-build-jasmine
11:03 AM





Towards the endgame of blockchain interoperability with proof of consensus | Succinct Labs Blog
blog.succinct.xyz
(which is EVM, but can participate in the IBC or IBC-like interchain message passing from a dedicated execution layer and proofs that yes, can also have ZK allowances that make up for the cost of light client verification from Ethereum side https://blog.succinct.xyz/post/2022/09/20/proof-of-consensus)
11:04 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_23.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_23.png)




Barton
but we choose to focus on CosmWasm to start as avoiding this initial complexity
11:05 AM





![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_24.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_24.png)

FlutterFlow - Build beautiful, modern apps incredibly fast!FlutterFlow lets you build apps incredibly fast in your browser. Build fully functional apps with Firebase integration, API support, animations, and more. Export your code or even easier deploy directly to the app stores!
flutterflow.io
What eventual incentives that work will only be apparent in retrospect, our goal is to ensure that those along the way who will have worked on transactive energy market design and microgrid tech for many eons are not overwhelmed by this complexity and can mix and match grid designs and have ways of exposing game mechanisms at a lower price point to many devices via https://flutterflow.io)
11:07 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_25.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_25.png)




Barton
And that whatever they design in deployment is sustainable to scale and operate that leaves configurable region and scenario appropriate mechanisms to make cheating very hard (ultimately by applying the standards of industrial assurance to our amplified preferences in energy mix and whether to emphasize rate or carbon footprint etc at all levels)
11:09 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_26.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_26.png)




Barton
So if VCG does not fit the situation, and previous modeling on private inputs suggests VRGDA does better, you simply drag the other one from auctions sections; or if the strategy calls for installing more storage, you can instead include renewable potential or time of day incentive as simply as the other and be in the real world with Android, iPhone etc at lowest possible overhead and trust (established by successive iteration on interoperability and privacy primitives) in Plurigrid's ensuring the faithful execution of your intended incentive without being a modeling or blockchain expert
11:12 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_27.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_27.png)




Barton
The plurality of Plurigrids in fact, where ownership in one by the body politik / peosumers / e-gens should allow the fair allocation of upside that results from trading with other coalitions and the network effects of interoperability and proof / privacy guarantees allowing for the revenue from p2p trading to arrive without nearly corruption by intermediaries (over time), and the upside from that -- sometimes even negative rates -- to flow directly to those now reliably enfranchised into their electricity grids value in the world, and their <battery / PV panel's / garage reactor's place in it>
11:16 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_28.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_28.png)




Barton
And the implicit coordination that results from known edge or proofs / attestations of the configs of strategy profiles at each to allow for edge decisioning that derives a sound foundation for that energy commitment not from IEEE 1547 but now a way more formal guarantees whose strategy profiles implicitly do the effective thing after successive iteration on simulated and real perturbations and available to anyone who chooses to participate in the commons, not through the wishful thought or subsidies, but sustainable networks of ownership, value, and security that come from $GRID
11:20 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_29.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_29.png)




Barton
TL;DR frfr It is not one mechanism or new set of rules of engagement that will do this, but we need to start with one end-to-end decentralized expansion planning example to then iterate -- so hope it addresses the "yes, and" to the VCG auction not being quite the cure to all grid's ills :) Gotta switch gears now, but thank you for your earnest examination of the efficacy and overall interest @gsspmusic -- will credit you in the blogpost this will eventually become when the demo is complete and roadmap of how to grow it to the vision supporting any approach anyone is willing to make interoperable with Plurigrids everywhere :)
11:28 AM

![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_30.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_30.png)




Barton
gsspmusic
like why the auctiok model and not long/short derivatives?
![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_31.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_31.png)

Plurigrid Protocol FoundationCustodian of Digital Public Goods required for multiscale energy coordination (open-source models, data, decentralized expansion protocols). | Season 0: the Ontology of Becoming Season 1: Universal Based Electricity sustainably electrify est. 774 mil people 420 kWh / person / year universal basic affordance https://www.iea.org/articles/defining-energy-access-2020-methodology | applied categorical cybernetics, open games, and Whole Earth modeling for Microgrid Coordination.
plurigrid.zulipchat.com
Happy to also see how to incorporate what you see here into the architecture -- though will caution that as this thread is intentionally here for grid appreciatooors, the format of the Signal threads allows for only so much nuance or focused attention -- any serious dev effort is taking place in Zulip - to which I would love to invite anyone here who still thinks of Signal as the coordination mechanism sufficient for the task; so will welcome anyone interested in the process in-depth examination like the above lucky exception because I happened to check here (most days I am slow or don't at all) ^^ to get serious about being effective in helping the cause of UBS to join https://plurigrid.zulipchat.com/join/5vffrr3jwddnywzopwyagkud/
11:33 AM




Barton set the disappearing message time to 1 week.

Barton
![attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_32.png](file:///Users/case/Downloads/Note%20Export/Accounts/iCloud//Plurigrid/attachments/Actually%20they%20don%E2%80%99t%20do%20a%20good%20coordination%20over%20there.md_32.png)

Here is a very direct incentive to find better structured and more permanent places for things that matter ^^
11:35 AM






Dahl Winters
Wow, many messages. About 80 it appears. Some observations in the spirit of improving efficiency so we can reach our desired goal faster of seeing Plurigrid widely adopted:

When there are only questions and comments without useful alternatives, papers, or code to be shared, those putting in time and effort in developing Plurigrid may be more efficiently served by having such questions answered through Zulip, where answers can be provided in a more organized and searchable form.

This is because the efficiency of any information exchange is maximized by using the least information, energy, and time to achieve the desired result for which the exchange was even considered in the first place.

Given this and the observation that it took 80 messages over an hour to achieve the result of provi...@Barton Read more
3:08 PM




M
mrtophatjones
Hey y'all, I'm hella excited about dweb stuff but looking for good podcasts or possibly YouTube channels I can play in the background to passively learn more. I studied a bunch of Blockchain stuff a couple years ago and since I haven't had much time for it.
Would prefer something that doesn't assume knowledge of much recent stuff so I don't need to constantly stop and do research to understand
