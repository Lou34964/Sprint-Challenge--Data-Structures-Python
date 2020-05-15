
import sys
from collections import deque

# class BinarySearchTreeNode:
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # Insert the given value into the tree
  # recursive `insert` implementation
  # def insert(self, value):
  #     # base case: we found a parking spot!
  #     # we're in an empty spot in the tree
  #     if self is None:
  #         self = BinarySearchTreeNode(value)
  #     # if we aren't at a base case,  move towards it
  #     else:
  #         # self is a node with a value
  #         # compare the value to the value at this node
  #         if value < self.value:
  #             # move to the left
  #             self.left.insert(value)
  #         # otherwise, value >= self.value
  #         else:
  #             self.right.insert(value)

  def insert(self, value):
    if value < self.value:

      if self.left:
        self.left.insert(value)

      else:
        self.left = BinarySearchTree(value)

    else:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)


  def contains(self, target):
    if self.value == target:
      return True
    else:
      if target > self.value:
        if self.right:
          return self.right.contains(target)

        if target < self.value:
          if self.left:
            return self.left.contains(target)


  def get_max(self):
    current_max = self.value
  

    while self.right:
      current_max = self.right.value
      self = self.right

    return current_max        


  def for_each(self, cb):
    cb(self.value)

    if self.left:
      self.left.for_each(cb)

    if self.right:
      self.right.for_each(cb)

  def depthfirst_for_each(self, cb):
    stack = []

    stack.append(self)

    while len(stack) > 0:
      current_node = stack.pop()
      
      if current_node.right:
        stack.append(current_node.right)

      if current_node.left:
        stack.append(current_node.left)

      cb(current_node.value)

  def breadthfirst_for_each(self, cb):
    q = deque()
    q.append(self)

    while len(q) > 0:
      current_node = q.popleft()
      if current_node.left:
        q.append(current_node.left)
      if current_node.right:
        q.append(current_node.right)
      cb(current_node.value)

  def in_order_print(self, node):
    if node:
      if node.left:        
        self.in_order_print(node.left)
      print(node.value)
      if node.right:
        self.in_order_print(node.right)

  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
    q = deque()
    q.append(self)

    while len(q) > 0:
      current_node = q.popleft()
      if current_node.left:
        q.append(current_node.left)
      if current_node.right:
        q.append(current_node.right)
      print(current_node.value)

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
    stack = []
    stack.append(self)

    while len(stack) > 0:
      current_node = stack.pop()
      if current_node.right:
        stack.append(current_node.right)
      if current_node.left:
        stack.append(current_node.left)
      print(current_node.value)