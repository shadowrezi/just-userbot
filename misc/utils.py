class Flag:
  def __init__(self, status=True) -> None:
    self.status = status

  def toggle(self):
    self.status = not self.status
