import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from rodent import Rodent

if __name__ == "__main__":
  engine = Rodent(content_dir=os.path.join(os.path.dirname(__file__), "__dataset__"))
  engine.create_index(persist=True)

  # engine.load_index('index.json')
  engine.save_index('index.json')

  query = u"exotic"

  results = engine.search(query, output='wages')

  sys.stdout.buffer.write(f'Results for: "{query}"\n'.encode())
  print(results)