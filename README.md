# Reinforcement Learning for Logo Generation  
*A proof-of-concept RL framework to generate logos, designed for TadReamk's STEM Internship Task.*  

## Design Philosophy  
1. **Logo-Centric Rewards**:  
   - Prioritizes simplicity (penalizes excess shapes), symmetry (rewards central alignment), and brand consistency (limits color palette).  
2. **Scalable State Representation**:  
   - Uses vector parameters (shape positions/sizes) instead of pixels for resolution-independent outputs.  
3. **Structured Actions**:  
   - Forces grid-based placement and predefined brand colors to enforce design principles.  

## Key Components  
- **Environment**: Simulates a canvas with actions constrained to logo design rules.  
- **Policy**: Untrained neural network (PPO/DQN-ready) to demonstrate learning potential.  
- **Trade-offs**: Favors interpretability over complexity; extensible to user feedback loops. 

*Note: Per task instructions, this is a design/code skeleton—no training is implemented.*
