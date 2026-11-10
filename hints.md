# NumPy Wrap-up Exercises: Hints (no code)

## Exercise 1: arrays, views and reshaping

**Creating `my_array` (20×30, random):**
- `np.random.random(...)`, `np.random.rand(...)`, or the newer `np.random.default_rng().random(...)`. Check whether the function wants a shape tuple or separate arguments (the notebook uses the tuple form with `np.random.random`).

**`my_array_subselect` (all rows except the last, columns 2 to 5):**
- This needs no function, only **slicing** on both axes: `array[row_slice, col_slice]`.
- Two things to watch: the stop index is *excluded*, and columns are 0-indexed, so "the second to the fifth column" means the slice's start and stop are not 2 and 5. Count carefully. The test expects 4 columns and 19 rows.
- Negative indices help for "all except the last".

**`my_array_subselect_reshaped` (38×2, and it should be a view):**
- `ndarray.reshape(...)` or `np.reshape(...)`.
- Think about whether this will really be a view. A slice of a bigger array isn't contiguous in memory, so `reshape` may silently return a **copy**. To check, use `.base`, `np.shares_memory(...)` or `np.may_share_memory(...)`, and `.flags` (see `C_CONTIGUOUS`). The notebook itself shows `.base` and `.flags.owndata`.
- The exercise statement says "view", so verify your result rather than assuming it.
- Hint: assigning to `.shape` instead of calling `reshape` raises an error when a view isn't possible, which can be a useful experiment.

## Exercise 2: Rocket class with random increments

- Random integer between 1 and 10: look at `np.random.randint(low, high)` and note whether `high` is **inclusive or exclusive**. This is the classic trap. The newer `Generator.integers(...)` has an `endpoint` parameter for the same issue.
- The rest is plain Python: `__init__` setting `self.x`, `self.y`, `self.z`, a `move_up` method that adds to `self.z`, a list comprehension or loop to build `space_rockets`, then a `for` loop for printing.

## Exercise 3: sampled sine wave

The signal is A·sin(2π·f·t + φ). The relevant pieces:

- **Time axis:** `np.linspace(start, stop, num, endpoint=True)` or `np.arange(...)`. Since the end point is included, think about which one handles that more cleanly and how to compute the number of samples from `T` and `f_s`. Beware of off-by-one errors: N intervals means N+1 points. Also watch the units (kHz vs Hz).
- **Constants:** `np.pi`.
- **The sine:** `np.sin(...)`, which works elementwise on the whole array.
- **Last ten elements:** negative slicing, e.g. `array[-10:]`.

Tip: with 400 kHz over 2 s you get about 800,000 samples. That's easy for NumPy, but it's a good reason to avoid Python loops. Also, with φ = π/2 your sine is really a cosine, which you can use as a sanity check on your first values.

## Sanity-check tools for all three

`.shape`, `.ndim`, `.size`, `.base`, and `np.shares_memory`.