# SEAT

This project provides a simulation engine, which we call SEAT (Simulation Engine for Adaptive Telematics), for the flexible generation of an insurance claims dataset with driver telematics information that matches the specific profile of a target market. 

## Usage

```python
import SEAT
# returns 'target protfolio'
SEAT.target(Insured.sex, Region, Insured.age, Car.use).fit(N,SD,random_state)
```
---
- <font size="2">Insured.sex = [$P^*(M)$, $P^*(F)$]</font>
- <font size="2">Region = [$P^*(R)$, $P^*(U)$] </font>
- <font size="2">Insured.age = [$P^*(A1)$, $P^*(A2)$, $P^*(A3)$, $P^*(A4)$, $P^*(A5)$]</font>
- <font size="2">Car.use = [$P^*(C1)$, $P^*(C2)$, $P^*(C3)$, $P^*(C4)$]</font>
- <font size="2">N = the number of observations </font>
- <font size="2">SD = the degree of random perturbation  </font>
  
  <font size="1.5">*See Table 3 in  'paper' for reference* </font>


## Algorithm

- Step 1:  Calculate conditional distributions of four covariates; 'Insured.sex', 'Region', 'Insured.age', and 'Car.use'.  

- Step 2:  Create a random sample from the standard uniform distribution and categorize it based on each conditional distribution in the order of 'Insured.sex', 'Region', 'Insured.age', and 'Car.use'. 

- Step 3: By repeating Step 2 $N$ times, gain $N$ configurations of the four covariates $$\{\mathcal{C}_i\}_{i=1,\ldots, N}$$ where $N$ is the number of total observations in the synthetic portfolio to be generated.
- Step 4: From the original portfolio, sample $N$ observations of the remaining variables (telematics and claims information) from their empirical distributions given each configuration  with white Gaussian noises. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Reference
[So, B., Boucher, J.-P., and Valdez, E. A. (2021). Synthetic dataset generation of driver telematics.
Risks, 9(4):58](https://www.mdpi.com/2227-9091/9/4/58)



```python

```
