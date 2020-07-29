import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from rodent import Rodent

if __name__ == "__main__":
  engine = Rodent(
    content_dir=os.path.join(os.path.dirname(__file__), "__dataset__"),
    index_dir=os.path.join(os.path.dirname(__file__))
  )
  engine.create_index(persist=True)

  # engine.load_index('index.json')
  engine.save_index(os.path.join(os.path.dirname(__file__), "index.json"))

  query = u"health of human body"

  results = engine.search(query, output='wages')

  sys.stdout.buffer.write(f'Results for: "{query}"\n'.encode())
  print(results)