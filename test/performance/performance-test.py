import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from pyhunt import PyHunt, PYHUNT_OUTPUT_WAGES

if __name__ == "__main__":
  engine = PyHunt(
    content_dir=os.path.join(os.path.dirname(__file__), "__dataset__"),
    index_dir=os.path.join(os.path.dirname(__file__))
  )
  engine.create_index(persist=True)

  # engine.load_index(os.path.join(os.path.dirname(__file__), "index.json"))
  engine.save_index(os.path.join(os.path.dirname(__file__), "index.json"))

  query = u"security document"

  results = engine.search(query, output=PYHUNT_OUTPUT_WAGES)

  sys.stdout.buffer.write(f'Results for: "{query}"\n'.encode())
  print(results)