# Reinforcement Learning for Logo Generation

## Overview
A proof-of-concept RL framework designed for TadReamk's STEM Internship Task, generating logos with:
- Strict symmetry requirements
- Brand color compliance
- Complexity constraints

## Design Philosophy

### Logo-Centric Design
1. **Reward System**:
   - *Simplicity*: Penalizes excess shapes (-0.5 per shape)
   - *Symmetry*: Heavy penalties for asymmetric designs (-0.1 per pixel from center)
   - *Brand Compliance*: Strong preference for brand colors (+2 for compliant, -1 otherwise)

2. **State Representation**:
   - Uses vector parameters (shape positions/sizes) instead of pixels
   - Resolution-independent outputs for scalability

3. **Action Space**:
   - Grid-based placement (8x8 grid enforced)
   - Predefined brand color palette

## Key Components

### Core Architecture
| Component          | Implementation Details                  |
|--------------------|-----------------------------------------|
| **Environment**    | Simulates canvas with logo design rules |
| **Policy**         | Untrained neural network (PPO/DQN-ready) |
| **State**          | Vectorized shape parameters             |

### Trade-offs
- Prioritizes interpretability over complexity
- Extensible to user feedback loops
- Designed as a training-ready skeleton (no training implemented)

## Usage
```bash
pip install -r requirements.txt
python src/demo.py
