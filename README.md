# rodent

Flat files search engine

**It's PoC - needs huge amount of improvements e.g. in performane field before production usage**

**Works only with UTF-8 files**

### Test dataset

Test dataset contains 2225 articles (4.8MB) from BBC (http://mlg.ucd.ie/datasets/bbc.html)

Some results on the dataset:

- Indexing time: ~4.5s
- Index size: ~17.8MB
- Searching through index: ~0.5s

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
- [ ] split index to separated files (by first letter of word?)
- [ ] try to use threads
- [x] saving index to file

### Unit tests

```
python -m unittest
```

### Time execution test

```
time python rodent.py
```