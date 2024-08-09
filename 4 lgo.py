class treeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def sorted_to_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = treeNode(arr[mid])
    root.left = sorted_to_bst(arr[:mid])
    root.right = sorted_to_bst(arr[mid + 1:])
    return root


def delete_node(root,key):
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left


        min_larger_node = root.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left

        root.value = min_larger_node.velue
        root.right = delete_node((root.right , min_larger_node.value))

    return  root