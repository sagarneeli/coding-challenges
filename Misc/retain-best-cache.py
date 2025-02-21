"""
Challenge:
Provide an implementation of the RetainBestCache class (skeletons below).

To begin with, assume that ranks will not change once read. Don't offer this information until the candidate asks.

It's usually wise to let the candidate ignore concurrency safety initially, to ensure they can get a core solution functioning first, but it's a good follow-up requirement.

# X is some class that has an integer property `rank`.

Code Skeleton:
Python:
class RetainBestCache(object):
    def __init__(self, slow_process: Callable[[K], X], capacity: int):
        # Implementation here

    def get(self, key: K) -> X:
        # Implementation here

Java:
public class RetainBestCache<K, V extends Rankable> {
    // Add any fields you need here

    /**
     * Constructor with a data source (assumed to be slow) and a cache size
     * @param ds the persistent layer of the cache
     * @param capacity the number of entries that the cache can hold
     */
    public RetainBestCache(DataSource<K, V> ds, int capacity) {
        // Implementation here
    }

    /**
     * Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
     * retrieves it from the data source and, if possible, caches it.
     * If the cache is full, attempt to cache the returned data,
     * evicting the V with lowest rank among the ones that it has available.
     * If there is a tie, the cache may choose any V with lowest rank to evict.
     * @param key the key of the cache entry being queried
     * @return the Rankable value of the cache entry
     */
    public V get(K key) {
        // Implementation here
    }
}

/**
 * For reference, here are the Rankable and DataSource interfaces.
 * You do not need to implement them, and should not make assumptions
 * about their implementations.
 */
public interface Rankable {
    /**
     * Returns the Rank of this object, using some algorithm and potentially
     * the internal state of the Rankable.
     */
    long getRank();
}

public interface DataSource<K, V extends Rankable> {
    V get(K key);
}
"""

from typing import Callable, TypeVar, Generic


class RetainBestCache(object):
    def __init__(self, slow_process: Callable[[K], X], capacity: int):
        # Implementation here

    def get(self, key: K) -> X:
        # Implementation here
