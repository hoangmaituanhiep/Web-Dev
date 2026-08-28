class Entity:
  cur_img = None
  gif = None

  def __init__(self, img1, gif):
    self.cur_img = img1
    self.gif = gif

class Big(Entity):
  count = None
  img2 = None
  line1 = 0
  line2 = 0

  def __init__(self, count, img1, img2, gif, line1, line2):
    super().__init__(img1, gif)
    self.count = count
    self.img2 = img2
    self.line1 = line1
    self.line2 = line2
  
  def increment(self):
    self.count+=1
    if self.count > line1:
      self.cur_img = img2
    if self.count > line2:
      self.cur_img = gif

class Bullet(Entity):
  def __init__(self, img, gif):
    super().__init__(img, gif)

class Gun(Entity):
  def __init__(self, img, gif=None):
    super().__init__(img, gif)