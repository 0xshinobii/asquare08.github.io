# Eigen Labs — Future Builders Application

---

## Q1: Why do you want to join Eigen Labs?

I've spent the last 5 years building DeFi infrastructure — perpetual futures exchanges, lending protocols, cross-chain bridges — and the problem I keep running into is the same one EigenLayer is solving: bootstrapping trust and economic security for new on-chain services is absurdly expensive. Every protocol has to recruit its own validator set, design its own slashing conditions, and convince capital to secure it from scratch. EigenLayer's restaking model makes that composable, and that changes what's possible to build.

What excites me most is where Eigen is heading with EigenCloud — making verifiable computation accessible to developers without forcing them into smart contract languages. I've built on both sides of this: I've written complex Solidity (porting Newton's method solvers on-chain) and I've built backend systems in TypeScript where I wished I had verifiability guarantees without the EVM's constraints. The idea that you can write normal code and get blockchain-level trust is the unlock I've been waiting for.

I want to work on this because it's the kind of hard infrastructure problem I'm drawn to, and because Eigen is the team actually shipping it.

---

## Q2: Tell us what you're great at and what's an ideal role for you.

I'm great at going deep on hard, unfamiliar problems and shipping production systems around them.

I started as a chip design engineer at MediaTek — no software background — taught myself Solidity, and within months was implementing Curve's CurveCrypto invariant on-chain (Newton's method iterative solver in Solidity, where gas costs and fixed-point arithmetic leave zero margin for error). I then designed a custom Avalanche Subnet where validators doubled as order matchers for a decentralized limit order book, and built the cross-chain asset bridge using LayerZero. After that, I picked up Move from scratch to build a leveraged lending protocol on Aptos that reached $7M TVL.

What I bring: the ability to own protocol-level smart contracts end-to-end, design systems at the consensus/infrastructure layer (not just application layer), and work across unfamiliar chains and languages quickly. I've done Solidity, Move, and Rust, and I'm comfortable with the math (AMM invariants, numerical methods, margin/liquidation systems).

Ideal role: protocol engineering or infrastructure engineering — working on EigenLayer core contracts, AVS design patterns, or EigenCloud's verifiable compute layer. I want to be close to the consensus and economic security primitives, not building frontend features.

---

## Q3: What would you build if you joined Eigen Labs?

A verifiable AI inference layer as an AVS on EigenLayer.

Right now, when you call an AI model API, you trust the provider to run the model they claim, with the weights they claim, and return honest outputs. There's no way to verify any of it. This is fine for chatbots but breaks down for high-stakes applications — financial decisions, medical triage, autonomous agents managing real assets.

I'd build an AVS where inference providers stake capital via EigenLayer restaking, commit to running specific models, and face slashing if their outputs can be proven incorrect or manipulated. The verification could use a combination of approaches: optimistic fraud proofs (re-run inference on dispute), trusted execution environments, or cryptographic commitments to model weights.

This maps directly to my background: I've designed slashing and liquidation systems, I understand staking economics from building DeFi protocols, and the "inference insurance" concept I've been exploring independently is essentially this — economic guarantees on AI outputs. EigenLayer provides the restaking substrate; this AVS would be the trust layer for AI.

---

## Cover Letter

Hi,

I'm a protocol engineer who's spent the last 5 years building DeFi infrastructure — two protocols from zero to production, including a perpetual futures exchange on a custom Avalanche Subnet and a leveraged lending protocol on Aptos ($7M TVL peak). Before that, I designed chips at MediaTek.

I'm applying to Eigen Labs because the restaking thesis directly addresses the hardest problem I've encountered as a protocol builder: bootstrapping trust and economic security from scratch. I've designed validator systems, cross-chain bridges, liquidation engines, and slashing-adjacent mechanisms — all of which map to EigenLayer's core infrastructure.

What I'd bring:

- Deep smart contract expertise across Solidity, Move, and Rust — I've ported Newton's method solvers to Solidity and built order book systems at the consensus layer
- Infrastructure-level thinking — I designed a custom Avalanche Subnet where validators acted as order matchers, built a LayerZero bridge for cross-chain collateral, and defined economic parameters (slashing, liquidation incentives) for production systems
- The ability to pick up new domains fast — chip design to DeFi to Move/Aptos, each time shipping production systems within months

I'm currently exploring verifiable AI infrastructure — making AI outputs economically accountable — which aligns closely with Eigen's vision for EigenCloud and the trust layer beyond digital money.

I'd love to contribute to EigenLayer's core protocol, AVS design patterns, or the verifiable compute layer. Happy to discuss further.

Atul Agarwal
atulagarwal893@gmail.com | x.com/0xshinobii | atulagarwal.dev
