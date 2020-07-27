# rodent

Flat files search engine

**It's PoC - needs huge amount of improvements e.g. in performane field before production usage**

**Works only with UTF-8 files**

### Requirements

- Python 3.8.x
- No need database!

### Features

- Files content indexing
- Persist indexes
- Adding single file to index
- stop words

### Test dataset

Test dataset contains 2225 articles (4.8MB) from BBC (http://mlg.ucd.ie/datasets/bbc.html)

Some results on the dataset:

- Single file indexing: \~0.8s
- Indexing time for whole test dataset: \~41s (±2s)
- Index size: \~2.6MB + \~100KB (files index)
- Searching word 'exotic' through already generated index: \~0.21s (±0.01s)
- grep on the same machine and the same word: \~0.25s (±0.03s)

### Todos


- [ ] Remove white characters from index (like \ufeff)
- [ ] Better UTF-8 support
- [ ] count word occurences in file and save it to index
- [ ] Improve stemming
- [ ] case sensitive/insensitive search
- [ ] extended config
- [ ] purge index
- [ ] index auto detection
- [ ] check graph structure to consider connections between words
- [ ] binary index
- [ ] try to use threads
- [ ] performance tests in more representative environment and standard deviation
- [x] stemming (English)
- [x] omit commas, dots, semicolons etc.
- [x] remove stop words from index (English)
- [x] ordering based on best match
- [x] config (e.g. minimal word length)
- [x] saving index to file
- [x] separated index for filenames

### Unit tests

```
python -m unittest
```

### Time execution test

```
time python rodent.py
```