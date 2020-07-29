# PyHunt

Flat files search engine

**It's PoC - needs huge amount of improvements before production usage**

**Works only with UTF-8 files**

### Requirements

- Python 3.8.x
- No need database!

### Features

- Files content indexing
- Persist indexes
- Adding single file to index
- Stop words
- Stemming

### Unit tests

```
./scripts/run-tests.py
```

### Performance test

```
./scripts/run-performance-test.py
```

Test dataset contains 2225 articles (4.8MB) from BBC (http://mlg.ucd.ie/datasets/bbc.html)

Some results for the dataset (on my local machine):

- Single file indexing: \~0.8s
- Indexing time for whole test dataset: \~36s (±2s)
- Index size: \~4.5MB + \~100KB (files index)
- Searching word 'exotic' through already generated index: \~0.28s (±0.01s)
- grep on the same machine and the same word: \~0.25s (±0.03s)

### Todos


- [ ] Remove white characters from index (like \ufeff)
- [ ] Better UTF-8 support
- [ ] Improve stemming
- [ ] extended config
- [ ] add directory prefix to file index (decrease index size) e.g. @index1/path/of/file.txt
- [ ] purge index
- [ ] index auto detection
- [ ] check graph structure to consider connections between words
- [ ] binary index
- [ ] try to use threads
- [ ] performance tests in more representative environment and standard deviation (Travis CI?)
- [ ] Support for other file types than .txt
- [x] count word occurences in file and save it to index
- [x] stemming (English)
- [x] omit commas, dots, semicolons etc.
- [x] remove stop words from index (English)
- [x] ordering based on best match
- [x] config (e.g. minimal word length)
- [x] saving index to file
- [x] separated index for filenames