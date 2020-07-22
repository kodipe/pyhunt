# rodent

Flat files search engine

**It's PoC - needs huge amount of improvements e.g. in performane field before production usage**

### Todos

- [ ] special characters support
- [ ] count word occurences in file and save it to index
- [ ] case sensitive/insensitive search
- [ ] ordering based on best match
- [ ] check graph structure to consider connections between words
- [ ] split index to separated files (by first letter of word?)
- [ ] try to use threads
- [x] saving index to file

### Time execution test

```
time python rodent.py
```