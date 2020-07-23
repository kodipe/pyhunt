# rodent

Flat files search engine

**It's PoC - needs huge amount of improvements e.g. in performane field before production usage**

**Works only with UTF-8 files**

### Test dataset

Test dataset contains 2225 articles (4.8MB) from BBC (http://mlg.ucd.ie/datasets/bbc.html)

Some results on the dataset:

- Indexing time: \~4.5s
- Index size:
  - without file index: \~18.5MB
  - with file index containing files id (\~100KB): \~4.6MB
- Searching word 'exotic' through already generated index:
  - only general index: \~0.5s
  - with separated files index: \~0.3s (±0.03s)
- grep on the same machine and the same word: \~0.25s (±0.03s)

### Todos

- [ ] omit commas, dots, semicolons etc.
- [ ] Remove white characters from index (like \ufeff)
- [ ] Better UTF-8 support
- [x] remove stop words from index (English)
- [ ] stemming (English)
- [ ] special characters support
- [ ] count word occurences in file and save it to index
- [ ] case sensitive/insensitive search
- [x] ordering based on best match
- [x] config (e.g. minimal word length)
- [ ] check graph structure to consider connections between words
- split index to separated files
  - [ ] by first letter of word
  - [x] separated index for filenames
- [ ] binary index
- [ ] try to use threads
- [x] saving index to file
- [ ] performance tests in more representative environment and standard deviation

### Unit tests

```
python -m unittest
```

### Time execution test

```
time python rodent.py
```