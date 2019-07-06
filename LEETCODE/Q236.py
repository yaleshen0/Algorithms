# time complexity: O(n)
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
# finds the path from root node to given node
# stores the path in a list path[], return true
# if path exists otherwise false
def findPath(root, path, k):
	if root is None:
		return False
	path.append(root.key)
	if root.key == k:
		return True

	if ((root.left!=None and findPath(root.left, path, k)) or
		root.right!=None and findPath(root.right, path, k)):
		return True

	# if not present in subtree rooted with root, remove
	# root from path and return False
	path.pop()
	return False
# returns LCA if node n1, n2 are present in the given
# binary tree otherwise return -1
def findLCA(root, n1, n2):

	# to store paths to n1 and n2 from the root
	path1 = []
	path2 = []

	# find paths from root to n1 and root to n2
	# if either n1 or n2 is not present, return -1
	if(not findPath(root, path1, n1) or not findPath(root, path2, n2)):
		return -1

	# compare the paths to get the first different value
	i = 0
	while(i < len(path1) and i < len(path2)):
		if path1[i] != path2[i]:
			break
		i += 1
	return path1[i-1]
# root = Node(1)
root =[3,5,1,6,2,0,8,None,None,7,4]
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("LCA(4, 5) = %d" %(findLCA(root, 4, 5,)))
print("LCA(4, 6) = %d" %(findLCA(root, 4, 6)))