# Reward System Design Notes

## Intentional Punitive Design
This framework employs a **strict reward system** to enforce logo design fundamentals. The punitive approach creates a challenging optimization landscape that would:
- Force RL agents to learn precise symmetry
- Strongly prefer brand consistency
- Naturally limit complexity

## Reward Components Breakdown

### 1. Shape Complexity Penalty
**Formula**:  
`simplicity = -0.5 * (num_shapes // 3)`

**Purpose**:  
- Discourages overcrowded designs
- Encourages minimalist logos
- Division by 3 creates non-linear penalty progression

**Effect**:  
| Shapes Added | Penalty |
|--------------|---------|
| 1-3          | -0.5    |
| 4-6          | -1.0    |
| 7-9          | -1.5    |

### 2. Symmetry Requirement
**Formula**:  
`symmetry = -0.1 * (abs(x - 32) + abs(y - 32))`

**Visualization**:  
```
Maximum Penalty (-6.4): Corner placement (0,0)
Minimum Penalty (0): Perfect center (32,32)
```

**Design Choice**:  
- 0.1 multiplier makes this the dominant reward factor
- Manhattan distance (not Euclidean) for computation efficiency
- Hardcoded center (32,32) for 64x64 canvas

### 3. Brand Color Compliance
**Rules**:  
```
+2 : Using brand color (red/blue)
-1 : Using non-brand color
```

**Implementation**:  
- Color index checked against `brand_colors` list
- Fixed values create clear optimization target

## Combined Reward Example
**Scenario**: 2 shapes placed  
1. Brand color, 10px from center  `reward = (-0.5) + (-0.1*10) + 2 = 0.5`

2. Non-brand color, centered  
   `reward = (-0.5) + 0 + (-1) = -1.5`

## Design Trade-offs
### Advantages
- **Clear Optimization Path**: Agents must satisfy all three factors
- **Interpretable**: Each component maps to design principles
- **Adjustable**: Multipliers can be tuned without structural changes

### Limitations
- **Sparse Rewards**: Early exploration may struggle
- **Fixed Weights**: Doesn't adapt to different logo styles
- **Pixel-Based**: Vector symmetry metrics might be preferable

## Potential Enhancements
1. **Curriculum Learning**:  
   Start with relaxed penalties, then gradually tighten

2. **Human Feedback Integration**:  
   Add reward shaping based on preference models

3. **Dynamic Weighting**:  
   ```python
   symmetry_weight = 1.0 - (episode/1000)  # Gradually reduce
   ```

4. **Advanced Symmetry Metrics**:  
   ```python
   rotational_symmetry = calculate_ssim(rotated_canvas)
   ```
