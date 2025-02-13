## Fixed sliding window
```python
d = {}
l, r = 0, 0
while r < len(s):
    # adding the next element Eg s[r]

    # removing the past element
    if r - l == k:
        l += 1
    
    r += 1

    # validate current window
    if r - l + 1 == k and len(d) == k - 1:

    # move the window
    r += 1
```

## Dynamic sliding window
```python

```

# Fast and slow pointers