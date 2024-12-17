## Performance Analysis

### Raw Data

#### Serial Binary Search Times (seconds):
- 0.023288
- 0.004525
- 0.005908
- 0.003527
- 0.003789
- 0.004158
- 0.003042
- 0.004139
- 0.003634
- 0.003540
- 0.003716
- 0.004267
- 0.004069
- 0.003807
- 0.003520

#### Parallel Binary Search Times (seconds):
- 0.031346
- 0.009295
- 0.006320
- 0.002512
- 0.002357
- 0.003464
- 0.002003
- 0.002735
- 0.004760
- 0.004642
- 0.004266
- 0.005376
- 0.005463
- 0.004687
- 0.002813

---

### Statistics

#### Serial Binary Search:
- **Mean:** 0.00526 seconds
- **Median:** 0.00381 seconds
- **Standard Deviation:** 0.00483 seconds

#### Parallel Binary Search:
- **Mean:** 0.00614 seconds
- **Median:** 0.00464 seconds
- **Standard Deviation:** 0.00757 seconds

---

### Which is Faster?

- Based on the **mean**, **serial binary search** is faster.
- Based on the **median**, **serial binary search** is also faster.

---

### Conclusion

For the given dataset and system configuration (MacOS M1 8GB), the serial binary search demonstrates faster performance on average. The parallel implementation incurs overhead that negates potential speedup, particularly for the current array size and process count.