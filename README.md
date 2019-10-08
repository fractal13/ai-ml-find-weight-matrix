This work is based on this brief outline:

- Generate synthetic data by picking a weight matrix either
  by hand (start with this) or randomly and running the known 
  model forward to generate the dynamics. 
- Then use this as the input to the learning system to see if 
  it can identify the original weight matrix used to generate 
  the observed dynamics. 
- Is the learning powerful enough to be able to reverse 
  engineer a complex dynamical system? 
- How under constrained is the system (how many alternative
  solutions are there) that replicate the observed behavior?
- How much data does it need to constrain the problem 
  sufficiently to identify the correct weight values?
