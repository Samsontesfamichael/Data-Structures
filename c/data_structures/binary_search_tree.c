/*
 * Binary Search Tree Implementation in C
 * Time Complexity:
 * - Insertion: O(log n) average, O(n) worst
 * - Searching: O(log n) average, O(n) worst
 * - Deletion: O(log n) average, O(n) worst
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Tree node structure
typedef struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

// Create a new node
TreeNode* create_node(int data) {
    TreeNode* new_node = (TreeNode*)malloc(sizeof(TreeNode));
    if (new_node == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new_node->data = data;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

// Insert a node - O(log n) average
TreeNode* insert(TreeNode* root, int data) {
    if (root == NULL) {
        return create_node(data);
    }
    
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else if (data > root->data) {
        root->right = insert(root->right, data);
    }
    // Duplicates not allowed
    
    return root;
}

// Search for a value - O(log n) average
TreeNode* search(TreeNode* root, int key) {
    if (root == NULL || root->data == key) {
        return root;
    }
    
    if (key < root->data) {
        return search(root->left, key);
    }
    
    return search(root->right, key);
}

// Find minimum value node
TreeNode* find_min(TreeNode* root) {
    if (root == NULL) {
        return NULL;
    }
    
    while (root->left != NULL) {
        root = root->left;
    }
    
    return root;
}

// Find maximum value node
TreeNode* find_max(TreeNode* root) {
    if (root == NULL) {
        return NULL;
    }
    
    while (root->right != NULL) {
        root = root->right;
    }
    
    return root;
}

// Delete a node - O(log n) average
TreeNode* delete_node(TreeNode* root, int key) {
    if (root == NULL) {
        return root;
    }
    
    // Find the node to delete
    if (key < root->data) {
        root->left = delete_node(root->left, key);
    } else if (key > root->data) {
        root->right = delete_node(root->right, key);
    } else {
        // Node with only one child or no child
        if (root->left == NULL) {
            TreeNode* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            TreeNode* temp = root->left;
            free(root);
            return temp;
        }
        
        // Node with two children
        TreeNode* temp = find_min(root->right);
        root->data = temp->data;
        root->right = delete_node(root->right, temp->data);
    }
    
    return root;
}

// Preorder traversal (Root -> Left -> Right)
void preorder(TreeNode* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

// Inorder traversal (Left -> Root -> Right) - gives sorted order
void inorder(TreeNode* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

// Postorder traversal (Left -> Right -> Root)
void postorder(TreeNode* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}

// Get height of tree
int get_height(TreeNode* root) {
    if (root == NULL) {
        return 0;
    }
    
    int left_height = get_height(root->left);
    int right_height = get_height(root->right);
    
    return (left_height > right_height ? left_height : right_height) + 1;
}

// Count nodes
int count_nodes(TreeNode* root) {
    if (root == NULL) {
        return 0;
    }
    
    return 1 + count_nodes(root->left) + count_nodes(root->right);
}

// Free all nodes
void free_tree(TreeNode* root) {
    if (root != NULL) {
        free_tree(root->left);
        free_tree(root->right);
        free(root);
    }
}

// Main function for testing
int main() {
    printf("=== Binary Search Tree Demo (C) ===\n\n");
    
    TreeNode* root = NULL;
    
    // Insertion
    printf("1. Insertion Operations:\n");
    int values[] = {50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65};
    int n = sizeof(values) / sizeof(values[0]);
    
    for (int i = 0; i < n; i++) {
        root = insert(root, values[i]);
    }
    printf("Inserted values: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", values[i]);
    }
    printf("\n");
    
    // Searching
    printf("\n2. Searching Operations:\n");
    TreeNode* found = search(root, 40);
    printf("Search for 40: %s\n", found ? "Found" : "Not found");
    found = search(root, 100);
    printf("Search for 100: %s\n", found ? "Not found" : "Found");
    
    // Min and Max
    printf("\n3. Finding Min and Max:\n");
    TreeNode* min_node = find_min(root);
    TreeNode* max_node = find_max(root);
    printf("Minimum value: %d\n", min_node ? min_node->data : -1);
    printf("Maximum value: %d\n", max_node ? max_node->data : -1);
    
    // Traversals
    printf("\n4. Tree Traversals:\n");
    printf("Preorder:  ");
    preorder(root);
    printf("\n");
    
    printf("Inorder:   ");
    inorder(root);
    printf("\n");
    
    printf("Postorder: ");
    postorder(root);
    printf("\n");
    
    // Tree properties
    printf("\n5. Tree Properties:\n");
    printf("Height: %d\n", get_height(root));
    printf("Total nodes: %d\n", count_nodes(root));
    
    // Deletion
    printf("\n6. Deletion Operations:\n");
    printf("Before deletion (inorder): ");
    inorder(root);
    printf("\n");
    
    root = delete_node(root, 20);
    printf("After deleting 20: ");
    inorder(root);
    printf("\n");
    
    root = delete_node(root, 30);
    printf("After deleting 30: ");
    inorder(root);
    printf("\n");
    
    root = delete_node(root, 50);
    printf("After deleting 50 (root): ");
    inorder(root);
    printf("\n");
    
    // Clean up
    free_tree(root);
    
    return 0;
}
